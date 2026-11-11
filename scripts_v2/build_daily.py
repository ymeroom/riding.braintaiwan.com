#!/usr/bin/env python3
"""Build the one-page-per-day "today" cards (daily/dayN.html).

Phone-first summary of what you need on the road: weather + clothing, stops with
km and map links, meals, tonight's lodging, nearest stations to bail out, bike
shops / hospitals and emergency numbers.

Sources: data/trip.json for the plan, index.html for the latest weekly forecast
and clothing advice (so a weather update followed by a re-run keeps both in sync).
Writes only daily/. Never touches index.html.

    python3 scripts_v2/build_daily.py          # every day
    python3 scripts_v2/build_daily.py 1        # only these days
"""
import html
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "daily"
sys.path.insert(0, str(ROOT / "scripts_v2"))
from build_sketches import est_times  # noqa: E402  (shared time estimate)

E = html.escape
EMOJI = re.compile("[\U0001F000-\U0001FFFF☀-➿️‍]")


def strip_tags(s):
    return re.sub(r"<[^>]+>", "", s)


def clean(s):
    s = re.sub(r"[（(][^）)]*\b[A-Z0-9]{2}\s?\d{2,4}\b[^）)]*[）)]", "", s)  # drop flight numbers (repo is public)
    return EMOJI.sub("", s).strip()


def first_sentence(s, limit=38):
    s = clean(strip_tags(s))
    m = re.match(r"(.+?[。！!])", s)
    s = m.group(1) if m else s
    return s if len(s) <= limit else s[:limit].rstrip() + "…"


def stop_name(s):
    s = clean(s)
    s = re.sub(r"【[^】]*】", "", s)
    if "：" in s:
        s = s.split("：", 1)[1]
    return s.strip()


def gmap(lat, lon):
    return f"https://www.google.com/maps/search/?api=1&query={lat:.5f},{lon:.5f}"


def tel_link(t):
    num = re.sub(r"[^\d#+]", "", t)
    return f'<a class="tel" href="tel:{E(num)}">{E(t)}</a>'


# ---------------------------------------------------------------- weather from index.html

def weather_blocks(n):
    s = (ROOT / "index.html").read_text(encoding="utf-8")
    st = [m.start() for m in re.finditer(r'            <div class="seasonal-box">', s)]
    seg = s[st[n - 1]: s.index("🎥", st[n - 1])]
    wk = re.search(r'<div class="seas-1m">🗓️ <strong>週間預報</strong>(.*?)<br><small>', seg)
    cl = re.search(r'<div class="seas-1m">👕 <strong>穿搭建議</strong>(.*?)</div>', seg)
    m1 = re.search(r'<div class="seas-1m">📅 <strong>1 個月預報</strong>(.*?)</div>', seg)
    out = {}
    if wk:
        txt = strip_tags(wk.group(1))
        head, _, body = txt.partition("：")
        parts = [p.strip() for p in body.split("｜")]
        out["issued"] = head.strip("（）")
        out["sky"] = parts[0]
        out["chips"] = parts[1:]
    if cl:
        out["clothing"] = re.sub(r"^（[^）]*）：", "", cl.group(1).strip())
    if m1 and not wk:
        out["month"] = strip_tags(m1.group(1)).strip()
    return out


# ---------------------------------------------------------------- sections

def sec_weather(d):
    w = weather_blocks(d["day"])
    wh = d.get("weather_hist", {})
    if "sky" in w:
        chips = "".join(f"<li>{E(c)}</li>" for c in w["chips"])
        body = (f'<p class="sky">{E(w["sky"])}</p><ul class="chips">{chips}</ul>'
                f'<p class="meta">氣象庁週間預報（{E(w["issued"])}）</p>')
    else:
        body = (f'<p class="sky">週間預報還沒涵蓋這天</p><p>{E(w.get("month", ""))}</p>'
                f'<p class="meta">去年同日：{E(wh.get("raw", ""))}</p>')
    if w.get("clothing"):
        body += f'<div class="wear"><b>穿搭</b>{w["clothing"]}</div>'
    return f'<section id="wx"><h2>天氣・穿搭</h2>{body}</section>'


def sec_route(d):
    tl = d["timeline"]
    times = est_times(d)
    planned = any(p.get("time") for p in tl)
    rows = []
    for i, p in enumerate(tl):
        lon, lat = p["coord"]
        name = stop_name(p["name"])
        tag = {"start": "出發", "end": "抵達"}.get(p["type"], "")
        rows.append(
            f'<li class="stop {p["type"]}"><span class="t">{times[i]}</span>'
            f'<span class="km">{p["km"]:.1f}<small>km</small></span>'
            f'<div class="what"><b>{E(name)}</b>{f"<em>{tag}</em>" if tag else ""}<span>{E(first_sentence(p.get("desc","")))}</span></div>'
            f'<a class="go" href="{gmap(lat, lon)}" target="_blank" rel="noopener" aria-label="在地圖打開 {E(name)}">地圖</a></li>')
    note = "時刻為預定" if planned else "時刻為估算（平均 15 km/h＋爬坡＋午休）"
    km = d.get("planned_km") or max(p["km"] for p in tl)
    gain = d.get("route_gain", d["nav"]["gain"])
    return (f'<section id="route"><h2>路線 <small>{km:.1f} km・爬升 {gain} m</small></h2>'
            f'<ol class="stops">{"".join(rows)}</ol><p class="meta">{note}</p></section>')


