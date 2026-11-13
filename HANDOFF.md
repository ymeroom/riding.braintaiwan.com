# 交班單：旅途中的網站維護

> 寫給接手的雲端 Claude。使用者 11/13–12/1 在日本騎車，電腦關機，只用手機透過 claude.ai/code 下指令。
> 最後更新：2026-11-08（交班前的本機 session）

## 1. 這個 repo 是什麼

- 2026 東京單車騎旅（19 天，Day 1＝11/13，Day k＝11/(12+k)，Day 19＝12/1）的行程網站。
- `main` 根目錄由 GitHub Pages 發佈到 https://riding.braintaiwan.com ，**推上 main 約 1–3 分鐘就上線**。
- **repo 是公開的**：不要放個人資料（Email、航班、訂房代號、手機號碼等）。

## 2. 絕對不要做的事

- **不要跑 `scripts_v2/build_site.py`**。`index.html` 有很多手改功能（live-cams、war-room、`sp-chip`、週間預報、穿搭建議），重新產生會全部洗掉。
- 改 `index.html` 只能做**片段插入／替換**（用 Python 依序定位，不要全域 replace）。
- 改完一定跑第 5 節的安全閘門，不過就 `git checkout -- .` 還原。

## 3. 每日自動排程（已在跑）

- Routine：`trig_015CqtC1rqD3E4Eev1jG2hDF`「東京騎旅 每日週間預報＋穿搭」
  - 管理頁：https://claude.ai/code/routines/trig_015CqtC1rqD3E4Eev1jG2hDF
  - 每天 02:47 UTC（10:47 台北／11:47 日本），11/8–12/1，模型 Sonnet，**直接推 main**。
  - 做的事：週間預報＋👕 穿搭建議（未來的 Day）、總覽表天氣欄、１か月予報有新版就換、颱風檢查。
- ⚠️ **已知問題**：11/7 測試時雲端沙盒的 proxy 擋了 `www.jma.go.jp`（CONNECT 403）。
  使用者需要在 claude.ai/code → 環境設定 → **Default** 環境，把網路改成自訂並允許 `www.jma.go.jp`。
  若排程回報「連不上氣象庁」，先提醒使用者做這個設定。
- 排程失敗時：`RemoteTrigger list_runs` → `get_run_log` 查原因；也可以 `run` 手動重跑。

## 4. 網站上的天氣區塊結構

每天卡片內有一個 `            <div class="seasonal-box">…</div>`（第 k 個＝Day k，全站共 19 個），裡面依序是：

1. ３か月予報（自動產生的部分）
2. `<div class="seas-1m">🗓️ <strong>週間預報</strong>（M/D HH:00 JST 發布・縣）：…</small></div>`
3. `<div class="seas-1m">👕 <strong>穿搭建議</strong>（依 M/D 週間預報）：…</div>`
4. `<div class="seas-1m">📅 <strong>1 個月預報</strong>（M/D 發布，…）：…</div>`
5. `<div class="seas-1m">🎥 <strong>Insta360 拍攝</strong>（X3）：…</div>`（每天的拍攝路段，手寫的，更新天氣時保留不動）

總覽表每列的天氣 `<td>` 內有 `<div class="wx-outlook">🗓️ <strong>週間預報</strong>（M/D）：…</div>`。

格式範例請直接看 `index.html` 裡 Day 1、Day 2 現有的內容照抄。

### 目前狀態（交班時）

| 項目 | 版本 | 下一次 |
|---|---|---|
| ３か月予報 | 10/20 發布（全部 19 天） | 11/24 前後（14:00 JST）|
| １か月予報 | 11/5 發布（全部 19 天） | 每週四 14:30 JST（11/12、11/19、11/26）|
| 週間預報＋穿搭 | 11/7 11:00 發布，只有 Day 1–2 | 每天 11:00／17:00 JST，涵蓋明天起 7 天 |
| 颱風 | 11/7：TC2638 往東北東遠離（約 29.6°N 152°E），不影響關東・東海 | 每天看 |

