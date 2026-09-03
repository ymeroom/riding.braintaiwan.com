"""由 data/trip.json 生成 README.md，確保與網站數字同源。"""
import json, io, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
trip = json.load(io.open(os.path.join(ROOT, 'data/trip.json'), encoding='utf-8'))
m = trip['meta']

rows = []
for d in trip['days']:
    n = d['nav']
    planned = d['timeline'][-1].get('km') if d['timeline'] else None
    km = f"{n['km']} km"
    if planned and abs(planned - n['km']) >= 2.0 and abs(planned - n['km']) / max(n['km'], 1) > 0.05:
        km += f"<br><sub>實走 {planned} km</sub>"
    booked = '✅' if d['hotel']['booked'] else '🔍'
    rows.append(f"| **Day {d['day']:02d}** | {d['date']} | {d['route_line'][:52]} | {km} "
                f"| +{n['gain']}m / -{n['loss']}m | {booked} {d['hotel']['name'][:26]} "
                f"| [GPX]({d['gpx']}) |")

readme = f"""# 🚴 2026 東京・富士五湖・伊豆・東京灣 19日秋季單車騎旅

> **Official Portal**: [https://riding.braintaiwan.com](https://riding.braintaiwan.com)
> **騎行期間**: 2026 年 11 月 13 日（五）～ 12 月 1 日（二），共 {m['days']} 日
> **總里程與爬升**: 實走 **{m.get('total_planned_km', m['total_km'])} km** ／ NAVITIME 最短路徑 **{m['total_km']} km** ｜ **+{m['total_gain']:,} m**

## 📐 數據來源

里程與爬升皆取自 **NAVITIME 自転車ルート検索**（路線偏好「坡少」），非估算值：

- **距離**：對 NAVITIME 路線幾何逐點以 haversine 累加。抽驗單日與 NAVITIME 網頁顯示值一致（熱海→江之島 56.6 km 完全吻合）。
- **爬升**：NAVITIME 路線幾何的座標為 `[經度, 緯度, 標高]` 三維，標高即其標高剖面圖的資料源。以 **3 公尺遲滯門檻**累加，與 Garmin／Strava 計法一致。
- **「實走」里程**：NAVITIME 只取得每日 4–8 個路線節點，節點之間由它自選路徑。本計畫刻意繞走自行車專用道與避坑舊道，故部分日程實走里程與 NAVITIME 最短路徑有出入，表中另行標註。

單一資料正本為 `data/trip.json`；`index.html` 與本 README 皆由 `scripts_v2/build_site.py`、`scripts_v2/build_readme.py` 生成，不手工編輯。

## 🗓️ 19 日行程總表

| 天數 | 日期 | 騎行區間 | 里程 | 爬升/下降 | 住宿 | 軌跡 |
| :---: | :---: | :--- | :---: | :---: | :--- | :---: |
{chr(10).join(rows)}

已完成訂房 **{m['booked']} / {m['days']}** 晚。

## 🌟 核心互動系統

1. **[19日詳細行程表與天氣作戰室](https://riding.braintaiwan.com/)** — 每日路線節點、住宿、避坑實戰、聖地巡禮，外加按「時間 × 地點」的逐時降雨矩陣（依你的出發時間與均速推算通過各節點的時刻）。
2. **[19日全路線地圖與標高剖面](https://riding.braintaiwan.com/tokyo_cycling_19days_map_demo.html)** — Leaflet ✕ 國土地理院 DEM ✕ 互動時間軸。
3. **[19首 Suno AI 雙主唱雙風格音樂詞庫](https://riding.braintaiwan.com/suno_cycling_soundtrack_19days.html)**

## 🛠️ 專案結構

```
data/trip.json            單一資料正本（路線、住宿、文化、NAVITIME 數據）
data/navitime_stats.json  NAVITIME 五種路線偏好的實測結果
data/navitime_urls.json   各日 NAVITIME shape API 查詢網址
data/meals.json           實地查證的餐廳（逐日補完中）
data/rinko.json           各鐵道公司的單車上車規定（サイクルトレイン／輪行）
data/bailout_stations.json  沿線可撤退車站與「沒站區」（OSM Overpass 實查）
data/bailout_lodging.json   沒站區 20 km 內的實際住宿點
data/support_poi.json     沿線單車店與醫院（OSM Overpass 實查）
data/emergency.json       緊急聯絡（119／110／JNTO 熱線／都縣別救急相談）
data/day_prefectures.json 各日經過的都縣（路線座標反向地理編碼求得）
data/songs.json           每日主題曲
templates/index_template.html  網站模板（手寫區塊）
scripts_v2/               生成腳本
```

重新生成網站：

```bash
python scripts_v2/compute_navitime.py <shape 快取目錄>   # 重算 NAVITIME 數據
python scripts_v2/build_trip_json.py                     # 合併成正本
python scripts_v2/build_day_map_demos.py                 # 產生 Day 3–19 逐日地圖 Demo
python scripts_v2/build_trip_json.py                     # 再跑一次讓 map_demo 連結生效
python scripts_v2/build_site.py                          # 產生 index.html
python scripts_v2/build_readme.py                        # 產生 README.md
```

## 🚃 撤退方案

每日卡片內建兩種撤退策略，資料為實查而非估計：

- **策略 A — 沿線有站**：以 OpenStreetMap Overpass 沿 NAVITIME 路線 3 km 內查出車站，
  換算沿線里程後依序列出。並交叉比對各鐵道公司的サイクルトレイン規定，逐站標示
  「免拆車可」或「此站需輪行袋」。
- **策略 B — 沒站區**：相鄰站距超過 12 km 者標為無站區間，於該段每 6 km 取樣，
  查出 20 km 內實際存在的住宿並附偏離距離。

本路線有三條鐵路提供**免拆車**的サイクルトレイン：富士急行線（Day 3–4）、
伊豆箱根鉄道駿豆線（Day 8–9，平日有時段限制）、伊豆急行（Day 9–10）。
其餘路段依 JR 手回り品規定，須拆解並完全收進輪行袋。

## 🔧 沿線支援與緊急聯絡

- **單車店**：沿路線 5 km 內查詢 `shop=bicycle`。**Day 3、4、5、9、10、11 沿線查無任何登錄單車店** ——
  富士五湖與伊豆這兩段共六天必須完全自給，補胎工具、備胎與鏈條扣務必自帶。
- **醫院**：沿路線 10 km 內查詢 `amenity=hospital`，標示偏離距離。
- **緊急聯絡**：119（救急）／110（警察）／Japan Visitor Hotline `050-3816-2787`（24 小時多語）
  ／各都縣的救急相談電話，依當日實際所在都縣自動對應。
- **單車事故務必報警**：交通事故証明書只有報警後才核發，而保險理賠需要它。

## 🛠️ 技術棧

- **路線與標高**: NAVITIME 自転車ルート（距離、三維標高幾何）
- **天氣**: Open-Meteo（免金鑰）逐時多點預報 + 日本氣象廳去年同期實測
- **地圖**: Leaflet.js ✕ 國土地理院 DEM ｜ **圖表**: Chart.js
- **部署**: GitHub Pages / Cloudflare Pages（`riding.braintaiwan.com`）
"""
io.open(os.path.join(ROOT, 'README.md'), 'w', encoding='utf-8').write(readme)
print('生成 README.md')