def place_card(x, label=""):
    bits = [f'<b>{E(x["name"])}</b>']
    if label:
        bits.insert(0, f'<em>{E(label)}</em>')
    if x.get("note"):
        bits.append(f'<span>{E(clean(x["note"]))}</span>')
    meta = " ・ ".join(E(v) for v in (x.get("hours"), x.get("bike")) if v)
    if meta:
        bits.append(f'<span class="meta">{meta}</span>')
    link = f'<a class="go" href="{E(x["map"])}" target="_blank" rel="noopener">地圖</a>' if x.get("map") else ""
    return f'<li><div class="what">{"".join(bits)}</div>{link}</li>'


def sec_meals(d):
    m = d.get("meals") or {}
    if not (m.get("lunch") or m.get("dinner")):
        return ""
    out = '<section id="eat"><h2>吃飯</h2>'
    if m.get("lunch"):
        out += f'<h3>午餐 <small>{E(m.get("lunch_note",""))}</small></h3><ul class="cards">{"".join(place_card(x) for x in m["lunch"])}</ul>'
    if m.get("dinner"):
        out += f'<h3>晚餐 <small>{E(m.get("dinner_note",""))}</small></h3><ul class="cards">{"".join(place_card(x) for x in m["dinner"])}</ul>'
    return out + "</section>"


def sec_hotel(d):
    h = d.get("hotel") or {}
    if not h.get("name"):
        return ""
    tel = h.get("tel") or (d.get("logistics") or {}).get("hotel_tel")
    rows = [f'<b>{E(h["name"])}</b>']
    if h.get("addr"):
        rows.append(f'<a href="{E(h.get("url") or "")}" target="_blank" rel="noopener">{E(h["addr"])}</a>')
    if h.get("bike"):
        rows.append(f'<span>{E(clean(h["bike"]))}</span>')
    if tel:
        rows.append(tel_link(tel))
    return f'<section id="hotel"><h2>今晚住宿</h2><div class="box">{"".join(f"<p>{r}</p>" for r in rows)}</div></section>'


def sec_bailout(d):
    b = d.get("bailout") or {}
    st = b.get("stations") or []
    if not st:
        return ""
    km_tot = d.get("planned_km") or max(p["km"] for p in d["timeline"])
    step = 10 if km_tot > 30 else 5
    picks = []
    for lo in range(0, int(km_tot) + 1, step):
        cand = [s for s in st if lo <= s["km"] < lo + step]
        if cand:
            picks.append(min(cand, key=lambda s: s["off_km"]))
    lis = "".join(
        f'<li><span class="km">{s["km"]:.0f}<small>km</small></span><div class="what"><b>{E(s["name"])}</b>'
        f'<span class="meta">{E(s.get("operator",""))} ・ 離路線 {s["off_km"]:.1f} km</span></div>'
        f'<a class="go" href="{gmap(s["lat"], s["lon"])}" target="_blank" rel="noopener">地圖</a></li>' for s in picks)
    rule = ""
    if b.get("lines"):
        ln = b["lines"][0]
        rule = f'<p class="meta">{E(ln["label"])}：{E(ln["rules"][0])}（{E(ln.get("fee",""))}）</p>'
    return (f'<section id="out"><details><summary><h2>撤退車站 <small>每 {step} km 最近的一站・點開</small></h2></summary>'
            f'<ul class="cards">{lis}</ul>{rule}</details></section>')


def sec_support(d):
    s = d.get("support") or {}
    shops = sorted([x for x in s.get("bike_shops", []) if x["off_km"] <= 1.5], key=lambda x: x["km"])[:4]
    hosp = sorted([x for x in s.get("hospitals", []) if x["off_km"] <= 1.0], key=lambda x: x["km"])
    hosp = [h for h in hosp if h.get("emergency")][:3] or hosp[:3]
    if not (shops or hosp):
        return ""

    def li(x):
        meta = " ・ ".join(v for v in (x.get("hours"), f'離路線 {x["off_km"]:.1f} km') if v)
        return (f'<li><span class="km">{x["km"]:.0f}<small>km</small></span><div class="what"><b>{E(x["name"])}</b>'
                f'<span class="meta">{E(meta)}</span></div><a class="go" href="{gmap(x["lat"], x["lon"])}" target="_blank" rel="noopener">地圖</a></li>')
    out = '<section id="help"><details><summary><h2>單車店・醫院 <small>點開</small></h2></summary>'
    if shops:
        out += f'<h3>單車店</h3><ul class="cards">{"".join(li(x) for x in shops)}</ul>'
    if hosp:
        out += f'<h3>醫院</h3><ul class="cards">{"".join(li(x) for x in hosp)}</ul>'
    return out + "</details></section>"


