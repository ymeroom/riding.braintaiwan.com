import sys, json

tracks = [
    {
        "track": 1,
        "day": "Day 1 (11/13 五)",
        "title": "世界線的起跑線 (World Line Departure)",
        "theme": "《命運石之門》✕《飆速宅男》✕《正宗哥吉拉》✕ 秋葉原出城至高尾山口",
        "style": "Upbeat J-Rock, energetic anime opening, fast driving drums, bright electric guitar riffs, synthesizer arpeggio, brass accents, Steins;Gate vibe, Japanese pop rock, 175 BPM",
        "intro_tag": "[Intro: Synth Arpeggio & Driving Guitar Riff]",
        "lyrics": """[Intro]
(Synth pulse fades into roaring guitar)
El Psy Kongroo... 踏上未知的世界線！
踏板旋轉，心跳超頻，出發！

[Verse 1]
秋葉原晨光染亮了電器街的窗 (Akihabara morning lights)
鎖定碼表歸零，跨上破風的車把
穿過銀座的喧囂，第一京濱筆直伸展
六鄉橋下，多摩川的秋芒如海浪般翻湧

[Verse 2]
耳邊響起總北高校熱血的吶喊
丸子橋旁，哥吉拉曾踏過的水岸
輪胎切開微涼的秋風，六十五公里專用道
零紅綠燈的河流，引領我逆流向上 (Heading west!)

[Pre-Chorus]
淺川水清，八王子在遠方招手
拋開都會的引力，齒盤鏈條咬合節奏
夕陽把影子拉長，高尾山林在眼前展開！

[Chorus]
(爆發高音 J-Rock)
走吧！奔向命運的世界線！(世界線の向こうへ！)
多摩川的水岸，寫下騎士最初的誓言
汗水蒸發在極樂湯的露天暖湯裡
高尾山下的星空，點燃了十九天的冒險！
Fly into the twilight sky!

[Guitar Solo]
(Fast shredding guitar with dual harmony)

[Bridge]
天狗的羽扇扇起秋天的信號
明天是大垂水峠，山道在召喚！

[Chorus]
走吧！奔向命運的世界線！(夢のプロローグ！)
雙輪畫出的軌跡，是無可取代的自由
這不是巧合，是命運石之門的指引
踏動雙腳，向著大山前進！

[Outro]
秋葉原到高尾山，八十九公里的序章
Ready for tomorrow...
(Final power chord resonating)"""
    },
    {
        "track": 2,
        "day": "Day 2 (11/14 六)",
        "title": "峠道狂詩曲 (Toge Rhapsody)",
        "theme": "《頭文字D》✕《信長協奏曲》✕ 縣道35秋山隱世溪谷 ➔ 都留",
        "style": "High-energy Anime Rock, Eurobeat-inspired driving beat, screaming electric guitar solo, punchy bassline, melodic J-Rock, Initial D style, autumn canyon vibe, 168 BPM",
        "intro_tag": "[Intro: Eurobeat Synth Stabs & Heavy Distortion Guitar]",
        "lyrics": """[Intro]
(Engine revving sound into blazing guitar riff)
清晨八點，甲州街道！
大垂水峠，全力攻頂！

[Verse 1]
晨霧還沒散開，高尾山腳空氣冰涼
國道二十號上坡，齒比切入輕檔
平均坡度百分之五點三，心率在胸口激盪
大垂水峠標高三百九十二米，瞬間踩在腳下！

[Verse 2]
相模湖畔急轉，左切山梨縣道三十五號 (Prefecture Road 35)
揮別大貨車的喧囂，歡迎來到車友的隱世秘境
秋山川溪谷兩側，楓紅如燃燒的戰旗
沿著戰國武田信玄的密道，穿行於林蔭光影

[Pre-Chorus]
三十五公里幽靜緩坡，秋風送來落葉香氣
汗水滴落上管，呼吸與山溪共鳴
秋山隧道標高六百七十四，分水嶺就在前方！

[Chorus]
(熱血爆發 J-Rock)
衝破重力！在峠道上狂飆！(峠を越えていけ！)
秋山溪谷的深紅，見證雙腿的燃燒
穿過黑暗隧道，迎來七公里的大長下坡！
滑降都留市，由加利旅館的溫暖晚餐在等待！
Ride through the canyon wind!

[Guitar Solo]
(Eurobeat fast melodic guitar solo)

[Bridge]
芭蕉翁曾在此駐足吟詠俳句
而我用飛旋的車輪，譜寫今天的壯遊詩篇！

[Chorus]
衝破重力！在峠道上狂飆！(風になれ！)
從相模湖到甲斐之國，六十公里的征途
這就是公路車的靈魂，用汗水換來的純粹
明天，富士五湖在雲端召喚！

[Outro]
都留市的夜色漸濃
由加利的榻榻米，洗去一日征塵...
(Fading acoustic guitar strum)"""
    },
    {
        "track": 3,
        "day": "Day 3 (11/15 日)",
        "title": "水鏡神域 (Mirrored Sacred Realm)",
        "theme": "《你的名字》✕《名偵探柯南》✕ 忍野八海 ✕ 雙湖見頃 ➔ 河口湖",
        "style": "Emotional Anime Pop Rock, sweeping cinematic strings, piano intro, soaring emotional vocals, RADWIMPS vibe, sparkling chimes, autumn lake breeze, 142 BPM",
        "intro_tag": "[Intro: Shimmering Piano & Cello Melody]",
        "lyrics": """[Intro]
(Melodic piano arpeggio)
八十年的雪水，從地心湧出...
那是神明的鏡子，照映著聖山。

[Verse 1]
離開都留沿著急行農路向上攀升
忍野八海清冽見底，草餅在火上烤出香氣
富士山巨大的白雪冠頂，突然穿透雲層矗立眼前
那是如同《你的名字》彗星劃過般的震撼！

[Verse 2]
海拔一千米，山中湖長池親水公園 (Lake Yamanaka)
水面如藍寶石，完美的逆富士倒映其中
旭日丘六百棵楓樹見頃，深紅金黃落滿湖畔
若遇風雨，轉進新倉山五重塔，紅塔雪山名畫定格

[Pre-Chorus]
不管晴空萬里或是薄霧輕籠
雙軌決策的每條路，都是不可思議的邂逅
滑降富士吉田，金色鳥居直指天際！

[Chorus]
(壯闊高亢 RADWIMPS 風格)
神聖的水鏡，倒映著千年的容顏 (時空を超えて！)
山中湖與河口湖，在秋色中交織成畫
今夜住在紅葉迴廊旁，Orange Cabin 的木屋
夜楓點燈如繁星墜落，夢幻的深紅隧道！
Touch the reflection of Mt. Fuji!

[Guitar Solo]
(Cinematic emotional guitar solo with lush strings)

[Bridge]
富士講御師的古道，迴盪著虔誠的鈴聲
在寒涼的暮色中，木屋的暖爐燃起橙光。

[Chorus]
神聖的水鏡，倒映著千年的容顏 (紅葉の輝き！)
雙湖見頃的最盛期，我們正站在風暴的核心
不用趕路，靜靜聆聽湖水的低語
明天，向著本棲湖的逆富士前進！

[Outro]
河口湖的夜楓，在黑暗中閃爍如夢
Good night, Mt. Fuji...
(Gentle piano note decaying)"""
    },
    {
        "track": 4,
        "day": "Day 4 (11/16 一)",
        "title": "千圓紙幣的晨光 (Morning Glow on the 1000-Yen Bill)",
        "theme": "《搖曳露營△ Yuru Camp》封神第一話聖地 ✕ 本棲湖浩庵逆富士",
        "style": "Acoustic Anime Pop, cheerful folk rock, acoustic guitar strumming, whistling, warm mandolin, cozy bass groove, Yuru Camp OST vibe, melodic female J-Pop, 128 BPM",
        "intro_tag": "[Intro: Whistling, Acoustic Guitar & Mandolin Strumming]",
        "lyrics": """[Intro]
(Cheerful acoustic whistling and rhythmic handclaps)
La la la... 早上六點半！
在觀光客醒來前，獨享無人的紅葉迴廊！

[Verse 1]
晨光穿透深紅楓葉灑在清涼的空氣裡
橘色木屋旁，整條迴廊只有我的車輪聲響
沿著湖北 View Line 奔馳，大石公園的湖面平靜如鏡
西湖療癒之里根場，傳統茅草屋頂在秋陽下微笑

[Verse 2]
精進湖邊停下腳步，看大室山依偎在大富士懷中
那是傳說中的「子抱富士」，可愛又莊嚴
轉過最後一個彎道，中之倉峠的山腳下
浩庵露營場的斜坡上，撫子與凜初次相遇的長椅！

[Pre-Chorus]
拿出錢包裡的一千日圓紙幣 (1000 Yen Bill)
對照眼前這幅《湖畔之春》的千古奇景
完全一模一樣！藍色水面上的倒影富士！

[Chorus]
(超元氣溫暖《搖曳露營》風)
晨光灑落在千圓紙幣的湖面！(ふじさんとキャンプ！)
本棲湖的風，吹散了所有的疲憊與煩惱
熱騰騰的咖哩麵，配上無價的富士水鏡
這就是單車露營者的終極天堂！
Shiny days, ride with the breeze!

[Guitar & Mandolin Solo]
(Playful acoustic solo with country folk vibe)

[Bridge]
青木原樹海在身後靜靜沉睡
浩庵房間的窗台上，夕陽把雪山染成粉紅。

[Chorus]
晨光灑落在千圓紙幣的湖面！(ゆるやかな旅路！)
騎過西湖與精進湖，抵達世界線的奇蹟
這份安靜與感動，只屬於清晨早起的騎士
明天下坡一千米，向著駿河灣出發！

[Outro]
(Whistling melody fade out)
富士山，晚安囉！
See you on the other side..."""
    },
    {
        "track": 5,
        "day": "Day 5 (11/17 二)",
        "title": "山獸神之森的休止符 (Sanctuary of the Ancient Woods)",
        "theme": "《幽靈公主》✕ 青木原原始樹海 ✕ 鳴澤冰穴 ✕ 甲州餺飥",
        "style": "Mystical Anime Ballad, ambient orchestral, cinematic Japanese flute (shinobue), taiko drum beat, warm electric piano, Princess Mononoke forest atmosphere, lush strings, 95 BPM",
        "intro_tag": "[Intro: Japanese Shinobue Flute & Ambient Wind FX]",
        "lyrics": """[Intro]
(Atmospheric taiko drum and mystical flute melody)
貞觀六年的熔岩之上，森林沉睡了一千年...
今天不趕路，傾聽大地的呼吸。

[Verse 1]
青木原樹海古老的林道，覆滿深綠青苔
熔岩巨木盤根錯節，宛如宮崎駿筆下的山獸神之森
鳴澤冰穴與富岳風穴，地心深處凝結著萬年寒冰
零度的地洞裡，封存著江戶時代蠶種的記憶

[Verse 2]
高原的氣候變幻莫測，這是我們預留的定海神針
若有風雨就進屋避寒，若是晴朗就深度探索
來到富士展望之湯 Yurari，浸入冒著白煙的露天溫泉
熱氣蒸騰中，巨大的富士山在眼前巍峨聳立

[Pre-Chorus]
大鐵鍋裡滾燙的甲州名物餺飥麵 (Hoto Noodles)
南瓜融化在濃郁味噌湯底，厚切麵條吸滿精華
戰國武田軍團的寶刀軍糧，溫暖了每一寸肌肉！

[Chorus]
(空靈大氣宮崎駿風交響)
在古老森林的懷抱裡，找回平靜的節奏 (森の囁き...)
這是一段為靈魂預留的休止符
冰穴的冷冽與溫泉的暖湯，交織出高原的詩意
蓄滿力量，準備迎接明天的千米大滑降！
Breathe in the ancient mountain air!

[Flute & Cello Solo]
(Emotional traditional Japanese flute dueling with cello)

[Bridge]
不要害怕停留，停留是為了看見更深沉的風景
當烏雲散開，富士山的雪冠在夕陽下閃耀金光。

[Chorus]
在古老森林的懷抱裡，找回平靜的節奏 (大自然の恵み)
五湖核心的緩衝日，讓旅程立於不敗之地
喝乾最後一口熱湯，整裝待發
駿河灣的召喚，就在明日山腳下！

[Outro]
(Gentle temple bell chiming and wind fading away)"""
    },
    {
        "track": 6,
        "day": "Day 6 (11/18 三)",
        "title": "破風降臨千米疾走 (Thousand-Meter Wind Descent)",
        "theme": "《鎌倉殿的13人》✕ 朝霧高原 ✕ 白糸之瀑 ➔ 富士宮千米長下坡",
        "style": "Fast-paced Symphonic J-Rock, blazing guitar riffs, dramatic string sections, thunderous drums, triumphant anime OST, wind-rush adrenaline, 172 BPM",
        "intro_tag": "[Intro: Fast Symphonic Strings & Heavy Double-Kick Drums]",
        "lyrics": """[Intro]
(Wind rushing sound into epic string crescendo)
海拔九百零五米，本棲湖出發！
連降八百米，千米大長下坡開始！

[Verse 1]
穿上防風長指手套，拉緊風衣領口
朝霧高原牧場一望無際，金黃秋芒在狂風中搖曳
右手是悠閒吃草的乳牛，左手是雄偉壯麗的富士西壁
八百年前源賴朝曾在此策馬，舉辦「富士之卷狩」！

[Verse 2]
朝霧 Food Park 喝一杯現煮熱牛奶暖手
來到天下名瀑白糸之瀑，寬達一百五十米如絲絹垂掛
富士山融雪從熔岩縫隙噴湧而出，水氣瀰漫著楓紅
深吸一口清涼水氣，再次跨上座墊！

[Pre-Chorus]
點放煞車，時速突破四十公里！
體感逼近冰點，潤井川河谷在腳下展開
從高寒高原一路向著溫暖的駿河灣狂飆！

[Chorus]
(速度感爆棚交響 J-Rock)
破風疾走！一千米的高差滑降！(風を切り裂いて！)
重力加速度在耳邊呼嘯成歌
從本棲湖的冰峰，直落富士宮的市街
這是一場單車生涯最暢快淋漓的極速飛行！
Descending from the mountain throne!

[Guitar Solo]
(Blazing fast tapping and sweep picking guitar solo)

[Bridge]
抵達富士山本宮淺間大社總本社
湧玉池清泉洗淨臉上的塵埃，鐵板上熱炒著香脆富士宮炒麵！

[Chorus]
破風疾走！一千米的高差滑降！(大空へ舞い降りろ！)
告別了富士五湖的高原寒涼
駿河灣的暖風已經在前方海平線招手
這場完美的下坡，寫下壯麗的轉折章節！

[Outro]
富士宮市區的晚風，溫柔而溫暖
Cheers to the descent!
(Ending power chord)"""
    },
    {
        "track": 7,
        "day": "Day 7 (11/19 四)",
        "title": "駿河灣的蔚藍防潮堤 (Suruga Blue Sea Wall)",
        "theme": "《Love Live! Sunshine!!》✕《萬葉集》田子浦 ➔ 千本松原海堤 ➔ 沼津 ➔ 三島",
        "style": "Sparkling Anime Idol Pop Rock, energetic brass section, driving synth-pop beat, catchy chorus, ocean breeze melody, Love Live Aqours style, sunny surf vibe, 160 BPM",
        "intro_tag": "[Intro: Bright Brass Horns & Upbeat Pop Synth]",
        "lyrics": """[Intro]
(1-2-3-Jump! Upbeat drum roll and sunny brass!)
沼津的蔚藍大海，我們來了！
踏上海堤專用道，全力衝刺！

[Verse 1]
沿著潤井川平緩下坡，一路騎到田子の浦港
正如山部赤人在《萬葉集》中吟誦的名句：
「走出田子浦，抬頭望富士，皚皚白雪覆峰巔！」
浩瀚的駿河灣在眼前展開，波光粼粼萬里無雲！

[Verse 2]
切入千本松原海岸防潮堤專用道 (Senbonmatsubara)
整整十五公里封閉專用道，零紅綠燈、零汽車！
左邊是弘法大師植下的萬棵蒼翠黑松林
右邊是波浪滔滔的太平洋，回頭是巨大的雪冠富士！

[Pre-Chorus]
這就是《Love Live! Sunshine!!》少女們奔跑的海灘
來到沼津港海鮮市場，大口享用肥美深海魚海鮮丼
現烤大帆立貝香氣撲鼻，海風撫平所有疲憊！

[Chorus]
(超元氣陽光 Aqours 風格)
迎著駿河灣的海風奔馳！(青空Jumping Heart！)
左手黑松林，右手大海洋，背後是雪白富士山
平坦的海堤專用道，是單車騎士的夢幻舞台
一路狂飆到三島，源兵衛川清泉流淌！
Shine bright like the ocean waves!

[Guitar & Synth Solo]
(Energetic dual solo with sunny beach synth vibe)

[Bridge]
走進三嶋大社，源賴朝曾在此祈求旗開得勝
街角百年老店飄出炭烤鰻魚飯的誘人醬香。

[Chorus]
迎著駿河灣的海風奔馳！(海風に乗って！)
告別高山挑戰，迎向伊豆半島的名湯之旅
這是一條無拘無束的蔚藍航線
明天，狩野川自行車道在前方等待！

[Outro]
沼津到三島，四十公里的陽光巡航
(Cheerful brass hit and ocean wave sound effect)"""
    },
    {
        "track": 8,
        "day": "Day 8 (11/20 五)",
        "title": "修善寺竹林幽夢 (Bamboo Dream of Shuzenji)",
        "theme": "《伊豆的舞孃》✕《月薪嬌妻》修善寺溫泉 ➔ 温泉宿 水口",
        "style": "Traditional-Modern J-Pop, shamisen fusion, gentle acoustic guitar, soft piano, nostalgic romantic melody, Hoshino Gen vibe, autumn hot spring breeze, 118 BPM",
        "intro_tag": "[Intro: Japanese Shamisen & Acoustic Fingerpicking]",
        "lyrics": """[Intro]
(Gentle shamisen notes blending into soft acoustic guitar)
弘法大師擊碎岩石的清泉...
伊豆最古老的千年名湯。

[Verse 1]
週五午後從三島出發，避開三連休的觀光車潮
沿著清澈的狩野川自行車道逆流平緩漫騎
二十公里輕鬆短程，微風吹拂水岸芒草
桂川兩旁的古老木造旅館，在秋楓中靜靜迎候

[Verse 2]
入住「温泉宿 水口」，傳統日式玄關妥善停好愛車
換上舒適浴衣與木屐，踩在石板路上發出清脆聲響
漫步走過朱紅色的桂橋，竹林小徑圓形竹椅仰望天空
彷彿走進川端康成筆下《伊豆的舞孃》純真年代

[Pre-Chorus]
想起《月薪嬌妻》新垣結衣與星野源的溫泉旅行
獨鈷之湯升起裊裊白煙，夏目漱石在此寫下《修善寺日記》
傍晚探訪虹之鄉，楓葉在夜間燈光下如燃燒的彩霞！

[Chorus]
(溫暖浪漫 J-Pop 旋律)
在修善寺的竹林深處做一場幽夢 (竹林の小径...)
千年古湯的暖流，融化了旅途所有疲憊
紅橋流水，楓葉落滿石階
今夜在榻榻米上，聽著溪流聲安然入眠
Dream in the autumn mist of Shuzenji.

[Shamisen & Piano Solo]
(Elegant and emotional solo blending traditional and modern styles)

[Bridge]
提早一天抵達的明智抉擇
避開了明日連休的喧囂，獨享這座古鎮的寧靜。

[Chorus]
在修善寺的竹林深處做一場幽夢 (古都の秋色)
伊豆半島的心臟，洗淨鉛華的溫柔
泡一杯靜岡煎茶，感受時光慢了下來
明天，冷川峠在山那端靜靜等待！

[Outro]
(Temple bell and gentle wind chime fading)
晚安，修善寺..."""
    },
    {
        "track": 9,
        "day": "Day 9 (11/21 六)",
        "title": "熔岩懸崖與伊豆之瞳 (Lava Cliffs and Eye of Izu)",
        "theme": "《藍海少女！》✕《火曜懸疑劇場》斷崖 ➔ 一碧湖 ➔ 城崎海岸 ➔ KAWANA",
        "style": "Epic Progressive Anime Rock, dynamic shifts, soaring guitar solos, dramatic ocean strings, energetic drum groove, anime adventure theme, coastal breeze, 155 BPM",
        "intro_tag": "[Intro: Dramatic Ocean Wave FX & Roaring Electric Guitar]",
        "lyrics": """[Intro]
(Thunderous drum roll and driving guitar riff)
三連休首日！果斷避開天城峠！
翻越冷川峠，直奔太平洋熔岩海岸！

[Verse 1]
告別修善寺切入縣道十二號冷川峠
幽靜林蔭道上幾乎沒有觀光大巴的廢氣干擾
標高三百七十一米輕鬆翻越，穿透林間抵達「伊豆之瞳」一碧湖
十萬年前形成的火山湖，水面倒映著滿山斑斕紅葉

[Verse 2]
順坡滑降直撲相模灣，《藍海少女！》的海風撲面而來
四千年前大室山火山噴發，滾燙熔岩流入冰冷大海
造就了城崎海岸鋸齒狀的黑色熔岩海蝕巨崖
二十三米高的門脇吊橋上，白浪在腳下瘋狂拍擊！

[Pre-Chorus]
這正是《火曜懸疑劇場》名偵探對決的懸崖聖地！
波濤洶湧的太平洋，在陽光下展現極致的鈷藍
沿著海岸公路巡航，抵達川奈海景第一排旅舍！

[Chorus]
(壯闊熱血 Anisong 高音)
在熔岩海崖與伊豆之瞳間飛馳！(荒波を越えて！)
四千年的火山地質，是大自然雕刻的史詩
海浪拍擊著玄武岩，激盪出自由的白色水花
入住海景民宿 KAWANA，海潮聲伴隨入夢！
Ride the edge of the Pacific Ocean!

[Guitar Solo]
(Epic neoclassical guitar solo with heavy whammy bar dives)

[Bridge]
三浦按針曾在此建造日本第一艘西式帆船
而我們駕馭著現代的鐵馬，航行在相模灣的邊界。

[Chorus]
在熔岩海崖與伊豆之瞳間飛馳！(青い海の記憶！)
完美破解連休車潮，開闢專屬的探險路線
從古老火山湖到壯麗海蝕崖
這是一場超越想像的伊豆東岸騎行！

[Outro]
相模灣的海浪拍打著窗櫺
海景第一排的星空，無比璀璨...
(Ocean waves fading out)"""
    },
    {
        "track": 10,
        "day": "Day 10 (11/22 日)",
        "title": "網代夕照的避風港 (Ajiro Golden Haven)",
        "theme": "《夏色奇蹟》✕ 網代風待ち港 ✕ 避開暗黑隧道 ➔ Apt南熱海",
        "style": "Relaxing City Pop, breezy guitar chords, retro 80s synth bass, smooth saxophone accent, warm sunset groove, Tatsuro Yamashita vibe, coastal seaside, 110 BPM",
        "intro_tag": "[Intro: Smooth Saxophone & 80s City Pop Electric Piano]",
        "lyrics": """[Intro]
(Groovy bassline with warm retro Rhodes piano and saxophone)
十七公里的悠閒...
避開喧囂，在網代港停下腳步。

[Verse 1]
離開川奈沿著相模灣海岸北上
宇佐美的金色沙灘上，衝浪客追逐著晨光的海浪
國道一百三十五號的黑暗隧道在眼前出現
果斷右轉切入網代漁港舊街，徹底避開危險黑點！

[Verse 2]
江戶時代的「風待ち港」，古老漁村飄著曬竹筴魚乾的鹹香
狹窄的老街上沒有呼嘯的自駕車潮
只有純樸的木造老屋與海鳥盤旋的叫聲
十七點四公里輕鬆短程，避開三連休熱海大塞車

[Pre-Chorus]
提早進駐長浜海灘海景第一排 Apt南熱海
私人陽台推開門，整個網代灣盡收眼底
金色夕陽把海面染成一片波光粼粼的琥珀色！

[Chorus]
(浪漫放鬆 City Pop 節奏)
在網代灣的夕陽裡找到避風港 (潮風のメロディ...)
慢下來的節奏，是給靈魂最好的犒賞
聽海浪輕輕拍打長浜白沙灘
在陽台上喝一杯靜岡柑橘酒，微醺的黃昏！
Golden sunset over Ajiro Bay.

[Saxophone & Guitar Solo]
(Smooth and jazzy saxophone solo with clean chorus guitar)

[Bridge]
松本清張曾在熱海寫下《點與線》的旅情
而我們用單車的慢速，讀懂了這片海岸的溫柔。

[Chorus]
在網代灣的夕陽裡找到避風港 (静かな入り江)
避開所有塞車煩惱，尊享無敵海景公寓
海潮聲像一首永遠唱不完的催眠曲
明天，熱海海上花火在夜空中綻放！

[Outro]
(Saxophone riff fading with seaside ocean breeze)
Good night, Minami-Atami..."""
    },
    {
        "track": 11,
        "day": "Day 11 (11/23 一)",
        "title": "海灣夜空的最後花火 (Fireworks Over the Caldera Bay)",
        "theme": "《煙花，應該和誰看？》✕ 米津玄師 ✕ 來宮神木 ✕ guest house MARUYA",
        "style": "Grand Cinematic J-Pop Ballad, emotional piano intro, massive orchestral explosion, soaring choral harmonies, Kenshi Yonezu 'Uchiage Hanabi' style, fireworks boom effects, 130 BPM",
        "intro_tag": "[Intro: Gentle Piano Strumming & Distant Ocean Echo]",
        "lyrics": """[Intro]
(Piano arpeggio with fireworks sparkle sound FX)
昇った花火は、横から見るか？下から見るか？
今夜，在熱海海灣的夜空下...

[Verse 1]
清晨從南熱海出發，沿著海岸平緩北上
走進熱海梅園，全日本最遲見頃的深紅楓葉正在燃燒
來宮神社的本州第一大楠神木，兩千一百年歲月靜靜守護
繞著巨木走一圈，祈求這趟七百七十六公里騎旅圓滿平安

[Verse 2]
下午三點入住熱海銀座商店街的 guest house MARUYA
文青設計的大廳，放妥愛車與行囊
距離熱海 Sun Beach 只有兩百五十公尺！
穿上便服散步三分鐘，直接抵達海灘特等席！

[Pre-Chorus]
二十點二十分，倒數計時！
三面環山的天然扇形海灣，化身為世界上最震撼的立體音響劇院
第一發金色巨型煙火，呼嘯著直衝天際！

[Chorus]
(爆發性交響 J-Pop《打上花火》米津玄師風格)
轟然綻放！在熱海海灣的夜空！(パッと光って咲いた！)
五彩斑斕的花火如瀑布般從天幕傾瀉而下
山壁迴盪著震天巨響，直接撞擊著騎士的心跳！
散場步行三分鐘回房，零塞車的極致奢華！
Uchiage Hanabi lighting up the sea!

[Strings & Guitar Solo]
(Massive emotional guitar solo supported by grand cinematic orchestra)

[Bridge]
尾崎紅葉在《金色夜叉》寫下熱海之月的悲歡離合
而今晚只有我們與漫天花火璀璨共舞。

[Chorus]
轟然綻放！在熱海海灣的夜空！(夜空を染める夢！)
照亮了相模灣的波浪，照亮了十一天的騎行回憶
在銀座商店街的小酒館乾杯慶祝
這是一生難忘的伊豆海上花火之夜！

[Outro]
(Fireworks boom echoing in distance into soft piano fading)
熱海銀座的燈火漸漸熄滅...
明天，湘南海岸在呼喚！"""
    },
    {
        "track": 12,
        "day": "Day 12 (11/24 二)",
        "title": "早雲柑橘道與湘南風 (Mandarin Groves and Shonan Breeze)",
        "theme": "《灌籃高手》流川楓公路 ✕《海街日記》✕ 縣道740柑橘道 ➔ 江之島",
        "style": "90s Classic Anime Hard Rock, crunchy overdrive electric guitars, driving baseline, anthemic WANDS/BAAD style, Slam Dunk OST vibe, sunny coastal highway, 165 BPM",
        "intro_tag": "[Intro: Chunky Overdrive Guitar Riff & Driving Rock Beat]",
        "lyrics": """[Intro]
(90s anime rock guitar intro - BAAD style!)
熱海銀座出發！
告別伊豆，奔向湘南海岸！

[Verse 1]
清晨沿著國道一百三十五號北上相模灣
果斷切入神奈川縣道七百四十號柑橘景觀道 (Pref 740)
徹底避開大貨車奔馳的江之浦暗黑長隧道！
在半山腰的蜜柑果園間爬升，居高臨下俯瞰蔚藍太平洋

[Verse 2]
一路順暢滑降抵達戰國難攻不落第一堅城——小田原城
北條早雲五代基業，護城河旁楓紅如畫
品嚐酥脆噴香的炸竹筴魚定食，體力瞬間滿血！
從小田原出發，前方是一馬平川的相模灣平原！

[Pre-Chorus]
切入湘南海岸防風林專用自行車道
耳邊響起《灌籃高手》熟悉的吉他旋律
想像流川楓戴著耳機在海風中破風飛馳！

[Chorus]
(燃爆 90 年代《灌籃高手》熱血硬搖滾)
奔向湘南海岸！迎著金色海浪！(君が好きだと叫びたい！)
早雲柑橘道的清香，與太平洋的海風交織成歌
小田原城後的六十公里坦途，輪胎在柏油路上尖叫！
江之島的海燈塔已在夕陽下閃耀！
Ride on the Shonan coastal highway!

[Guitar Solo]
(Classic 90s screaming melodic rock guitar solo)

[Bridge]
《海街日記》四姐妹在極樂寺的生活詩篇
在我們車輪轉動的節奏裡緩緩重現。

[Chorus]
奔向湘南海岸！迎著金色海浪！(誰にも譲らない夢！)
征服了伊豆半島的所有高山峠道
在平坦的海岸防風林裡享受極速快感
今晚在江之島，品嚐熱騰騰吻仔魚丼！

[Outro]
江之島的日落把相模灣染成一片金紅
(Final heavy rock drum fill and guitar chord)"""
    },
    {
        "track": 13,
        "day": "Day 13 (11/25 三)",
        "title": "高校前的命運路口 (Destiny Crossing at Kamakura High)",
        "theme": "《灌籃高手》世紀平交道 ✕《倒數第二次戀愛》✕ 柏尾川綠道 ➔ 橫濱",
        "style": "Nostalgic J-Rock, melodic pop punk, ringing acoustic-electric guitar, emotional singalong chorus, ASIAN KUNG-FU GENERATION vibe, youth memories, coastal railroad, 158 BPM",
        "intro_tag": "[Intro: Ringing Railroad Crossing Chime & Energetic Guitar Riff]",
        "lyrics": """[Intro]
(Ding-ding-ding railroad bell into fast AJIKAN style guitar!)
鎌倉高校前！
綠色江之電正緩緩駛過！

[Verse 1]
清晨七點半，抵達全亞洲最著名的平交道口
碧藍大海與七里濱的浪花作為背景
彷彿看見櫻木花道背著球鞋、晴子在對面微笑揮手
三十年的青春熱血，在這一刻與現實世界重疊！

[Verse 2]
轉進鎌倉古都，長谷寺九點一八米十一面觀音莊嚴佇立
回遊式庭園中深秋紅葉倒映在清澈池水中
《倒數第二次戀愛》極樂寺站前漫步
告別山道，切入平整平坦的柏尾川水岸自行車道！

[Pre-Chorus]
柏尾川專用道一路無紅綠燈向北延伸
穿過戶塚進入橫濱港未來二十一區 (Minato Mirai 21)
摩天大樓與巨型摩天輪在水岸天際線拔地而起！

[Chorus]
(熱血青春 ASIAN KUNG-FU GENERATION 風格)
在命運的平交道口向青春致敬！(遥か彼方へ！)
江之電的鈴聲喚醒了心底不滅的熱血
沿著柏尾川水岸綠道順暢滑進橫濱港
連住東京灣台場基地，免行李暢快漫騎！
Cross the line into Yokohama's skyline!

[Guitar Solo]
(Catchy melodic indie rock guitar duel)

[Bridge]
一八五九年黑船來航打破了鎖國的平靜
而我們用單車的雙輪，丈量著從鎌倉幕府到現代港灣的時光。

[Chorus]
在命運的平交道口向青春致敬！(未来へのリライト！)
三十公里的平坦水岸巡航，輕鬆愜意
東京灣的海風吹散了連日的疲勞
今夜在摩天輪下，為後半段的黃金篇章舉杯！

[Outro]
橫濱港未來的霓虹燈在海面跳躍
(Railroad bell chime fades into ambient city sounds)"""
    },
    {
        "track": 14,
        "day": "Day 14 (11/26 四)",
        "title": "獨角獸與彩虹之橋 (Unicorn on the Rainbow Bridge)",
        "theme": "《機動戰士鋼彈 UC》獨角獸 ✕《大搜查線》彩虹大橋 ✕ 台場水岸巡航",
        "style": "Epic Sawano-style Electronic Orchestral Rock, dramatic drop, powerful synth brass, intense heavy drums, Hiroyuki Sawano Gundam UC style, Odaiba futuristic bay, 148 BPM",
        "intro_tag": "[Intro: Sawano-style Cinematic Drop, Epic Choir & Synth Brass]",
        "lyrics": """[Intro]
(Massive electronic synth drop with dramatic orchestral strings)
Destruction Mode... 啟動！
在東京灣的彩虹之上破風飛翔！

[Verse 1]
橫濱山下公園漫步，百年銀杏落滿黃金地毯
歷史郵輪冰川丸號靜靜泊在蔚藍港灣
第一京濱平坦寬闊，輕裝無行李自由馳騁
穿越羽田水岸，切入豐洲大橋專用自行車道！

[Verse 2]
奧運水岸專用道寬達五米，視野無限開闊
眼前是《大搜查線》織田裕二怒吼的彩虹大橋！
「無法封鎖彩虹大橋！」——但單車可以自由穿行！
《戀愛世代》木村拓哉的水晶蘋果在海風中閃爍

[Pre-Chorus]
抵達台場 DiverCity 廣場
一比一等身大獨角獸鋼彈 RX-0 巍峨聳立
紅色神經感應框架在陽光下轉換為毀滅模式！

[Chorus]
(澤野弘之風格燃爆交響電音搖滾)
跨越彩虹大橋！奔向鋼彈的誓言！(可能性の獣！)
東京灣的蔚藍天際線在眼前三百度展開
免行李的純粹自由，讓雙輪快如閃電
在台場海濱公園的夕陽下，見證未來之城！
Unicorn awaken on Tokyo Bay!

[Guitar & Synth Solo]
(Heavy drop with shredding electric guitar and dubstep-orchestral fusion)

[Bridge]
幕末江戶幕府修築砲台抵禦黑船
如今化身為全日本最前衛浪漫的海濱綠道。

[Chorus]
跨越彩虹大橋！奔向鋼彈的誓言！(希望の光！)
三十八公里的海灣巡航，一馬平川
今晚連住東京灣水岸基地，盡情享受下町前奏
明天，前往兩津勘吉的葛飾故鄉！

[Outro]
獨角獸鋼彈頭部天線閉合
(Dramatic orchestral chord resonating into distance)"""
    },
    {
        "track": 15,
        "day": "Day 15 (11/27 五)",
        "title": "葛飾下町的昭和人情 (Shitamachi Memories of Katsushika)",
        "theme": "《烏龍派出所》兩津勘吉 ✕《男人真命苦》車寅次郎 ➔ 柴又 ➔ 花庵旅舍",
        "style": "Nostalgic Upbeat Shitamachi Pop, bouncy brass and accordion, energetic ska-punk rhythm, cheerful retro J-Pop, Kochikame opening vibe, lively street banter, 150 BPM",
        "intro_tag": "[Intro: Retro Accordion & Bouncy Brass Horn Section]",
        "lyrics": """[Intro]
(Lively Kochikame style whistle and brass stabs!)
「大家注意啦！我是葛飾區龜有公園前派出所的兩津勘吉！」
出發！前往人情味滿滿的葛飾下町！

[Verse 1]
告別台場海濱，穿過葛西臨海公園
直徑一百一十七米巨大鑽石摩天輪旋轉在藍天
切入中川水岸自行車道，避開所有市區紅綠燈與車潮
河堤兩旁秋草金黃，下町清涼微風撲面而來

[Verse 2]
抵達柴又帝釋天題經寺，雕刻長廊精美絕倫
矢切之渡的人力木船在江戶川上悠悠搖晃
《男人真命苦》寅次郎雕像在車站前親切打招呼
熱騰騰的現烤草糰子與炭烤鰻魚飯香氣撲鼻！

[Pre-Chorus]
穿過純樸的昭和懷舊商店街
抵達葛飾金町「花庵旅舍 (Hostel Hana An)」
官方確認可安全放單車，連住兩晚徹底放鬆！

[Chorus]
(超歡樂《烏龍派出所》主題曲風格)
葛飾下町的昭和人情味！(葛飾ラプソディー！)
沒有摩天大樓的冷漠，只有居酒屋的溫暖笑聲
中川的水流長又長，兩津的自行車又在河堤上狂奔
入住水元公園旁的花庵，享受悠閒的下町慢活！
Shitamachi memories flowing with love!

[Accordion & Brass Solo]
(Jovial and bouncy ska-pop solo with laughing whistles)

[Bridge]
《秒速五公分》鐵道平交道在暮色中叮噹作響
金町老街的串燒小店冒起陣陣白煙。

[Chorus]
葛飾下町的昭和人情味！(おいでよ亀有！)
避開市中心擁擠嘈雜，選擇水岸旁的隱世基地
今晚免收行李，在下町居酒屋乾一杯生啤酒
明天輕裝出擊，江戶川水岸無重力暢騎！

[Outro]
「阿兩！又偷懶去騎單車啦！」
(Lively brass fanfare finish!)"""
    },
    {
        "track": 16,
        "day": "Day 16 (11/28 六)",
        "title": "江戶川無重力巡航 (Zero-Gravity Cruise on Edogawa)",
        "theme": "《四月是你的謊言》水岸 ✕《烏龍派出所》江戶川巡邏 ➔ 週末輕裝巡航",
        "style": "Breezy Acoustic J-Pop, fingerstyle acoustic guitar, uplifting flute, light percussion, relaxing indie pop, weekend cycling cruise, crystal blue sky, 122 BPM",
        "intro_tag": "[Intro: Gentle Acoustic Guitar Picking & Warm Piano Notes]",
        "lyrics": """[Intro]
(Peaceful acoustic guitar with gentle bird chirping)
免收行李的週六早晨...
全車卸下重負，像羽毛一樣輕盈。

[Verse 1]
從金町花庵旅舍出發，車架上沒有沈重的馬鞍包
切入江戶川專用自行車道，寬闊河堤一望無際
秋日澄澈的藍天倒映在平靜水面上
正如《四月是你的謊言》水岸堤防上的夕陽騎行

[Verse 2]
中川與麗子在河堤上放著風箏
江戶時代利根川東遷工程造就了這片沃野
踩動踏板毫不費力，無重力巡航在秋風中
流山白壁古街道喝一杯手沖咖啡，享受時間停滯

[Pre-Chorus]
不用換飯店，不用趕進度
這是十九天長途跋涉中，最奢侈的漫活時光！

[Chorus]
(輕盈悠揚的清新 J-Pop)
在江戶川水岸享受無重力巡航 (風の歌が聞こえる)
把身心的疲憊全部交給金黃色的河堤
輪胎輕快地滾動，心靈如白鷺般自由飛翔
今夜回到花庵連住，下町老街的人情依然溫暖！
Floating on the river breeze.

[Acoustic & Flute Solo]
(Breezy indie folk solo with sweet acoustic melodies)

[Bridge]
常磐線鐵道高架下傳來列車規律的震動
下町老店熱騰騰的關東煮，溫暖著旅人的胃。

[Chorus]
在江戶川水岸享受無重力巡航 (心軽やかに)
這不是競賽，而是一場與自己的深度對話
看著落日把江戶川染成一片金紅
明天清晨，水元公園萬棵水杉即將震撼登場！

[Outro]
(Acoustic strumming slowly fading into quiet river sounds)"""
    },
    {
        "track": 17,
        "day": "Day 17 (11/29 日)",
        "title": "萬棵水杉的黃金童話 (Golden Fairy Tale of Metasequoia)",
        "theme": "《鬼滅之刃》大正淺草 ✕ 水元公園 1,800 棵水杉黃金森林見頃 ➔ 淺草",
        "style": "Ethereal Cinematic Folk Pop, acoustic guitar picking, lush cello and violin, warm choral hums, fairy-tale autumn forest, Studio Ghibli meets modern J-Pop, 116 BPM",
        "intro_tag": "[Intro: Ethereal Strings, Cello & Whispering Choral Harmonies]",
        "lyrics": """[Intro]
(Dreamy harp and cello arpeggio)
清晨六點半，騎車五分鐘...
走進全東京最大的黃金森林。

[Verse 1]
水元公園的薄霧還在水面上輕輕飄蕩
一千八百棵水杉巨木拔地參天，倒映在清澈水鄉
十一月底見頃最盛期，整座森林轉為濃郁的金黃與紅褐色
宛如走進北歐童話世界，美得令人屏息凝神！

[Verse 2]
離開金色童話水杉林，沿著中川與隅田川水岸順暢進城
眼前出現巨大的紅色雷門燈籠——淺草寺到了！
西元六二八年創建的江戶最古老寺廟
《鬼滅之刃》大正時代繁華夜景，炭治郎初遇無慘之聖地！

[Pre-Chorus]
仲見世通飄著人形燒與煎餅香氣
《淺草小子》北野武與法蘭西座的昭和熱血傳奇
進駐水岸文青旅舍，這座城市正在展現它最燦爛的容顏！

[Chorus]
(吉卜力宮崎駿風空靈大氣交響民謠)
萬棵水杉織就的黃金童話！(メタセコイアの森！)
晨霧中的金黃紅褐，是東京深秋最極致的秘境
從靜謐水鄉騎進繁華古剎淺草雷門
一場跨越童話與歷史的奇幻穿越！
Golden forest whispering in the morning mist!

[Violin & Cello Solo]
(Sweeping emotional string solo filled with autumn nostalgia)

[Bridge]
隅田川的遊船緩緩駛向東京灣
晴空塔在金色夕陽下高聳入雲。

[Chorus]
萬棵水杉織就的黃金童話！(黄金の夢幻境)
十六公里的短程漫騎，沉浸在深秋的畫卷中
明天，東京金秋的最高潮——神宮外苑與東大銀杏
即將為這趟騎旅寫下最輝煌的篇章！

[Outro]
淺草寺的暮鐘在夜空中迴盪
(Temple bell resonating into peaceful silence)"""
    },
    {
        "track": 18,
        "day": "Day 18 (11/30 一)",
        "title": "神宮外苑的黃金雨 (Golden Rain at Jingu Gaien)",
        "theme": "《東京愛情故事》莉香名場面 ✕《東大特訓班》赤門 ✕ 神宮外苑銀杏大道",
        "style": "Iconic 90s J-Pop Anthem, shimmering chorus guitar, expressive saxophone solo, passionate emotional melody, Kazumasa Oda / Love Story wa Totsuzen ni vibe, golden falling leaves, 124 BPM",
        "intro_tag": "[Intro: Iconic 90s City Pop Guitar Strum & Saxophone Hook]",
        "lyrics": """[Intro]
(Legendary 90s J-Pop piano chords and electric guitar hook)
何から伝えればいいのか...
在神宮外苑的黃金雨中，與東京相遇！

[Verse 1]
東京大學本鄉校區，古老的加賀藩赤門古樸莊嚴
《東大特訓班》阿部寬熱血激勵的百年學府
安田講堂前，參天巨大銀杏樹鋪滿厚厚的黃金地毯
每一步踩在落葉上，都發出金秋清脆的沙沙聲

[Verse 2]
環騎皇居二重橋與伏見櫓，江戶幕府德川將軍居城遺址
直奔明治神宮外苑——東京金秋最震撼的高潮！
大正十二年種植的一百四十六棵銀杏樹
三百公尺純粹金黃的立體隧道，見頃最盛期遮蔽了整個天空！

[Pre-Chorus]
這正是《東京愛情故事》莉香與完治世紀分別的名場面！
《HERO》木村拓哉檢察官在林蔭道漫步的片頭曲
落葉紛飛如漫天黃金雨，飄落在車把與肩膀上！

[Chorus]
(經典熱情 90 年代《突如其來的愛情》風格)
在神宮外苑淋一場黃金雨！(ラブ・ストーリーは突然に！)
三百米金黃隧道，落葉紛飛如夢似幻
東大赤門的古韻，皇居的威嚴，與外苑的浪漫
這是東京秋天獻給騎士最深情的告白！
Dancing in the golden ginkgo rain!

[Saxophone Solo]
(Passionate and expressive 90s J-Pop saxophone solo)

[Bridge]
十九天的汗水與風雨，在這一刻全部化為純金的記憶
我們騎過了高山、大海、湖泊與古鎮，如今站在繁華的頂峰。

[Chorus]
在神宮外苑淋一場黃金雨！(黄金色に輝く街！)
金秋的東京，為這趟壯遊披上最華麗的告別長袍
回到秋葉原的起點，心底湧動著滿滿的感動
明天，七百七十六公里的世界線即將圓滿閉環！

[Outro]
(Saxophone and guitar soaring together as leaves fall)
東京的秋天，謝謝你！
Arigato, Tokyo..."""
    },
    {
        "track": 19,
        "day": "Day 19 (12/01 二)",
        "title": "776公里的世界線閉環 (Closing the 776km World Line)",
        "theme": "《Love Live!》神田明神 ✕《命運石之門》閉環 ✕ 776km 完騎圓滿返台",
        "style": "Triumphant Anisong Finale, celebratory stadium rock, full brass section, soaring vocal harmonies, fast double-time chorus, emotional graduation anthem, Love Live style, 178 BPM",
        "intro_tag": "[Intro: Triumphant Brass Fanfare & Stadium Handclaps]",
        "lyrics": """[Intro]
(Epic triumphant brass fanfare with fast double-time drums)
七百七十六公里！
十九天的冒險，在今天畫下完美句點！
All riders, hands in the air!

[Verse 1]
最後一個清晨，來到江戶總鎮守神田明神
《Love Live!》μ's 少女們奔跑特訓的神社石階
在平將門命的神前深深一躬，祈求旅途平安圓滿
感恩十九天萬里無雲的恩賜，感恩一路平安的守護

[Verse 2]
回到 CycleTrip Base 秋葉原，十一點前順利還車
檢查車架、卸下陪伴十九天的馬鞍包
這台陪我征服大垂水峠、朝霧千米長下坡與冷川峠的戰友
在陽光下閃耀著光芒，辛苦了，我的夥伴！

[Pre-Chorus]
日暮里站站內專用轉乘口，刷臉進站只需一秒鐘！
京成 Skyliner 特急指定席，三十六分鐘直分成田機場
窗外飛速掠過的關東平原，一幕幕回憶如潮水湧上心頭！

[Chorus]
(終極盛大高亢《Love Live!》畢業紀念曲風)
七百七十六公里的世界線圓滿閉環！(僕らの奇跡！)
從秋葉原出發，穿過多摩川、翻越大垂水
在河口湖看見紅葉迴廊，在本棲湖遇見千圓逆富士
駿河灣的海堤、修善寺的古湯、熱海的花火與神宮外苑的銀杏
這不是夢境，是我們用雙腳寫下的壯麗史詩！
We made it! The ultimate journey is complete!

[Guitar & Brass Climax Solo]
(Massive stadium rock solo with all instruments firing in celebration)

[Bridge]
起飛的引擎在成田機場轟鳴，飛機穿透雲層
俯瞰舷窗外白雪皚皚的富士山，在陽光下向我們揮手告別。

[Chorus]
七百七十六公里的世界線圓滿閉環！(ありがとう、すべての出会い！)
滿載十九天的回憶、感動與榮耀，平安返回溫暖的家
這趟騎旅永遠不會結束，它將成為心中永恆的力量
下一次的冒險，我們路上再見！
Ride forever into the golden sky!

[Outro]
(Grand final chord, celebratory crowd cheering and fireworks echo fading)
東京・富士・伊豆 19日秋季單車騎旅
—— 完全完騎 (Mission Accomplished) ——
(Fading into silence)"""
    }
]

