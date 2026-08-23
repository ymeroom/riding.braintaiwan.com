import urllib.request, json, sys, os

# Update Day 1 - Day 5 metadata with the exact requested routes & logic

# Re-run generator with exact user descriptions
with open("d:/2026東京單車騎旅/generate_19days_data.py", "r", encoding="utf-8") as f:
    code = f.read()

# Update Day 1 title and cues
old_d1 = '''    {
        "day": 1,
        "date": "11/13（五）",
        "title": "出城篇：多摩川水岸 ➔ 淺川 ➔ 高尾山口極樂湯",
        "wps": [cycletrip_base, rokugo_bridge, tamagawa_fuchu, asakawa_junction, takao_basecamp],
        "hotel": "Mt. Takao Base Camp",
        "hotel_addr": "東京都八王子市高尾町1799-3",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%85%AB%E7%8E%8B%E5%AD%90%E5%B8%82%E9%AB%98%E5%B0%BE%E7%94%BA1799-3+Mt.Takao+Base+Camp",
        "booked": True,
        "cues": [
            "09:30 秋葉原 CycleTrip Base 出發，走國道 15 號（第一京濱）南下",
            "六鄉橋切入多摩川自行車道（左岸/右岸專用道）",
            "府中四谷橋切入淺川自行車道，全封閉平緩逆流上坡",
            "抵達高尾山口站旁 Mt. Takao Base Camp 入住，步行 3 分鐘泡極樂湯"
        ],
        "weather": "☀️ 晴 ｜ 11.8°C ~ 19.6°C ｜ 0.0mm ｜ 9.4h",
        "foliage": "多摩川水岸秋芒 ｜ 淺川水岸林木初染紅"
    },'''

new_d1 = '''    {
        "day": 1,
        "date": "11/13（五）",
        "title": "出城篇：秋葉原 ➔ 銀座/品川 ➔ 國道15號(第一京濱) ➔ 六鄉橋 ➔ 多摩川自行車道 ➔ 府中 (50.4km) ➔ 高尾山口 (Mt. Takao Base Camp 190m)",
        "wps": [cycletrip_base, [139.7680, 35.6700], [139.7400, 35.6300], rokugo_bridge, tamagawa_fuchu, asakawa_junction, takao_basecamp],
        "hotel": "Mt. Takao Base Camp",
        "hotel_addr": "東京都八王子市高尾町1799-3",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%85%AB%E7%8E%8B%E5%AD%90%E5%B8%82%E9%AB%98%E5%B0%BE%E7%94%BA1799-3+Mt.Takao+Base+Camp",
        "booked": True,
        "cues": [
            "09:30 秋葉原 CycleTrip Base 出發，穿過銀座與品川，沿國道 15 號（第一京濱）平坦南下",
            "六鄉橋直接切入「多摩川自行車道」，享受全封閉水岸專用道逆流緩上",
            "抵達府中四谷橋（里程約 50.4 km），無縫切入「淺川自行車道」",
            "沿淺川平緩騎至終點高尾山口，入住 Mt. Takao Base Camp（海拔 190m），步行 3 分鐘泡極樂湯溫泉"
        ],
        "weather": "☀️ 晴 ｜ 11.8°C ~ 19.6°C ｜ 0.0mm ｜ 9.4h",
        "foliage": "多摩川水岸秋芒 ｜ 淺川水岸林木初染紅"
    },'''

code = code.replace(old_d1, new_d1)

