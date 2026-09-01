"""抓取氣象庁「３か月予報」與「エルニーニョ監視速報」，寫成 data/seasonal_outlook.json。

資料源都是官方原始檔，不經第三方：
  https://www.jma.go.jp/bosai/season/data/P3M/<areaCode>.json   ← 官網地圖與文字頁共用的同一份 JSON
  https://www.data.jma.go.jp/cpd/elnino/kanshi_joho/kanshi_joho1.html

行程橫跨関東甲信（東京・神奈川・山梨・埼玉）與東海（静岡）兩個季節預報區，
兩區各自由不同氣象台發表，因此兩份都抓，再依 data/day_prefectures.json 對到每一天。

JSON 內的日文原文一律保留為權威值，繁中欄位（zh_*）只是輔助譯註：
天候敘述用的是氣象庁的定型句，用片語字典逐段對譯；遇到字典沒有的新句型就留空，
由網頁只顯示日文原文——寧可少一行中文，也不要生出沒根據的翻譯。

用法：  python scripts_v2/fetch_seasonal_outlook.py
"""
import io, json, os, re, sys, urllib.request
from datetime import datetime, timedelta, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
JST = timezone(timedelta(hours=9))
UA = {'User-Agent': 'Mozilla/5.0 (compatible; tokyo-cycling-trip/1.0)'}

SEASON_API = 'https://www.jma.go.jp/bosai/season/data/P3M/{code}.json'
ENSO_URL = 'https://www.data.jma.go.jp/cpd/elnino/kanshi_joho/kanshi_joho1.html'
SEASON_PAGE = 'https://www.jma.go.jp/bosai/season/#area_type=offices&area_code={pref}&term=3month'

# 抓哪幾個季節預報區（全国留著當對照，網頁不一定用得上）
REGIONS = {
    '010000': {'name': '全国', 'zh': '全國'},
    '010300': {'name': '関東甲信地方', 'zh': '關東甲信', 'pref_code': '130000'},
    '010400': {'name': '東海地方', 'zh': '東海', 'pref_code': '220000'},
}

PREF_TO_REGION = {
    '東京都': '010300', '神奈川県': '010300', '山梨県': '010300', '埼玉県': '010300',
    '千葉県': '010300', '群馬県': '010300', '栃木県': '010300', '茨城県': '010300',
    '長野県': '010300',
    '静岡県': '010400', '愛知県': '010400', '岐阜県': '010400', '三重県': '010400',
}

# 氣象庁天候定型句 → 繁中。順序有意義：長句在前，避免被短句先吃掉。
WEATHER_PHRASES = [
    ('平年に比べ曇りや雨または雪の日が多い', '陰雨或雪的日子較常年多'),
    ('平年と同様に曇りや雨または雪の日が多い', '陰雨或雪的日子偏多，與常年相當'),
    ('平年に比べ曇りや雨の日が多い', '陰雨日較常年多'),
    ('平年と同様に曇りや雨の日が多い', '陰雨日偏多，與常年相當'),
    ('平年に比べ晴れの日が少ない', '晴天日較常年少'),
    ('平年に比べ晴れの日が多い', '晴天日較常年多'),
    ('平年と同様に晴れの日が多い', '晴天日偏多，與常年相當'),
    ('平年と同様に晴れの日が少ない', '晴天日偏少，與常年相當'),
    ('数日の周期で変わ', '天氣以數日為週期變化'),
]

ENSO_PHRASES = [
    ('エルニーニョ現象が続いているとみられる', '聖嬰現象持續中'),
    ('エルニーニョ現象が発生しているとみられる', '聖嬰現象發生中'),
    ('エルニーニョ現象が続く見込み', '聖嬰現象將持續'),
    ('エルニーニョ現象が発生する可能性が高い', '聖嬰現象發生機率高'),
    ('ラニーニャ現象が続いているとみられる', '反聖嬰現象持續中'),
    ('ラニーニャ現象が発生しているとみられる', '反聖嬰現象發生中'),
    ('ラニーニャ現象が続く見込み', '反聖嬰現象將持續'),
    ('平常の状態が続いているとみられる', '海溫維持平常狀態'),
    ('平常の状態が続く可能性が高い', '海溫可能維持平常狀態'),
]