## 5. 安全閘門（推 main 前必做）

比對修改前後的 `index.html`：

- `seasonal-box` 出現次數＝19
- `live-cams`、`war-room`、`sp-chip`、`<script`、`</html>` 的出現次數不變
- 檔案大小變化在 ±3% 內
- Python `html.parser` 能 parse 完；`git diff --stat` 只動到預期的檔案
- 抽查改到的數字與 JSON 一致

## 6. 資料來源（氣象庁 bosai JSON，不要爬 HTML）

- 週間預報：`https://www.jma.go.jp/bosai/forecast/data/forecast/<office>.json`，取陣列 index 1。
  - `timeSeries[0]`：weatherCodes、pops、reliabilities；`timeSeries[1]`：tempsMin/Max（含 Upper/Lower）；`tempAverage`：平年值。
  - office：東京 130000、神奈川 140000、山梨 190000（只有甲府站，富士五湖約再低 3–5°C）、静岡 220000、埼玉 110000。
  - 各 Day 對應的縣：`data/day_prefectures.json`。路線細節：`data/trip.json`（route_line、expert_tip）。
- １か月：`https://www.jma.go.jp/bosai/season/data/P1M/010300.json`（関東甲信）、`010400.json`（東海）。
- ３か月：同路徑 `P3M`。更新方式見 `scripts_v2/fetch_seasonal_outlook.py`，但**只能片段替換**（用 `build_site` 的 `render_seasonal_day(n, seas)`、`outlook_cell(n, seas)` 算出新舊片段逐天換，`weather-outlook.html` 用 `render_outlook_page(trip, seas, fol)` 重寫）。
- 颱風：`https://www.jma.go.jp/bosai/typhoon/data/targetTc.json` → `TC<id>/specifications.json`。

## 7. 穿搭建議用的衣物（只能用這些名稱）

- **騎車**：短袖排汗衣（1 件）、刷毛長袖排汗衣（1 件）、紫色長袖（薄全拉鍊車衣，中層）、綠色外套（Van Rysel 冬季防風保暖）、白色航海外套（防雨防風）、MH500 雨褲（右褲管要束緊）、刷毛長車褲（冷天）、薄長車褲（暖天）、防風手套、鞋套。
- **不騎車**：黑紅刷毛外套、Uniqlo 喀什米爾發熱衣（1 件，房間與晚上出門穿；晚上出門穿「發熱衣＋黑紅刷毛外套」）、MH100 長褲（晚上出門；富士五湖等冷的晚上外套 MH500 雨褲）、短褲（房間、睡覺）。
- 發熱衣**不可騎車穿**（吸汗不易乾，停車或下坡會失溫）。
- 室內（使用者實測）：黑紅刷毛外套在有暖氣的室內太熱，房間裡穿發熱衣就好，覺得涼再加紫色長袖；黑紅刷毛外套只在晚上出門時穿。
- 底層選擇：≤5°C、高原或下雨的冷天穿刷毛長袖排汗衣，其他天都穿短袖排汗衣（涼的早上靠紫色長袖＋綠色外套保暖）。
- 11/12 起已不帶：薄長袖排汗衣、第 2 件短袖排汗衣，**不要再出現在穿搭建議裡**。
- 規則：降水機率 ≥50% 要講雨具怎麼穿；最低溫 ≤5°C 要提刷毛長車褲、防風手套、鞋套。
- 使用者衣物已備齊，**不要推薦購買新衣物**。

## 8. 手機上可能收到的臨時請求

- 「今天／明天天氣？」→ 抓 JMA JSON 直接回答，必要時更新網站。
- 「改路線／跳過某天」→ 改 `index.html` 對應片段即可，`gpx`、地圖 demo 不必重產（除非使用者要求）。
  注意：Day 4／5 的 gpx 與地圖 demo 仍是舊規劃（Day 4 收本栖湖、Day 5 浩庵繞圈），訂房已改為 Day 4 住河口湖船津、Day 5 河口湖→本栖湖。使用者決定看天氣再定，尚未重跑。