# Generate Master Suno AI Soundtrack HTML
html_content = f'''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>東京・富士五湖・伊豆・東京灣 19日單車騎旅 ｜ 19首 Suno AI 官方雙語音樂詞庫 (J-POP / Anime Rock / Anisong)</title>
    <style>
        :root {{
            --bg-dark: #0B0F19;
            --card-bg: #131D2F;
            --card-hover: #1E293B;
            --border: #233554;
            --text-light: #F8FAFC;
            --text-muted: #94A3B8;
            --primary: #2563EB;
            --accent: #F59E0B;
            --purple: #A855F7;
            --success: #10B981;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-light);
            line-height: 1.6;
            padding: 16px;
        }}

        .container {{
            max-width: 1280px;
            margin: 0 auto;
        }}

        header {{
            background: linear-gradient(135deg, #1E1B4B 0%, #31102E 50%, #451A03 100%);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 24px 28px;
            margin-bottom: 24px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
            box-shadow: 0 8px 24px rgba(0,0,0,0.3);
        }}

        .header-title h1 {{
            font-size: 24px;
            font-weight: 800;
            color: #FFFFFF;
            margin-bottom: 6px;
        }}

        .header-title p {{
            font-size: 14px;
            color: #CBD5E1;
        }}

        .nav-links {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }}

        .nav-btn {{
            background: rgba(255, 255, 255, 0.12);
            color: #FFFFFF;
            padding: 9px 16px;
            border-radius: 8px;
            text-decoration: none;
            font-size: 13px;
            font-weight: 700;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            border: 1px solid rgba(255, 255, 255, 0.2);
            transition: all 0.15s ease;
        }}

        .nav-btn:hover {{
            background: rgba(255, 255, 255, 0.25);
            transform: translateY(-1px);
        }}

        .nav-btn.primary {{
            background: var(--primary);
            border-color: #3B82F6;
        }}

        /* 快速導覽列 */
        .quick-nav-bar {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 12px 16px;
            margin-bottom: 24px;
            display: flex;
            gap: 8px;
            overflow-x: auto;
            white-space: nowrap;
            scrollbar-width: thin;
        }}

        .track-nav-btn {{
            background: #1E293B;
            border: 1px solid #334155;
            color: #94A3B8;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.15s ease;
        }}

        .track-nav-btn:hover {{
            background: #2563EB;
            color: #FFFFFF;
            border-color: #60A5FA;
        }}

        /* 曲目卡片 */
        .track-card {{
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 24px;
            transition: all 0.2s ease;
        }}

        .track-card:hover {{
            border-color: #3B82F6;
            box-shadow: 0 8px 24px rgba(37, 99, 235, 0.15);
        }}

        .track-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 12px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 14px;
            margin-bottom: 16px;
        }}

        .track-title-box h2 {{
            font-size: 19px;
            font-weight: 800;
            color: #F8FAFC;
            display: flex;
            align-items: center;
            gap: 8px;
        }}

        .track-badge {{
            background: #2563EB;
            color: #FFFFFF;
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 800;
        }}

        .track-day {{
            font-size: 13px;
            color: var(--accent);
            font-weight: 700;
            margin-top: 4px;
        }}

        .track-theme {{
            background: rgba(168, 85, 247, 0.1);
            border: 1px solid rgba(168, 85, 247, 0.3);
            color: #D8B4FE;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 12.5px;
            margin-bottom: 14px;
        }}

        .prompt-box {{
            background: #0F172A;
            border: 1px solid #334155;
            border-left: 4px solid var(--accent);
            border-radius: 8px;
            padding: 12px 14px;
            margin-bottom: 16px;
            position: relative;
        }}

        .prompt-header {{
            font-size: 12px;
            font-weight: 700;
            color: var(--accent);
            margin-bottom: 4px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }}

        .prompt-text {{
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 12px;
            color: #E2E8F0;
            word-break: break-all;
        }}

        .copy-btn {{
            background: #334155;
            color: #F8FAFC;
            border: none;
            padding: 4px 10px;
            border-radius: 4px;
            font-size: 11px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
        }}

        .copy-btn:hover {{
            background: #2563EB;
        }}

        .lyrics-box {{
            background: #090D16;
            border: 1px solid #1E293B;
            border-radius: 10px;
            padding: 18px;
            font-family: inherit;
            font-size: 13.5px;
            color: #CBD5E1;
            line-height: 1.7;
            white-space: pre-line;
        }}

        .lyrics-tag {{
            color: #38BDF8;
            font-weight: 700;
        }}
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="header-title">
            <h1>東京・富士五湖・伊豆・東京灣 19日秋季單車騎旅</h1>
            <p>🎵 19首 Suno AI 官方雙語音樂原聲帶詞庫 ｜ J-POP ✕ Anime Rock ✕ Anisong ✕ 影視動漫聖地巡禮</p>
        </div>
        <div class="nav-links">
            <a href="tokyo_fuji_cycling_itinerary_19days_v2.html" class="nav-btn primary">📋 返回 19日總行程表 ➔</a>
            <a href="tokyo_cycling_19days_map_demo.html" target="_blank" class="nav-btn">🗺️ 19日互動地圖 Demo ↗</a>
        </div>
    </header>

    <!-- 快速曲目跳轉列 -->
    <div class="quick-nav-bar">
'''

