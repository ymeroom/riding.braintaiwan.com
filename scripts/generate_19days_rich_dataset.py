import urllib.request, json, sys, time, os
sys.stdout.reconfigure(encoding='utf-8')

# Key Waypoints for all 19 days
cycletrip_base = [139.7785, 35.6985] # Akihabara (5m)
ginza = [139.7680, 35.6700] # Ginza
shinagawa = [139.7400, 35.6300] # Shinagawa
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
yamanakako_nagaike = [138.8650, 35.4300] # Yamanakako Nagaike
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
atami_sun_beach = [139.0750, 35.0970]
maruya_atami = [139.07248, 35.09436] # guest house MARUYA (銀座町7-8, 10m)
 # Atami Sun Beach (3m)

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

# 19-Day Deep In-Depth Metadata with Detailed Timelines & Expert Callouts
days_meta = [
    {
        "day": 1,
        "date": "11/13（五）",
        "title": "出城篇：秋葉原 ➔ 銀座/品川 ➔ 國道15號(第一京濱) ➔ 六鄉橋 ➔ 多摩川自行車道 ➔ 府中 (50.4km) ➔ 高尾山口 (Mt. Takao Base Camp 190m)",
        "wps": [cycletrip_base, ginza, shinagawa, rokugo_bridge, tamagawa_fuchu, asakawa_junction, takao_basecamp],
        "hotel": "Mt. Takao Base Camp",
        "hotel_addr": "東京都八王子市高尾町1799-3",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%9D%B1%E4%BA%AC%E9%83%BD%E5%85%AB%E7%8E%8B%E5%AD%90%E5%B8%82%E9%AB%98%E5%B0%BE%E7%94%BA1799-3+Mt.Takao+Base+Camp",
        "booked": True,
        "bike_status": "🚲 戶外活動大本營，門口與室內設專用單車架",
        "weather": "☀️ 晴 ｜ 11.8°C ~ 19.6°C ｜ 0.0mm ｜ 9.4h",
        "foliage": "多摩川水岸秋芒 ｜ 淺川水岸林木初染紅",
        "timeline": [
            {"name": "起點：秋葉原 CycleTrip Base", "km": 0.0, "type": "start", "coord": cycletrip_base, "desc": "09:30 取車、胎壓檢查、配件測試、加購免責補償保險 (CDW)。"},
            {"name": "市區順暢出城：銀座・品川", "km": 4.5, "type": "waypoint", "coord": ginza, "desc": "走國道 15 號（第一京濱），路肩寬闊平坦，避開繁雜巷弄。"},
            {"name": "關鍵轉折點：六鄉橋", "km": 16.2, "type": "pivot", "coord": rokugo_bridge, "desc": "🚨 離開幹道，無縫切入「多摩川自行車道（左岸專用道）」。"},
            {"name": "水岸補給：二子玉川・多摩川綠地", "km": 28.5, "type": "rest", "coord": [139.627, 35.611], "desc": "眺望多摩川秋芒金黃搖曳，享受全封閉無紅綠燈巡航。"},
            {"name": "專用道切換：府中四谷橋", "km": 50.4, "type": "pivot", "coord": tamagawa_fuchu, "desc": "🚨 橫跨多摩川，無縫銜接「淺川自行車道」，繼續逆流緩上。"},
            {"name": "八王子水岸漫騎", "km": 68.0, "type": "scenic", "coord": asakawa_junction, "desc": "淺川兩側林木微紅，坡度僅 0.3% 極度舒適。"},
            {"name": "終點：Mt. Takao Base Camp", "km": 89.7, "type": "end", "coord": takao_basecamp, "desc": "抵達高尾山腳（海拔 190m），入住專業單車基地，步行 3 分鐘泡極樂湯露天溫泉。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 徹底避開世田谷區暗渠綠道（密集路擋與牽車限制），走第一京濱＋多摩川/淺川雙水岸專用道，享受整整 65 公里完全封閉、零紅綠燈直達高尾山腳！"
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
        "bike_status": "🚲 官方確認：可安全停放單車",
        "weather": "☀️ 快晴 ｜ 7.8°C ~ 17.2°C ｜ 0.0mm ｜ 8.9h",
        "foliage": "🍁 秋山溪谷見頃 ｜ 兩側山壁層林盡染",
        "timeline": [
            {"name": "起點：Mt. Takao Base Camp", "km": 0.0, "type": "start", "coord": takao_basecamp, "desc": "清晨 08:00 出發，趁週六觀光大車尚未湧現前攻頂。"},
            {"name": "甲州街道直攻：大垂水峠", "km": 3.8, "type": "pivot", "coord": otarumi_pass, "desc": "標高 392m（爬升 +202m，平均坡度 5.3%），清晨路況極佳無車。"},
            {"name": "相模湖畔滑降", "km": 9.5, "type": "scenic", "coord": sagamiko, "desc": "順坡滑降至相模湖（海拔 205m），欣賞晨霧湖景。"},
            {"name": "關鍵轉折點：相模湖左轉縣道35號", "km": 12.0, "type": "pivot", "coord": [139.185, 35.608], "desc": "🚨 果斷切入「秋山街道」，避開國道 20 號大貨車地獄！"},
            {"name": "秋山川幽靜溪谷緩升", "km": 28.0, "type": "scenic", "coord": akiyama_highway, "desc": "整整 35km 禁止大型貨車通行，秋楓層林盡染，緩坡 2-3% 極致舒服。"},
            {"name": "最高點：秋山隧道", "km": 48.5, "type": "warning", "coord": [138.980, 35.565], "desc": "標高 674m，穿過隧道後開始享受 7km 爽快大下坡！"},
            {"name": "終點：都留 由加利旅館", "km": 61.0, "type": "end", "coord": tsuru_yukari, "desc": "抵達都留市（海拔 484m），入住溫馨日式旅館，品嚐家常晚餐。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 國道 20 號過相模湖後路幅驟縮且大砂石車多，縣道 35 號秋山街道是關東單車界公認的「避大車隱世聖地」，坡度溫和、景觀絕美！"
    },
    {
        "day": 3,
        "date": "11/15（日）",
        "title": "湖泊篇：由加利旅館 ➔【晴天版】山中湖完整環湖一圈+忍野八海 / 【陰雨天版】新倉山五重塔 ➔ 河口湖 (宿 Orange Cabin Inn)",
        "wps": [tsuru_yukari, [138.8600, 35.5200], oshino_hakkai, yamanakako_nagaike, yamanakako, [138.8400, 35.4200], arakurayama, orange_cabin],
        "hotel": "Orange Cabin Inn far from station",
        "hotel_addr": "山梨縣南都留郡富士河口湖町河口1916-3",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E5%B1%B1%E6%A2%A8%E7%9C%8C%E5%8D%97%E9%83%BD%E7%95%99%E9%83%A1%E5%84%82%E5%A3%AB%E6%B2%B3%E5%8F%A3%E6%B9%96%E7%94%BA%E6%B2%B3%E5%8F%A31916-3+Orange+Cabin+Inn",
        "booked": True,
        "bike_status": "🚲 獨棟鄉村木屋，前廊與玄關空間充裕好停車",
        "weather": "☀️ 快晴 ｜ 4.5°C ~ 15.1°C ｜ 0.0mm ｜ 9.6h",
        "foliage": "🔥 雙湖見頃最盛期 ｜ 晴天環山中湖、陰天直取五重塔",
        "timeline": [
            {"name": "起點：由加利旅館", "km": 0.0, "type": "start", "coord": tsuru_yukari, "desc": "清晨觀察富士山頭雲層，依天候啟動雙軌決策。"},
            {"name": "富士急行線農路：縣道713號", "km": 6.5, "type": "waypoint", "coord": [138.8600, 35.5200], "desc": "走大野夏狩線生活農路緩上，避開國道 139 號車流。"},
            {"name": "神之湧泉：忍野八海", "km": 18.2, "type": "scenic", "coord": oshino_hakkai, "desc": "欣賞清澈透底的富士雪水湧泉，品嚐現烤熱草餅。"},
            {"name": "☀️【晴天版】山中湖長池親水公園", "km": 24.5, "type": "scenic", "coord": yamanakako_nagaike, "desc": "海拔 1,000m，眺望雄偉富士山倒映湖面（逆富士名所）。"},
            {"name": "☀️【晴天版】旭日丘湖畔紅葉祭", "km": 30.0, "type": "scenic", "coord": yamanakako, "desc": "漫步 600 棵巨木紅葉林蔭道，感受五湖最高湖泊秋色。"},
            {"name": "☁️【陰雨版】新倉山淺間五重塔", "km": 42.0, "type": "pivot", "coord": arakurayama, "desc": "若遇陰雨避開千米高原，直接前往五重塔拍明信片富士景觀。"},
            {"name": "終點：河口湖 Orange Cabin Inn", "km": 53.2, "type": "end", "coord": orange_cabin, "desc": "入住紅葉迴廊旁獨棟木屋（海拔 857m），晚上漫步夜楓點燈。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 11月中旬山中湖若遇陰雨天，氣溫會暴跌至 2-3°C 且無景觀；若遇晴天則是 100 分絕景！因此晴天環山中湖、陰雨天直取五重塔是最高明策略。"
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
        "bike_status": "🚲 湖畔民宿/青旅，提供單車友善停放",
        "weather": "☀️ 快晴 ｜ 3.2°C ~ 14.6°C ｜ 0.0mm ｜ 9.1h",
        "foliage": "🔥 紅葉迴廊最高峰 ｜ 依前日天候靈活啟動分支",
        "timeline": [
            {"name": "晨間必做：河口湖紅葉迴廊", "km": 0.0, "type": "start", "coord": orange_cabin, "desc": "06:30 步行 3 分鐘獨享無人「紅葉迴廊」晨光深紅隧道。"},
            {"name": "🌲【分支A】新倉山淺間五重塔", "km": 6.5, "type": "scenic", "coord": arakurayama, "desc": "晨光順光拍攝五重塔與白雪冠頂富士山。"},
            {"name": "湖北 View Line & 大石公園", "km": 14.0, "type": "scenic", "coord": oishi_park, "desc": "北岸全景眺望河口湖與富士山倒影。"},
            {"name": "西湖療癒之里根場", "km": 22.5, "type": "scenic", "coord": saiko_iyashi, "desc": "傳統茅草屋聚落與深秋古樸紅葉。"},
            {"name": "精進湖「子抱富士」", "km": 32.0, "type": "scenic", "coord": shojiko, "desc": "他見富士經典視角，湖面寧靜無波。"},
            {"name": "終點：本棲湖北岸浩庵", "km": 41.9, "type": "end", "coord": motosuko_kouan, "desc": "《搖曳露營》聖地，房間窗前直擊日幣千圓紙幣逆富士。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 住在 Orange Cabin 的最大紅利就是「06:30 晨光空景」！在 08:30 觀光大巴湧入前拍完，隨後一路向西探索靜謐三湖。"
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
        "bike_status": "🚲 高原住宿基地，彈性停放",
        "weather": "☀️ 晴朗 ｜ 5.8°C ~ 16.4°C ｜ 0.0mm ｜ 8.8h",
        "foliage": "🔥 西湖/本棲湖深秋紅葉 ｜ 熔岩樹海蒼茫",
        "timeline": [
            {"name": "起點：本棲湖浩庵 / 河口湖", "km": 0.0, "type": "start", "coord": motosuko_kouan, "desc": "全行程核心天候緩衝日，保有 100% 彈性。"},
            {"name": "青木原樹海林蔭道", "km": 8.0, "type": "scenic", "coord": shojiko, "desc": "熔岩原始森林，負離子森呼吸漫遊。"},
            {"name": "富岳風穴與鳴澤冰穴", "km": 16.5, "type": "scenic", "coord": [138.6900, 35.4800], "desc": "天然地質奇景與地心寒冰探秘。"},
            {"name": "富士展望之湯 Yurari 溫泉", "km": 24.0, "type": "rest", "coord": [138.7100, 35.4850], "desc": "露天溫泉眺望富士山，品嚐熱騰騰南瓜餺飥麵。"},
            {"name": "終點：五湖基地休整", "km": 38.1, "type": "end", "coord": motosuko_kouan, "desc": "為明日千米大長下坡做好防寒裝備與體力準備。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 高原天候變幻莫測，Day 5 緩衝讓您在遇到低溫或陣雨時有完整空間補完景點，立於不敗之地！"
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
        "bike_status": "🚲 市區商旅，可向櫃檯確認停放或攜入房",
        "weather": "☀️ 萬里晴空 ｜ 4.2°C ~ 15.8°C ｜ 0.0mm ｜ 9.0h",
        "foliage": "朝霧高原金黃芒草 ｜ 白糸之瀑水氣楓紅",
        "timeline": [
            {"name": "起點：本棲湖浩庵", "km": 0.0, "type": "start", "coord": motosuko_kouan, "desc": "清晨水鏡千圓逆富士晨光攝影（標高 905m）。"},
            {"name": "朝霧高原牧場", "km": 12.0, "type": "scenic", "coord": asagiri_plateau, "desc": "金黃秋芒搖曳，右牛群左富士雄偉西壁。"},
            {"name": "朝霧 Food Park 暖身補給", "km": 18.5, "type": "rest", "coord": [138.580, 35.370], "desc": "喝現煮熱牛奶暖手，穿戴防風裝備。"},
            {"name": "天下名瀑：白糸之瀑", "km": 27.0, "type": "scenic", "coord": shiraito_falls, "desc": "水氣如絲絹垂掛（海拔 450m），周邊楓紅環繞。"},
            {"name": "潤井川長下坡滑降", "km": 34.0, "type": "warning", "coord": [138.600, 35.260], "desc": "一路平穩滑降，海拔直落 800 公尺！"},
            {"name": "終點：富士宮市區飯店", "km": 39.6, "type": "end", "coord": fujinomiya_center, "desc": "參拜富士山本宮淺間大社總本社，大啖富士宮炒麵。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 自 905m 滑降至 115m，時速 40km/h 體感逼近 0°C！務必佩戴防風長指手套與風衣，煞車平穩點放防熱衰竭。"
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
        "bike_status": "🚲 市區商旅，可向櫃檯確認停放",
        "weather": "☀️ 快晴 ｜ 2.2°C ~ 13.9°C ｜ 0.0mm ｜ 8.3h",
        "foliage": "田子之浦富士海景 ｜ 千本松原蒼翠黑松",
        "timeline": [
            {"name": "起點：富士宮市區", "km": 0.0, "type": "start", "coord": fujinomiya_center, "desc": "沿潤井川自行車道緩降出城。"},
            {"name": "田子の浦港・港公園", "km": 13.5, "type": "scenic", "coord": tagonoura_port, "desc": "抵達駿河灣海岸，回望巨大雪冠富士山。"},
            {"name": "千本松原海岸防潮堤專用道", "km": 18.0, "type": "pivot", "coord": senbonmatsubara, "desc": "🚨 切入 15km 全封閉海堤專用道，零紅綠燈狂飆！"},
            {"name": "沼津港海鮮市場", "km": 33.0, "type": "rest", "coord": numazu_port, "desc": "大口享用新鮮深海魚海鮮丼、現烤帆立貝。"},
            {"name": "終點：三島市區飯店", "km": 41.3, "type": "end", "coord": mishima_center, "desc": "漫步三嶋大社與源兵衛川清泉，享用百年炭烤鰻魚飯。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 千本松原海堤專用道左側黑松林、右側駿河灣，回頭是富士山，全平路零紅綠燈，是全日本頂級海景路段！"
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
        "bike_status": "🚲 傳統溫泉名宿，設有玄關室內/遮雨停放處",
        "weather": "☀️ 快晴 ｜ 6.9°C ~ 18.6°C ｜ 0.0mm ｜ 9.6h",
        "foliage": "🔥 修善寺・虹之鄉見頃 ｜ 古湯楓紅",
        "timeline": [
            {"name": "起點：三島市區", "km": 0.0, "type": "start", "coord": mishima_center, "desc": "避開明日三連休車潮，提早進駐修善寺。"},
            {"name": "狩野川自行車專用道", "km": 8.5, "type": "scenic", "coord": [138.9350, 35.0300], "desc": "沿清澈狩野川逆流平緩漫騎，專用道安全舒適。"},
            {"name": "修善寺溫泉街入口", "km": 19.0, "type": "scenic", "coord": [138.930, 34.972], "desc": "抵達伊豆最古老溫泉名湯（海拔 103m）。"},
            {"name": "終點：温泉宿 水口", "km": 20.9, "type": "end", "coord": shuzenji_mizuguchi, "desc": "換浴衣漫步竹林小徑與獨鈷之湯，傍晚賞虹之鄉夜楓。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 11/20（五）提早進駐修善寺是老手神操作，完全避開 11/21 三連休湧入的恐怖觀光車潮！"
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
        "bike_status": "🚲 官方確認：海景民宿可安全停放單車",
        "weather": "☀️ 快晴 ｜ 5.9°C ~ 19.3°C ｜ 0.0mm ｜ 9.3h",
        "foliage": "🔥 一碧湖伊豆之瞳見頃 ｜ 熔岩海岸海藍",
        "timeline": [
            {"name": "起點：修善寺 温泉宿 水口", "km": 0.0, "type": "start", "coord": shuzenji_mizuguchi, "desc": "啟動三連休避坑密道。"},
            {"name": "避坑密道：縣道12號冷川峠", "km": 11.5, "type": "pivot", "coord": hiekawa_pass, "desc": "🚨 果斷放棄塞車的國道414天城峠，走幽靜林蔭峠道翻山（371m）。"},
            {"name": "伊豆之瞳：一碧湖", "km": 26.0, "type": "scenic", "coord": ippeki_lake, "desc": "探訪火山湖倒映滿山紅葉秘境（海拔 170m）。"},
            {"name": "城崎海岸・門脇吊橋", "km": 36.5, "type": "scenic", "coord": jogasaki_coast, "desc": "俯瞰 4000 年火山熔岩海蝕懸崖與白浪。"},
            {"name": "終點：kawana seaview standard", "km": 47.9, "type": "end", "coord": kawana_seaview, "desc": "入住相模灣海景第一排民宿，在海潮聲中入眠。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 三連休首日天城峠塞滿大巴廢氣漫天，冷川峠車流少、林道幽美，安全直達相模灣海岸！"
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
        "bike_status": "🚲 官方確認：海景公寓可安全停放單車",
        "weather": "☀️ 快晴 ｜ 7.6°C ~ 19.2°C ｜ 0.0mm ｜ 9.3h",
        "foliage": "網代灣蔚藍海水 ｜ 沿岸柑橘金黃",
        "timeline": [
            {"name": "起點：kawana seaview standard", "km": 0.0, "type": "start", "coord": kawana_seaview, "desc": "沿相模灣海岸北上。"},
            {"name": "宇佐美海岸", "km": 8.5, "type": "scenic", "coord": usami_beach, "desc": "蔚藍海浪與金色沙灘晨景。"},
            {"name": "避坑密道：網代漁港舊街", "km": 14.0, "type": "pivot", "coord": ajiro_old_street, "desc": "🚨 避開國道 135 號危險長隧道，切入漁港舊街沿海繞行。"},
            {"name": "終點：Apt南熱海-網代", "km": 17.4, "type": "end", "coord": apt_minami_atami, "desc": "入住長浜海灘海景第一排公寓（下多賀440），陽台看網代灣日落。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 17.4km 輕鬆短程，避開三連休中日熱海市區大塞車，早早進房享受私人海景陽台。"
    },
    {
        "day": 11,
        "date": "11/23（一）",
        "title": "花火篇：Apt南熱海 ➔ 熱海梅園最晚紅葉 ➔ 熱海銀座商店街 ➔ 晚上 20:20 熱海海上花火大會 (宿 guest house MARUYA)",
        "wps": [apt_minami_atami, atami_baien, [139.068, 35.100], maruya_atami],
        "hotel": "guest house MARUYA",
        "hotel_addr": "靜岡縣熱海市銀座町7-8",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E9%8A%80%E5%BA%A7%E7%94%BA7-8+guest+house+MARUYA",
        "booked": True,
        "bike_status": "🚲 位於熱海銀座商店街，文青旅舍設有室內/玄關單車停放空間",
        "weather": "☀️ 快晴 ｜ 10.4°C ~ 19.7°C ｜ 0.0mm ｜ 9.7h",
        "foliage": "🎆 熱海海上花火大會 ｜ 熱海梅園日本最晚紅葉祭",
        "timeline": [
            {"name": "起點：Apt南熱海 (下多賀440)", "km": 0.0, "type": "start", "coord": apt_minami_atami, "desc": "退房後沿海岸平緩北上，享受相模灣晨光。"},
            {"name": "熱海梅園紅葉祭", "km": 6.5, "type": "scenic", "coord": atami_baien, "desc": "欣賞日本最晚紅葉名所（見頃期間），深紅楓葉與古橋溪流相映。"},
            {"name": "來宮神社・兩千年大楠神木", "km": 8.0, "type": "scenic", "coord": [139.066, 35.100], "desc": "參拜本州第一大巨樹，繞神木一圈祈求騎旅平安、福壽延年。"},
            {"name": "辦理入住：guest house MARUYA", "km": 10.2, "type": "pivot", "coord": maruya_atami, "desc": "下午 15:00 抵達熱海銀座商店街 7-8 入住 MARUYA，放妥單車與行李。"},
            {"name": "晚上 20:20 熱海海上花火大會", "km": 10.5, "type": "scenic", "coord": atami_sun_beach, "desc": "步行 3 分鐘直達熱海 Sun Beach 海灘！感受天然扇形海灣的高空巨型煙火與山壁回音震撼！"},
            {"name": "終點：guest house MARUYA", "km": 10.8, "type": "end", "coord": maruya_atami, "desc": "散場步行 3 分鐘悠閒返回旅舍，完全不必搭車擠人潮，輕鬆品嚐在地居酒屋。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 住在熱海銀座町 MARUYA 是觀賞熱海花火的「神仙級地理位置」！距離海灘僅 250m，散場步行 3 分鐘直接進房休息，徹底免去所有交通煩惱！"
    },
    {
        "day": 12,
        "date": "11/24（二）",
        "title": "湘南篇：熱海銀座 MARUYA ➔ 縣道740號柑橘道 ➔ 小田原城 ➔ 湘南海岸防風林 ➔ 江之島",
        "wps": [maruya_atami, atami_sun_beach, pref740_mikan, odawara_castle, shonan_cr, enoshima_island],
        "hotel": "江之島 / 藤澤市區飯店",
        "hotel_addr": "神奈川縣藤澤市江之島周邊",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%B1%9F%E4%B9%8B%E5%B3%B6",
        "booked": False,
        "bike_status": "🚲 湘南單車友善飯店，多設停放處",
        "weather": "☀️ 快晴 ｜ 8.9°C ~ 18.0°C ｜ 0.0mm ｜ 9.4h",
        "foliage": "小田原城護城河楓紅 ｜ 灌籃高手湘南海岸",
        "timeline": [
            {"name": "起點：guest house MARUYA (熱海銀座)", "km": 0.0, "type": "start", "coord": maruya_atami, "desc": "08:30 由熱海銀座町出發，沿相模灣公路北上。"},
            {"name": "熱海陽光海灘・伊豆山水岸", "km": 2.5, "type": "scenic", "coord": atami_sun_beach, "desc": "晨光中的相模灣蔚藍海景。"},
            {"name": "避坑密道：縣道740號柑橘景觀道", "km": 11.5, "type": "pivot", "coord": pref740_mikan, "desc": "🚨 避開江之浦暗黑長隧道，半山腰俯瞰相模灣海景（162m）。"},
            {"name": "小田原城天守閣", "km": 22.0, "type": "scenic", "coord": odawara_castle, "desc": "護城河楓紅與歷史古城，品嚐酥脆炸竹筴魚。"},
            {"name": "湘南海岸自行車專用道", "km": 38.0, "type": "scenic", "coord": shonan_cr, "desc": "小田原後一馬平川相模灣平路，沿防風林專用道直奔湘南。"},
            {"name": "終點：江之島 / 藤澤市區飯店", "km": 61.5, "type": "end", "coord": enoshima_island, "desc": "眺望江之島海燈塔與夕陽。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 從熱海市區直接出發省去了南熱海 7km 路程，縣道 740 柑橘景觀道零大車，小田原之後更是全程平坦的湘南海岸巡航！"
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
        "bike_status": "🚲 都會港灣飯店，可向櫃檯確認停放",
        "weather": "⛅ 陰/晴 ｜ 9.3°C ~ 12.4°C ｜ 0.0mm ｜ 0.0h",
        "foliage": "🔥 鎌倉長谷寺古寺紅葉 ｜ 橫濱港灣夜景",
        "timeline": [
            {"name": "起點：江之島", "km": 0.0, "type": "start", "coord": enoshima_island, "desc": "清晨朝聖《灌籃高手》鎌倉高校前平交道。"},
            {"name": "鎌倉長谷寺古寺紅葉", "km": 7.5, "type": "scenic", "coord": kamakura_hase, "desc": "長谷觀音與深秋庭園倒影。"},
            {"name": "專用道入口：柏尾川水岸綠道", "km": 16.0, "type": "pivot", "coord": kashio_river_cr, "desc": "🚨 切入平整水岸專用道，無紅綠燈直達橫濱。"},
            {"name": "終點：橫濱港未來飯店", "km": 32.4, "type": "end", "coord": yokohama_minatomirai, "desc": "傍晚漫步紅磚倉庫與港未來摩天輪夜景。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 告別山道，正式進入「水岸綠道悠閒巡航期」，柏尾川綠道讓進橫濱市區變得輕鬆優雅。"
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
        "bike_status": "🚲 灣區現代飯店，空間寬敞",
        "weather": "☀️ 快晴 ｜ 6.2°C ~ 18.6°C ｜ 0.0mm ｜ 9.0h",
        "foliage": "橫濱山下公園黃金銀杏 ｜ 東京灣彩虹大橋",
        "timeline": [
            {"name": "起點：橫濱港未來", "km": 0.0, "type": "start", "coord": yokohama_minatomirai, "desc": "橫濱山下公園漫步黃金銀杏大道。"},
            {"name": "第一京濱 / 羽田水岸", "km": 18.5, "type": "waypoint", "coord": [139.7350, 35.5450], "desc": "順暢平坦幹道進東京。"},
            {"name": "豐洲大橋專用自行車道", "km": 32.0, "type": "scenic", "coord": toyosu_bridge, "desc": "寬闊專用道眺望東京灣天際線與彩虹大橋。"},
            {"name": "終點：台場海濱公園 / 有明", "km": 38.8, "type": "end", "coord": odaiba_marine_park, "desc": "傍晚與獨角獸鋼彈立像合影，欣賞東京灣夕陽。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 38.8km 全平路，沿著東京灣吹著海風巡航，視覺開闊無比。"
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
        "bike_status": "🚲 官方確認：下町青年旅舍可安全停放單車",
        "weather": "☀️ 晴/多雲 ｜ 7.3°C ~ 16.2°C ｜ 0.0mm ｜ 3.7h",
        "foliage": "葛西海濱秋芒 ｜ 葛飾純樸下町風情",
        "timeline": [
            {"name": "起點：台場海濱公園", "km": 0.0, "type": "start", "coord": odaiba_marine_park, "desc": "出發前往下町。"},
            {"name": "葛西臨海公園", "km": 11.0, "type": "scenic", "coord": kasai_rinkai_park, "desc": "穿越巨型摩天輪與海濱秋芒水岸。"},
            {"name": "中川・江戶川水岸專用道", "km": 19.0, "type": "pivot", "coord": [139.870, 35.700], "desc": "🚨 切入下町水岸綠道，避開市區人車。"},
            {"name": "柴又帝釋天老街", "km": 26.0, "type": "scenic", "coord": shibamata_taishakuten, "desc": "參拜古寺，品嚐現做草糰子與炭烤鰻魚。"},
            {"name": "終點：花庵旅舍 (Hostel Hana An)", "km": 28.5, "type": "end", "coord": hostel_hana_an, "desc": "葛飾金町 4-23-11，官方確認可安全放單車。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 避開市中心吵雜飯店，入住水元公園旁清幽下町旅舍，連住 2 晚徹底放鬆！"
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
        "bike_status": "🚲 官方確認：連住免移車，安全安心",
        "weather": "☀️ 快晴 ｜ 8.4°C ~ 19.8°C ｜ 0.0mm ｜ 9.1h",
        "foliage": "🔥 江戶老街與水岸金秋 ｜ 週末輕裝巡航",
        "timeline": [
            {"name": "起點：花庵旅舍", "km": 0.0, "type": "start", "coord": hostel_hana_an, "desc": "【輕裝免行李】週末輕鬆巡航。"},
            {"name": "江戶川自行車道", "km": 15.0, "type": "scenic", "coord": [139.8800, 35.8400], "desc": "寬闊河堤專用道暢快奔馳。"},
            {"name": "葛飾水岸老街小店", "km": 30.0, "type": "rest", "coord": [139.8000, 35.8000], "desc": "體驗東京純樸人情味居酒屋。"},
            {"name": "終點：花庵旅舍連住", "km": 45.0, "type": "end", "coord": hostel_hana_an, "desc": "連住免換飯店、免收行李，極致悠閒。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 週末免背行李，以最輕盈的狀態在江戶川水岸慢騎，享受下町慢活節奏。"
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
        "bike_status": "🚲 市區商旅，可向櫃檯確認停放",
        "weather": "☀️ 晴/多雲 ｜ 9.0°C ~ 15.3°C ｜ 0.0mm ｜ 5.2h",
        "foliage": "🔥 水元公園水杉見頃最高峰 ｜ 歐美童話巨木林",
        "timeline": [
            {"name": "清晨必做：水元公園水杉林", "km": 2.0, "type": "scenic", "coord": mizumoto_park, "desc": "06:30 騎車 5 分鐘直達，獨享晨霧中的 1,800 棵水杉黃金森林見頃最盛期！"},
            {"name": "中川・隅田川水岸綠道", "km": 9.5, "type": "waypoint", "coord": [139.820, 35.730], "desc": "順暢平緩進城。"},
            {"name": "終點：淺草雷門 / 上野飯店", "km": 16.6, "type": "end", "coord": asakusa_kaminarimon, "desc": "參拜淺草寺，入住市區休整。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 水元公園是全東京規模最大的水杉巨木林，11 月底見頃時宛如置身歐美童話世界！"
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
        "bike_status": "🚲 市區商旅，可向櫃檯確認停放",
        "weather": "☀️ 快晴 ｜ 7.1°C ~ 16.3°C ｜ 0.0mm ｜ 8.9h",
        "foliage": "🔥 神宮外苑與東大銀杏見頃最高峰 ｜ 黃金大道",
        "timeline": [
            {"name": "起點：淺草", "km": 0.0, "type": "start", "coord": asakusa_kaminarimon, "desc": "東京市區金秋銀杏最高潮巡禮。"},
            {"name": "東京大學本鄉校區", "km": 4.5, "type": "scenic", "coord": todai_hongo, "desc": "赤門漫步、安田講堂前百年大銀杏黃金地毯。"},
            {"name": "皇居二重橋環騎", "km": 10.0, "type": "scenic", "coord": imperial_palace, "desc": "經典護城河與開闊林蔭道。"},
            {"name": "明治神宮外苑銀杏林蔭道", "km": 16.5, "type": "scenic", "coord": jingu_gaien, "desc": "300公尺黃金隧道見頃最盛期，莉香名場面巡禮。"},
            {"name": "終點：秋葉原 / 上野飯店", "km": 23.7, "type": "end", "coord": cycletrip_base, "desc": "慶祝 776km 完美閉環。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 東京金秋的最強句點！一天集齊東大百年銀杏、皇居與神宮外苑黃金雨。"
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
        "bike_status": "🚲 順利還車完成",
        "weather": "☀️ 快晴 ｜ 6.4°C ~ 20.0°C ｜ 0.0mm ｜ 7.1h",
        "foliage": "神田明神古松 ｜ 776km 世界線圓滿閉環",
        "timeline": [
            {"name": "起點：秋葉原", "km": 0.0, "type": "start", "coord": cycletrip_base, "desc": "神田明神平安祈福還願。"},
            {"name": "還車：CycleTrip Base 秋葉原", "km": 2.5, "type": "pivot", "coord": cycletrip_base, "desc": "11:00 前順利還車、驗車完畢。"},
            {"name": "日暮里搭乘京成 Skyliner", "km": 5.0, "type": "waypoint", "coord": [139.7710, 35.7280], "desc": "刷臉進站 36 分鐘直分成田機場。"},
            {"name": "終點：成田國際機場", "km": 7.9, "type": "end", "coord": [140.392, 35.772], "desc": "滿載 19 天回憶圓滿返台。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 776km 世界線圓滿閉環！"
    }
]

def fetch_osrm(wps):
    coord_str = ';'.join([f'{c[0]},{c[1]}' for c in wps])
    url = f'http://router.project-osrm.org/route/v1/bicycle/{coord_str}?overview=full&geometries=geojson'
    for _ in range(3):
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, timeout=12) as resp:
                data = json.loads(resp.read().decode('utf-8'))
                if 'routes' in data and len(data['routes']) > 0:
                    r = data['routes'][0]
                    return round(r['distance'] / 1000.0, 1), r['geometry']['coordinates']
        except Exception as e:
            time.sleep(1.0)
    return 0.0, []

def get_gsi_elev(lon, lat):
    url = f"https://cyberjapandata2.gsi.go.jp/general/dem/scripts/getelevation.php?lon={lon}&lat={lat}&outtype=JSON"
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=4) as resp:
            return float(json.loads(resp.read().decode('utf-8')).get('elevation', 0))
    except:
        return 0.0

all_days_data = []

print("=== 重新生成 19 天完整路網幾何、GSI DEM 標高與 GPX 檔案 ===")
for item in days_meta:
    d_num = item["day"]
    dist_km, coords = fetch_osrm(item["wps"])
    if not coords:
        print(f"Warning: no coords for Day {d_num}")
        continue
    
    sample_rate = max(1, len(coords) // 45)
    chart_coords = coords[::sample_rate]
    if coords[-1] not in chart_coords:
        chart_coords.append(coords[-1])
    
    elev_pts = []
    accum_dist = 0
    prev_pt = chart_coords[0]
    for i, pt in enumerate(chart_coords):
        if i > 0:
            dx = (pt[0] - prev_pt[0]) * 91.0
            dy = (pt[1] - prev_pt[1]) * 111.0
            accum_dist += (dx**2 + dy**2)**0.5
            prev_pt = pt
        e_val = get_gsi_elev(pt[0], pt[1])
        elev_pts.append({
            "km": round(min(dist_km, accum_dist), 1),
            "ele": round(e_val, 1),
            "lon": pt[0],
            "lat": pt[1]
        })
        time.sleep(0.01)
    
    gain = sum([max(0, elev_pts[i]["ele"]-elev_pts[i-1]["ele"]) for i in range(1, len(elev_pts)) if abs(elev_pts[i]["ele"]-elev_pts[i-1]["ele"])>=3.5])
    loss = sum([max(0, elev_pts[i-1]["ele"]-elev_pts[i]["ele"]) for i in range(1, len(elev_pts)) if abs(elev_pts[i-1]["ele"]-elev_pts[i]["ele"])>=3.5])

    # GPX file
    gpx = f'''<?xml version="1.0" encoding="UTF-8"?>
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
        gpx += f'      <trkpt lat="{pt[1]}" lon="{pt[0]}"></trkpt>\n'
    gpx += '''    </trkseg>
  </trk>
</gpx>'''
    
    with open(f"d:/2026東京單車騎旅/day{d_num}_track.gpx", "w", encoding="utf-8") as gf:
        gf.write(gpx)
    with open(f"C:/Users/ymero/Downloads/day{d_num}_track.gpx", "w", encoding="utf-8") as gf:
        gf.write(gpx)

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
        "bike_status": item["bike_status"],
        "weather": item["weather"],
        "foliage": item["foliage"],
        "timeline": item["timeline"],
        "expert_tip": item["expert_tip"],
        "coords": coords,
        "elev_profile": elev_pts
    }
    all_days_data.append(day_record)
    print(f"✅ Day {d_num:02d} 生成完成：{dist_km} km, +{round(gain)}m")

with open("d:/2026東京單車騎旅/all_19days_route_data.json", "w", encoding="utf-8") as jf:
    json.dump(all_days_data, jf, ensure_ascii=False)
print("all_19days_route_data.json saved with full timelines and expert tips!")
