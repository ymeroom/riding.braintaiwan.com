"""由 data/trip.json 生成 index.html。

模板 templates/index_template.html 保留所有手寫區塊（CSS、hero、行前提醒、
黑名單避坑表、主題切換器、音樂播放器 JS），只把資料驅動的三塊換掉：
  {{SUMMARY_TABLE}}    19日總覽表
  {{DAY_CARDS}}        每日詳細卡片
  {{WEATHER_WAR_ROOM}} 天氣作戰室（今日／明日 時間×地點矩陣、一週地點預報）
  {{WEATHER_JS}}       作戰室與每日卡片的天氣邏輯
  {{EXTRA_CSS}}        上述新區塊的樣式

天氣有兩層，不要混用：逐日的「去年同日實測」與 Open-Meteo 即時預報留在原本位置；
data/seasonal_outlook.json 是氣象庁３か月予報，屬於「月・區域平均的三分位機率」，
只並列在同一格／同一張卡片旁做長期趨勢對照，不參與任何逐日判斷。

紅葉也是同樣兩層：每日卡片的「🍁 見頃實績」是去年同日的地點性格；
data/foliage_forecast.json 是 JMC 紅葉見頃予想（市級標本木、每月更新），
與季節預報同一層，只在總覽表上方並列做趨勢對照，不參與逐日判斷。手動維護，
每年 9 月上旬起 JMC 逐月發表新一期（來源見 JSON 內 _source）。
"""
import json, io, os, html, re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load(p):
    return json.load(io.open(os.path.join(ROOT, p), encoding='utf-8'))


def esc(s):
    return html.escape(str(s or ''), quote=True)


_FW = str.maketrans('０１２３４５６７８９＋－', '0123456789+-')


def tel_href(s):
    """把顯示用的電話字串壓成純撥號碼：全形轉半形、+81→0、只留數字。

    資料裡的 tel 欄常夾雜標籤（「23區 03-3212-2323」）或全形數字
    （「０４７－７０２－７３８６」），直接塞進 href 會變成撥不出去的死連結。
    """
    t = str(s or '').translate(_FW).strip()
    if t.startswith('+81'):
        t = '0' + t[3:]
    nums = re.findall(r'\d[\d\-\s]{6,}\d', t)
    digits = re.sub(r'\D', '', nums[-1]) if nums else re.sub(r'\D', '', t)
    return digits


# ─────────────────── JMA 季節預報（３か月予報） ───────────────────

_CLS = {'気温': ('偏低', '平年並', '偏高'), '降水量': ('偏少', '平年並', '偏多')}


def _short_prob(p, kind):
    """三分位機率壓成表格塞得下的一句：最大階級 + 機率。並列最大值照氣象庁寫法並陳。"""
    labels = _CLS[kind]
    vals = [p['below'], p['normal'], p['above']]
    mx = max(vals)
    return '‧'.join(labels[i] for i, v in enumerate(vals) if v == mx) + f' {mx}%'


def _long_prob(p, kind):
    return p.get('zh') or _short_prob(p, kind)


def _merge_regions(month, seas, codes):
    """同一個月、多個預報區：文字與機率完全一致就併成一列掛兩個區名，不同才分列。"""
    groups = []
    for code in codes:
        reg = seas['regions'].get(code)
        m = reg['monthly'].get(month) if reg else None
        if not m:
            continue
        for g in groups:
            if g[1] == m:
                g[0].append(reg['zh_name'])
                break
        else:
            groups.append(([reg['zh_name']], m))
    return [('・'.join(names), m) for names, m in groups]


def day_outlook(day, seas):
    """該日的（區域名, 當月展望）清單；該日落在預報期間外就回 []。"""
    if not seas:
        return []
    info = seas['days'].get(str(day))
    if not info or not info['covered']:
        return []
    return _merge_regions(info['month'], seas, info['regions'])


def outlook_cell(day, seas):
    """總覽表天氣欄裡，接在去年實測底下的那一小塊。"""
    if not seas:
        return ''
    gs = day_outlook(day, seas)
    if not gs:
        return ('<div class="wx-outlook wx-none">🔭 不在本期３か月予報'
                f'（{esc(seas["meta"]["target_label"])}）範圍</div>')
    out = []
    for names, m in gs:
        tip = ' ／ '.join(x.strip() for x in (m.get('weather'), m.get('気温_text'),
                                             m.get('降水量_text')) if x)
        bits = [('氣溫 ' if k == '気温' else '降水 ') + _short_prob(m[k], k)
                for k in ('気温', '降水量') if m.get(k)]
        zh = m.get('weather_zh')
        out.append(f'<div class="wx-outlook" title="{esc(tip)}">'
                   f'🔭 <strong>JMA {esc(m["label"])}展望</strong>（{esc(names)}）'
                   + (f'<br>{esc(zh)}' if zh else '')
                   + (f'<br>{" ｜ ".join(bits)}' if bits else '') + '</div>')
    return ''.join(out)


def render_seasonal_day(day, seas):
    """每日卡片裡，接在「去年同日實測」底下的季節預報列。"""
    if not seas:
        return ''
    gs = day_outlook(day, seas)
    if not gs:
        return ('            <div class="seasonal-box seasonal-none"><span class="weather-icon">🔭</span> '
                f'本日不在氣象庁３か月予報（{esc(seas["meta"]["target_label"])}，'
                f'{esc(seas["meta"]["issued_label"])} 發表）的範圍內；'
                f'{esc(seas["meta"]["next_release_text"])} 的新一期會往後延伸涵蓋。</div>')
    rows = []
    for names, m in gs:
        seg = [f'<strong>{esc(m["label"])}・{esc(names)}</strong>']
        if m.get('weather'):
            zh = m.get('weather_zh')
            seg.append(esc(m['weather'].strip()) + (f'（{esc(zh)}）' if zh else ''))
        for k in ('気温', '降水量'):
            if m.get(k):
                seg.append(('氣溫 ' if k == '気温' else '降水量 ') + esc(_long_prob(m[k], k)))
        rows.append(' ｜ '.join(seg))
    return ('            <div class="seasonal-box"><span class="weather-icon">🔭</span> '
            '<strong>氣象庁季節預報</strong>（月・區域平均的機率，不是本日天氣）：'
            + '<br>'.join(rows) + '</div>')


def render_seasonal_note(trip, seas):
    """總覽表上方的一段說明：本期預報講了什麼、背景是什麼、下次什麼時候更新。"""
    if not seas:
        return ''
    meta, enso = seas['meta'], seas['enso']
    months, uncovered = [], []
    for d in trip['days']:
        info = seas['days'].get(str(d['day']))
        if not info:
            continue
        if info['covered']:
            if info['month'] not in months:
                months.append(info['month'])
        else:
            uncovered.append(d['day'])
    items = []
    for mo in months:
        for names, m in _merge_regions(mo, seas, ('010300', '010400')):
            seg = [f'<strong>{esc(m["label"])}・{esc(names)}</strong>']
            if m.get('weather'):
                zh = m.get('weather_zh')
                seg.append('天候「' + esc(m['weather'].strip()) + '」'
                           + (f'（{esc(zh)}）' if zh else ''))
            for k in ('気温', '降水量'):
                if m.get(k):
                    seg.append(('氣溫 ' if k == '気温' else '降水量 ') + esc(_long_prob(m[k], k)))
            items.append('<li>' + ' ｜ '.join(seg) + '</li>')
    season = seas['regions']['010300'].get('season') or {}
    if season.get('気温'):
        items.append(f'<li><strong>{esc(season.get("label", "向こう３か月"))}平均・關東甲信</strong> ｜ '
                     f'氣溫 {esc(_long_prob(season["気温"], "気温"))}</li>')
    enso_zh = '、'.join(enso.get('headline_zh') or [])
    miss = ('　Day ' + '／'.join(str(x) for x in uncovered) + ' 落在預報期間之外。') if uncovered else ''
    others = meta.get('other_releases') or {}
    other_txt = ('（' + esc('；'.join(v['text'] for v in others.values())) + '）') if others else ''
    return f"""        <div class="seasonal-note">
            <div class="sn-head">🔭 氣象庁 {esc(meta['product'])} ｜ {esc(meta['issued_label'])} 發表，對象 {esc(meta['target_label'])}</div>
            <ul>{''.join(items)}</ul>
            <div class="sn-enso">🌊 背景：エルニーニョ監視速報 {esc(enso['no'])}（{esc(enso['issued_ja'])}）—
                {esc('　'.join(enso['headline']))}{f'（{esc(enso_zh)}）' if enso_zh else ''}
                <a href="{esc(enso['url'])}" target="_blank" rel="noopener">原文 ↗</a></div>
            <div class="sn-warn">⚠️ 這是<strong>月・區域平均的三分位機率</strong>，不是逐日天氣，也不能拿來決定哪天騎哪一段——
                逐日決策請用上方「天氣作戰室」的 Open-Meteo 時序預報。{miss}</div>
            <div class="sn-next">🗓️ 下次更新：{esc(meta['next_release_text'])} {other_txt}
                ｜ 重新抓取：<code>python scripts_v2/fetch_seasonal_outlook.py</code></div>
        </div>
"""


def render_foliage_note(fol):
    """總覽表上方：JMC 紅葉見頃予想。與季節預報同一層 —— 月・區域平均，不參與逐日判斷。

    每日卡片的「🍁 紅葉見頃實績」是去年同日的地點性格；這一塊是今年的預報趨勢，兩者並列對照。
    """
    if not fol:
        return ''
    reg = fol['regional']
    crows = ''.join(
        f'<tr><td><strong>{esc(c["name"])}</strong><br><small>{esc(c["role"])}</small></td>'
        f'<td>{esc(c["red"])}<br><small>平年 {esc(c["red_delta"])} 天</small></td>'
        f'<td>{esc(c["yellow"])}<br><small>平年 {esc(c["yellow_delta"])} 天</small></td>'
        f'<td>{esc(c.get("caveat", "—"))}</td></tr>'
        for c in fol['cities'])
    reads = ''.join(f'<li>{esc(x)}</li>' for x in fol.get('trip_readout', []))
    return f"""        <div class="seasonal-note foliage-note">
            <div class="sn-head">🍁 {esc(fol['_product'])} ｜ {esc(fol['_issued_label'])}</div>
            <div class="fn-region">🗾 <strong>{esc(reg['_area'])}</strong>（{esc(reg['_updated'])}）
                ｜ {esc(reg['temp'])} {esc(reg['koyo'])} {esc(reg['kouyou'])}</div>
            <div class="table-wrapper"><table class="fn-table"><thead><tr>
                <th>觀測點（行程對應）</th><th>楓葉見頃</th><th>銀杏見頃</th><th>注意</th>
            </tr></thead><tbody>{crows}</tbody></table></div>
            <ul>{reads}</ul>
            <div class="sn-warn">⚠️ 這是<strong>市級標本木的區域平均預報</strong>，不是景點見頃日，也不能拿來排哪天騎哪段——
                景點海拔／樹種會讓實際見頃前後偏移一週以上。每日卡片的「🍁 見頃實績」是去年同日的地點性格，兩者對照著看。</div>
            <div class="sn-next">🗓️ 下次更新：{esc(fol['_next_release'])}
                ｜ 來源：<a href="{esc(fol['_source'])}" target="_blank" rel="noopener">JMC 紅葉予想 ↗</a>
                ｜ {esc(fol['_verified'])}</div>
        </div>
"""


