def fetch_osrm_with_retry(url, retries=3):
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=12) as resp:
                return json.loads(resp.read().decode('utf-8'))['routes'][0]
        except Exception as e:
            print(f"OSRM retry {attempt+1}/{retries} due to: {e}")
            time.sleep(1.5)
    return None

import urllib.request, urllib.parse, json, sys, time, os
sys.stdout.reconfigure(encoding='utf-8')

# Key Waypoints for all 19 days
cycletrip_base = [139.7785, 35.6985] # Akihabara (5m)
rokugo_bridge = [139.7120, 35.5390] # Rokugo (3m)
tamagawa_fuchu = [139.4850, 35.6600] # Fuchu (40m)
asakawa_junction = [139.4000, 35.6550] # Asakawa junction (75m)
takao_basecamp = [139.2708, 35.6315] # Mt. Takao Base Camp (190m)

otarumi_pass = [139.2450, 35.6150] # Otarumi Pass (392m)
sagamiko = [139.1900, 35.6130] # Sagami Lake (205m)
akiyama_highway = [139.0600, 35.5800] # Pref 35 Akiyama (350m)
tsuru_yukari = [138.90582, 35.55057] # Yukari Ryokan (484m)

oshino_hakkai = [138.8320, 35.4600] # Oshino (930m)
yamanakako = [138.8800, 35.4050] # Yamanakako Asahigaoka (990m)
arakurayama = [138.8020, 35.5010] # Arakurayama Pagoda (850m)
orange_cabin = [138.7610, 35.5280] # Orange Cabin Inn (845m)

oishi_park = [138.7450, 35.5230] # Oishi Park (835m)
saiko_iyashi = [138.6750, 35.5000] # Saiko Iyashi no Sato (910m)
shojiko = [138.6080, 35.4850] # Shojiko (900m)
motosuko_kouan = [138.564758, 35.473095] # Motosuko Kouan (905m)

asagiri_plateau = [138.5750, 35.4000] # Asagiri (830m)
shiraito_falls = [138.5880, 35.3120] # Shiraito (450m)
fujinomiya_center = [138.6150, 35.2220] # Fujinomiya (115m)

tagonoura_port = [138.6950, 35.1420] # Tagonoura (2m)
senbonmatsubara = [138.8000, 35.1050] # Senbonmatsubara (3m)
numazu_port = [138.8580, 35.0830] # Numazu (3m)
mishima_center = [138.9150, 35.1220] # Mishima (25m)

shuzenji_mizuguchi = [138.92598, 34.97020] # Onsen Yado Mizuguchi (99m)
hiekawa_pass = [139.0200, 34.9600] # Hiekawa Pass (380m)
ippeki_lake = [139.1000, 34.9200] # Ippeki Lake (170m)
jogasaki_coast = [139.1300, 34.8900] # Jogasaki Coast (25m)
kawana_seaview = [139.12343, 34.96987] # kawana seaview standard (36m)

usami_beach = [139.0800, 35.0080] # Usami (5m)
ajiro_old_street = [139.0880, 35.0420] # Ajiro (5m)
apt_minami_atami = [139.08211, 35.04507] # Apt南熱海 (下多賀440, 4m)
izu_kansya = [139.06842, 35.05392] # Izu Kansya (下多賀1473-11, 9m)
atami_baien = [139.0550, 35.0980] # Atami Plum Garden (85m)
atami_sun_beach = [139.0750, 35.0970] # Atami Sun Beach (3m)

pref740_mikan = [139.1450, 35.1550] # Pref 740 Mikan Highway (150m)
odawara_castle = [139.1550, 35.2500] # Odawara Castle (15m)
shonan_cr = [139.3100, 35.3200] # Shonan Coastal Path (5m)
enoshima_island = [139.4820, 35.3080] # Enoshima (5m)

kamakura_hase = [139.5350, 35.3120] # Kamakura Hasedera (15m)
kashio_river_cr = [139.5300, 35.3800] # Kashio River (12m)
yokohama_minatomirai = [139.6350, 35.4550] # Minato Mirai (4m)

toyosu_bridge = [139.7820, 35.6500] # Toyosu Bridge (8m)
odaiba_marine_park = [139.7750, 35.6300] # Odaiba (4m)

kasai_rinkai_park = [139.8600, 35.6450] # Kasai (3m)
shibamata_taishakuten = [139.8780, 35.7570] # Shibamata (2m)
hostel_hana_an = [139.86586, 35.76727] # Hostel Hana An Kanamachi (1m)