def fetch(url, as_json=False):
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=30) as r:
        raw = r.read()
    return json.loads(raw.decode('utf-8')) if as_json else raw.decode('utf-8', 'replace')


def gloss(sentence, table):
    """把日文定型句逐段對到繁中；沒有任何片語命中就回空字串（網頁只顯示日文）。"""
    hits, pos = [], []
    for ja, zh in table:
        i = sentence.find(ja)
        if i >= 0 and zh not in hits:
            hits.append(zh)
            pos.append(i)
    return '；'.join(z for _, z in sorted(zip(pos, hits)))


def prob_zh(below, normal, above, kind):
    """三分位機率 → 中文。並列最大值時照氣象庁寫法講成「A或B 各N%」。"""
    labels = ('偏低', '平年並', '偏高') if kind == '気温' else ('偏少', '平年並', '偏多')
    vals = [below, normal, above]
    mx = max(vals)
    win = [labels[i] for i, v in enumerate(vals) if v == mx]
    head = '或'.join(win) + (' 各 ' if len(win) > 1 else ' ') + f'{mx}%'
    return f'{head}（{labels[0]}{below} / {labels[1]}{normal} / {labels[2]}{above}）'


def parse_region(doc):
    """把一份 P3M JSON 拆成「向こう３か月」總論 + 每月明細。"""
    months = [datetime.fromisoformat(t).strftime('%Y-%m') for t in doc['timeDefines']]

    # 向こう３か月 總論
    season = {'label': doc['metInfos'][0].get('termName', '向こう３か月')}
    for it in doc['metInfos'][0]['items']:
        if 'feature' in it:
            for el in it['feature'].get('elements', []):
                season[f'{el["kind"]}_text'] = el['text'].strip()
        elif it.get('kind'):
            b, n, a = int(it['below']), int(it['normal']), int(it['above'])
            season[it['kind']] = {'below': b, 'normal': n, 'above': a,
                                  'zh': prob_zh(b, n, a, it['kind'])}

    # 每月：situations / elements / probabilities 全都靠 refId 對到月份，不能用位置 zip
    per = {m: {'label': f'{int(m[5:7])}月', 'month': m} for m in months}

    def month_of(ref_id):
        idx = int(ref_id) - 1
        return months[idx] if 0 <= idx < len(months) else None

    for blk in doc.get('timeInfos', []):
        feat = blk.get('feature')
        if feat:
            for s in feat.get('situations', []):
                m = month_of(s['refId'])
                if m:
                    txt = s['text'].strip()
                    per[m]['weather'] = txt
                    per[m]['weather_zh'] = gloss(txt, WEATHER_PHRASES)
            for el in feat.get('elements', []):
                for t in el.get('texts', []):
                    m = month_of(t['refId'])
                    if m:
                        per[m][f'{el["kind"]}_text'] = t['text'].strip()
        for p in blk.get('probabilities', []):
            m = month_of(p['refId'])
            if m:
                b, n, a = int(p['below']), int(p['normal']), int(p['above'])
                per[m][p['kind']] = {'below': b, 'normal': n, 'above': a,
                                     'zh': prob_zh(b, n, a, p['kind'])}

    nxt = {}
    for info in doc.get('additionalInfos', []):
        nxt[info['target']] = {'text': info['text'].strip(), 'datetime': info.get('datetime')}

    return {
        'issued': doc['reportDatetime'],
        'office': doc.get('publishingOffice', ''),
        'months': months,
        'season': season,
        'monthly': per,
        'next_release': nxt,
    }