# ─────────────────────────── 總覽表 ───────────────────────────

def render_summary_table(trip, seas=None, fol=None):
    rows = []
    for d in trip['days']:
        n, h = d['nav'], d['hotel']
        w = d['weather_hist']
        badge = ('<span class="badge-booked">✅ 🏨 已訂房</span>' if h['booked']
                 else '<span class="badge-pending">🔍 待訂房</span>')
        hotel_cell = f"<strong>{esc(h['name'])}</strong>"
        if h['url'] and h['addr']:
            hotel_cell += (f'<br><a href="{esc(h["url"])}" target="_blank" rel="noopener" '
                           f'class="map-link">📍 {esc(h["addr"])} ↗</a>')
        elif h['addr']:
            hotel_cell += f'<br><small style="color:#64748B;">{esc(h["addr"])}</small>'
        pk, nk = d.get('planned_km'), n.get('km')
        km_cell = f"<strong>{nk if nk is not None else '—'} km</strong>"
        if pk and nk and abs(pk - nk) >= 2.0 and abs(pk - nk) / max(nk, 1) > 0.05:
            km_cell += f"<br><small style=\"color:#B45309;\">實走 {pk} km</small>"
        wx = (f"{esc(w['icon'])} {esc(w['text'])} ｜ {w['lo']}°C ~ {w['hi']}°C<br>"
              f"降水 {w['rain']}mm ｜ 日照 {w['sun']}h") if w['lo'] is not None else esc(w['raw'])
        wx += outlook_cell(d['day'], seas)
        rows.append(f"""                    <tr class="summary-row-clickable" onclick="scrollToDay({d['day']})" title="點擊直達 Day {d['day']} 詳細騎行日程">
                        <td><strong>{esc(d['date'])}<br><span style="color:#B91C1C;">Day {d['day']}</span></strong><br><a href="#day-{d['day']}" class="day-jump-badge" onclick="event.stopPropagation(); scrollToDay({d['day']}); return false;">👇 詳細日程 ➔</a><br>{badge}</td>
                        <td>{esc(d['route_line'])}</td>
                        <td>{km_cell}</td>
                        <td>+{n.get('gain','—')}m / -{n.get('loss','—')}m<br><small style="color:#64748B;">海拔 {n.get('min_e','—')}~{n.get('max_e','—')}m</small></td>
                        <td>{hotel_cell}</td>
                        <td>{wx}</td>
                        <td>{esc(d['foliage'])}</td>
                    </tr>""")
    m = trip['meta']
    return render_seasonal_note(trip, seas) + render_foliage_note(fol) + f"""        <h2 class="section-title">📊 19日每日里程、爬升、去年實測天氣＋JMA 季節預報與紅葉見頃總覽 ｜ 💡 點擊任一日程即可直達下方詳細規劃</h2>
        <div class="data-source-note">📐 里程與爬升：<strong>NAVITIME 自転車ルート実測</strong>（路線偏好「{m['source'].split('（')[1].split('）')[0] if '（' in m['source'] else '坡少'}」）；標高取自 NAVITIME 路線幾何三維座標，以 3 公尺遲滯門檻累加，與 Garmin／Strava 計法一致。全程合計 <strong>NAVITIME 最短路徑 {m['total_km']} km ／ 本計畫實走約 {m.get('total_planned_km', m['total_km'])} km ／ +{m['total_gain']:,} m</strong>。<br>兩個里程都是真的：NAVITIME 只取得每日 4–8 個路線節點，節點之間由它自選最短路；本計畫刻意繞走自行車專用道與避坑舊道，因此實走較長。爬升以 NAVITIME 為準。</div>
        <div class="table-wrapper">
            <table>
                <thead>
                    <tr>
                        <th style="width: 12%;">📅 日期（週幾）/ 天數</th>
                        <th style="width: 22%;">🚲 當日區間與核心騎行路線</th>
                        <th style="width: 8%;">📏 里程</th>
                        <th style="width: 11%;">⛰️ 爬升/下降</th>
                        <th style="width: 16%;">🏨 住宿飯店與地圖導航</th>
                        <th style="width: 18%;">☀️ 去年實測 ＋ 🔭 JMA 季節預報</th>
                        <th style="width: 13%;">🍁 紅葉見頃實績</th>
                    </tr>
                </thead>
                <tbody>
{chr(10).join(rows)}
                </tbody>
            </table>
        </div>"""


# ─────────────────────────── 每日卡片 ───────────────────────────

def render_player(day, songs):
    s = songs.get(str(day))
    if not s:
        return ''
    return f"""                <div class="theme-music-player" data-track="{esc(s['track'])}">
                    <button class="player-btn" onclick="toggleThemePlayer(this)" aria-label="播放 Day {day} 主題曲">
                        <svg class="icon-play" viewBox="0 0 24 24"><path fill="currentColor" d="M8 5v14l11-7z"/></svg>
                        <svg class="icon-pause" viewBox="0 0 24 24" style="display:none;"><path fill="currentColor" d="M6 19h4V5H6v14zm8-14v14h4V5h-4z"/></svg>
                    </button>
                    <div class="player-info">
                        <div class="player-label">🎵 Day {day} Theme Song</div>
                        <div class="player-title">{esc(s['title'])}</div>
                    </div>
                    <div class="player-progress-container" onclick="seekThemePlayer(event, this)">
                        <div class="player-progress-bar"></div>
                    </div>
                    <div class="player-time">0:00 / 0:00</div>
                    <audio src="{esc(s['audio'])}" preload="none" ontimeupdate="updateThemePlayerProgress(this)" onloadedmetadata="setPlayerDuration(this)" onended="resetThemePlayer(this)"></audio>
                </div>"""


def render_timeline(d):
    ICON = {'start': '🚩', 'end': '🏁', 'pivot': '🚨', 'scenic': '🌄',
            'rest': '☕', 'waypoint': '📍', 'warning': '⚠️'}
    items = []
    for t in d['timeline']:
        items.append(f"""                    <li class="tl-item tl-{esc(t.get('type','waypoint'))}">
                        <span class="tl-km">{t.get('km','')} km</span>
                        <span class="tl-icon">{ICON.get(t.get('type'),'📍')}</span>
                        <div><strong>{esc(t.get('name'))}</strong><br>{esc(t.get('desc'))}</div>
                    </li>""")
    return f"""            <div class="route-step">
                <span class="step-label">路線節點：</span>
                <ul class="tl-list">
{chr(10).join(items)}
                </ul>
            </div>"""


def render_meals(d):
    m = d.get('meals') or {}
    if not m.get('lunch') and not m.get('dinner'):
        return f"""            <div class="meal-box meal-todo">
                <strong>🍴 餐食：待實地查證補上</strong>
                <div style="margin-top:4px; font-size:12.5px;">此日午餐／晚餐尚未查證確認。刻意留白而非填入未經查證的店家 —— 營業時間與單車停放狀況需逐一確認後才寫入。</div>
            </div>"""
    out = []
    for key, label, cls in (('lunch', '🍴 午餐', 'meal-lunch'), ('dinner', '🍻 晚餐', 'meal-dinner')):
        opts = m.get(key) or []
        if not opts:
            continue
        lis = []
        for o in opts:
            link = (f' （<a href="{esc(o["map"])}" target="_blank" rel="noopener">📍 Google Maps 導航 ↗</a>）'
                    if o.get('map') else '')
            tel = (f'<a href="tel:{tel_href(o["tel"])}" class="meal-tel">📞 {esc(o["tel"])}</a>'
                   if o.get('tel') else '')
            meta = []
            if o.get('hours'):
                meta.append(f"🕐 {esc(o['hours'])}")
            if o.get('closed'):
                meta.append(f"公休 {esc(o['closed'])}")
            if o.get('bike'):
                meta.append(f"📍 {esc(o['bike'])}")
            metaline = (f'<br><span class="meal-meta">{" ｜ ".join(meta)}</span>' if meta else '')
            src = (f'<span class="meal-src">查證：{esc(o["src"])}</span>' if o.get('src') else '')
            lis.append(f'<li><strong>{esc(o.get("name"))}</strong>'
                       f'{" — " + esc(o["note"]) if o.get("note") else ""}{link}{tel}{metaline}{src}</li>')
        out.append(f"""            <div class="meal-box {cls}">
                <strong>{label}{" — " + esc(m.get(key + "_note")) if m.get(key + "_note") else ""}</strong>
                <ul>{"".join(lis)}</ul>
            </div>""")
    return '\n'.join(out)


def render_hotel(d):
    h = d['hotel']
    if not h.get('name'):
        return ''
    status = ('<div class="booking-status status-booked">✅ 已完成訂房</div>' if h['booked']
              else '<div class="booking-status status-pending">🔍 尚未訂房 — 需儘早確認</div>')
    tel = (f'<a href="tel:{tel_href(h["tel"])}" class="hotel-tel">📞 {esc(h["tel"])}</a>'
           if h.get('tel') else '')
    link = (f'<a href="{esc(h["url"])}" target="_blank" rel="noopener" class="hotel-link">📍 在 Google Maps 查看旅館位置 ↗</a>'
            if h.get('url') else '')
    return f"""            <div class="hotel-box">
                <div class="hotel-name">🏨 住宿：{esc(h['name'])}</div>
                <div class="hotel-address">地址：{esc(h['addr'])}</div>
                {status}
                <div class="bike-store-info">{esc(h['bike'])}</div>
                <div class="hotel-actions">{link}{tel}</div>
            </div>"""


def _spread(stations, want=9):
    """站太多時（都心動輒上百站）依里程均勻取樣，保留頭尾。"""
    if len(stations) <= want:
        return stations
    lo, hi = stations[0]['km'], stations[-1]['km']
    span = max(hi - lo, 0.1)
    picked, used = [], set()
    for i in range(want):
        target = lo + span * i / (want - 1)
        best = min((s for s in stations if id(s) not in used),
                   key=lambda s: abs(s['km'] - target), default=None)
        if best is not None:
            used.add(id(best))
            picked.append(best)
    picked.sort(key=lambda s: s['km'])
    return picked