mizumoto_park = [139.8700, 35.7870] # Mizumoto Park (1m)
kawagoe_kitain = [139.4850, 35.9180] # Kawagoe Kitain (18m)
asakusa_kaminarimon = [139.7980, 35.7130] # Asakusa Kaminarimon (3m)

todai_hongo = [139.7620, 35.7120] # Todai Hongo (22m)
imperial_palace = [139.7550, 35.6850] # Imperial Palace (12m)
jingu_gaien = [139.7180, 35.6740] # Meiji Jingu Gaien (32m)
kanda_myojin = [139.7680, 35.7020] # Kanda Myojin (15m)

days_meta = [
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
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
    },
    {
        "day": 6,
        "date": "11/18（三）",
        "title": "下坡篇：本棲湖浩庵 ➔ 朝霧高原 ➔ 白糸之瀑 ➔ 富士宮 (千米長下坡)",
        "wps": [motosuko_kouan, asagiri_plateau, shiraito_falls, fujinomiya_center],
        "hotel": "富士宮市區商務溫泉飯店",
        "hotel_addr": "靜岡縣富士宮市（淺間大社總本社旁）",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E5%AF%8C%E5%A3%AB%E5%B1%B1%E6%9C%AC%E5%AE%AE%E6%B7%BA%E9%96%93%E5%A4%A7%E7%A4%BE",
        "booked": False,
        "cues": [
            "清晨本棲湖水鏡逆富士晨光攝影",
            "南下朝霧高原牧場，右牛群左富士雄偉西壁",
            "天下名瀑「白糸之瀑」水氣如絹、紅葉環繞",
            "沿潤井川河谷千米大長下坡爽快滑降富士宮，品嚐炒麵"
        ],
        "weather": "☀️ 萬里晴空 ｜ 4.2°C ~ 15.8°C ｜ 0.0mm ｜ 9.0h",
        "foliage": "朝霧高原金黃芒草 ｜ 白糸之瀑水氣楓紅"
    },
    {
        "day": 7,
        "date": "11/19（四）",
        "title": "海堤篇：富士宮 ➔ 潤井川CR ➔ 田子の浦港 ➔ 駿河灣千本松原海堤 ➔ 三島",
        "wps": [fujinomiya_center, tagonoura_port, senbonmatsubara, numazu_port, mishima_center],
        "hotel": "三島市區飯店",
        "hotel_addr": "靜岡縣三島市（三嶋大社旁）",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E4%B8%89%E5%B6%8B%E5%A4%A7%E7%A4%BE",
        "booked": False,
        "cues": [
            "由富士宮沿潤井川自行車道緩降至田子の浦港",
            "切入全封閉千本松原海岸海堤專用道，15km 零紅綠燈狂飆",
            "沼津港大口享用新鮮深海魚海鮮丼",
            "平路巡航至三島市，漫步三嶋大社與源兵衛川清泉"
        ],
        "weather": "☀️ 快晴 ｜ 2.2°C ~ 13.9°C ｜ 0.0mm ｜ 8.3h",
        "foliage": "田子之浦富士海景 ｜ 千本松原蒼翠黑松"
    },
    {
        "day": 8,
        "date": "11/20（五）",
        "title": "名湯篇：三島 ➔ 狩野川自行車道 ➔ 修善寺溫泉水口 (提早避開三連休)",
        "wps": [mishima_center, [138.9350, 35.0300], shuzenji_mizuguchi],
        "hotel": "Onsen Yado Mizuguchi (温泉宿 水口)",
        "hotel_addr": "靜岡縣伊豆市修善寺3463-17",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E4%BC%8A%E8%B1%86%E5%B8%82%E4%BF%AE%E5%96%84%E5%AF%BA3463-17+%E6%B8%A9%E6%B3%89%E5%AE%BF%E6%B0%B4%E5%8F%A3",
        "booked": True,
        "cues": [
            "由三島沿清澈平緩的狩野川自行車道逆流漫騎",
            "下午早早抵達修善寺，入住「温泉宿 水口」換浴衣",
            "漫步竹林小徑、獨鈷之湯、桂橋紅葉",
            "傍晚探訪虹之鄉賞夜楓點燈，徹底回血"
        ],
        "weather": "☀️ 快晴 ｜ 6.9°C ~ 18.6°C ｜ 0.0mm ｜ 9.6h",
        "foliage": "🔥 修善寺・虹之鄉見頃 ｜ 古湯楓紅"
    },
    {
        "day": 9,
        "date": "11/21（六）",
        "title": "海景篇：修善寺 ➔ 避開天城峠 (走冷川峠) ➔ 一碧湖 ➔ 城崎海岸 ➔ 伊東川奈",
        "wps": [shuzenji_mizuguchi, hiekawa_pass, ippeki_lake, jogasaki_coast, kawana_seaview],
        "hotel": "kawana seaview standard (KAWANA)",
        "hotel_addr": "靜岡縣伊東市新井484-30 KAWANA",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E4%BC%8A%E6%9D%B1%E5%B8%82%E6%96%B0%E4%BA%95484-30+KAWANA",
        "booked": True,
        "cues": [
            "果斷放棄三連休塞車的天城峠，走縣道 12 號冷川峠幽靜翻越",
            "探訪「伊豆之瞳」一碧湖倒映滿山楓紅",
            "城崎海岸門脇吊橋俯瞰 4000 年火山熔岩海蝕崖白浪",
            "入住相模灣海景第一排「kawana seaview standard」"
        ],
        "weather": "☀️ 快晴 ｜ 5.9°C ~ 19.3°C ｜ 0.0mm ｜ 9.3h",
        "foliage": "🔥 一碧湖伊豆之瞳見頃 ｜ 熔岩海岸海藍"
    },
    {
        "day": 10,
        "date": "11/22（日）",
        "title": "海灣篇：伊東川奈 ➔ 宇佐美 ➔ 避開危險長隧道 (走網代舊街) ➔ Apt南熱海",
        "wps": [kawana_seaview, usami_beach, ajiro_old_street, apt_minami_atami],
        "hotel": "Apt南熱海-網代",
        "hotel_addr": "靜岡縣熱海市下多賀440",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E4%B8%8B%E5%A4%9A%E8%B2%BA440+Apt%E5%8D%97%E7%86%B1%E6%B5%B7",
        "booked": True,
        "cues": [
            "避開國道 135 號危險長隧道，切入宇佐美與網代漁港舊街",
            "17.4km 輕鬆短程，避開三連休熱海市中心恐怖塞車潮",
            "入住長浜海水浴場第一排「Apt南熱海-網代」，陽台賞海景日落"
        ],
        "weather": "☀️ 快晴 ｜ 7.6°C ~ 19.2°C ｜ 0.0mm ｜ 9.3h",
        "foliage": "網代灣蔚藍海水 ｜ 沿岸柑橘金黃"
    },
    {
        "day": 11,
        "date": "11/23（一）",
        "title": "花火篇：南熱海換宿 ➔ 熱海梅園最晚紅葉 ➔ 晚上 20:20 熱海海上花火大會",
        "wps": [apt_minami_atami, izu_kansya, atami_baien, atami_sun_beach, izu_kansya],
        "hotel": "Izu Kansya (伊豆観舎)",
        "hotel_addr": "靜岡縣熱海市下多賀1473-11",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E4%B8%8B%E5%A4%9A%E8%B2%BA1473-11+Izu+Kansya",
        "booked": True,
        "cues": [
            "上午由下多賀 440 移步至 Izu Kansya 卸下行李",
            "日間輕裝前往「熱海梅園」欣賞日本最晚紅葉祭與來宮神社大楠",
            "晚上 20:20～20:40 直擊震撼海灣回音的「熱海海上花火大會」",
            "煙火散場搭 5 分鐘電車或騎車 15 分鐘回南熱海，完全免塞車！"
        ],
        "weather": "☀️ 快晴 ｜ 10.4°C ~ 19.7°C ｜ 0.0mm ｜ 9.7h",
        "foliage": "🎆 熱海海上花火大會 ｜ 熱海梅園遲楓"
    },
    {
        "day": 12,
        "date": "11/24（二）",
        "title": "湘南篇：南熱海 ➔ 縣道740號柑橘道 ➔ 小田原城 ➔ 湘南海岸防風林 ➔ 江之島",
        "wps": [izu_kansya, atami_sun_beach, pref740_mikan, odawara_castle, shonan_cr, enoshima_island],
        "hotel": "江之島 / 藤澤市區飯店",
        "hotel_addr": "神奈川縣藤澤市江之島周邊",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%B1%9F%E4%B9%8B%E5%B3%B6",
        "booked": False,
        "cues": [
            "切入縣道 740 號柑橘景觀道，徹底避開江之浦暗黑長隧道",
            "小田原城參觀天守閣與護城河楓紅，品嚐酥脆炸竹筴魚",
            "小田原過後一馬平川相模灣平路，沿湘南防風林專用道直奔江之島"
        ],
        "weather": "☀️ 快晴 ｜ 8.9°C ~ 18.0°C ｜ 0.0mm ｜ 9.4h",
        "foliage": "小田原城護城河楓紅 ｜ 灌籃高手湘南海岸"
    },
    {
        "day": 13,
        "date": "11/25（三）",
        "title": "古寺篇：江之島 ➔ 鎌倉高校前平交道 ➔ 長谷寺 ➔ 柏尾川水岸 ➔ 橫濱港未來",
        "wps": [enoshima_island, kamakura_hase, kashio_river_cr, yokohama_minatomirai],
        "hotel": "橫濱港未來飯店",
        "hotel_addr": "神奈川縣橫濱市中區/西區",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%A9%AB%E6%BF%B1%E6%B8%AF%E6%9C%AA%E4%BE%86",
        "booked": False,
        "cues": [
            "清晨朝聖《灌籃高手》鎌倉高校前平交道",
            "參拜長谷寺觀音與古寺庭園深秋紅葉",
            "沿平整的柏尾川水岸自行車道直達橫濱港未來摩天輪"
        ],
        "weather": "⛅ 陰/晴 ｜ 9.3°C ~ 12.4°C ｜ 0.0mm ｜ 0.0h",
        "foliage": "🔥 鎌倉長谷寺古寺紅葉 ｜ 橫濱港灣夜景"
    },
    {
        "day": 14,
        "date": "11/26（四）",
        "title": "灣岸篇：橫濱 ➔ 第一京濱/羽田 ➔ 豐洲大橋 ➔ 台場海濱公園",
        "wps": [yokohama_minatomirai, [139.7350, 35.5450], toyosu_bridge, odaiba_marine_park],
        "hotel": "台場 / 有明飯店",
        "hotel_addr": "東京都港區台場 / 江東區有明",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E5%8F%B0%E5%A0%B4%E6%B5%B7%E6%BF%B1%E5%85%AC%E5%9C%92",
        "booked": False,
        "cues": [
            "橫濱山下公園漫步黃金銀杏大道",
            "經羽田水岸切入豐洲大橋專用自行車道眺望東京灣天際線",
            "傍晚抵達台場海濱公園與獨角獸鋼彈立像合影"
        ],
        "weather": "☀️ 快晴 ｜ 6.2°C ~ 18.6°C ｜ 0.0mm ｜ 9.0h",
        "foliage": "橫濱山下公園黃金銀杏 ｜ 東京灣彩虹大橋"
    },
    {
        "day": 15,
        "date": "11/27（五）",
        "title": "下町篇：台場 ➔ 葛西臨海公園 ➔ 中川水岸綠道 ➔ 柴又 ➔ 葛飾金町花庵",
        "wps": [odaiba_marine_park, kasai_rinkai_park, shibamata_taishakuten, hostel_hana_an],
        "hotel": "花庵旅舍 (Hostel Hana An)",
        "hotel_addr": "東京都葛飾區金町4-23-11",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E8%91%9B%E9%A3%BE%E5%8D%80%E9%87%91%E7%94%BA4-23-11+%E8%8A%B1%E5%BA%B5%E6%97%85%E8%88%8D",
        "booked": True,
        "cues": [
            "沿東京灣專用道穿越葛西臨海公園與巨型摩天輪",
            "切入中川與江戶川水岸自行車道，避開市區繁雜車潮",
            "入住水元公園旁清幽的「花庵旅舍（金町4-23-11）」",
            "漫步柴又老街品嚐草糰子與鰻魚飯"
        ],
        "weather": "☀️ 晴/多雲 ｜ 7.3°C ~ 16.2°C ｜ 0.0mm ｜ 3.7h",
        "foliage": "葛西海濱秋芒 ｜ 葛飾純樸下町風情"
    },
    {
        "day": 16,
        "date": "11/28（六）",
        "title": "漫遊篇：金町出發 ➔【輕裝免行李】江戶川CR / 荒川 ➔ 葛飾老街 ➔ 金町",
        "wps": [hostel_hana_an, [139.8800, 35.8400], kawagoe_kitain, [139.8000, 35.8000], hostel_hana_an],
        "hotel": "花庵旅舍 (Hostel Hana An)",
        "hotel_addr": "東京都葛飾區金町4-23-11",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E8%91%9B%E9%A3%BE%E5%8D%80%E9%87%91%E7%94%BA4-23-11+%E8%8A%B1%E5%BA%B5%E6%97%85%E8%88%8D",
        "booked": True,
        "cues": [
            "週末免收行李，以最輕快的狀態暢騎江戶川專用道",
            "探訪流山白壁古街道或小江戶老街",
            "傍晚返回金町花庵旅舍連住休整"
        ],
        "weather": "☀️ 快晴 ｜ 8.4°C ~ 19.8°C ｜ 0.0mm ｜ 9.1h",
        "foliage": "🔥 江戶老街與水岸金秋 ｜ 週末輕裝巡航"
    },
    {
        "day": 17,
        "date": "11/29（日）",
        "title": "水杉篇：金町退房 ➔ 水元公園（萬棵水杉黃金森林見頃）➔ 柴又 ➔ 淺草",
        "wps": [hostel_hana_an, mizumoto_park, shibamata_taishakuten, asakusa_kaminarimon],
        "hotel": "淺草 / 上野 / 東京市區飯店",
        "hotel_addr": "東京都台東區淺草/上野",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%B7%BA%E8%8D%89%E9%9B%B7%E9%96%80",
        "booked": False,
        "cues": [
            "清晨 06:30 騎車 5 分鐘直達水元公園，獨享晨霧中的萬棵水杉黃金森林！",
            "沿中川與隅田川水岸順暢騎進淺草雷門",
            "下午入住淺草/上野飯店休整"
        ],
        "weather": "☀️ 晴/多雲 ｜ 9.0°C ~ 15.3°C ｜ 0.0mm ｜ 5.2h",
        "foliage": "🔥 水元公園水杉見頃最高峰 ｜ 歐美童話巨木林"
    },
    {
        "day": 18,
        "date": "11/30（一）",
        "title": "金秋篇：淺草 ➔ 東大本鄉銀杏 ➔ 皇居 ➔ 明治神宮外苑銀杏大道 ➔ 秋葉原",
        "wps": [asakusa_kaminarimon, todai_hongo, imperial_palace, jingu_gaien, cycletrip_base],
        "hotel": "秋葉原 / 上野飯店",
        "hotel_addr": "東京都千代田區秋葉原/神田",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E7%A7%8B%E8%91%89%E5%8E%9F",
        "booked": False,
        "cues": [
            "東京大學本鄉校區漫步赤門與百年大銀杏黃金地毯",
            "皇居二重橋環騎，直奔明治神宮外苑銀杏林蔭道",
            "欣賞東京金秋最經典的黃金雨與莉香名場面巡禮"
        ],
        "weather": "☀️ 快晴 ｜ 7.1°C ~ 16.3°C ｜ 0.0mm ｜ 8.9h",
        "foliage": "🔥 神宮外苑與東大銀杏見頃最高峰 ｜ 黃金大道"
    },
    {
        "day": 19,
        "date": "12/01（二）",
        "title": "圓滿篇：秋葉原市區 ➔ 神田明神 ➔ CycleTrip Base 還車 ➔ 日暮里 ➔ 機場",
        "wps": [cycletrip_base, kanda_myojin, cycletrip_base, [139.7710, 35.7280]],
        "hotel": "返台溫暖的家",
        "hotel_addr": "成田國際機場",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%88%90%E7%94%B0%E5%9C%8B%E9%9A%9B%E6%A9%9F%E5%A0%B4",
        "booked": False,
        "cues": [
            "神田明神平安祈福，感恩 776km 順利完騎",
            "CycleTrip Base 秋葉原順利還車",
            "日暮里站搭乘京成 Skyliner 36 分鐘直達機場，圓滿收官！"
        ],
        "weather": "☀️ 快晴 ｜ 6.4°C ~ 20.0°C ｜ 0.0mm ｜ 7.1h",
        "foliage": "神田明神古松 ｜ 776km 世界線圓滿閉環"
    }
]

