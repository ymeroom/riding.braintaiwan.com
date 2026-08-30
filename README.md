# 🚴 2026 東京・富士五湖・伊豆・東京灣 19日秋季單車騎旅

> **Official Portal**: [https://riding.braintaiwan.com](https://riding.braintaiwan.com)
> **騎行期間**: 2026 年 11 月 13 日（五）～ 12 月 1 日（二），共 19 日
> **總里程與爬升**: **683.7 km ｜ +4,923 m**

## 📐 數據來源

里程與爬升皆取自 **NAVITIME 自転車ルート検索**（路線偏好「坡少」），非估算值：

- **距離**：對 NAVITIME 路線幾何逐點以 haversine 累加。抽驗單日與 NAVITIME 網頁顯示值一致（熱海→江之島 56.6 km 完全吻合）。
- **爬升**：NAVITIME 路線幾何的座標為 `[經度, 緯度, 標高]` 三維，標高即其標高剖面圖的資料源。以 **3 公尺遲滯門檻**累加，與 Garmin／Strava 計法一致。
- **「實走」里程**：NAVITIME 只取得每日 4–8 個路線節點，節點之間由它自選路徑。本計畫刻意繞走自行車專用道與避坑舊道，故部分日程實走里程與 NAVITIME 最短路徑有出入，表中另行標註。

單一資料正本為 `data/trip.json`；`index.html` 與本 README 皆由 `scripts_v2/build_site.py`、`scripts_v2/build_readme.py` 生成，不手工編輯。

## 🗓️ 19 日行程總表

| 天數 | 日期 | 騎行區間 | 里程 | 爬升/下降 | 住宿 | 軌跡 |
| :---: | :---: | :--- | :---: | :---: | :--- | :---: |
| **Day 01** | 11/13（五） | 秋葉原 ➔ 銀座/品川 ➔ 國道15號(第一京濱) ➔ 六鄉橋 ➔ 多摩川自行車道 ➔ 府中 (50.4 | 73.7 km<br><sub>實走 81.5 km</sub> | +238m / -50m | ✅ Mt. Takao Base Camp | [GPX](day1_track.gpx) |
| **Day 02** | 11/14（六） | 高尾山口 ➔ 甲州街道(國道20) ➔ 大垂水峠(392m) ➔ 千木良 ➔ 相模湖 ➔ 日本三奇橋(猿 | 53.7 km<br><sub>實走 60.4 km</sub> | +769m / -482m | ✅ ビジネス旅館 由加利 (Yukari Ryokan) | [GPX](day2_track.gpx) |
| **Day 03** | 11/15（日） | 由加利旅館 ➔【晴天版】山中湖完整環湖一圈+忍野八海 / 【陰雨天版】新倉山五重塔 ➔ 河口湖 (宿 O | 57.8 km<br><sub>實走 53.2 km</sub> | +892m / -518m | ✅ Orange Cabin Inn far from  | [GPX](day3_track.gpx) |
| **Day 04** | 11/16（一） | 清晨紅葉迴廊 ➔【情境A】五重塔+往西騎本棲湖浩庵 / 【情境B】補騎山中湖 / 【情境C】河口湖西湖漫 | 41.1 km | +383m / -342m | 🔍 本棲湖 民宿 浩庵 / 河口湖機動 (kagelow | [GPX](day4_track.gpx) |
| **Day 05** | 11/17（二） | 【富士五湖核心天候緩衝日】應變高原多變氣候 ➔ 補完五湖 ➔ 樹海步道 ➔ 溫泉休整 | 40.2 km<br><sub>實走 38.1 km</sub> | +267m / -276m | 🔍 本棲湖浩庵 / 河口湖 / 富士吉田 | [GPX](day5_track.gpx) |
| **Day 06** | 11/18（三） | 本棲湖浩庵 ➔ 朝霧高原 ➔ 白糸之瀑 ➔ 富士宮 (千米長下坡) | 39.1 km | +162m / -949m | 🔍 富士宮市區商務溫泉飯店 | [GPX](day6_track.gpx) |
| **Day 07** | 11/19（四） | 富士宮 ➔ 潤井川CR ➔ 田子の浦港 ➔ 駿河灣千本松原海堤 ➔ 三島 | 44.4 km<br><sub>實走 41.3 km</sub> | +67m / -161m | 🔍 三島市區飯店 | [GPX](day7_track.gpx) |
| **Day 08** | 11/20（五） | 三島 ➔ 狩野川自行車道 ➔ 修善寺溫泉水口 (提早避開三連休) | 21.9 km | +116m / -37m | ✅ Onsen Yado Mizuguchi (温泉宿  | [GPX](day8_track.gpx) |
| **Day 09** | 11/21（六） | 修善寺 ➔ 避開天城峠 (走冷川峠) ➔ 一碧湖 ➔ 城崎海岸 ➔ 伊東川奈 | 47.5 km | +862m / -916m | ✅ kawana seaview standard (K | [GPX](day9_track.gpx) |
| **Day 10** | 11/22（日） | 伊東川奈 ➔ 宇佐美 ➔ 避開危險長隧道 (走網代舊街) ➔ Apt南熱海 | 16.8 km | +164m / -203m | ✅ Apt南熱海-網代 | [GPX](day10_track.gpx) |
| **Day 11** | 11/23（一） | Apt南熱海 ➔ 熱海梅園最晚紅葉 ➔ 熱海銀座商店街 ➔ 晚上 20:20 熱海海上花火大會 (宿 g | 12.7 km<br><sub>實走 10.8 km</sub> | +235m / -234m | ✅ guest house MARUYA | [GPX](day11_track.gpx) |
| **Day 12** | 11/24（二） | 熱海銀座 MARUYA ➔ 縣道740號柑橘道 ➔ 小田原城 ➔ 湘南海岸防風林 ➔ 江之島 | 65.6 km<br><sub>實走 61.5 km</sub> | +468m / -468m | 🔍 江之島 / 藤澤市區飯店 | [GPX](day12_track.gpx) |
| **Day 13** | 11/25（三） | 江之島 ➔ 鎌倉高校前平交道 ➔ 長谷寺 ➔ 柏尾川水岸 ➔ 橫濱港未來 | 32.6 km | +111m / -113m | 🔍 橫濱港未來飯店 | [GPX](day13_track.gpx) |
| **Day 14** | 11/26（四） | 橫濱 ➔ 第一京濱/羽田 ➔ 豐洲大橋 ➔ 台場海濱公園 | 37.6 km | +45m / -45m | 🔍 台場 / 有明飯店 | [GPX](day14_track.gpx) |
| **Day 15** | 11/27（五） | 台場 ➔ 葛西臨海公園 ➔ 中川水岸綠道 ➔ 柴又 ➔ 葛飾金町花庵 | 27.5 km | +37m / -41m | ✅ 花庵旅舍 (Hostel Hana An) | [GPX](day15_track.gpx) |
| **Day 16** | 11/28（六） | 金町出發 ➔【輕裝免行李】江戶川CR / 荒川 ➔ 葛飾老街 ➔ 金町 | 29.8 km<br><sub>實走 45.0 km</sub> | +19m / -17m | ✅ 花庵旅舍 (Hostel Hana An) | [GPX](day16_track.gpx) |
| **Day 17** | 11/29（日） | 金町退房 ➔ 水元公園（萬棵水杉黃金森林見頃）➔ 柴又 ➔ 淺草 | 14.6 km<br><sub>實走 16.6 km</sub> | +17m / -14m | 🔍 淺草 / 上野 / 東京市區飯店 | [GPX](day17_track.gpx) |
| **Day 18** | 11/30（一） | 淺草 ➔ 東大本鄉銀杏 ➔ 皇居 ➔ 明治神宮外苑銀杏大道 ➔ 秋葉原 | 24.8 km | +48m / -48m | 🔍 秋葉原 / 上野飯店 | [GPX](day18_track.gpx) |
| **Day 19** | 12/01（二） | 秋葉原市區 ➔ 神田明神 ➔ CycleTrip Base 還車 ➔ 日暮里 ➔ 機場 | 2.3 km<br><sub>實走 7.9 km</sub> | +23m / -23m | 🔍 返台溫暖的家 | [GPX](day19_track.gpx) |

已完成訂房 **9 / 19** 晚。

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
data/songs.json           每日主題曲
templates/index_template.html  網站模板（手寫區塊）
scripts_v2/               生成腳本
```

重新生成網站：

```bash
python scripts_v2/compute_navitime.py <shape 快取目錄>   # 重算 NAVITIME 數據
python scripts_v2/build_trip_json.py                     # 合併成正本
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

## 🛠️ 技術棧

- **路線與標高**: NAVITIME 自転車ルート（距離、三維標高幾何）
- **天氣**: Open-Meteo（免金鑰）逐時多點預報 + 日本氣象廳去年同期實測
- **地圖**: Leaflet.js ✕ 國土地理院 DEM ｜ **圖表**: Chart.js
- **部署**: GitHub Pages / Cloudflare Pages（`riding.braintaiwan.com`）