def render_bailout(d):
    b = d.get('bailout')
    if not b:
        return ''
    STRAT = {
        'A': ('策略 A · 沿線有站', 'bo-a'),
        'A+B': ('策略 A ＋ B · 部分路段無站', 'bo-ab'),
        'B': ('策略 B · 全線無站', 'bo-b'),
    }
    label, cls = STRAT.get(b['strategy'], ('撤退方案', 'bo-a'))

    # 上車規定
    lines_html = []
    for ln in b['lines']:
        cyc = ln['mode'].startswith('免拆車')
        rules = ''.join(f'<li>{esc(r)}</li>' for r in ln.get('rules', []))
        extra = []
        if ln.get('section'):
            extra.append(f"區間 {esc(ln['section'])}")
        if ln.get('fee'):
            extra.append(esc(ln['fee']))
        if ln.get('tel'):
            extra.append(f'☎ <a href="tel:{tel_href(ln["tel"].split("（")[0])}">{esc(ln["tel"])}</a>')
        warn = (f'<div class="bo-warn">{esc(ln["warning"])}</div>' if ln.get('warning') else '')
        note = (f'<div class="bo-note">{esc(ln["note"])}</div>' if ln.get('note') else '')
        lines_html.append(
            f'<div class="bo-line {"bo-cycle" if cyc else "bo-rinko"}">'
            f'<div class="bo-line-head">{"🚴‍♂️ 免拆車" if cyc else "🎒 需輪行袋"}'
            f'<strong>{esc(ln["label"])}</strong></div>'
            f'{"<div class=bo-meta>" + " ｜ ".join(extra) + "</div>" if extra else ""}'
            f'<ul>{rules}</ul>{warn}{note}'
            f'<div class="bo-src">查證：{esc(ln.get("src"))}</div></div>')

    # 沿線車站
    st = b['stations']
    if st:
        shown = _spread(st)
        # 交叉比對：サイクルトレイン 的排除站／限定站，避免推車到不能上車的站才發現
        cycs = [l for l in b['lines'] if l['mode'].startswith('免拆車')]

        def flag(name):
            """只在能確定判斷時才標記：站必須屬於該免拆車路線，
            再看它是否落在可上下車名單／排除名單。判不出來就不標。"""
            for c in cycs:
                on_line = set(c.get('line_stations') or [])
                if on_line and name not in on_line:
                    continue  # 這站不在這條線上，換下一條線判斷
                allowed = set(c.get('allowed') or [])
                excluded = set(c.get('excluded') or [])
                if name in excluded or (allowed and name not in allowed):
                    return '<em class="bo-x">此站需輪行袋</em>'
                if name in allowed or (on_line and not allowed):
                    return '<em class="bo-ok">免拆車可</em>'
            return ''

        chips = ''.join(
            f'<span class="bo-st"><b>{s["km"]}km</b> {esc(s["name"])}'
            f'{f"<i>+{s['off_km']}km</i>" if s["off_km"] >= 1.0 else ""}{flag(s["name"])}</span>'
            for s in shown)
        more = (f'<div class="bo-note">沿線共 {len(st)} 站，上表為依里程均勻取樣；'
                f'站名後的 +N km 為需偏離路線的距離。</div>' if len(st) > len(shown) else '')
        stations_html = f'<div class="bo-sub">🚉 沿線可撤退車站</div><div class="bo-chips">{chips}</div>{more}'
    else:
        stations_html = ''

    # 沒站區 → 策略 B
    gaps_html = []
    for g in b['gaps']:
        samples = []
        for s in g.get('samples', []):
            lodg = s.get('lodging') or []
            if not lodg:
                samples.append(f'<li><b>第 {s["at_km"]} km</b>：20 km 內查無登錄住宿 —— 此段最需避免天黑</li>')
                continue
            items = '、'.join(
                f'{esc(x["name"])}<span class="bo-det">偏離 {x["detour_km"]}km</span>' for x in lodg[:3])
            samples.append(f'<li><b>第 {s["at_km"]} km</b>：{items}</li>')
        body = (f'<ul class="bo-lodging">{"".join(samples)}</ul>' if samples
                else '<div class="bo-note">此段住宿查詢尚未完成。</div>')
        gaps_html.append(
            f'<div class="bo-gap"><div class="bo-gap-head">⚠️ 無站區間 {g["from_km"]}–{g["to_km"]} km'
            f'（連續 {g["span_km"]} km 無車站：{esc(g["after"])} ➜ {esc(g["before"])}）</div>'
            f'<div class="bo-note">此段無法搭車撤退，改採策略 B：於 20 km 內找住宿點。'
            f'以下為沿線實查之登錄住宿（OpenStreetMap）：</div>{body}</div>')

    cyc_names = '、'.join(l['label'].split('（')[0] for l in b['lines'] if l['mode'].startswith('免拆車'))
    if b['strategy'] == 'B':
        premise = ('<div class="bo-premise bo-premise-b">🎒 <strong>已備輪行袋，但本日派不上用場</strong> —— '
                   '全線 3 km 內沒有任何車站，無法搭車撤退。今天唯一的退路是下方的策略 B：'
                   '就近找住宿。行前請把水、糧食與保暖層帶足。</div>')
    else:
        premise = ('<div class="bo-premise">🎒 <strong>已備輪行袋</strong> —— 只要到得了車站，策略 A 隨時成立。'
                   + (f'本日另有 <strong>{esc(cyc_names)}</strong> 提供免拆車服務，可省下拆裝的 15–20 分鐘。'
                      if cyc_names else '本日無免拆車路線，一律需拆解裝袋。')
                   + ('　⚠️ 但本日有無站區間（見下方），該段仍須改用策略 B。' if b['gaps'] else '')
                   + '</div>')
    return f"""            <div class="bailout-box">
                <div class="bo-title">🚃 撤退方案 <span class="bo-badge {cls}">{esc(label)}</span></div>
                {premise}
                <div class="bo-sub">🚆 本日適用的單車上車規定</div>""" + f"""
                {''.join(lines_html)}
                {stations_html}
                {''.join(gaps_html)}
            </div>"""


def render_day_cards(trip, songs, seas=None):
    out = []
    for d in trip['days']:
        n, w, st = d['nav'], d['weather_hist'], d['stage']
        if st and st['first']:
            out.append(f"""        <div class="stage-header">
            <span>{esc(st['label'])}</span>
            <span>{esc(st['range'])}</span>
        </div>""")
        wx_pill = (f'<span class="weather-pill">{esc(w["icon"])} {w["lo"]}~{w["hi"]}°C ｜ {w["rain"]}mm</span>'
                   if w['lo'] is not None else '')
        # NAVITIME 走它自己選的路；本計畫刻意繞走專用道／避坑舊道，兩個里程都對，差異要講明
        planned = d['timeline'][-1].get('km') if d['timeline'] else None
        navkm = n.get('km')
        gapnote = ''
        if planned and navkm and abs(planned - navkm) >= 2.0 and abs(planned - navkm) / max(navkm, 1) > 0.05:
            longer = planned > navkm
            gapnote = (f'<div class="km-gap">📐 NAVITIME 最短路徑 <strong>{navkm} km</strong>，'
                       f'本計畫實走 <strong>{planned} km</strong>'
                       f'（{"刻意繞走自行車專用道／避坑舊道，多 " if longer else "較 NAVITIME 短 "}'
                       f'{abs(round(planned - navkm, 1))} km{"" if longer else "，以實走為準"}）。'
                       f'下方時間×地點矩陣的抵達時刻以<strong>實走里程</strong>推算。</div>')
        links = [f'<a href="{d["gpx"]}" download class="act-btn act-gpx">💾 下載 Day {d["day"]} GPX 軌跡</a>']
        if d.get('map_demo'):
            links.insert(0, f'<a href="{d["map_demo"]}" class="act-btn act-map">🗺️ Day {d["day"]} 詳細地圖與標高 Demo ➔</a>')
        culture = d.get('culture') or {}
        cul_rows = []
        for key, label in (('anime', '📺 動畫/漫畫聖地'), ('movie', '🎥 經典日劇/電影'), ('history', '🏯 歷史地理人文')):
            if culture.get(key):
                cul_rows.append(f'<div>・<strong>{label}：</strong> {esc(culture[key])}</div>')
        cul = (f"""            <div class="culture-box">
                <strong>🎬 影視動漫與歷史人文聖地巡禮：</strong>
                {"".join(cul_rows)}
            </div>""" if cul_rows else '')
        out.append(f"""        <!-- Day {d['day']} -->
        <div class="day-card" id="day-{d['day']}" data-date="{esc(d['date'])}">
            <div class="day-header">
                <div>
                    <div class="day-title"><span class="day-num">Day {d['day']}</span> {esc(d['date'])} {esc(d['route_line'])}</div>
                    <div class="day-stats">
                        <strong>{n.get('km','—')} km</strong> ｜ <span class="elev-pill">+{n.get('gain','—')} m / -{n.get('loss','—')} m</span> ｜ 海拔 {n.get('min_e','—')}~{n.get('max_e','—')} m
                        {wx_pill}
                        <span class="koyo-pill">🍁 {esc(d['foliage'])}</span>
                        <span class="nav-src">NAVITIME 實測</span>
                    </div>
{gapnote}
                    <div class="theme-weather-widget" data-day="{d['day']}">載入天氣中…</div>
{render_player(d['day'], songs)}
                </div>
            </div>
            <div class="day-content">
{render_timeline(d)}
{render_meals(d)}
{render_hotel(d)}
{render_bailout(d)}
{render_support(d, trip)}
            <div class="weather-box"><span class="weather-icon">{esc(w['icon'])}</span> 去年同日實測（氣象廳）：{esc(w['text'])} ｜ 氣溫 {w['lo']}°C ~ {w['hi']}°C ｜ 降水 {w['rain']}mm ｜ 日照 {w['sun']}h</div>
{render_seasonal_day(d['day'], seas)}
            <div class="foliage-box"><span class="foliage-icon">🍁</span> 紅葉預測：{esc(d['foliage'])}</div>
            <div class="highlight-badge">{d['expert_tip'] or ''}</div>
{cul}
            <div class="day-actions">{"".join(links)}</div>
            </div>
        </div>""")
    return '\n'.join(out)


# ─────────────────── 緊急聯絡 / 沿線支援 ───────────────────