for t in tracks:
    html_content += f'        <a href="#track-{t["track"]}" class="track-nav-btn">T{t["track"]:02d}: Day {t["track"]}</a>\n'

html_content += '''    </div>

    <!-- 19 首曲目詳細卡片 -->
'''

for t in tracks:
    html_content += f'''    <div class="track-card" id="track-{t['track']}">
        <div class="track-header">
            <div class="track-title-box">
                <h2><span class="track-badge">Track {t['track']:02d}</span> 《{t['title']}》</h2>
                <div class="track-day">📅 {t['day']}</div>
            </div>
        </div>

        <div class="track-theme">
            🎬 <strong>影視動漫與歷史意象：</strong> {t['theme']}
        </div>

        <div class="prompt-box">
            <div class="prompt-header">
                <span>🎛️ Suno AI Style of Music (風格提示詞)</span>
                <button class="copy-btn" onclick="copyPrompt('prompt-{t['track']}')">複製風格詞</button>
            </div>
            <div class="prompt-text" id="prompt-{t['track']}">{t['style']}</div>
        </div>

        <div class="lyrics-box" id="lyrics-{t['track']}">{t['lyrics']}</div>
    </div>
'''

html_content += '''</div>

<script>
function copyPrompt(id) {
    const text = document.getElementById(id).innerText;
    navigator.clipboard.writeText(text).then(() => {
        alert("已成功複製 Suno AI 風格提示詞！可直接貼上至 Suno 創作欄。");
    });
}
</script>

</body>
</html>'''

# Write to Downloads and Workspace
with open("C:/Users/ymero/Downloads/suno_cycling_soundtrack_19days.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("d:/2026東京單車騎旅/suno_cycling_soundtrack_19days.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Master 19-Track Suno AI Soundtrack HTML successfully generated at suno_cycling_soundtrack_19days.html!")