# Fetch full route GeoJSON & GSI Elevation for every day
all_days_data = []

print("=== 開始為 19 天生成完整的單車路網座標、GSI標高曲線與 GPX 軌跡 ===")
for item in days_meta:
    d_num = item["day"]
    wps = item["wps"]
    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in wps])
    url = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    r_data = fetch_osrm_with_retry(url)
    if not r_data:
        continue
    dist_km = round(r_data['distance'] / 1000.0, 1)
    coords = r_data['geometry']['coordinates']
        dist_km = round(r_data['distance'] / 1000.0, 1)
        coords = r_data['geometry']['coordinates']

    # Sample for chart
    sample_rate = max(1, len(coords) // 50)
    chart_coords = coords[::sample_rate]
    if coords[-1] not in chart_coords:
        chart_coords.append(coords[-1])

    elev_pts = []
    accum_dist = 0
    prev_pt = chart_coords[0]
    
    # Calculate distance steps
    for i, pt in enumerate(chart_coords):
        if i > 0:
            # Approximate dist in km
            dx = (pt[0] - prev_pt[0]) * 91.0 # lon diff to km approx at 35N
            dy = (pt[1] - prev_pt[1]) * 111.0 # lat diff to km approx
            accum_dist += (dx**2 + dy**2)**0.5
            prev_pt = pt
        
        # Get GSI elevation
        gsi_url = f"https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={pt[0]}&lat={pt[1]}&outtype=JSON"
        try:
            req_gsi = urllib.request.Request(gsi_url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req_gsi, timeout=4) as g_resp:
                e_val = float(json.loads(g_resp.read().decode('utf-8')).get('elevation', 0))
        except:
            e_val = 0.0
        
        elev_pts.append({
            "km": round(min(dist_km, accum_dist), 1),
            "ele": round(e_val, 1),
            "lon": pt[0],
            "lat": pt[1]
        })
        time.sleep(0.01)

    gain = sum([max(0, elev_pts[i]["ele"]-elev_pts[i-1]["ele"]) for i in range(1, len(elev_pts)) if abs(elev_pts[i]["ele"]-elev_pts[i-1]["ele"])>=3.5])
    loss = sum([max(0, elev_pts[i-1]["ele"]-elev_pts[i]["ele"]) for i in range(1, len(elev_pts)) if abs(elev_pts[i-1]["ele"]-elev_pts[i]["ele"])>=3.5])

    # Generate GPX file
    gpx_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<gpx version="1.1" creator="TokyoCycling2026" xmlns="http://www.topografix.com/GPX/1/1">
  <metadata>
    <name>Day {d_num}: {item["title"]}</name>
    <desc>{dist_km} km | +{round(gain)}m / -{round(loss)}m</desc>
  </metadata>
  <trk>
    <name>Day {d_num}: {item["title"]}</name>
    <trkseg>
'''
    for pt in coords:
        gpx_content += f'      <trkpt lat="{pt[1]}" lon="{pt[0]}"></trkpt>\n'
    gpx_content += '''    </trkseg>
  </trk>
</gpx>'''
    
    # Save GPX
    with open(f"d:/2026東京單車騎旅/day{d_num}_track.gpx", "w", encoding="utf-8") as gf:
        gf.write(gpx_content)
    with open(f"C:/Users/ymero/Downloads/day{d_num}_track.gpx", "w", encoding="utf-8") as gf:
        gf.write(gpx_content)

    day_record = {
        "day": d_num,
        "date": item["date"],
        "title": item["title"],
        "dist_km": dist_km,
        "gain": round(gain),
        "loss": round(loss),
        "start_e": round(elev_pts[0]["ele"]),
        "peak_e": round(max([p["ele"] for p in elev_pts])),
        "end_e": round(elev_pts[-1]["ele"]),
        "hotel": item["hotel"],
        "hotel_addr": item["hotel_addr"],
        "hotel_url": item["hotel_url"],
        "booked": item["booked"],
        "weather": item["weather"],
        "foliage": item["foliage"],
        "cues": item["cues"],
        "coords": coords, # Full polyline
        "elev_profile": elev_pts # Chart data
    }
    all_days_data.append(day_record)
    print(f"✅ Day {d_num:02d} 資料與 GPX 生成完成：{dist_km} km, +{round(gain)}m")

# Write all days data JSON for web app
with open("d:/2026東京單車騎旅/all_19days_route_data.json", "w", encoding="utf-8") as jf:
    json.dump(all_days_data, jf, ensure_ascii=False)
print("all_19days_route_data.json saved successfully!")