def render_emergency_card(trip):
    em = trip.get('emergency') or {}
    if not em:
        return ''
    core = ''.join(
        f'<a class="em-card" href="tel:{tel_href(c["tel"])}">'
        f'<div class="em-num">{esc(c["tel"])}</div>'
        f'<div class="em-label">{esc(c["label"])}</div>'
        f'<div class="em-when">{esc(c["when"])}</div>'
        f'<div class="em-note">{esc(c["note"])}</div></a>'
        for c in em.get('core', []))
    pa = em.get('prefecture_advice') or {}
    rows = ''.join(
        f'<tr><td><strong>{esc(k)}</strong></td><td>{esc(v["name"])}</td>'
        f'<td>{esc(v["short"]) or "—"}</td>'
        f'<td>{"".join(f"<a href=tel:{tel_href(n)}>{esc(n.strip())}</a> " for n in v["tel"].split("／"))}</td>'
        f'<td>{esc(v["hours"])}</td></tr>'
        for k, v in pa.items() if not k.startswith('_'))
    acc = em.get('accident_checklist') or {}
    steps = ''.join(f'<li>{esc(s)}</li>' for s in acc.get('steps', []))
    return f"""        <h2 class="section-title">🚨 緊急聯絡 ｜ 出事時第一時間要打的電話</h2>
        <div class="emergency-block">
            <div class="em-grid">{core}</div>
            <div class="em-sub">{esc(pa.get('_label'))}</div>
            <div class="em-note-line">{esc(pa.get('_note'))}</div>
            <div class="table-wrapper"><table class="em-table"><thead><tr>
                <th>都縣</th><th>窗口</th><th>短碼</th><th>完整號碼</th><th>時間</th>
            </tr></thead><tbody>{rows}</tbody></table></div>
            <div class="em-checklist"><strong>🩹 {esc(acc.get('_label'))}</strong><ol>{steps}</ol></div>
            <div class="em-src">{esc(em.get('_verified'))} ｜ 來源：{esc(pa.get('_src'))}</div>
        </div>"""


def render_support(d, trip):
    """沿線單車店與醫院 + 當日所在都縣的救急相談電話。"""
    sp = d.get('support') or {}
    bikes, hosps = sp.get('bike_shops') or [], sp.get('hospitals') or []
    if not bikes and not hosps and not d.get('prefectures'):
        return ''

    def chips(items, cls, empty):
        if not items:
            return f'<div class="sp-empty">{empty}</div>'
        out = []
        for x in items:
            tel = (f'<a href="tel:{tel_href(x["tel"])}">📞</a>'
                   if x.get('tel') else '')
            hrs = f'<i>{esc(x["hours"])}</i>' if x.get('hours') else ''
            off = f'<u>+{x["off_km"]}km</u>' if x['off_km'] >= 0.5 else ''
            out.append(f'<span class="sp-chip {cls}"><b>{x["km"]}km</b> {esc(x["name"])}{off}{tel}{hrs}</span>')
        return f'<div class="sp-chips">{"".join(out)}</div>'

    pa = ((trip.get('emergency') or {}).get('prefecture_advice')) or {}
    pref_rows = []
    for p in d.get('prefectures', []):
        v = pa.get(p)
        if not v:
            continue
        nums = ' ／ '.join(
            f'<a href="tel:{tel_href(n)}">{esc(n.strip())}</a>' for n in v['tel'].split('／'))
        pref_rows.append(f'<li><strong>{esc(p)}</strong> {esc(v["name"])}：'
                         f'{esc(v["short"]) + " ／ " if v["short"] else ""}{nums}（{esc(v["hours"])}）</li>')
    pref_html = (f'<div class="sp-label">🚨 本日所在都縣・該叫救護車嗎</div><ul class="sp-pref">{"".join(pref_rows)}</ul>'
                 if pref_rows else '')

    bt, ht = sp.get('bike_total', 0), sp.get('hospital_total', 0)
    more_b = f'（沿線 5 km 內共 {bt} 家，依里程取樣）' if bt > len(bikes) else ''
    more_h = f'（沿線 10 km 內共 {ht} 家，依里程取樣）' if ht > len(hosps) else ''
    return f"""            <div class="support-box">
                <div class="sp-title">🔧 沿線支援</div>
                <div class="sp-label">🚲 單車店 <span class="sp-more">{more_b}</span></div>
                {chips(bikes, 'sp-bike', '⚠️ 本日路線 5 km 內查無登錄單車店 —— 補胎工具與備胎務必自帶，出發前檢查胎壓與煞車。')}
                <div class="sp-label">🏥 醫院 <span class="sp-more">{more_h}</span></div>
                {chips(hosps, 'sp-hosp', '⚠️ 本日路線 10 km 內查無登錄醫院。')}
                {pref_html}
                <div class="sp-src">單車店與醫院位置取自 OpenStreetMap，僅供定位參考；營業時間請以現場或電話為準。</div>
            </div>"""


# ─────────────────── 首屏數字卡 / 緩衝日 ───────────────────

def render_stats_grid(trip):
    m = trip['meta']
    longest = max(trip['days'], key=lambda d: d.get('planned_km') or d['nav'].get('km', 0))
    hardest = max(trip['days'], key=lambda d: d['nav'].get('gain', 0))
    cards = [
        (f"{m['days']} 天", '總騎行天數'),
        (f"{m.get('total_planned_km', m['total_km'])} km", '實走總里程（本計畫路線）'),
        (f"{m['total_km']} km", 'NAVITIME 最短路徑'),
        (f"+{m['total_gain']:,} m", 'NAVITIME 實測總爬升'),
        (f"Day {longest['day']}", f"最長單日 {longest.get('planned_km') or longest['nav']['km']} km"),
        (f"Day {hardest['day']}", f"最硬單日 +{hardest['nav']['gain']} m"),
        (f"{m['booked']} / {m['days']}", '已完成訂房'),
    ]
    inner = ''.join(f'<div class="stat-card"><div class="val">{v}</div><div class="label">{l}</div></div>'
                    for v, l in cards)
    return f'        <div class="stats-grid">{inner}</div>'


def render_buffer_days(trip):
    """挑出真正可當緩衝的短里程日。排除首日（取車）與末日（還車返程），
    兩者行程固定、無法拿來吸收天候延誤。"""
    mid = [d for d in trip['days'] if d['day'] not in (1, trip['meta']['days'])]
    picks = sorted(mid, key=lambda d: (d['nav'].get('km', 0), d['nav'].get('gain', 0)))[:3]
    picks.sort(key=lambda d: d['day'])
    lis = []
    for d in picks:
        where = (d['hotel']['name'] or '').split('/')[0].strip()[:20]
        lis.append(f"<li><strong>Day {d['day']}（{esc(where)}）— {d['nav']['km']} km ／ +{d['nav']['gain']} m</strong>："
                   f"當日騎乘量低，遇雨可整日兩鐵輪行、提早入住，或把行程往後平移一天。</li>")
    lis.append('<li><strong>每日騎乘多為 2.5 ~ 4 小時</strong>：秋冬降雨多為 2-3 小時短暫冷鋒，'
               '可利用早晨或午後空檔避開 —— 上方<a href="#war-room">天氣作戰室</a>的「時間 × 地點」矩陣正是為此而設。</li>')
    return '\n                        '.join(lis)


# ─────────────────────── 天氣作戰室 ───────────────────────

def render_war_room(trip):
    opts = ''.join(f'<option value="{d["day"]}">Day {d["day"]} {esc(d["date"])} {esc(d["route_line"])[:22]}</option>'
                   for d in trip['days'])
    return f"""        <h2 class="section-title">🌦️ 天氣作戰室 ｜ 按小時 × 按地點的騎行決策台</h2>
        <div class="war-room" id="war-room">
            <div class="wr-banner" id="wr-banner">初始化中…</div>

            <div class="wr-controls">
                <label>檢視日程
                    <select id="wr-day">{opts}</select>
                </label>
                <label>出發時間
                    <input type="time" id="wr-start" value="08:30">
                </label>
                <label>巡航均速
                    <select id="wr-speed">
                        <option value="12">12 km/h（重裝爬坡）</option>
                        <option value="15" selected>15 km/h（重裝巡航）</option>
                        <option value="18">18 km/h（輕裝平路）</option>
                        <option value="22">22 km/h（快騎）</option>
                    </select>
                </label>
                <button type="button" id="wr-reload" class="wr-btn">↻ 重新取得</button>
            </div>

            <div class="wr-tabs">
                <button type="button" class="wr-tab active" data-pane="today">☀️ 今日 · 時間 × 地點</button>
                <button type="button" class="wr-tab" data-pane="tomorrow">🌤️ 明日 · 時間 × 地點</button>
                <button type="button" class="wr-tab" data-pane="week">📅 一週 · 按地點</button>
            </div>

            <div class="wr-pane active" id="wr-pane-today"><div class="wr-loading">載入中…</div></div>
            <div class="wr-pane" id="wr-pane-tomorrow"><div class="wr-loading">載入中…</div></div>
            <div class="wr-pane" id="wr-pane-week"><div class="wr-loading">載入中…</div></div>

            <div class="wr-legend">
                <span><i class="sw sw0"></i> 0–19%</span><span><i class="sw sw1"></i> 20–39%</span>
                <span><i class="sw sw2"></i> 40–59%</span><span><i class="sw sw3"></i> 60–79%</span>
                <span><i class="sw sw4"></i> 80%+</span>
                <span class="wr-eta-key">◉ = 依均速預計抵達該點的時段</span>
                <span class="wr-src">資料：Open-Meteo（免金鑰）｜ 時區 Asia/Tokyo</span>
            </div>
        </div>"""


def render_weather_js(trip):
    days = [{'day': d['day'], 'date': d['date'],
             'iso': None,
             'route': esc(d['route_line'])[:40],
             'hist': {'lo': d['weather_hist']['lo'], 'hi': d['weather_hist']['hi'],
                      'rain': d['weather_hist']['rain'], 'icon': d['weather_hist']['icon'],
                      'text': d['weather_hist']['text']},
             'pts': [{'n': t['name'], 'km': t.get('km', 0),
                      'lat': round(t['coord'][1], 4), 'lon': round(t['coord'][0], 4)}
                     for t in d['timeline']]}
            for d in trip['days']]
    # 由 meta.start 推算每天的實際日期
    from datetime import date, timedelta
    y, m, dd = map(int, trip['meta']['start'].split('-'))
    base = date(y, m, dd)
    for i, d in enumerate(days):
        d['iso'] = (base + timedelta(days=i)).isoformat()
    payload = json.dumps(days, ensure_ascii=False, separators=(',', ':'))
    return "<script>\nconst TRIP_DAYS = " + payload + ";\n" + WEATHER_JS_BODY + "\n</script>"