def sec_sos(d, emg):
    core = "".join(f'<li>{tel_link(c["tel"])}<span>{E(c["label"])}</span></li>' for c in emg["core"][:3])
    adv = emg.get("prefecture_advice", {})
    pref = ""
    for p in d.get("prefectures") or []:
        a = adv.get(p)
        if a:
            short = f'{a["short"]} ／ ' if a.get("short") else ""
            pref += f'<li><span>{E(p)}・不確定要不要叫救護車</span><span class="tel-plain">{E(short + a["tel"])}</span></li>'
    return (f'<section id="sos"><h2>緊急</h2><ul class="sos">{core}{pref}</ul>'
            '<p class="meta">發生事故不論輕重都要打 110，保險理賠需要「交通事故証明書」。</p></section>')


# ---------------------------------------------------------------- page

CSS = """
:root{--bg:#f6f4ef;--card:#fff;--ink:#1d1f24;--muted:#61656e;--line:#e2ddd2;--accent:#b8442c;--accent-ink:#fff;--blue:#27405f;--chip:#efe9dd;color-scheme:light}
@media (prefers-color-scheme:dark){:root:not([data-theme=light]){--bg:#15171b;--card:#1f2228;--ink:#eceae5;--muted:#a3a6ad;--line:#33363d;--accent:#e2735b;--accent-ink:#15171b;--blue:#9db7d6;--chip:#2a2d34;color-scheme:dark}}
*{box-sizing:border-box}html{-webkit-text-size-adjust:100%}
body{margin:0;background:var(--bg);color:var(--ink);font:16px/1.55 -apple-system,"PingFang TC","Noto Sans TC","Microsoft JhengHei",sans-serif}
.top{position:sticky;top:0;z-index:5;background:var(--bg);border-bottom:1px solid var(--line);padding:10px max(14px,env(safe-area-inset-right,0px)) 10px max(14px,env(safe-area-inset-left,0px))}
.top .row{display:flex;justify-content:space-between;align-items:center;gap:8px;max-width:640px;margin:0 auto}
.top a{color:var(--ink);text-decoration:none;font-size:14px;padding:6px 10px;border:1px solid var(--line);border-radius:999px;background:var(--card)}
.top .d{font-weight:800;font-size:15px}
main{max-width:640px;margin:0 auto;padding:14px max(14px,env(safe-area-inset-right,0px)) 40px max(14px,env(safe-area-inset-left,0px));display:flex;flex-direction:column;gap:14px}
header h1{margin:2px 0 0;font-size:24px;line-height:1.25;text-wrap:balance}
header p{margin:4px 0 0;color:var(--muted);font-size:14.5px}
nav.jump{display:flex;gap:6px;overflow-x:auto;padding:2px 0 4px;scrollbar-width:none}
nav.jump a{flex:none;font-size:13.5px;color:var(--ink);text-decoration:none;background:var(--chip);border-radius:999px;padding:5px 11px}
section{background:var(--card);border:1px solid var(--line);border-radius:14px;padding:14px;scroll-margin-top:64px}
h2{margin:0 0 10px;font-size:17px;display:flex;gap:8px;align-items:baseline;flex-wrap:wrap}
h2 small,h3 small{font-weight:400;color:var(--muted);font-size:13px}
h3{margin:12px 0 6px;font-size:15px}
.sky{margin:0;font-size:20px;font-weight:800}
.chips{list-style:none;margin:8px 0 0;padding:0;display:flex;flex-wrap:wrap;gap:6px}
.chips li{background:var(--chip);border-radius:8px;padding:3px 9px;font-size:14px}
.wear{margin-top:12px;padding:10px 12px;border-left:4px solid var(--accent);background:var(--chip);border-radius:6px;font-size:15px}
.wear b:first-child{display:block;font-size:13px;color:var(--accent);margin-bottom:2px}
.meta{color:var(--muted);font-size:13px;margin:8px 0 0}
ol.stops,ul.cards{list-style:none;margin:0;padding:0;display:flex;flex-direction:column}
.stops li,.cards li{display:flex;align-items:center;gap:10px;padding:10px 0;border-top:1px solid var(--line)}
.stops li:first-child,.cards li:first-child{border-top:0}
.t{flex:none;width:44px;font-variant-numeric:tabular-nums;color:var(--muted);font-size:14px}
.km{flex:none;width:52px;text-align:right;font-weight:800;font-variant-numeric:tabular-nums;font-size:17px}
.km small{font-weight:400;font-size:11px;margin-left:1px;color:var(--muted)}
.what{flex:1;min-width:0;display:flex;flex-direction:column}
.what b{font-size:15.5px}.what em{font-style:normal;font-size:12px;color:var(--accent);font-weight:700}
.what span{font-size:13.5px;color:var(--muted)}
.stops .what span{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.stop.start .km,.stop.end .km{color:var(--accent)}
a.go{flex:none;font-size:14px;font-weight:700;text-decoration:none;color:var(--accent-ink);background:var(--accent);border-radius:10px;padding:9px 12px;min-width:56px;text-align:center}
.box p{margin:0 0 6px}.box a{color:var(--blue)}
a.tel{color:var(--blue);font-weight:800;font-size:17px}
ul.sos{list-style:none;margin:0;padding:0;display:flex;flex-direction:column;gap:8px}
ul.sos li{display:flex;flex-direction:column}ul.sos span{font-size:13.5px;color:var(--muted)}.tel-plain{font-weight:700;color:var(--ink)!important;font-size:15px!important}
footer{display:flex;flex-direction:column;gap:8px}
footer a{display:block;text-align:center;padding:12px;border-radius:12px;background:var(--card);border:1px solid var(--line);color:var(--ink);text-decoration:none;font-weight:700}
details summary{list-style:none;cursor:pointer}details summary::-webkit-details-marker{display:none}
details summary h2{margin:0}details[open] summary h2{margin-bottom:10px}
details summary h2::after{content:"＋";margin-left:auto;color:var(--muted)}details[open] summary h2::after{content:"－"}
a:focus-visible{outline:3px solid var(--blue);outline-offset:2px}
"""