# Update Day 2 title and cues
old_d2 = '''    {
        "day": 2,
        "date": "11/14（六）",
        "title": "山道篇：清晨大垂水峠 ➔ 相模湖 ➔ 縣道35秋山街道 ➔ 都留",
        "wps": [takao_basecamp, otarumi_pass, sagamiko, akiyama_highway, tsuru_yukari],
        "hotel": "ビジネス旅館 由加利 (Yukari Ryokan)",
        "hotel_addr": "山梨縣都留市上谷1丁目3-4",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E9%83%BD%E7%95%99%E5%B8%82%E4%B8%8A%E8%B0%B71%E4%B8%81%E7%9B%AE3-4+%E7%94%B1%E5%8A%A0%E5%88%A9%E6%97%85%E9%A4%A8",
        "booked": True,
        "cues": [
            "08:00 高尾出發，清晨無車翻越大垂水峠（標高 392m）",
            "相模湖畔左轉，切入山梨縣道 35 號（秋山街道）",
            "整整 35km 沿秋山川溪谷緩升，零大貨車、路況極幽靜",
            "穿過秋山隧道（674m）順暢大下坡滑降至都留市入住由加利旅館"
        ],
        "weather": "☀️ 快晴 ｜ 7.8°C ~ 17.2°C ｜ 0.0mm ｜ 8.9h",
        "foliage": "🍁 秋山溪谷見頃 ｜ 兩側山壁層林盡染"
    },'''

new_d2 = '''    {
        "day": 2,
        "date": "11/14（六）",
        "title": "山道篇：Mt. Takao Base Camp (190m) ➔ 甲州街道(國道20) ➔ 大垂水峠 (392m) ➔ 相模湖 (205m) ➔ 縣道35號秋山街道 ➔ 都留 由加利旅館 (484m)",
        "wps": [takao_basecamp, otarumi_pass, sagamiko, akiyama_highway, tsuru_yukari],
        "hotel": "ビジネス旅館 由加利 (Yukari Ryokan)",
        "hotel_addr": "山梨縣都留市上谷1丁目3-4",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E9%83%BD%E7%95%99%E5%B8%82%E4%B8%8A%E8%B0%B71%E4%B8%81%E7%9B%AE3-4+%E7%94%B1%E5%8A%A0%E5%88%A9%E6%97%85%E9%A4%A8",
        "booked": True,
        "cues": [
            "08:00 由 Mt. Takao Base Camp 出發，沿甲州街道（國道20號）直攻大垂水峠（標高 392m，爬升 +202m，清晨避開觀光大車）",
            "順坡滑降至相模湖畔（海拔 205m），左轉切入山梨縣道 35 號（秋山街道）",
            "整整 35km 沿秋山川幽靜溪谷緩緩爬升，完全避開大貨車",
            "穿過標高 674m 的秋山隧道後，一路順暢大下坡滑降至都留市，入住由加利旅館（海拔 484m）"
        ],
        "weather": "☀️ 快晴 ｜ 7.8°C ~ 17.2°C ｜ 0.0mm ｜ 8.9h",
        "foliage": "🍁 秋山溪谷見頃 ｜ 兩側山壁層林盡染"
    },'''

code = code.replace(old_d2, new_d2)

# Update Day 3 title and cues
old_d3 = '''    {
        "day": 3,
        "date": "11/15（日）",
        "title": "湖泊篇：都留 ➔ 忍野八海 ➔ 山中湖紅葉祭 ➔ 河口湖紅葉迴廊",
        "wps": [tsuru_yukari, [138.8600, 35.5200], oshino_hakkai, yamanakako, arakurayama, orange_cabin],
        "hotel": "Orange Cabin Inn far from station",
        "hotel_addr": "山梨縣南都留郡富士河口湖町河口1916-3",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E5%8D%97%E9%83%BD%E7%95%99%E9%83%A1%E5%84%82%E5%A3%AB%E6%B2%B3%E5%8F%A3%E6%B9%96%E7%94%BA%E6%B2%B3%E5%8F%A31916-3+Orange+Cabin+Inn",
        "booked": True,
        "cues": [
            "由加利旅館出發，走富士急行線生活農路（縣道713號）緩上",
            "探訪忍野八海神之湧泉與現烤草餅",
            "巡航海拔 1,000m 山中湖旭日丘紅葉祭與長池親水公園",
            "順坡滑降至富士吉田金鳥居與新倉山五重塔，下午入住 Orange Cabin",
            "傍晚步行 3 分鐘漫步「河口湖紅葉迴廊」夜間點燈"
        ],
        "weather": "☀️ 快晴 ｜ 4.5°C ~ 15.1°C ｜ 0.0mm ｜ 9.6h",
        "foliage": "🔥 雙湖見頃最盛期 ｜ 楓紅如火與白雪富士"
    },'''