WEATHER_JS_BODY = r"""
const WX_TZ = 'Asia/Tokyo';
const WX_HOURS = [6,7,8,9,10,11,12,13,14,15,16,17,18,19,20];
const WX_HORIZON = 16;               // Open-Meteo 免費預報上限（天）
const WX_REST_MIN_PER_STOP = 12;     // 每個節點的停留緩衝（分鐘）

function wxCode(c){
  if(c===0) return {e:'☀️',t:'晴'};
  if(c<=3)  return {e:'⛅',t:'多雲'};
  if(c===45||c===48) return {e:'🌫️',t:'霧'};
  if(c<=57) return {e:'🌦️',t:'毛毛雨'};
  if(c<=67) return {e:'🌧️',t:'雨'};
  if(c<=77) return {e:'❄️',t:'雪'};
  if(c<=82) return {e:'🌦️',t:'陣雨'};
  if(c<=86) return {e:'🌨️',t:'陣雪'};
  return {e:'⛈️',t:'雷雨'};
}
function popClass(p){ if(p==null) return 'sw0'; if(p<20) return 'sw0'; if(p<40) return 'sw1'; if(p<60) return 'sw2'; if(p<80) return 'sw3'; return 'sw4'; }
function todayISO(){ return new Date().toLocaleDateString('sv-SE',{timeZone:WX_TZ}); }
function daysBetween(a,b){ return Math.round((new Date(b+'T00:00:00Z')-new Date(a+'T00:00:00Z'))/86400000); }

/* 依出發時間與均速推算每個節點的抵達時刻 */
function etaFor(pts, startHHMM, speed){
  const [h,m] = startHHMM.split(':').map(Number);
  const t0 = h*60 + m;
  return pts.map((p,i)=>{
    const mins = t0 + (Number(p.km)/speed)*60 + i*WX_REST_MIN_PER_STOP;
    return {idx:i, minutes:mins, hour:Math.floor(mins/60),
            label:String(Math.floor(mins/60)%24).padStart(2,'0')+':'+String(Math.round(mins%60)).padStart(2,'0')};
  });
}

/* 一次抓多個地點的逐時預報（Open-Meteo 支援逗號分隔的多座標） */
async function fetchHourly(pts, isoDate){
  const lat = pts.map(p=>p.lat).join(','), lon = pts.map(p=>p.lon).join(',');
  const u = 'https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+
    '&hourly=temperature_2m,apparent_temperature,precipitation_probability,precipitation,weather_code,wind_speed_10m'+
    '&timezone='+encodeURIComponent(WX_TZ)+'&start_date='+isoDate+'&end_date='+isoDate;
  const r = await fetch(u); if(!r.ok) throw new Error('HTTP '+r.status);
  const j = await r.json();
  return Array.isArray(j) ? j : [j];
}

async function fetchDaily(spots, startISO, endISO){
  const lat = spots.map(p=>p.lat).join(','), lon = spots.map(p=>p.lon).join(',');
  const u = 'https://api.open-meteo.com/v1/forecast?latitude='+lat+'&longitude='+lon+
    '&daily=weather_code,temperature_2m_max,temperature_2m_min,precipitation_probability_max,precipitation_sum,wind_speed_10m_max'+
    '&timezone='+encodeURIComponent(WX_TZ)+'&start_date='+startISO+'&end_date='+endISO;
  const r = await fetch(u); if(!r.ok) throw new Error('HTTP '+r.status);
  const j = await r.json();
  return Array.isArray(j) ? j : [j];
}

const SNOW_CODES = new Set([71,73,75,77,85,86]);
const WX_WIND_ALERT = 8;      // m/s，側風／逆風騎乘明顯吃力的門檻
const WX_COLD_ALERT = 8;      // °C，體感溫度＋降雨合併判斷失溫風險的門檻

/* 掃描候選出發時間，找全線最高降雨機率最低的一個（用同一批已抓到的 series，不多打 API） */
function suggestBestStart(pts, series, curStart, speed){
  if(!series) return null;
  const candidates = ['06:30','07:00','07:30','08:00','08:30','09:00','09:30','10:00'];
  function riskOf(hhmm){
    const eta = etaFor(pts, hhmm, speed);
    let maxPop = -1;
    pts.forEach((p,i)=>{
      const hh = series[i] && series[i].hourly;
      if(!hh) return;
      const k = hh.time.findIndex(t=>Number(t.slice(11,13))===eta[i].hour);
      const pop = k>=0 ? hh.precipitation_probability[k] : null;
      if(pop!=null && pop>maxPop) maxPop = pop;
    });
    return maxPop;
  }
  const curRisk = riskOf(curStart);
  let best = {hhmm:curStart, risk:curRisk};
  candidates.forEach(c=>{
    const r = riskOf(c);
    if(r>=0 && (best.risk<0 || r<best.risk)) best = {hhmm:c, risk:r};
  });
  if(curRisk>=0 && best.hhmm!==curStart && (curRisk-best.risk)>=15){
    return '<div class="wr-suggest">💡 掃描 06:30–10:00 出發時段：<strong>'+best.hhmm+'</strong> 出發全線最高降雨機率最低（'+best.risk+
      '%），比你目前設定的 '+curStart+'（'+curRisk+'%）低。</div>';
  }
  if(curRisk>=0 && curRisk<20){
    return '<div class="wr-suggest">✅ 你目前設定的出發時間 '+curStart+' 已經是本日風險較低的區間之一（全線最高降雨機率 '+curRisk+'%）。</div>';
  }
  return null;
}

/* ── A/B：時間 × 地點 熱力矩陣 ── */
function renderMatrix(day, series, startHHMM, speed){
  const pts = day.pts, eta = etaFor(pts, startHHMM, speed);
  let head = '<th class="wr-corner">地點 / 里程</th>' + WX_HOURS.map(h=>'<th>'+String(h).padStart(2,'0')+'</th>').join('');
  let rows = '', cautions = [], severes = [];
  pts.forEach((p,i)=>{
    const s = series ? series[i] : null;
    const hh = s && s.hourly ? s.hourly : null;
    let tds = '';
    WX_HOURS.forEach(h=>{
      const k = hh ? hh.time.findIndex(t=>Number(t.slice(11,13))===h) : -1;
      const pop = k>=0 ? hh.precipitation_probability[k] : null;
      const tmp = k>=0 ? Math.round(hh.temperature_2m[k]) : null;
      const feel = k>=0 ? hh.apparent_temperature[k] : null;
      const wind = k>=0 ? hh.wind_speed_10m[k] : null;
      const code = k>=0 ? hh.weather_code[k] : null;
      const isEta = eta[i].hour===h;
      const cls = 'wx-c '+popClass(pop)+(isEta?' wx-eta':'');
      let inner = '';
      if(isEta){ inner = '<b>◉</b>'; }
      if(tmp!=null && (isEta || pop>=40)) inner += '<span class="wx-v">'+tmp+'°<br>'+(pop==null?'':pop+'%')+'</span>';
      if(isEta){
        const isSnow = code!=null && SNOW_CODES.has(code);
        const isCold = feel!=null && feel<WX_COLD_ALERT && (pop==null || pop>=40 || (k>=0 && hh.precipitation[k]>0));
        const isWindy = wind!=null && wind>=WX_WIND_ALERT;
        if(isSnow) severes.push('❄️ '+eta[i].label+' '+p.n+'（降雪，路面可能結冰）');
        if(isCold) severes.push('🥶 '+eta[i].label+' '+p.n+'（體感 '+Math.round(feel)+'°C＋降雨，注意失溫）');
        if(pop!=null && pop>=40) cautions.push('☔ '+eta[i].label+' '+p.n+'（降雨機率 '+pop+'%）');
        if(isWindy) cautions.push('💨 '+eta[i].label+' '+p.n+'（風速 '+wind.toFixed(1)+' m/s）');
      }
      tds += '<td class="'+cls+'" title="'+String(h).padStart(2,'0')+':00 '+p.n+(pop!=null?' 降雨 '+pop+'%':'')+(tmp!=null?' '+tmp+'°C':'')+(wind!=null?' 風速 '+wind.toFixed(1)+'m/s':'')+'">'+inner+'</td>';
    });
    rows += '<tr><th class="wr-rowhead"><span class="wr-pn">'+p.n+'</span><span class="wr-km">'+p.km+' km · 預計 '+eta[i].label+'</span></th>'+tds+'</tr>';
  });
  const severeHtml = severes.length ? '<div class="wr-alert-severe">🚨 高風險：<br>'+severes.map(a=>'・'+a).join('<br>')+'</div>' : '';
  const cautionHtml = cautions.length ? '<div class="wr-alert">⚠️ 依你的出發時間與均速，下列節點通過時需注意：<br>'+cautions.map(a=>'・'+a).join('<br>')+'</div>' : '';
  const okHtml = (!severes.length && !cautions.length) ? '<div class="wr-ok">✅ 依目前預報，全線通過時段皆無明顯降雨／強風／低溫風險。</div>' : '';
  const suggestHtml = series ? (suggestBestStart(pts, series, startHHMM, speed) || '') : '';
  return '<div class="wr-title">Day '+day.day+' · '+day.date+' · '+day.route+
         '<span class="wr-sub">出發 '+startHHMM+' ｜ 均速 '+speed+' km/h ｜ 每點停留 '+WX_REST_MIN_PER_STOP+' 分</span></div>'+
         (series?(suggestHtml+severeHtml+cautionHtml+okHtml):'')+
         '<div class="wr-scroll"><table class="wx-matrix"><thead><tr>'+head+'</tr></thead><tbody>'+rows+'</tbody></table></div>';
}

function renderReference(day, why){
  const h = day.hist;
  const pts = day.pts.map(p=>'<li><strong>'+p.n+'</strong> <span class="wr-km">'+p.km+' km</span></li>').join('');
  return '<div class="wr-title">Day '+day.day+' · '+day.date+' · '+day.route+'</div>'+
    '<div class="wr-note">'+why+'</div>'+
    '<div class="wr-hist">📊 <strong>去年同日實測（日本氣象廳）</strong>：'+(h.icon||'')+' '+(h.text||'')+
    ' ｜ '+h.lo+'°C ~ '+h.hi+'°C ｜ 降水 '+h.rain+'mm</div>'+
    '<div class="wr-note-sub">本日路線節點（預報開放後將自動填入逐時降雨與氣溫）：</div><ul class="wr-ptlist">'+pts+'</ul>';
}

/* ── C：一週 · 按地點 ── */
function renderWeek(rows){
  if(!rows) return '';
  let head='<th>日程</th><th>地點</th><th>天氣</th><th>最高/最低</th><th>降雨機率</th><th>雨量</th><th>最大風速</th>';
  let body = rows.map(r=>{
    const w = wxCode(r.code);
    const isSnow = SNOW_CODES.has(r.code);
    const isWindy = r.wind!=null && r.wind>=WX_WIND_ALERT;
    const rowCls = isSnow ? 'wk-snow' : (r.pop>=40 ? 'wk-wet' : (isWindy ? 'wk-windy' : ''));
    return '<tr'+(rowCls?' class="'+rowCls+'"':'')+'>'+
      '<td><strong>Day '+r.day+'</strong><br><small>'+r.date+'</small></td>'+
      '<td>'+r.spot+'</td>'+
      '<td>'+w.e+' '+w.t+'</td>'+
      '<td>'+Math.round(r.hi)+'° / '+Math.round(r.lo)+'°</td>'+
      '<td class="'+popClass(r.pop)+'">'+(r.pop==null?'—':r.pop+'%')+'</td>'+
      '<td>'+(r.mm==null?'—':r.mm+' mm')+'</td>'+
      '<td>'+(isWindy?'💨 ':'')+(r.wind==null?'—':Math.round(r.wind)+' m/s')+'</td></tr>';
  }).join('');
  return '<div class="wr-scroll"><table class="wx-week"><thead><tr>'+head+'</tr></thead><tbody>'+body+'</tbody></table></div>';
}

/* ── 主流程 ── */
const WR = {day:null, start:'08:30', speed:15};

function activeDayIndex(){
  const t = todayISO();
  const i = TRIP_DAYS.findIndex(d=>d.iso===t);
  return i>=0 ? i : 0;
}

async function paneMatrix(dayObj, elId){
  const el = document.getElementById(elId);
  const gap = daysBetween(todayISO(), dayObj.iso);
  if(gap < 0 || gap > WX_HORIZON){
    const why = gap<0 ? '此日程已過。' :
      '距離 '+dayObj.date+' 還有 <strong>'+gap+' 天</strong>，超出 Open-Meteo 的 '+WX_HORIZON+
      ' 天預報範圍。抵達 '+WX_HORIZON+' 天內時，本表會自動換成逐時 × 逐點的真實預報。';
    el.innerHTML = renderReference(dayObj, why);
    return;
  }
  el.innerHTML = '<div class="wr-loading">取得 '+dayObj.pts.length+' 個節點的逐時預報中…</div>';
  try{
    const s = await fetchHourly(dayObj.pts, dayObj.iso);
    el.innerHTML = renderMatrix(dayObj, s, WR.start, WR.speed);
  }catch(e){
    el.innerHTML = '<div class="wr-err">天氣服務暫時無法連線（'+e.message+'）。'+
      '<button type="button" class="wr-btn" onclick="wrRefresh()">重試</button></div>'+renderReference(dayObj,'以下為離線可用的歷史參考：');
  }
}

async function paneWeek(){
  const el = document.getElementById('wr-pane-week');
  const t = todayISO();
  const upcoming = TRIP_DAYS.filter(d=>daysBetween(t,d.iso)>=0).slice(0,7);
  const list = upcoming.length ? upcoming : TRIP_DAYS.slice(0,7);
  const inRange = list.filter(d=>daysBetween(t,d.iso)<=WX_HORIZON);
  if(!inRange.length){
    const gap = daysBetween(t, TRIP_DAYS[0].iso);
    el.innerHTML = '<div class="wr-note">距離出發還有 <strong>'+gap+' 天</strong>，超出 '+WX_HORIZON+
      ' 天預報範圍。以下為各日<strong>去年同日氣象廳實測</strong>，出發前 '+WX_HORIZON+' 天內會自動換成真實預報。</div>'+
      '<div class="wr-scroll"><table class="wx-week"><thead><tr><th>日程</th><th>路線</th><th>去年天氣</th><th>最高/最低</th><th>降水</th></tr></thead><tbody>'+
      list.map(d=>'<tr><td><strong>Day '+d.day+'</strong><br><small>'+d.date+'</small></td><td>'+d.route+'</td><td>'+
        (d.hist.icon||'')+' '+(d.hist.text||'')+'</td><td>'+d.hist.hi+'° / '+d.hist.lo+'°</td><td>'+d.hist.rain+' mm</td></tr>').join('')+
      '</tbody></table></div>';
    return;
  }
  el.innerHTML = '<div class="wr-loading">取得未來 '+inRange.length+' 日的地點預報中…</div>';
  try{
    const spots = inRange.map(d=>{ const p=d.pts[d.pts.length-1]; return {lat:p.lat, lon:p.lon, name:p.n}; });
    const s0 = inRange[0].iso, s1 = inRange[inRange.length-1].iso;
    const res = await fetchDaily(spots, s0, s1);
    const rows = inRange.map((d,i)=>{
      const dd = res[i].daily, k = dd.time.indexOf(d.iso);
      return {day:d.day, date:d.date, spot:spots[i].name,
              code:dd.weather_code[k], hi:dd.temperature_2m_max[k], lo:dd.temperature_2m_min[k],
              pop:dd.precipitation_probability_max[k], mm:dd.precipitation_sum[k], wind:dd.wind_speed_10m_max[k]};
    });
    el.innerHTML = '<div class="wr-note">每一列取<strong>當日終點所在地</strong>的預報 —— 決定隔天要不要調整行程時看這張。</div>'+renderWeek(rows);
  }catch(e){
    el.innerHTML = '<div class="wr-err">一週預報取得失敗（'+e.message+'）。<button type="button" class="wr-btn" onclick="wrRefresh()">重試</button></div>';
  }
}

function wrBanner(){
  const t = todayISO(), gap = daysBetween(t, TRIP_DAYS[0].iso);
  const el = document.getElementById('wr-banner');
  if(gap>0){
    el.className='wr-banner wr-pre';
    el.innerHTML='🗓️ 距離 11/13 出發還有 <strong>'+gap+' 天</strong>。'+
      (gap>WX_HORIZON ? '目前顯示去年同日氣象廳實測作為參考；進入 '+WX_HORIZON+' 天預報範圍後會自動切換為真實逐時預報。'
                      : '已進入預報範圍，顯示真實逐時預報。');
  } else if(gap<=0 && daysBetween(t, TRIP_DAYS[TRIP_DAYS.length-1].iso)>=0){
    const i=activeDayIndex();
    el.className='wr-banner wr-live';
    el.innerHTML='🚴 騎行中 — 今天是 <strong>Day '+TRIP_DAYS[i].day+'（'+TRIP_DAYS[i].date+'）</strong>：'+TRIP_DAYS[i].route;
  } else {
    el.className='wr-banner wr-post';
    el.innerHTML='🏁 行程已結束。以下為完整資料保存。';
  }
}

async function wrRefresh(){
  const i = WR.day==null ? activeDayIndex() : TRIP_DAYS.findIndex(d=>d.day===WR.day);
  const cur = TRIP_DAYS[i], nxt = TRIP_DAYS[Math.min(i+1, TRIP_DAYS.length-1)];
  document.getElementById('wr-day').value = cur.day;
  await paneMatrix(cur, 'wr-pane-today');
  await paneMatrix(nxt, 'wr-pane-tomorrow');
  await paneWeek();
}

/* 每日卡片內嵌的小天氣列 */
async function inlineWeather(){
  const els = [...document.querySelectorAll('.theme-weather-widget')];
  const t = todayISO();
  const io2 = new IntersectionObserver(async (ents)=>{
    for(const en of ents){
      if(!en.isIntersecting) continue;
      io2.unobserve(en.target);
      const dn = Number(en.target.dataset.day);
      const d = TRIP_DAYS.find(x=>x.day===dn); if(!d) continue;
      const gap = daysBetween(t, d.iso);
      if(gap<0 || gap>WX_HORIZON){
        en.target.innerHTML = '<span class="iw-ref">📊 去年同日：'+(d.hist.icon||'')+' '+d.hist.hi+'° / '+d.hist.lo+'° ｜ 降水 '+d.hist.rain+'mm'+
          (gap>WX_HORIZON?' ｜ <span class="iw-cd">預報 '+(gap-WX_HORIZON)+' 天後開放</span>':'')+'</span>';
        continue;
      }
      try{
        const mid = d.pts[Math.floor(d.pts.length/2)];
        const s = await fetchDaily([{lat:mid.lat,lon:mid.lon}], d.iso, d.iso);
        const dd = s[0].daily, w = wxCode(dd.weather_code[0]);
        const pop = dd.precipitation_probability_max[0];
        en.target.innerHTML = '<span class="iw-live">'+w.e+' '+w.t+' ｜ '+Math.round(dd.temperature_2m_max[0])+'° / '+
          Math.round(dd.temperature_2m_min[0])+'° ｜ 降雨機率 '+pop+'%</span>'+
          (pop>=40?'<a class="iw-jump" href="#war-room">⚠️ 看逐時 × 逐點矩陣 ➔</a>':'');
      }catch(e){ en.target.innerHTML='<span class="iw-ref">天氣暫時無法連線</span>'; }
    }
  },{rootMargin:'150px'});
  els.forEach(e=>io2.observe(e));
}

document.addEventListener('DOMContentLoaded', ()=>{
  wrBanner();
  const sel=document.getElementById('wr-day'), st=document.getElementById('wr-start'), sp=document.getElementById('wr-speed');
  sel.value = TRIP_DAYS[activeDayIndex()].day;
  sel.addEventListener('change', e=>{ WR.day=Number(e.target.value); wrRefresh(); });
  st.addEventListener('change', e=>{ WR.start=e.target.value; wrRefresh(); });
  sp.addEventListener('change', e=>{ WR.speed=Number(e.target.value); wrRefresh(); });
  document.getElementById('wr-reload').addEventListener('click', wrRefresh);
  document.querySelectorAll('.wr-tab').forEach(b=>b.addEventListener('click', ()=>{
    document.querySelectorAll('.wr-tab').forEach(x=>x.classList.remove('active'));
    document.querySelectorAll('.wr-pane').forEach(x=>x.classList.remove('active'));
    b.classList.add('active');
    document.getElementById('wr-pane-'+b.dataset.pane).classList.add('active');
  }));
  wrRefresh();
  inlineWeather();
});
"""


