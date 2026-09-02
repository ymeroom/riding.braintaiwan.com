import urllib.request, json, sys, os

# Geocode guest house MARUYA
maruya_coord = [139.07248, 35.09436] # 熱海市銀座町7-8 (約 10m)

# Update Day 11 and Day 12 in generate_19days_rich_dataset.py

with open("d:/2026東京單車騎旅/generate_19days_rich_dataset.py", "r", encoding="utf-8") as f:
    code = f.read()

# Replace maruya coordinates and metadata
maruya_def = "maruya_atami = [139.07248, 35.09436] # guest house MARUYA (銀座町7-8, 10m)\n"
code = code.replace("atami_sun_beach = [139.0750, 35.0970]", "atami_sun_beach = [139.0750, 35.0970]\n" + maruya_def)

# Replace Day 11 metadata
old_d11 = '''    {
        "day": 11,
        "date": "11/23（一）",
        "title": "花火篇：南熱海換宿 ➔ 熱海梅園最晚紅葉 ➔ 晚上 20:20 熱海海上花火大會",
        "wps": [apt_minami_atami, izu_kansya, atami_baien, atami_sun_beach, izu_kansya],
        "hotel": "Izu Kansya (伊豆観舎)",
        "hotel_addr": "靜岡縣熱海市下多賀1473-11",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E9%9D%99%E5%B2%A1%E7%9C%8C%E7%86%B1%E6%B5%B7%E5%B8%82%E4%B8%8B%E5%A4%9A%E8%B2%BA1473-11+Izu+Kansya",
        "booked": True,
        "bike_status": "🚲 獨棟度假別墅，私密空間好停放",
        "weather": "☀️ 快晴 ｜ 10.4°C ~ 19.7°C ｜ 0.0mm ｜ 9.7h",
        "foliage": "🎆 熱海海上花火大會 ｜ 熱海梅園遲楓",
        "timeline": [
            {"name": "起點：Apt南熱海", "km": 0.0, "type": "start", "coord": apt_minami_atami, "desc": "上午移步至隔壁「Izu Kansya（下多賀1473-11）」卸行李。"},
            {"name": "長浜海水浴場漫步", "km": 0.4, "type": "scenic", "coord": [139.070, 35.050], "desc": "距離民宿僅 400m，踏浪看海喝咖啡。"},
            {"name": "熱海梅園紅葉祭", "km": 7.5, "type": "scenic", "coord": atami_baien, "desc": "白天輕裝前往欣賞日本最晚紅葉與來宮神社大楠。"},
            {"name": "晚上 20:20 熱海海上花火大會", "km": 12.0, "type": "pivot", "coord": atami_sun_beach, "desc": "熱海 Sun Beach 直擊高空巨型煙火音浪迴盪！"},
            {"name": "終點：Izu Kansya", "km": 17.7, "type": "end", "coord": izu_kansya, "desc": "散場騎車 15 分鐘（或搭車 5 分鐘）回下多賀，完全免塞車。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 住南熱海是觀賞熱海花火的最高明策略，享受最頂級的煙火視覺，卻能 100% 避開熱海市區散場交通癱瘓！"
    },'''

new_d11 = '''    {
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
    },'''

code = code.replace(old_d11, new_d11)

# Replace Day 12 metadata (Starts from MARUYA)
old_d12 = '''    {
        "day": 12,
        "date": "11/24（二）",
        "title": "湘南篇：南熱海 ➔ 縣道740號柑橘道 ➔ 小田原城 ➔ 湘南海岸防風林 ➔ 江之島",
        "wps": [izu_kansya, atami_sun_beach, pref740_mikan, odawara_castle, shonan_cr, enoshima_island],
        "hotel": "江之島 / 藤澤市區飯店",
        "hotel_addr": "神奈川縣藤澤市江之島周邊",
        "hotel_url": "https://www.google.com/maps/search/?api=1&query=%E6%B1%9F%E4%B9%8B%E5%B3%B6",
        "booked": False,
        "bike_status": "🚲 湘南單車友善飯店，多設停放處",
        "weather": "☀️ 快晴 ｜ 8.9°C ~ 18.0°C ｜ 0.0mm ｜ 9.4h",
        "foliage": "小田原城護城河楓紅 ｜ 灌籃高手湘南海岸",
        "timeline": [
            {"name": "起點：Izu Kansya", "km": 0.0, "type": "start", "coord": izu_kansya, "desc": "出發北上相模灣。"},
            {"name": "避坑密道：縣道740號柑橘景觀道", "km": 14.5, "type": "pivot", "coord": pref740_mikan, "desc": "🚨 避開江之浦暗黑長隧道，半山腰俯瞰相模灣海景（162m）。"},
            {"name": "小田原城天守閣", "km": 28.0, "type": "scenic", "coord": odawara_castle, "desc": "護城河楓紅與歷史古城，品嚐酥脆炸竹筴魚。"},
            {"name": "湘南海岸自行車專用道", "km": 45.0, "type": "scenic", "coord": shonan_cr, "desc": "小田原後一馬平川相模灣平路，沿防風林專用道直奔湘南。"},
            {"name": "終點：江之島 / 藤澤市區飯店", "km": 68.4, "type": "end", "coord": enoshima_island, "desc": "眺望江之島海燈塔與夕陽。"}
        ],
        "expert_tip": "💡 <strong>在地車友實戰解析：</strong> 縣道 740 柑橘景觀道是單車愛好者心中的隱藏瑰寶，小田原之後更是全程平坦的湘南海岸巡航！"
    },'''

new_d12 = '''    {
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
    },'''

code = code.replace(old_d12, new_d12)

with open("d:/2026東京單車騎旅/generate_19days_rich_dataset.py", "w", encoding="utf-8") as f:
    f.write(code)

print("Updated generate_19days_rich_dataset.py with guest house MARUYA!")