- 改完用繁體中文、精簡回報（使用者在路上看手機）。

## 8.5 手繪行程圖（sketches/）

- `sketches/dayN.html`（19 頁）＋ `sketches/index.html`（木版畫海報總覽），每天四種：① 繪卷 ② 旅のしおり ③ 鳥瞰圖 ④ 木版畫。
- 由 `scripts_v2/build_sketches.py` 產生：只讀 `data/trip.json`、`dayN_track.gpx`，只寫 `sketches/`，**可以安全重跑**（跟 build_site 不同）。
- Day 1 用 `sketches/_hand/day1_v*.svg` 的手繪版，其他天由程式依里程點、GPX、景物關鍵字畫。改路線後重跑即可。
- 列印檔 `sketches/print/`：`dayN-postcard.pdf`、`dayN-a5.pdf`（各 4 頁）、`all-postcard.pdf`、`all-a5.pdf`（76 頁），含 3 mm 出血。
  改圖後依序跑 `python3 scripts_v2/build_sketches.py` → `node scripts_v2/build_print.js`（全部約 5 分鐘；`node scripts_v2/build_print.js 4 5` 只重做指定天，不更新全集檔）。
- `index.html` 每天卡片的 `day-content` 開頭有一個 `sketch-link` 連結；頂部按鈕列有「🎨 19 日手繪行程圖」。

## 8.6 一日一頁「今日重點」（daily/、today/）

- `daily/dayN.html`：手機版當天重點（天氣・穿搭、路線里程點＋地圖鈕、吃飯、住宿、撤退車站、單車店・醫院、緊急電話）。
- 由 `scripts_v2/build_daily.py` 產生：讀 `data/trip.json`＋從 `index.html` 抓最新週間預報與穿搭，只寫 `daily/`，可安全重跑。
  **每次更新天氣後要跑一次 `python3 scripts_v2/build_daily.py`**，兩邊天氣才會一致（自動排程的指令還沒加這一步）。
- `today/`：依日本時間自動顯示當天那頁（行程前顯示 Day 1、結束後顯示 Day 19），可加到手機主畫面。
- 主網站頂部按鈕「📱 今日重點」、每天卡片的 `daily-link`。

## 8.7 拍攝檢查表（filming.html）

- `filming.html`：Insta360 X3（360° 5.7K 30fps）＋ GO 3S（2.7K 30fps）＋ S23 Ultra 手機（4K 30fps、HDR10+ 關、位置標籤開）設定與每日拍攝／備份檢查表，手寫靜態頁，勾選存在瀏覽器 localStorage。
- 主網站頂部按鈕「🎥 拍攝檢查表」。

## 8.7 實騎紀錄（actual/）

- 使用者每天會上傳 Garmin 的 FIT（zip）。解析後只公開：距離、騎乘／全程時間、爬升、出發／抵達時間、簡化軌跡。
  **心率、卡路里、原始 FIT、逐點時間戳一律不進 repo**（repo 公開）。
- 軌跡：`actual/dayN_actual.gpx`（RDP 簡化、無時間）；摘要：`data/actual_rides.json`（build_daily.py 會在今日重點頁最上面顯示）。
- 手繪圖：`data/actual_rides.json` 該天有 `timeline`（含 time、coord）＋`route_line` 時，`build_sketches.py` 改用實騎資料畫（Day 1 不再用 `_hand/` 手繪版），之後重跑 `build_print.js`。
- 地圖：在 `dayN_route_map_demo.html` 的 `map.fitBounds(...)` 後加紅色虛線 `actualLine`＋圖層切換，`#map` 下方加 `actual-ride` 說明框；主網站該天卡片 `daily-link` 後加 `actual-ride` 區塊。

## 9. Git 慣例

- commit 訊息英文；推 main 被拒就 `git pull --rebase origin main` 後重跑閘門再推。
- 結尾加 `Co-Authored-By:` 行（依當下模型）。