def render_extra_css():
    return r"""
/* ── JMA 季節預報（３か月予報）── */
.seasonal-note{background:#F5F3FF;border:1px solid #DDD6FE;color:#4C1D95;border-radius:12px;padding:14px 17px;font-size:12.5px;line-height:1.85;margin-bottom:14px}
.seasonal-note .sn-head{font-size:14px;font-weight:800;margin-bottom:6px}
.seasonal-note ul{margin:4px 0 8px 20px;padding:0}
.seasonal-note li{margin:3px 0}
.seasonal-note .sn-enso{border-top:1px dashed #C4B5FD;padding-top:8px;margin-top:4px}
.seasonal-note .sn-warn{background:#FFF7ED;border:1px solid #FED7AA;color:#9A3412;border-radius:8px;padding:8px 11px;margin-top:8px}
.seasonal-note .sn-next{margin-top:8px;color:#6D28D9;font-weight:700}
.seasonal-note code{background:#EDE9FE;border-radius:4px;padding:1px 6px;font-size:11.5px}
.seasonal-note a{color:#6D28D9}
/* 紅葉見頃予想：與季節預報同一層，改用楓紅色系區隔 */
.foliage-note{background:#FEF2F2;border-color:#FECACA;color:#7F1D1D}
.foliage-note .sn-head{color:#991B1B}
.foliage-note .sn-next{color:#B91C1C}
.foliage-note .sn-next a,.foliage-note a{color:#B91C1C}
.foliage-note .fn-region{border-top:1px dashed #FCA5A5;padding-top:8px;margin-top:4px}
.foliage-note .fn-table{width:100%;min-width:520px;border-collapse:collapse;margin:8px 0;font-size:11.5px}
.foliage-note .fn-table th,.foliage-note .fn-table td{border:1px solid #FECACA;padding:5px 7px;text-align:left;vertical-align:top}
.foliage-note .fn-table th{background:#FEE2E2;font-weight:800}
.foliage-note .fn-table small{opacity:.75}
/* 表格欄內：色彩交給主題（深色列會反轉），只用虛線與 🔭 跟上面的去年實測分開 */
.wx-outlook{margin-top:7px;padding-top:6px;border-top:1px dashed rgba(139,92,246,.5);color:inherit;opacity:.88;font-size:11px;line-height:1.6}
.wx-outlook.wx-none{border-top-color:rgba(148,163,184,.5);opacity:.6}
.seasonal-box{background:#F5F3FF;border:1px solid #DDD6FE;color:#4C1D95;border-radius:8px;padding:10px 13px;font-size:12.5px;line-height:1.8;margin-top:10px}
.seasonal-box.seasonal-none{background:#F8FAFC;border-color:#E2E8F0;color:#64748B}

/* ── 天氣作戰室 ── */
.war-room{background:#FFF;border:1px solid var(--card-border);border-radius:14px;padding:18px;margin-bottom:28px;box-shadow:0 4px 14px rgba(0,0,0,.04)}
.wr-banner{border-radius:8px;padding:10px 14px;font-size:13.5px;margin-bottom:14px}
.wr-banner.wr-pre{background:var(--tip-bg);border:1px solid var(--tip-border);color:var(--tip-text)}
.wr-banner.wr-live{background:var(--success-bg);border:1px solid var(--success-border);color:var(--success-text)}
.wr-banner.wr-post{background:#F1F5F9;border:1px solid #CBD5E1;color:#475569}
.wr-controls{display:flex;flex-wrap:wrap;gap:12px;align-items:flex-end;margin-bottom:14px}
.wr-controls label{display:flex;flex-direction:column;gap:4px;font-size:12px;color:var(--text-muted);font-weight:700}
.wr-controls select,.wr-controls input{padding:7px 10px;border:1px solid var(--card-border);border-radius:7px;font-size:13px;font-family:inherit;background:#FFF;color:var(--text-dark)}
.wr-controls select{max-width:320px}
.wr-btn{padding:8px 14px;border:1px solid var(--card-border);border-radius:7px;background:#F8FAFC;font-size:12.5px;font-weight:700;cursor:pointer;color:var(--text-dark)}
.wr-btn:hover{background:#EEF2F7}
.wr-tabs{display:flex;gap:6px;border-bottom:2px solid var(--card-border);margin-bottom:14px;flex-wrap:wrap}
.wr-tab{padding:9px 14px;border:0;background:none;font-size:13.5px;font-weight:700;color:var(--text-muted);cursor:pointer;border-bottom:3px solid transparent;margin-bottom:-2px;font-family:inherit}
.wr-tab.active{color:var(--primary);border-bottom-color:var(--primary)}
.wr-pane{display:none}
.wr-pane.active{display:block}
.wr-title{font-size:15px;font-weight:800;color:#1E293B;margin-bottom:10px}
.wr-title .wr-sub{display:block;font-size:12px;font-weight:600;color:var(--text-muted);margin-top:3px}
.wr-scroll{overflow-x:auto;-webkit-overflow-scrolling:touch}
table.wx-matrix{border-collapse:separate;border-spacing:2px;font-size:11.5px;min-width:640px}
table.wx-matrix th{font-weight:700;color:var(--text-muted);padding:3px 5px;font-size:11px;white-space:nowrap}
table.wx-matrix .wr-corner{text-align:left}
table.wx-matrix .wr-rowhead{text-align:left;background:#F8FAFC;border-radius:6px;padding:6px 9px;position:sticky;left:0;z-index:2;box-shadow:2px 0 4px rgba(0,0,0,.04);max-width:190px}
.wr-pn{display:block;font-size:12px;color:var(--text-dark);font-weight:700;white-space:normal}
.wr-km{display:block;font-size:10.5px;color:var(--text-muted);font-weight:600}
td.wx-c{width:38px;height:38px;text-align:center;border-radius:6px;vertical-align:middle;line-height:1.15}
td.wx-c .wx-v{display:block;font-size:9.5px;font-weight:700;color:#0F172A}
td.wx-c b{font-size:13px;color:#B91C1C}
td.wx-eta{outline:2px solid var(--primary);outline-offset:-2px}
.sw0{background:#F1F5F9}.sw1{background:#DBEAFE}.sw2{background:#93C5FD}.sw3{background:#60A5FA}.sw4{background:#3B82F6}
td.sw0{background:#F1F5F9}td.sw1{background:#DBEAFE}td.sw2{background:#93C5FD}td.sw3{background:#60A5FA;color:#FFF}td.sw4{background:#3B82F6;color:#FFF}
td.sw3 .wx-v,td.sw4 .wx-v{color:#FFF}
table.wx-week{width:100%;border-collapse:collapse;font-size:12.5px;min-width:560px}
table.wx-week th,table.wx-week td{border:1px solid var(--card-border);padding:8px 10px;text-align:left}
table.wx-week th{background:#F8FAFC;font-size:11.5px;color:var(--text-muted)}
tr.wk-wet{background:#FEF2F2}
tr.wk-snow{background:#EFF6FF}
tr.wk-windy{background:#FFF7ED}
.wr-alert{background:var(--warning-bg);border:1px solid var(--warning-border);color:var(--warning-text);border-radius:8px;padding:10px 13px;font-size:12.5px;margin-bottom:12px;line-height:1.7}
.wr-alert-severe{background:#FEF2F2;border:1px solid #FECACA;color:#7F1D1D;border-radius:8px;padding:10px 13px;font-size:12.5px;margin-bottom:12px;line-height:1.7;font-weight:700}
.wr-suggest{background:var(--tip-bg);border:1px solid var(--tip-border);color:var(--tip-text);border-radius:8px;padding:10px 13px;font-size:12.5px;margin-bottom:12px;line-height:1.7}
.wr-ok{background:var(--success-bg);border:1px solid var(--success-border);color:var(--success-text);border-radius:8px;padding:10px 13px;font-size:12.5px;margin-bottom:12px}
.wr-note,.wr-note-sub{font-size:12.5px;color:var(--text-muted);margin-bottom:10px;line-height:1.7}
.wr-hist{background:var(--weather-bg);border:1px solid var(--weather-border);color:var(--weather-text);border-radius:8px;padding:10px 13px;font-size:12.5px;margin-bottom:10px}
.wr-ptlist{margin:0 0 0 18px;padding:0;font-size:12.5px;line-height:1.9}
.wr-loading{padding:22px;text-align:center;color:var(--text-muted);font-size:13px}
.wr-err{background:var(--warning-bg);border:1px solid var(--warning-border);color:var(--warning-text);border-radius:8px;padding:10px 13px;font-size:12.5px;margin-bottom:10px}
.wr-legend{display:flex;flex-wrap:wrap;gap:12px;align-items:center;margin-top:12px;font-size:11px;color:var(--text-muted)}
.wr-legend i.sw{display:inline-block;width:13px;height:13px;border-radius:3px;vertical-align:-2px;margin-right:3px}
.wr-eta-key{font-weight:700;color:var(--primary)}
.wr-src{margin-left:auto}
/* 每日卡片內嵌天氣列 */
.theme-weather-widget{margin-top:8px;font-size:12.5px}
.iw-ref{color:var(--text-muted)}
.iw-cd{color:var(--accent);font-weight:700}
.iw-live{font-weight:700;color:var(--weather-text)}
.iw-jump{margin-left:8px;color:var(--warning-text);font-weight:700;text-decoration:underline}
/* ── 路線節點時間軸 ── */
.tl-list{list-style:none;margin:8px 0 0;padding:0}
.tl-item{display:flex;gap:9px;align-items:flex-start;padding:7px 0;border-bottom:1px dashed var(--card-border);font-size:13px;line-height:1.65}
.tl-item:last-child{border-bottom:0}
.tl-km{flex:0 0 58px;font-size:11.5px;font-weight:800;color:var(--secondary);padding-top:2px}
.tl-icon{flex:0 0 20px}
.tl-pivot{background:#FFFBEB;border-radius:6px;padding-left:6px;padding-right:6px}
.tl-warning{background:var(--warning-bg);border-radius:6px;padding-left:6px;padding-right:6px}
/* ── 餐食 ── */
.meal-box{border-radius:8px;padding:12px 14px;margin-bottom:12px;font-size:13px;line-height:1.7}
.meal-box ul{margin:6px 0 0 17px;padding:0}
.meal-box li{margin-bottom:5px}
.meal-lunch{background:#F0FDF4;border:1px solid #86EFAC;border-left:4px solid #16A34A;color:#166534}
.meal-dinner{background:#FFFBEB;border:1px solid #FCD34D;border-left:4px solid #D97706;color:#92400E}
.meal-todo{background:#F8FAFC;border:1px dashed #CBD5E1;color:var(--text-muted)}
.meal-meta{font-size:11.5px;opacity:.85}
.meal-src{display:block;font-size:10.5px;opacity:.6;margin-top:2px}
.meal-tel{display:inline-block;margin-left:6px;padding:1px 8px;border-radius:5px;background:rgba(0,0,0,.08);font-size:11.5px;font-weight:700;text-decoration:none;color:inherit}
.meal-verified{font-size:11px;color:var(--text-muted);margin-bottom:10px;padding:6px 10px;background:#F8FAFC;border-radius:6px;border-left:3px solid #16A34A}
/* ── 緊急聯絡 ── */
.emergency-block{background:#FFF;border:1px solid var(--card-border);border-left:5px solid #DC2626;border-radius:12px;padding:18px;margin-bottom:28px}
.em-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:11px;margin-bottom:16px}
.em-card{display:block;background:#FEF2F2;border:1px solid #FCA5A5;border-radius:9px;padding:12px 14px;text-decoration:none;color:#7F1D1D;transition:transform .12s}
.em-card:hover{transform:translateY(-2px)}
.em-num{font-size:22px;font-weight:900;letter-spacing:.5px;color:#B91C1C}
.em-label{font-size:13px;font-weight:800;margin-top:2px}
.em-when{font-size:11.5px;opacity:.9;margin-top:4px;font-weight:700}
.em-note{font-size:11px;opacity:.8;margin-top:5px;line-height:1.6}
.em-sub{font-size:13.5px;font-weight:800;margin:14px 0 4px}
.em-note-line{font-size:12px;color:var(--text-muted);margin-bottom:9px;line-height:1.65}
table.em-table{width:100%;border-collapse:collapse;font-size:12.5px;min-width:560px}
table.em-table th,table.em-table td{border:1px solid var(--card-border);padding:7px 9px;text-align:left}
table.em-table th{background:#F8FAFC;font-size:11.5px;color:var(--text-muted)}
table.em-table a{color:#B91C1C;font-weight:700;text-decoration:none;white-space:nowrap}
.em-checklist{margin-top:14px;background:#FFFBEB;border:1px solid #FCD34D;border-radius:9px;padding:12px 14px;font-size:12.5px;color:#92400E}
.em-checklist ol{margin:6px 0 0 18px;padding:0;line-height:1.85}
.em-src{font-size:10.5px;color:var(--text-muted);margin-top:10px}
/* ── 沿線支援 ── */
.support-box{background:#F8FAFC;border:1px solid var(--card-border);border-left:4px solid #0F766E;border-radius:8px;padding:12px 14px;margin-bottom:12px}
.sp-title{font-size:13.5px;font-weight:800;color:#0F766E;margin-bottom:8px}
.sp-label{font-size:12px;font-weight:800;margin:9px 0 5px;opacity:.9}
.sp-more{font-weight:500;opacity:.65;font-size:11px}
.sp-chips{display:flex;flex-wrap:wrap;gap:5px}
.sp-chip{font-size:11.5px;background:#FFF;border:1px solid var(--card-border);border-radius:6px;padding:3px 8px;white-space:nowrap}
.sp-chip b{margin-right:4px}
.sp-chip u{text-decoration:none;opacity:.6;margin-left:4px;font-size:10.5px}
.sp-chip i{font-style:normal;opacity:.6;margin-left:5px;font-size:10.5px}
.sp-chip a{margin-left:5px;text-decoration:none}
.sp-bike b{color:#0F766E}
.sp-hosp b{color:#B91C1C}
.sp-empty{font-size:12px;background:var(--warning-bg);border:1px solid var(--warning-border);color:var(--warning-text);border-radius:7px;padding:8px 11px;line-height:1.65}
.sp-pref{margin:4px 0 0 17px;padding:0;font-size:12px;line-height:1.85}
.sp-pref a{color:#B91C1C;font-weight:700;text-decoration:none}
.sp-src{font-size:10.5px;color:var(--text-muted);margin-top:8px}
/* ── 撤退方案 ── */
.bailout-box{background:#EFF6FF;border:1px solid #93C5FD;border-left:4px solid #2563EB;border-radius:8px;padding:12px 14px;margin-bottom:12px;font-size:13px;color:#1E3A8A;line-height:1.7}
.bailout-box ul{margin:6px 0 0 17px;padding:0}
.bailout-todo{background:#F8FAFC;border:1px dashed #CBD5E1;border-left:4px dashed #CBD5E1;color:var(--text-muted)}
/* ── 卡片雜項 ── */
.nav-src{display:inline-block;background:#1E293B;color:#FFF;font-size:10.5px;font-weight:700;padding:2px 7px;border-radius:5px;margin-left:4px;letter-spacing:.3px}
.badge-pending{display:inline-block;background:#FEF3C7;color:#92400E;font-size:11px;font-weight:700;padding:2px 7px;border-radius:5px}
.status-pending{background:var(--koyo-bg);border:1px solid var(--koyo-border);color:var(--koyo-text)}
.hotel-actions{display:flex;gap:8px;flex-wrap:wrap;margin-top:8px;align-items:center}
.hotel-tel{display:inline-flex;align-items:center;gap:4px;background:#065F46;color:#FFF;padding:5px 12px;border-radius:6px;font-size:12.5px;font-weight:700;text-decoration:none}
.day-actions{margin-top:14px;display:flex;gap:10px;flex-wrap:wrap}
.act-btn{display:inline-flex;align-items:center;gap:6px;padding:7px 14px;border-radius:7px;font-size:12.5px;font-weight:700;text-decoration:none;color:#FFF}
.act-map{background:#2563EB}
.act-gpx{background:var(--accent)}
.culture-box{background:rgba(147,51,234,.07);border:1px solid #C084FC;border-left:5px solid #9333EA;border-radius:8px;padding:12px 15px;margin:12px 0;font-size:12.5px;line-height:1.7;color:#4C1D95}
.culture-box>strong{color:#7E22CE;font-size:13.5px;display:block;margin-bottom:4px}

/* ── 撤退方案 ── */
.bo-title{font-size:14px;font-weight:800;margin-bottom:10px;display:flex;align-items:center;gap:9px;flex-wrap:wrap}
.bo-badge{font-size:11px;font-weight:700;padding:2px 9px;border-radius:20px}
.bo-a{background:#DCFCE7;color:#166534}.bo-ab{background:#FEF3C7;color:#92400E}.bo-b{background:#FEE2E2;color:#991B1B}
.bo-sub{font-size:12.5px;font-weight:700;margin:12px 0 6px;opacity:.85}
.bo-premise-b{background:var(--warning-bg)!important;border-color:var(--warning-border)!important;color:var(--warning-text)}
.bo-premise{background:rgba(22,163,74,.1);border:1px solid rgba(22,163,74,.35);border-radius:7px;padding:8px 12px;font-size:12.5px;line-height:1.7;margin-bottom:4px}
.bo-line{border-radius:8px;padding:9px 12px;margin-bottom:8px;background:rgba(255,255,255,.65)}
.bo-line.bo-cycle{border-left:4px solid #16A34A}
.bo-line.bo-rinko{border-left:4px solid #64748B}
.bo-line-head{font-size:12.5px;display:flex;gap:7px;align-items:baseline;flex-wrap:wrap}
.bo-line-head strong{font-size:13px}
.bo-line ul{margin:5px 0 0 17px;padding:0;font-size:12px;line-height:1.7}
.bo-meta{font-size:11.5px;opacity:.8;margin-top:3px}
.bo-warn{margin-top:6px;padding:6px 10px;border-radius:6px;background:var(--warning-bg);color:var(--warning-text);font-size:12px;font-weight:700}
.bo-note{font-size:11.5px;opacity:.75;margin-top:6px;line-height:1.65}
.bo-src{font-size:10.5px;opacity:.55;margin-top:5px}
.bo-chips{display:flex;flex-wrap:wrap;gap:5px}
.bo-st{font-size:11.5px;background:rgba(255,255,255,.8);border:1px solid rgba(30,58,138,.18);border-radius:6px;padding:3px 8px;white-space:nowrap}
.bo-st b{color:#1D4ED8;margin-right:4px}
.bo-st i{font-style:normal;opacity:.6;margin-left:4px;font-size:10.5px}
.bo-st em{font-style:normal;margin-left:5px;font-size:10px;font-weight:700;padding:1px 5px;border-radius:4px}
.bo-ok{background:#DCFCE7;color:#166534}
.bo-x{background:#FEE2E2;color:#991B1B}
.bo-gap{margin-top:10px;border-radius:8px;padding:10px 12px;background:var(--warning-bg);border:1px solid var(--warning-border)}
.bo-gap-head{font-size:12.5px;font-weight:800;color:var(--warning-text)}
.bo-lodging{margin:6px 0 0 17px;padding:0;font-size:12px;line-height:1.85;color:var(--warning-text)}
.bo-det{font-size:10.5px;opacity:.7;margin-left:4px}
.km-gap{background:#FFFBEB;border:1px solid #FCD34D;border-left:4px solid #D97706;border-radius:7px;padding:8px 12px;font-size:12px;color:#92400E;margin-top:8px;line-height:1.65}
.data-source-note{background:#F8FAFC;border:1px solid var(--card-border);border-left:4px solid #1E293B;border-radius:8px;padding:10px 14px;font-size:12.5px;color:var(--text-muted);margin-bottom:14px;line-height:1.7}
@media (max-width:768px){
  .wr-controls{gap:8px}
  .wr-controls select{max-width:100%}
  table.wx-matrix .wr-rowhead{max-width:120px}
  td.wx-c{width:32px;height:34px}
  .wr-src{margin-left:0;width:100%}
  .tl-km{flex:0 0 48px}
}
"""


