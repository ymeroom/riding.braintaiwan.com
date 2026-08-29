import re

css_block = """
<!-- WEATHER WIDGET CSS -->
<style>
.theme-weather-widget {
    background: var(--bg-light, #f8fafc);
    border: 1px solid var(--card-border, #e2e8f0);
    border-radius: 8px;
    padding: 12px 14px;
    margin: 12px 0 16px 0;
    font-size: 14px;
    color: var(--text-dark, #1e293b);
    display: flex;
    flex-direction: column;
    gap: 8px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.05);
}
.weather-main-row {
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-wrap: wrap;
    gap: 8px;
}
.weather-basic-info {
    display: flex;
    align-items: center;
    gap: 12px;
}
.weather-icon-img {
    width: 40px;
    height: 40px;
    background: var(--primary-light, #e0e0e0);
    border-radius: 50%;
}
.weather-temp {
    font-size: 18px;
    font-weight: 700;
    color: var(--primary, #333);
}
.weather-desc {
    font-size: 13px;
    color: var(--text-muted, #64748b);
}
.weather-rain-alert {
    background: var(--warning-bg, #fef2f2);
    border-left: 4px solid var(--warning-border, #f87171);
    color: var(--warning-text, #991b1b);
    padding: 8px 12px;
    border-radius: 4px;
    font-size: 13px;
    font-weight: 600;
    margin-top: 4px;
}
.weather-config-btn {
    font-size: 11px;
    color: var(--text-muted);
    cursor: pointer;
    text-decoration: underline;
    background: none;
    border: none;
    padding: 0;
}
</style>
"""