new_d3 = '''    {
        "day": 3,
        "date": "11/15（日）",
        "title": "湖泊篇：由加利旅館 ➔【晴天版】山中湖完整環湖一圈+忍野八海 / 【陰雨天版】新倉山五重塔 ➔ 河口湖 (宿 Orange Cabin Inn)",
        "wps": [tsuru_yukari, [138.8600, 35.5200], oshino_hakkai, yamanakako, [138.8500, 35.4250], arakurayama, orange_cabin],
        "hotel": "Orange Cabin Inn far from station",
        "hotel_addr": "山梨縣南都留郡富士河口湖町河口1916-3",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E5%8D%97%E9%83%BD%E7%95%99%E9%83%A1%E5%84%82%E5%A3%AB%E6%B2%B3%E5%8F%A3%E6%B9%96%E7%94%BA%E6%B2%B3%E5%8F%A31916-3+Orange+Cabin+Inn",
        "booked": True,
        "cues": [
            "【☀️ 晴天版本（推薦）】：由加利出發 ➔ 忍野八海神之湧泉 ➔ 海拔1,000m「山中湖完整繞湖一圈（長池親水公園+旭日丘紅葉祭）」➔ 經富士吉田滑降至河口湖 Orange Cabin (53.2km, +799m)",
            "【☁️ 陰雨天版本（避險）】：由加利出發 ➔ 避開千米高原，沿生活農路直達「新倉山五重塔」拍照 ➔ 直接前往 Orange Cabin 提早入住休整 (22.2km, +532m)",
            "傍晚步行 3 分鐘漫步「河口湖紅葉迴廊」夜間點燈，完全免塞車"
        ],
        "weather": "☀️ 快晴 ｜ 4.5°C ~ 15.1°C ｜ 0.0mm ｜ 9.6h",
        "foliage": "🔥 雙湖見頃最盛期 ｜ 晴天環山中湖、陰天直取五重塔"
    },'''

code = code.replace(old_d3, new_d3)

# Update Day 4 title and cues
old_d4 = '''    {
        "day": 4,
        "date": "11/16（一）",
        "title": "探索篇：清晨紅葉迴廊 ➔ 湖北View Line ➔ 西湖 ➔ 精進湖 ➔ 本棲湖浩庵",
        "wps": [orange_cabin, oishi_park, saiko_iyashi, shojiko, motosuko_kouan],
        "hotel": "本棲湖 民宿 浩庵 / 機動",
        "hotel_addr": "山梨縣南巨摩郡身延町中之倉2926",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E5%8D%97%E5%B7%A8%E6%91%A9%E9%83%A1%E8%BA%AB%E5%BB%B6%E7%94%BA%E4%B8%AD%E4%B9%8B%E5%80%892926+%E6%B5%A9%E5%BA%B5",
        "booked": False,
        "cues": [
            "06:30 步行/單車獨享無人「河口湖紅葉迴廊」晨光空景",
            "沿湖北 View Line 騎行大石公園、西湖療癒之里根場茅草屋",
            "探訪精進湖「子抱富士」，抵達本棲湖北岸浩庵",
            "下午在房間窗前欣賞千圓紙幣逆富士與夕陽"
        ],
        "weather": "☀️ 快晴 ｜ 3.2°C ~ 14.6°C ｜ 0.0mm ｜ 9.1h",
        "foliage": "🔥 紅葉迴廊最高峰 ｜ 深紅隧道與湖面倒影"
    },'''