def page(d, days, emg, navi):
    n = d["day"]
    tl = d["timeline"]
    parts = [re.sub(r"【[^】]*】|\s*[（(][^）)]*[）)]", "", x).strip() for x in d["route_line"].split("➔")]
    start, end = parts[0], parts[-1]
    km = d.get("planned_km") or max(p["km"] for p in tl)
    gain = d.get("route_gain", d["nav"]["gain"])
    prev_ = f'<a href="day{n-1}.html">← Day {n-1}</a>' if n > 1 else "<span></span>"
    next_ = f'<a href="day{n+1}.html">Day {n+1} →</a>' if n < len(days) else "<span></span>"
    secs = [sec_weather(d), sec_route(d), sec_meals(d), sec_hotel(d), sec_bailout(d), sec_support(d), sec_sos(d, emg)]
    jump = "".join(f'<a href="#{i}">{t}</a>' for i, t in (("wx", "天氣"), ("route", "路線"), ("eat", "吃飯"), ("hotel", "住宿"),
                                                         ("out", "撤退"), ("help", "補給"), ("sos", "緊急")) if f'id="{i}"' in "".join(secs))
    links = [f'<a href="../index.html#day-{n}">完整行程（主網站 Day {n}）</a>',
             f'<a href="../sketches/day{n}.html">手繪行程圖</a>',
             f'<a href="../{E(d["gpx"])}" download>下載 GPX 軌跡</a>']
    if navi.get(str(n)):
        links.insert(1, f'<a href="{E(navi[str(n)])}" target="_blank" rel="noopener">NAVITIME 路線</a>')
    return f"""<!doctype html><html lang="zh-Hant"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="theme-color" content="#f6f4ef"><title>Day {n} 今日重點</title>
<meta name="description" content="Day {n} {E(d['date'])} {E(d.get('subtitle',''))}：天氣、路線、吃飯、住宿、撤退與緊急聯絡">
<style>{CSS}</style></head><body>
<div class="top"><div class="row">{prev_}<span class="d">Day {n}・{E(d['date'])}</span>{next_}</div></div>
<main><header><h1>{E(start)} → {E(end)}</h1><p>{E(d.get('subtitle',''))}・{km:.1f} km・爬升 {gain} m</p></header>
<nav class="jump" aria-label="跳到">{jump}</nav>
{"".join(secs)}
<footer>{"".join(links)}</footer></main></body></html>"""


def main():
    trip = json.loads((ROOT / "data/trip.json").read_text(encoding="utf-8"))
    navi = json.loads((ROOT / "data/navitime_urls.json").read_text(encoding="utf-8"))
    days = trip["days"]
    only = [int(a) for a in sys.argv[1:]]
    OUT.mkdir(exist_ok=True)
    for d in days:
        if only and d["day"] not in only:
            continue
        (OUT / f"day{d['day']}.html").write_text(page(d, days, trip["emergency"], navi), encoding="utf-8")
        print("wrote", OUT / f"day{d['day']}.html")


if __name__ == "__main__":
    main()