js_block = """
<!-- WEATHER WIDGET JS -->
<script>
const OWM_API_KEY = localStorage.getItem('owm_api_key') || '';

const DAY_LOCATIONS = {
    1: { lat: 35.628, lon: 139.270, name: "高尾/八王子", alt: "雨天建議：改搭京王線轉乘，或在沿線室內參觀" },
    2: { lat: 35.626, lon: 139.119, name: "上野原/相模湖", alt: "雨天建議：改搭 JR 中央本線至下個目的地，單車上火車" },
    3: { lat: 35.498, lon: 138.769, name: "富士河口湖", alt: "雨天建議：搭乘復古巴士遊覽美術館、音樂盒之森等室內景點" },
    4: { lat: 35.418, lon: 138.868, name: "山中湖", alt: "雨天建議：搭乘富士急行巴士，或在日歸溫泉館躲雨放鬆" },
    5: { lat: 35.308, lon: 138.934, name: "御殿場", alt: "雨天建議：御殿場 Premium Outlets 室內購物行程" },
    6: { lat: 35.232, lon: 139.106, name: "箱根", alt: "雨天建議：改買箱根周遊券，搭乘登山鐵道、纜車與海賊船" },
    7: { lat: 35.257, lon: 139.155, name: "小田原", alt: "雨天建議：參觀小田原城室內展覽，或直接搭乘 JR" },
    8: { lat: 35.095, lon: 139.073, name: "熱海", alt: "雨天建議：全日溫泉飯店放鬆，或參觀 MOA 美術館" },
    9: { lat: 34.971, lon: 139.098, name: "伊東", alt: "雨天建議：搭乘伊豆急行線欣賞海景，避開淋雨騎行" },
    10: { lat: 34.679, lon: 138.945, name: "下田", alt: "雨天建議：下田海中水族館、黑船博物館等室內設施" },
    11: { lat: 34.976, lon: 138.932, name: "伊豆", alt: "雨天建議：搭乘駿河灣渡輪避開騎行，享受海上風光" },
    12: { lat: 35.101, lon: 138.859, name: "沼津", alt: "雨天建議：沼津港深海水族館與海鮮市場室內大啖美食" },
    13: { lat: 35.161, lon: 138.676, name: "富士", alt: "雨天建議：轉搭 JR 東海道本線避雨" },
    14: { lat: 34.975, lon: 138.382, name: "靜岡", alt: "雨天建議：參觀靜岡市區博物館，或搭新幹線快速移動" },
    15: { lat: 35.319, lon: 139.550, name: "鎌倉", alt: "雨天建議：江之電沿線巡禮，或在古民家咖啡廳聽雨休息" },
    16: { lat: 35.443, lon: 139.638, name: "橫濱", alt: "雨天建議：紅磚倉庫、港未來區室內無縫逛街" },
    17: { lat: 35.689, lon: 139.691, name: "東京", alt: "雨天建議：善用東京地下鐵進行都市探索" },
    18: { lat: 35.689, lon: 139.691, name: "東京", alt: "雨天建議：東京車站地下街或新宿大型百貨全日購物" },
    19: { lat: 35.776, lon: 140.318, name: "成田", alt: "雨天建議：搭乘 Skyliner 提早前往機場免稅店休息" }
};

async function fetchWeatherForDay(dayNum, container) {
    if (!OWM_API_KEY) {
        container.innerHTML = `<div style="font-size:12px;color:var(--text-muted);">☁️ 即時天氣預報模組。 <button class="weather-config-btn" onclick="setOWMKey()">點此輸入 OpenWeatherMap API Key 以啟用</button></div>`;
        return;
    }
    const loc = DAY_LOCATIONS[dayNum];
    if (!loc) return;

    try {
        const res = await fetch(`https://api.openweathermap.org/data/2.5/forecast?lat=${loc.lat}&lon=${loc.lon}&appid=${OWM_API_KEY}&units=metric&lang=zh_tw`);
        const data = await res.json();
        
        if (data.cod !== "200") {
            container.innerHTML = `<div style="font-size:12px;color:red;">天氣載入失敗: ${data.message}</div>`;
            return;
        }

        const current = data.list[0];
        const temp = Math.round(current.main.temp);
        const feels_like = Math.round(current.main.feels_like);
        const desc = current.weather[0].description;
        const icon = current.weather[0].icon;
        const pop = Math.round(current.pop * 100);
        const isRain = pop >= 40 || current.weather[0].main.includes('Rain');

        let html = `
            <div class="weather-main-row">
                <div class="weather-basic-info">
                    <img src="https://openweathermap.org/img/wn/${icon}@2x.png" class="weather-icon-img" alt="weather icon">
                    <div>
                        <div class="weather-temp">${temp}°C <span style="font-size:12px; font-weight:normal; color:var(--text-muted);">體感 ${feels_like}°C</span></div>
                        <div class="weather-desc">📍 ${loc.name} | ${desc} | 降雨機率: ${pop}%</div>
                    </div>
                </div>
                <button class="weather-config-btn" onclick="setOWMKey()">⚙️ 更新 Key</button>
            </div>
        `;

        if (isRain) {
            html += `
                <div class="weather-rain-alert" style="display:block;">
                    ⚠️ 今日降雨機率較高 (${pop}%)：<br>
                    🚲 ${loc.alt}
                </div>
            `;
        }

        container.innerHTML = html;
    } catch (err) {
        container.innerHTML = `<div style="font-size:12px;color:red;">天氣服務暫時無法連線</div>`;
    }
}

function setOWMKey() {
    const key = prompt("請輸入您的 OpenWeatherMap API Key (Free Tier 即可):", OWM_API_KEY);
    if (key !== null) {
        localStorage.setItem('owm_api_key', key.trim());
        location.reload();
    }
}

document.addEventListener("DOMContentLoaded", () => {
    const observer = new IntersectionObserver((entries) => {
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                const dayNum = entry.target.getAttribute('data-day');
                fetchWeatherForDay(dayNum, entry.target);
                observer.unobserve(entry.target);
            }
        });
    }, { rootMargin: "100px" });

    document.querySelectorAll('.theme-weather-widget').forEach(el => {
        observer.observe(el);
    });
});
</script>
"""

def process_html(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            html = f.read()
    except FileNotFoundError:
        return
    
    if '<!-- WEATHER WIDGET CSS -->' not in html:
        html = html.replace('</head>', css_block + '\n</head>')
    if '<!-- WEATHER WIDGET JS -->' not in html:
        html = html.replace('</body>', js_block + '\n</body>')

    for day in range(1, 20):
        widget_html = f'<div class="theme-weather-widget" id="weather-day-{day}" data-day="{day}">載入即時天氣預報中...</div>'
        
        # Avoid duplicate injection
        if f'id="weather-day-{day}"' in html:
            continue
            
        # Inject weather AFTER stats-bar
        pattern = rf'(<div class="day-card" id="day-{day}">.*?<div class="day-stats"[^>]*>.*?</div>)'
        
        if re.search(pattern, html, flags=re.DOTALL):
            html = re.sub(pattern, r'\1\n        ' + widget_html, html, count=1, flags=re.DOTALL)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Processed {filename}")

process_html('index.html')
process_html('tokyo_fuji_cycling_itinerary_19days_v2.html')