new_d4 = '''    {
        "day": 4,
        "date": "11/16（一）",
        "title": "分支篇：清晨紅葉迴廊 ➔【情境A】五重塔+往西騎本棲湖浩庵 / 【情境B】補騎山中湖 / 【情境C】河口湖西湖漫遊",
        "wps": [orange_cabin, arakurayama, oishi_park, saiko_iyashi, shojiko, motosuko_kouan],
        "hotel": "本棲湖 民宿 浩庵 / 河口湖機動 (kagelow / 富士見205)",
        "hotel_addr": "山梨縣南巨摩郡身延町中之倉2926",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%9C%AC%E6%A3%B2%E6%B9%96%E6%B5%A9%E5%BA%B5",
        "booked": False,
        "cues": [
            "【必做】06:30 步行/單車獨享無人「河口湖紅葉迴廊」晨光深紅隧道",
            "【分支A（Day 3 已去過山中湖）】：前往新倉山五重塔 ➔ 沿湖北View Line/大石公園 ➔ 西湖療癒之里 ➔ 精進湖 ➔ 直攻本棲湖浩庵 (41.9km, +392m)",
            "【分支B（Day 3 未去山中湖）】：今天輕裝補騎山中湖環湖+忍野八海 ➔ 返回河口湖 (kagelow / 富士見205 / 浩庵)",
            "【分支C（天候依然不佳）】：在河口湖與西湖周邊景觀咖啡、大石公園、溫泉休整漫步"
        ],
        "weather": "☀️ 快晴 ｜ 3.2°C ~ 14.6°C ｜ 0.0mm ｜ 9.1h",
        "foliage": "🔥 紅葉迴廊最高峰 ｜ 依前日天候靈活啟動分支"
    },'''

code = code.replace(old_d4, new_d4)

# Update Day 5 title and cues
old_d5 = '''    {
        "day": 5,
        "date": "11/17（二）",
        "title": "緩衝篇：富士五湖核心天候緩衝日 ➔ 樹海步道 ➔ 溫泉休整",
        "wps": [motosuko_kouan, shojiko, [138.6900, 35.4800], motosuko_kouan],
        "hotel": "本棲湖浩庵 / 河口湖 / 富士吉田",
        "hotel_addr": "山梨縣富士五湖周邊",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%9C%AC%E6%A3%B2%E6%B9%96%E6%B5%A9%E5%BA%B5",
        "booked": False,
        "cues": [
            "高原天候防護定海神針，若前兩天遇低溫陣雨在此全數補完",
            "漫遊青木原樹海、富岳風穴、鳴澤冰穴自然奇景",
            "富士展望溫泉 Yurari 享受露天暖湯，品嚐南瓜餺飥麵"
        ],
        "weather": "☀️ 晴朗 ｜ 5.8°C ~ 16.4°C ｜ 0.0mm ｜ 8.8h",
        "foliage": "🔥 西湖/本棲湖深秋紅葉 ｜ 蒼茫寧靜"
    },'''

new_d5 = '''    {
        "day": 5,
        "date": "11/17（二）",
        "title": "緩衝篇：【富士五湖核心天候緩衝日】應變高原多變氣候 ➔ 補完五湖 ➔ 樹海步道 ➔ 溫泉休整",
        "wps": [motosuko_kouan, shojiko, [138.6900, 35.4800], motosuko_kouan],
        "hotel": "本棲湖浩庵 / 河口湖 / 富士吉田",
        "hotel_addr": "山梨縣富士五湖周邊",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%9C%AC%E6%A3%B2%E6%B9%96%E6%B5%A9%E5%BA%B5",
        "booked": False,
        "cues": [
            "【核心天候緩衝】：應對 11 月中旬富士五湖多變氣候（防低溫、陣雨、初霜），全日保留 100% 彈性",
            "若前幾天天候受阻：今日可完整補齊山中湖、新倉山或五湖未竟景點！",
            "若天候良好：深度探訪青木原樹海、富岳風穴、鳴澤冰穴，前往富士展望之湯 Yurari 享受露天溫泉暖湯與甲州餺飥麵"
        ],
        "weather": "☀️ 晴朗 ｜ 5.8°C ~ 16.4°C ｜ 0.0mm ｜ 8.8h",
        "foliage": "🔥 西湖/本棲湖深秋紅葉 ｜ 熔岩樹海蒼茫"
    },'''

code = code.replace(old_d5, new_d5)

with open("d:/2026東京單車騎旅/generate_19days_data.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated generate_19days_data.py with exact user specifications for Days 1-5!")