def main():
    trip = load('data/trip.json')
    songs = load('data/songs.json')
    seas = load('data/seasonal_outlook.json')
    fol = load('data/foliage_forecast.json')
    tpl = io.open(os.path.join(ROOT, 'templates/index_template.html'), encoding='utf-8').read()
    out = (tpl
           .replace('<!--{{EMERGENCY_CARD}}-->', render_emergency_card(trip))
           .replace('<!--{{STATS_GRID}}-->', render_stats_grid(trip))
           .replace('<!--{{BUFFER_DAYS}}-->', render_buffer_days(trip))
           .replace('<!--{{WEATHER_WAR_ROOM}}-->', render_war_room(trip))
           .replace('<!--{{SUMMARY_TABLE}}-->', render_summary_table(trip, seas, fol))
           .replace('<!--{{DAY_CARDS}}-->', render_day_cards(trip, songs, seas))
           .replace('<!--{{WEATHER_JS}}-->', render_weather_js(trip))
           .replace('/*{{EXTRA_CSS}}*/', render_extra_css()))
    leftover = [p for p in ('{{EMERGENCY_CARD}}', '{{STATS_GRID}}', '{{BUFFER_DAYS}}', '{{WEATHER_WAR_ROOM}}',
                            '{{SUMMARY_TABLE}}', '{{DAY_CARDS}}', '{{WEATHER_JS}}',
                            '{{EXTRA_CSS}}') if p in out]
    if leftover:
        raise SystemExit(f'佔位符未替換: {leftover}')
    dest = os.path.join(ROOT, 'index.html')
    io.open(dest, 'w', encoding='utf-8').write(out)
    print(f'生成 {dest} — {len(out):,} 字元')
    return out


if __name__ == '__main__':
    main()