def parse_enso(html):
    txt = re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', ' ', html))
    m = re.search(r'エルニーニョ監視速報（(No\.\s*\d+)）\s*(.*?)\s*気象庁\s*大気海洋部\s*'
                  r'(令和\d+年\d+月\d+日)\s*(.*?)\s*解説へ', txt)
    if not m:
        raise RuntimeError('エルニーニョ監視速報 版面已改，主文擷取失敗')
    no, subject, issued, head = m.group(1), m.group(2).strip(), m.group(3), m.group(4)
    lines = [s.strip() + '。' for s in head.split('。') if s.strip()]
    return {
        'no': no.replace(' ', ''),
        'subject': subject,
        'issued_ja': issued,
        'headline': lines,
        'headline_zh': [z for z in (gloss(l, ENSO_PHRASES) for l in lines) if z],
        'url': ENSO_URL,
    }


def build_day_map(outlook_months, day_prefs, trip):
    """每一天 → 涵蓋的預報區 + 該天所屬月份的展望；超出預報期間的日子標 covered=false。"""
    start = datetime.strptime(trip['meta']['start'], '%Y-%m-%d').date()
    out = {}
    for d in trip['days']:
        n = d['day']
        date = start + timedelta(days=n - 1)
        month = date.strftime('%Y-%m')
        codes, seen = [], set()
        for p in day_prefs.get(str(n), []):
            c = PREF_TO_REGION.get(p)
            if c and c not in seen:
                seen.add(c)
                codes.append(c)
        out[str(n)] = {
            'date': date.isoformat(),
            'month': month,
            'regions': codes,
            'covered': month in outlook_months,
        }
    return out


def main():
    sys.stdout.reconfigure(encoding='utf-8')
    trip = json.load(io.open(os.path.join(ROOT, 'data/trip.json'), encoding='utf-8'))
    day_prefs = json.load(io.open(os.path.join(ROOT, 'data/day_prefectures.json'), encoding='utf-8'))

    regions = {}
    for code, info in REGIONS.items():
        print(f'抓取 {info["name"]} ({code}) …')
        parsed = parse_region(fetch(SEASON_API.format(code=code), as_json=True))
        parsed['name'] = info['name']
        parsed['zh_name'] = info['zh']
        if info.get('pref_code'):
            parsed['page'] = SEASON_PAGE.format(pref=info['pref_code'])
        regions[code] = parsed

    print('抓取 エルニーニョ監視速報 …')
    enso = parse_enso(fetch(ENSO_URL))

    ref = regions['010300']
    months = ref['months']
    nr = ref['next_release'].get('３か月予報', {})

    doc = {
        'meta': {
            'product': '３か月予報',
            'issued': ref['issued'],
            'issued_label': datetime.fromisoformat(ref['issued']).strftime('%Y-%m-%d %H:%M JST'),
            'target_months': months,
            'target_label': f'{int(months[0][5:7])}月〜{int(months[-1][5:7])}月',
            'next_release': nr.get('datetime'),
            'next_release_text': nr.get('text', ''),
            'other_releases': {k: v for k, v in ref['next_release'].items() if k != '３か月予報'},
            'fetched_at': datetime.now(JST).isoformat(timespec='seconds'),
            'api': SEASON_API.format(code='<areaCode>'),
        },
        'enso': enso,
        'regions': regions,
        'days': build_day_map(months, day_prefs, trip),
    }

    path = os.path.join(ROOT, 'data/seasonal_outlook.json')
    with io.open(path, 'w', encoding='utf-8') as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
        f.write('\n')

    covered = sum(1 for v in doc['days'].values() if v['covered'])
    print(f'\n✅ data/seasonal_outlook.json')
    print(f'   發表：{doc["meta"]["issued_label"]}　對象：{doc["meta"]["target_label"]}')
    print(f'   行程 {len(doc["days"])} 天中 {covered} 天落在預報期間內')
    print(f'   下次發表：{doc["meta"]["next_release_text"]}')
    for line in enso['headline']:
        print(f'   ENSO：{line}')


if __name__ == '__main__':
    main()
