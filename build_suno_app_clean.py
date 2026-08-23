import json, sys

# Master self-contained builder for Suno Soundtrack with 1-click COPY for BOTH style prompt and lyrics

tracks = [
    {
        "track": 1,
        "day": "Day 1 (11/13 五)",
        "title": "世界線的起跑線 (World Line Departure)",
        "theme": "《命運石之門》✕《飆速宅男》✕《正宗哥吉拉》✕ 秋葉原出城至高尾山口",
        "style": "Upbeat J-Rock, energetic anime opening, fast driving drums, bright electric guitar riffs, synthesizer arpeggio, brass accents, Steins;Gate vibe, Japanese pop rock, 175 BPM",
        "lyrics": """[Intro]
(Synth pulse fades into roaring guitar)
El Psy Kongroo... 踏上未知的世界線！
踏板旋轉，心跳超頻，出發！
(ペダルを踏み込め、新たな世界線へ！)

[Verse 1 - 漢文]
秋葉原晨光染亮了電器街的窗
鎖定碼表歸零，跨上破風的車把
穿過銀座的喧囂，第一京濱筆直伸展
六鄉橋下，多摩川的秋芒如海浪般翻湧

[Verse 2 - 日本語]
秋葉原の朝焼け背に受けて
ペダルを踏み込めば 始まるプロローグ
多摩川の風が 頬を撫でてゆく
シン・ゴジラの足跡、丸子橋を越えて
八王子の空へ、道は続いてる

[Pre-Chorus - 雙語交織]
耳邊響起總北高校熱血的吶喊 (耳元に響く熱いエール)
拋開都會的重力，鏈條咬合未來的節奏 (未来へのリズム)
夕陽把影子拉長，高尾山林在眼前展開！
(高尾の山々が 茜色に染まる！)

[Chorus - 雙語高亢合唱]
走吧！奔向命運的世界線！(行こう！運命の世界線へ！)
多摩川的水岸，寫下騎士最初的誓言 (多摩川の岸辺に 刻む誓い)
汗水蒸發在極樂湯的露天暖湯裡 (汗を流せば 極楽の湯)
高尾山下的星空，點燃十九天的冒險！(十九日の旅が 今始まる！)
Fly into the twilight sky!

[Guitar Solo]
(Fast shredding anime guitar solo with synthesizer counterpoint)

[Bridge - 日本語]
天狗の羽扇が 秋の合図を送る
明日は大垂水峠、未知の坂道へ
車輪を回せば 広がる新しい世界！

[Chorus - 雙語熱血爆發]
走吧！奔向命運的世界線！(夢の彼方へ 駆け抜けろ！)
雙輪畫出的軌跡，是無可取代的自由 (ペダルを回せ、自由の風になれ)
這不是巧合，是命運石之門的指引 (運命の扉を 開く旅立ち)
踏動雙腳，向著大山全力前進！(明日へ向かって、全力で走れ！)

[Outro]
秋葉原到高尾山，八十九公里的序章
エル・プサイ・コングルゥ、明日も走るんだ！
(Final power chord resonating into silence)"""
    },
    {
        "track": 2,
        "day": "Day 2 (11/14 六)",
        "title": "峠道狂詩曲 (Toge Rhapsody)",
        "theme": "《頭文字D》✕《信長協奏曲》✕ 縣道35秋山隱世溪谷 ➔ 都留",
        "style": "High-energy Anime Rock, Eurobeat-inspired driving beat, screaming electric guitar solo, punchy bassline, melodic J-Rock, Initial D style, autumn canyon vibe, 168 BPM",
        "lyrics": """[Intro]
(Eurobeat synth stabs and engine revving into blazing guitar riff)
清晨八點，甲州街道！
大垂水峠，全力攻頂！
(峠を越えろ、限界の先へ！)

[Verse 1 - 漢文]
晨霧還沒散開，高尾山腳空氣冰涼
國道二十號上坡，齒比切入輕檔
平均坡度百分之五點三，心率在胸口激盪
大垂水峠標高三百九十二米，瞬間踩在腳下！

[Verse 2 - 日本語]
相模湖の青を 左手に見て
県道三十五号、秋山街道へ
大型車のない 静寂の渓谷
武田の隠し道、紅葉のトンネルを抜けて
ギアを上げて 坂道を駆け上がる

[Pre-Chorus - 雙語交織]
三十五公里幽靜緩坡，秋風送來落葉香氣 (落ち葉の香る 静かな峠)
呼吸與山溪共鳴，分水嶺就在眼前！(分水嶺のトンネル目指して)
秋山隧道標高六百七十四，衝刺！(ラストスパート、駆け上がれ！)

[Chorus - 雙語高亢合唱]
衝破重力！在峠道上狂飆！(重力を振り切れ！峠のラプソディ)
秋山溪谷的深紅，見證雙腿的燃燒 (燃える紅葉と 尽きない情熱)
穿過黑暗隧道，迎來七公里的極速長下坡！(トンネル抜ければ 七キロのダウンヒル)
滑降都留市，由加利旅館的暖燈在等待！(由加利旅館の 温もりが待つ！)
Ride through the canyon wind!

[Guitar Solo]
(Eurobeat fast melodic guitar solo with squealing pinch harmonics)

[Bridge - 日本語]
松尾芭蕉が愛した この都留の街
旅人の夢を 乗せて回る車輪
甲斐絹の風が 優しく頬を撫でる

[Chorus - 雙語熱血爆發]
衝破重力！在峠道上狂飆！(風になれ、山を越えていけ！)
從相模湖到甲斐之國，六十公里的征途 (六十キロの 誇らしき足跡)
這就是公路車的靈魂，用汗水換來的純粹 (汗と情熱が 紡ぎ出すメロディ)
明天，富士五湖在雲端召喚！(明日は富士五湖、雲の上の世界へ！)

[Outro]
都留市的夜色漸濃，由加利的榻榻米洗去征塵
静かな甲斐の夜、おやすみなさい...
(Fading acoustic guitar strum)"""
    },
    {
        "track": 3,
        "day": "Day 3 (11/15 日)",
        "title": "水鏡神域 (Mirrored Sacred Realm)",
        "theme": "《你的名字》✕《名偵探柯南》✕ 忍野八海 ✕ 雙湖見頃 ➔ 河口湖",
        "style": "Emotional Anime Pop Rock, sweeping cinematic strings, piano intro, soaring emotional vocals, RADWIMPS vibe, sparkling chimes, autumn lake breeze, 142 BPM",
        "lyrics": """[Intro]
(Melodic piano arpeggio with shimmering chime FX)
八十年的雪水，從地心湧出...
那是神明的鏡子，照映著聖山。
(時空を超えて、巡り合う奇跡の水鏡...)

[Verse 1 - 漢文]
離開都留沿著急行農路向上攀升
忍野八海清冽見底，草餅在火上烤出香氣
富士山巨大的白雪冠頂，突然穿透雲層矗立眼前
那是如同《你的名字》彗星劃過般的震撼！

[Verse 2 - 日本語]
八十年の雪解け水、湧き出る神の泉
山中湖の波間に 逆さ富士が揺れる
旭日丘の紅葉、湖畔を真っ赤に染めて
新倉山の五重塔、絵画のような絶景
風と光が 聖なる山を包み込む

[Pre-Chorus - 雙語交織]
不管晴空萬里或是薄霧輕籠 (晴れの日も、霧の朝も)
雙軌決策的每條路，都是不可思議的邂逅 (すべての道が 奇跡の出会い)
滑降富士吉田，金色鳥居直指天際！(金鳥居を抜けて、河口湖へ！)

[Chorus - 雙語高亢合唱]
神聖的水鏡，倒映著千年的容顏！(千年の祈りを 映す水鏡)
山中湖與河口湖，在秋色中交織成畫 (湖畔を彩る 黄金の秋)
今夜住在紅葉迴廊旁，Orange Cabin 的木屋 (もみじ回廊のほとり、木の温もり)
夜楓點燈如繁星墜落，夢幻的深紅隧道！(星降る夜に 輝く紅葉トンネル！)
Touch the reflection of Mt. Fuji!

[Strings & Guitar Solo]
(Cinematic emotional guitar solo with soaring orchestral strings)

[Bridge - 日本語]
富士講の祈り、今も響く古道
暖炉の火が 静かに燃えている
星空の下、富士のシルエットが浮かび上がる

[Chorus - 雙語熱血爆發]
神聖的水鏡，倒映著千年的容顏！(紅葉の輝き、心奪われて)
雙湖見頃的最盛期，我們正站在風暴的核心 (奇跡の季節を 駆け抜ける旅人)
不用趕路，靜靜聆聽湖水的低語 (湖の囁きに 耳を澄ませば)
明天，向著本棲湖的逆富士前進！(明日は本栖湖、逆さ富士の待つ場所へ！)

[Outro]
河口湖的夜楓在黑暗中閃爍如夢
おやすみ、富士の聖なる夜よ...
(Gentle piano note decaying)"""
    },
    {
        "track": 4,
        "day": "Day 4 (11/16 一)",
        "title": "千圓紙幣的晨光 (Morning Glow on the 1000-Yen Bill)",
        "theme": "《搖曳露營△ Yuru Camp》封神第一話聖地 ✕ 本棲湖浩庵逆富士",
        "style": "Acoustic Anime Pop, cheerful folk rock, acoustic guitar strumming, whistling, warm mandolin, cozy bass groove, Yuru Camp OST vibe, melodic female J-Pop, 128 BPM",
        "lyrics": """[Intro]
(Cheerful acoustic whistling and rhythmic handclaps)
La la la... 早上六點半！
在觀光客醒來前，獨享無人的紅葉迴廊！
(ふじさんと、風と、私のじてんしゃ！)

[Verse 1 - 漢文]
晨光穿透深紅楓葉灑在清涼的空氣裡
橘色木屋旁，整條迴廊只有我的車輪聲響
沿著湖北 View Line 奔馳，大石公園的湖面平靜如鏡
西湖療癒之里根場，傳統茅草屋頂在秋陽下微笑

[Verse 2 - 日本語]
精進湖のほとり、「子抱き富士」を眺めて
湖北ビューラインを 風と共に駆け抜ける
本栖湖の坂を登れば 浩庵キャンプ場
志摩リンとなでしこが 出会ったあのベンチ
千円札の裏の景色が 目の前に広がる

[Pre-Chorus - 雙語交織]
拿出錢包裡的一千日圓紙幣 (千円札を取り出して)
《湖畔之春》的奇蹟在眼前重現 (名画のような 逆さ富士の朝)
完全一模一樣！藍色水面上的倒影富士！(本栖ブルーに 映る雪の峰！)

[Chorus - 雙語高亢合唱]
晨光灑落在千圓紙幣的湖面！(千円札の富士に 朝日が差す！)
本棲湖的清風，吹散了所有的疲憊與煩惱 (本栖湖の風が 心を解き放つ)
熱騰騰的咖哩麵，配上無價的富士水鏡 (温かいカレー麺と 最高の水鏡)
這就是單車露營者的終極天堂！(ここはサイクリストの パラダイス！)
Shiny days, ride with the breeze!

[Guitar & Mandolin Solo]
(Playful acoustic solo with country folk whistling)

[Bridge - 日本語]
青木ヶ原の樹海が 静かに見守る
夕暮れの紅富士が 湖を染めてゆく
窓辺のマグカップ、温かいコーヒーを淹れて

[Chorus - 雙語熱血爆發]
晨光灑落在千圓紙幣的湖面！(ゆるやかな旅路、どこまでも行こう！)
騎過西湖與精進湖，抵達世界線的奇蹟 (湖を巡る 奇跡のストーリー)
這份安靜與感動，只屬於清晨早起的騎士 (朝焼けの光を 独り占めにして)
明天下坡一千米，向著駿河灣出發！(明日はダウンヒル、駿河湾へ飛び込もう！)

[Outro]
富士山，晚安囉！
浩庵の夜空に、満天の星が降る...
(Whistling melody fade out)"""
    },
    {
        "track": 5,
        "day": "Day 5 (11/17 二)",
        "title": "山獸神之森的休止符 (Sanctuary of the Ancient Woods)",
        "theme": "《幽靈公主》✕ 青木原原始樹海 ✕ 鳴澤冰穴 ✕ 甲州餺飥",
        "style": "Mystical Anime Ballad, ambient orchestral, cinematic Japanese flute (shinobue), taiko drum beat, warm electric piano, Princess Mononoke forest atmosphere, lush strings, 95 BPM",
        "lyrics": """[Intro]
(Atmospheric taiko drum and mystical flute melody)
貞觀六年的熔岩之上，森林沉睡了一千年...
今天不趕路，傾聽大地的呼吸。
(千年の樹海に、静かな風が吹き抜ける...)

[Verse 1 - 漢文]
青木原樹海古老的林道，覆滿深綠青苔
熔岩巨木盤根錯節，宛如宮崎駿筆下的山獸神之森
鳴澤冰穴與富岳風穴，地心深處凝結著萬年寒冰
零度的地洞裡，封存著江戶時代蠶種的記憶

[Verse 2 - 日本語]
苔むす溶岩の森、もののけの囁き
太古の息吹が 樹海を包み込む
ゆらりの湯に浸かり 富士を仰ぎ見れば
湯煙の向こうに 輝く白銀の峰
旅の疲れが ほどけて消えてゆく

[Pre-Chorus - 雙語交織]
大鐵鍋裡滾燙的甲州名物餺飥麵 (熱々のほうとう 湯気が立ち上る)
南瓜融化在濃郁味噌湯底 (かぼちゃが溶ける 味噌の甘み)
戰國武田軍團的寶刀軍糧，溫暖著騎士的心！(信玄の宝刀、温もりをありがとう)

[Chorus - 雙語高亢合唱]
在古老森林的懷抱裡，找回平靜的節奏！(太古の森で 心を整えて)
這是一段為靈魂預留的休止符 (魂を癒やす 静かな休息)
冰穴的冷冽與溫泉的暖湯，交織出高原的詩意 (氷穴の静寂と 温泉のぬくもり)
蓄滿力量，準備迎接明天的千米大滑降！(明日への力を 蓄えるんだ！)
Breathe in the ancient mountain air!

[Flute & Cello Solo]
(Emotional traditional Japanese flute dueling with cello)

[Bridge - 日本語]
止まることもまた、旅の大切な一歩
雲が晴れれば 黄金の夕富士が現れる
自然の恵みに 感謝を捧げて

[Chorus - 雙語熱血爆發]
在古老森林的懷抱裡，找回平靜的節奏！(大自然の腕に 抱かれて眠る)
五湖核心的緩衝日，讓旅程立於不敗之地 (緩やかなリズムが 力に変わる)
喝乾最後一口熱湯，整裝待發 (心も体も 満たされた今)
駿河灣的召喚，就在明日山腳下！(駿河の海が 私を呼んでいる！)

[Outro]
静かな森よ、ありがとう。駿河湾へ！
(Gentle temple bell chiming and wind fading away)"""
    },
    {
        "track": 6,
        "day": "Day 6 (11/18 三)",
        "title": "破風降臨千米疾走 (Thousand-Meter Wind Descent)",
        "theme": "《鎌倉殿的13人》✕ 朝霧高原 ✕ 白糸之瀑 ➔ 富士宮千米長下坡",
        "style": "Fast-paced Symphonic J-Rock, blazing guitar riffs, dramatic string sections, thunderous drums, triumphant anime OST, wind-rush adrenaline, 172 BPM",
        "lyrics": """[Intro]
(Wind rushing sound into epic string crescendo and double-kick drums)
海拔九百零五米，本棲湖出發！
連降八百米，千米大長下坡開始！
(千メートルの風になれ！ダウンヒル開始！)

[Verse 1 - 漢文]
穿上防風長指手套，拉緊風衣領口
朝霧高原牧場一望無際，金黃秋芒在狂風中搖曳
右手是悠閒吃草的乳牛，左手是雄偉壯麗的富士西壁
八百年前源賴朝曾在此策馬，舉辦「富士之卷狩」！

[Verse 2 - 日本語]
朝霧フードパークで 温かいミルクを飲んで
白糸の滝へ、岩肌から湧き出る清流
幅百五十メートルの 白い絹のカーテン
水しぶき浴びて、さあ下り坂の始まりだ
ブレーキを緩めて、重力と戯れる

[Pre-Chorus - 雙語交織]
時速突破四十公里，點放煞車破風飛馳！(時速四十キロ、風を切り裂いて)
潤井川河谷在腳下展開 (潤井川の谷が 広がる)
從冰封高原一路向著溫暖的駿河灣狂飆！(駿河の海へと 一気に下れ！)

[Chorus - 雙語高亢合唱]
破風疾走！一千米的高差滑降！(千メートルの風になれ！ダウンヒル！)
重力加速度在耳邊呼嘯成歌 (耳をかすめる 疾風のメロディ)
從本棲湖的冰峰，直落富士宮的市街 (本栖の山から 富士宮の街へ)
淺間大社湧玉池清泉，鐵板上熱炒著脆香炒麵！(湧玉の清流と 焼きそばの香り！)
Descending from the mountain throne!

[Guitar Solo]
(Blazing fast tapping and sweep picking guitar solo)

[Bridge - 日本語]
富士山本宮浅間大社、朱塗りの本殿
旅の安全を祈り、駿河湾の風を感じる
高原の寒さを 置き去りにして

[Chorus - 雙語熱血爆發]
破風疾走！一千米的高差滑降！(大空へ飛び立つ 鳥のように！)
告別了富士五湖的高原寒涼 (高原を後に、青い海を目指す)
駿河灣的暖風已經在前方海平線招手 (駿河の風が 優しく迎えてくれる)
這場完美的下坡，寫下壯麗的轉折章節！(最高のスリル、忘れられない疾走！)

[Outro]
富士宮市區的晚風，溫柔而溫暖
最高のダウンヒル、ありがとう！
(Ending heavy power chord)"""
    },
    {
        "track": 7,
        "day": "Day 7 (11/19 四)",
        "title": "駿河灣的蔚藍防潮堤 (Suruga Blue Sea Wall)",
        "theme": "《Love Live! Sunshine!!》✕《萬葉集》田子浦 ➔ 千本松原海堤 ➔ 沼津 ➔ 三島",
        "style": "Sparkling Anime Idol Pop Rock, energetic brass section, driving synth-pop beat, catchy chorus, ocean breeze melody, Love Live Aqours style, sunny surf vibe, 160 BPM",
        "lyrics": """[Intro]
(1-2-3-Jump! Upbeat drum roll and sunny brass!)
沼津的蔚藍大海，我們來了！
踏上海堤專用道，全力衝刺！
(輝く駿河湾へ、青空Jumping Heart！)

[Verse 1 - 漢文]
沿著潤井川平緩下坡，一路騎到田子の浦港
正如山部赤人在《萬葉集》中吟誦的名句：
「走出田子浦，抬頭望富士，皚皚白雪覆峰巔！」
浩瀚的駿河灣在眼前展開，波光粼粼萬里無雲！

[Verse 2 - 日本語]
千本松原の堤防、十五キロの専用道
信号も車もない、僕たちだけのシーサイドロード
左に広がる松林、右には青い太平洋
振り返れば 雄大な雪化粧の富士山
Aqoursの歌声が 波音に重なってゆく

[Pre-Chorus - 雙語交織]
沼津港海鮮市場，大口享用肥美深海魚海鮮丼 (沼津港で味わう 新鮮な海の幸)
現烤大帆立貝香氣撲鼻 (ホタテの香ばしい匂い)
海風撫平了疲憊，向著三島市區前進！(三島の街へ 軽やかに走る！)

[Chorus - 雙語高亢合唱]
迎著駿河灣的海風奔馳！(青空へJumping Heart！海風に乗って)
左手黑松林，右手大海洋，背後是雪白富士山 (松原と海と 白い富士の山)
平坦的海堤專用道，是單車騎士的夢幻舞台 (果てなき堤防、最高のステージ)
一路狂飆到三島，源兵衛川清泉流淌！(三島湧水、源兵衛川のせせらぎ！)
Shine bright like the ocean waves!

[Guitar & Synth Solo]
(Energetic dual solo with sunny beach synth vibe)

[Bridge - 日本語]
三嶋大社の森で、頼朝の旗揚げを想う
炭火で焼かれた うなぎの香ばしい匂い
せせらぎの街が 優しく迎えてくれる

[Chorus - 雙語熱血爆發]
迎著駿河灣的海風奔馳！(未來への扉を 開け放て！)
告別高山挑戰，迎向伊豆半島的名湯之旅 (高山を越えて、伊豆の温泉郷へ)
這是一條無拘無束的蔚藍航線 (果てしない青が 私を包み込む)
明天，狩野川自行車道在前方等待！(明日は狩野川、清流沿いの旅路へ！)

[Outro]
沼津到三島，四十公里的陽光巡航
輝く海よ、また会おう！
(Cheerful brass hit and ocean wave sound effect)"""
    },
    {
        "track": 8,
        "day": "Day 8 (11/20 五)",
        "title": "修善寺竹林幽夢 (Bamboo Dream of Shuzenji)",
        "theme": "《伊豆的舞孃》✕《月薪嬌妻》修善寺溫泉 ➔ 温泉宿 水口",
        "style": "Traditional-Modern J-Pop, shamisen fusion, gentle acoustic guitar, soft piano, nostalgic romantic melody, Hoshino Gen vibe, autumn hot spring breeze, 118 BPM",
        "lyrics": """[Intro]
(Gentle shamisen notes blending into soft acoustic guitar)
弘法大師擊碎岩石的清泉...
伊豆最古老的千年名湯。
(弘法大師の独鈷の湯、歴史が息づく温泉郷...)

[Verse 1 - 漢文]
週五午後從三島出發，避開三連休的觀光車潮
沿著清澈的狩野川自行車道逆流平緩漫騎
二十公里輕鬆短程，微風吹拂水岸秋芒
桂川兩旁的古老木造旅館，在秋楓中靜靜迎候

[Verse 2 - 日本語]
温泉宿・水口の引き戸を開けて
愛車を預け、浴衣に着替える
独鈷の湯から 立ち上る湯煙
朱塗りの桂橋、竹林の小径へ
川端康成の「伊豆の踊子」の面影を探して

[Pre-Chorus - 雙語交織]
《月薪嬌妻》新垣結衣走過的溫泉街道 (みくりと平匡が 歩いた小道)
夏目漱石在此寫下《修善寺日記》的靜謐 (漱石の日記に 綴られた静寂)
傍晚探訪虹之鄉，夜楓在燈光下如燃燒彩霞！(闇に浮かぶ 幻想の紅葉！)

[Chorus - 雙語高亢合唱]
在修善寺的竹林深處做一場幽夢！(竹林の小径で 夢を見る)
千年古湯的暖流，融化了旅途所有疲憊 (千年の名湯が 疲れを癒やす)
紅橋流水，楓葉落滿古老石階 (もみじ散る石段、紅き橋を渡り)
今夜在榻榻米上，聽著溪流聲安然入眠！(川の音を聞きながら 眠りにつく)
Dream in the autumn mist of Shuzenji.

[Shamisen & Piano Solo]
(Elegant and emotional solo blending traditional and modern styles)

[Bridge - 日本語]
提早一天抵達的明智抉擇 (一足早く訪れた静寂)
連休の喧騒を逃れた 静かな伊豆の夜
静香な煎茶を 味わいながら

[Chorus - 雙語熱血爆發]
在修善寺的竹林深處做一場幽夢！(古都の秋色に 心を染めて)
伊豆半島的心臟，洗淨鉛華的溫柔 (伊豆の温もりが 染み渡る夜)
泡一杯靜岡煎茶，感受時光慢了下來 (時の流れが ゆっくりとほどけてゆく)
明天，冷川峠在山那端靜靜等待！(明日は冷川峠、新たな峠越えへ！)

[Outro]
泡一杯靜岡煎茶，時光慢了下來
修善寺の夜よ、おやすみなさい...
(Temple bell and gentle wind chime fading)"""
    },
    {
        "track": 9,
        "day": "Day 9 (11/21 六)",
        "title": "熔岩懸崖與伊豆之瞳 (Lava Cliffs and Eye of Izu)",
        "theme": "《藍海少女！》✕《火曜懸疑劇場》斷崖 ➔ 一碧湖 ➔ 城崎海岸 ➔ KAWANA",
        "style": "Epic Progressive Anime Rock, dynamic shifts, soaring guitar solos, dramatic ocean strings, energetic drum groove, anime adventure theme, coastal breeze, 155 BPM",
        "lyrics": """[Intro]
(Dramatic ocean wave FX and roaring electric guitar)
三連休首日！果斷避開天城峠大巴車潮！
翻越冷川峠，直奔太平洋熔岩海岸！
(冷川峠を越えて、荒波の城ヶ崎へ！)

[Verse 1 - 漢文]
告別修善寺切入縣道十二號冷川峠
幽靜林蔭道上幾乎沒有觀光大巴的廢氣干擾
標高三百七十一米輕鬆翻越，穿透林間抵達「伊豆之瞳」一碧湖
十萬年前形成的火山湖，水面倒映著滿山斑斕紅葉

[Verse 2 - 日本語]
坂を下りきれば 相模湾の青い海
「あまんちゅ！」の風が 頬を通り抜ける
大室山の溶岩が 造り出した城ヶ崎
二十三メートルの 門脇吊橋を渡る
足元で砕け散る 太平洋の白波

[Pre-Chorus - 雙語交織]
這正是《火曜懸疑劇場》名偵探對決的懸崖聖地！(サスペンスドラマの 崖っぷちの決闘)
波濤洶湧的太平洋，在陽光下展現極致鈷藍 (コバルトブルーの 雄大な海原)
抵達川奈海景第一排旅舍！(海辺の宿・川奈で 潮風を聴く！)

[Chorus - 雙語高亢合唱]
在熔岩海崖與伊豆之瞳間飛馳！(荒波を越えて、伊豆の瞳へ！)
四千年的火山地質，是大自然雕刻的史詩 (四千年の溶岩が 刻む大自然の詩)
海浪拍擊著玄武岩，激盪出自由的白色水花 (波飛沫上げて 駆け抜ける海岸線)
入住海景旅舍 KAWANA，海潮聲伴隨入夢！(波の音を枕に 夢の中へ！)
Ride the edge of the Pacific Ocean!

[Guitar Solo]
(Epic neoclassical guitar solo with heavy whammy bar dives)

[Bridge - 日本語]
三浦按針が造った 日本最初の洋式帆船
僕たちのペダルも 海原を渡る船のように
風を受けて 遥かなる東海道へ

[Chorus - 雙語熱血爆發]
在熔岩海崖與伊豆之瞳間飛馳！(青い海の記憶、胸に刻んで)
完美破解連休車潮，開闢專屬的探險路線 (渋滞を避けた 賢者のルート)
從古老火山湖到壯麗海蝕崖 (湖から海崖へ、広がる絶景)
這是一場超越想像的伊豆東岸騎行！(伊豆の東海岸を 駆け抜けろ！)

[Outro]
相模灣的海浪拍打著窗櫺
太平洋の夜明けを 楽しみに待とう...
(Ocean waves fading out)"""
    },
    {
        "track": 10,
        "day": "Day 10 (11/22 日)",
        "title": "網代夕照的避風港 (Ajiro Golden Haven)",
        "theme": "《夏色奇蹟》✕ 網代風待ち港 ✕ 避開暗黑隧道 ➔ Apt南熱海",
        "style": "Relaxing City Pop, breezy guitar chords, retro 80s synth bass, smooth saxophone accent, warm sunset groove, Tatsuro Yamashita vibe, coastal seaside, 110 BPM",
        "lyrics": """[Intro]
(Groovy bassline with warm retro Rhodes piano and saxophone)
十七公里的悠閒...
避開喧囂，在網代港停下腳步。
(潮風が薫る、静かな網代の午後...)

[Verse 1 - 漢文]
離開川奈沿著相模灣海岸北上
宇佐美的金色沙灘上，衝浪客追逐著晨光的海浪
國道一百三十五號的黑暗隧道在眼前出現
果斷右轉切入網代漁港舊街，徹底避開危險黑點！

[Verse 2 - 日本語]
江戸の風待ち港、網代の古い町並み
干物の香ばしい匂いが 潮風に漂う
トンネルを避けて走る 秘密の抜け道
長浜海水浴場、白い砂浜が広がる
南熱海のアパートメント、バルコニーから海を望む

[Pre-Chorus - 雙語交織]
十七公里的短程漫騎，避開連休大塞車 (渋滞を横目に のんびりポタリング)
私人陽台推開門，整個網代灣盡收眼底 (バルコニーいっぱいに 広がる海)
金色夕陽把海面染成一片波光粼粼的琥珀色！(夕陽が海を 黄金色に染めてゆく)

[Chorus - 雙語高亢合唱]
在網代灣的夕陽裡找到避風港！(網代の入り江に 響く波の音)
慢下來的節奏，是給靈魂最好的犒賞 (ゆっくり流れる 時間の贅沢)
聽海浪輕輕拍打長浜白沙灘 (白砂に寄せる 静かな波)
在陽台上喝一杯靜岡柑橘酒，微醺的黃昏！(みかん酒を片手に 暮れゆく海を眺めよう)
Golden sunset over Ajiro Bay.

[Saxophone & Guitar Solo]
(Smooth and jazzy saxophone solo with clean chorus guitar)

[Bridge - 日本語]
松本清張の「点と線」、旅情溢れる熱海の海
僕たちは自転車で この町の優しさを知った
波音だけが 部屋を満たしてゆく

[Chorus - 雙語熱血爆發]
在網代灣的夕陽裡找到避風港！(心解き放つ 静かな入り江)
避開所有塞車煩惱，尊享無敵海景公寓 (誰にも邪魔されない 海辺の隠れ家)
海潮聲像一首永遠唱不完的催眠曲 (波の子守唄に 包まれながら)
明天，熱海海上花火在夜空中綻放！(明日は熱海の花火、夜空を焦がせ！)

[Outro]
南熱海的夜色溫柔無比
南熱海の夜、明日は花火祭り！
(Saxophone riff fading with seaside ocean breeze)"""
    },
    {
        "track": 11,
        "day": "Day 11 (11/23 一)",
        "title": "海灣夜空的最後花火 (Fireworks Over the Caldera Bay)",
        "theme": "《煙花，應該和誰看？》✕ 米津玄師 ✕ 來宮神木 ✕ guest house MARUYA",
        "style": "Grand Cinematic J-Pop Ballad, emotional piano intro, massive orchestral explosion, soaring choral harmonies, Kenshi Yonezu 'Uchiage Hanabi' style, fireworks boom effects, 130 BPM",
        "lyrics": """[Intro]
(Piano arpeggio with fireworks sparkle sound FX)
昇った花火は、横から見るか？下から見るか？
今夜，在熱海海灣的夜空下...
(パッと光って咲いた、海辺の花火...)

[Verse 1 - 漢文]
清晨從南熱海出發，沿著海岸平緩北上
走進熱海梅園，全日本最遲見頃的深紅楓葉正在燃燒
來宮神社兩千一百年大楠神木，巍峨靜立守護
繞著巨木走一圈，祈求這趟長途騎旅平安圓滿

[Verse 2 - 日本語]
午後三時、熱海銀座・MARUYAにチェックイン
レトロな商店街、自転車を預けて
サンビーチまで歩いて たったの三分
浴衣に着替えて 砂浜の特等席へ
扇形のカルデラ湾が 巨大な劇場に変わる

[Pre-Chorus - 雙語交織]
二十點二十分，倒數計時！(八時二十分、カウントダウン！)
三面環山的天然扇形海灣，化身立體音響劇院 (山々に囲まれた 天然のスタジアム)
第一發金色巨型煙火呼嘯著直衝天際！(夜空を切り裂く 大輪の花火！)

[Chorus - 雙語高亢合唱]
轟然綻放！在熱海海灣的夜空！(パッと光って咲いた！熱海の夜空に)
五彩斑斕的花火如瀑布般從天幕傾瀉而下 (降り注ぐ光の滝、響き渡る重低音)
天然山壁迴盪著震天音浪，撞擊著心跳！(山々にこだまする 歓喜のシンフォニー)
散場步行三分鐘回房，零塞車的極致奢華！(歩いて三分の宿、最高の贅沢を！)
Uchiage Hanabi lighting up the sea!

[Strings & Guitar Solo]
(Massive emotional guitar solo supported by grand cinematic orchestra)

[Bridge - 日本語]
貫一とお宮が泣いた 熱海の月夜
今夜の僕たちは 満天の花火と踊る
居酒屋で乾杯、忘れられない夜

[Chorus - 雙語熱血爆發]
轟然綻放！在熱海海灣的夜空！(夜空を染める夢、永遠の輝き)
照亮了相模灣的波浪，照亮了十一天的騎行回憶 (十一日間の旅路を 照らし出す光)
在銀座商店街的小酒館乾杯慶祝 (銀座の街角で 語り明かそう)
這是一生難忘的伊豆海上花火之夜！(一生に一度の 奇跡の花火ナイト！)

[Outro]
熱海銀座的燈火漸漸溫柔
熱海の夜に 咲いた光よ、永遠に...
明天，湘南海岸在呼喚！
(Fireworks boom echoing in distance into soft piano fading)"""
    },
    {
        "track": 12,
        "day": "Day 12 (11/24 二)",
        "title": "早雲柑橘道與湘南風 (Mandarin Groves and Shonan Breeze)",
        "theme": "《灌籃高手》流川楓公路 ✕《海街日記》✕ 縣道740柑橘道 ➔ 江之島",
        "style": "90s Classic Anime Hard Rock, crunchy overdrive electric guitars, driving baseline, anthemic WANDS/BAAD style, Slam Dunk OST vibe, sunny coastal highway, 165 BPM",
        "lyrics": """[Intro]
(90s anime rock guitar intro - BAAD style!)
熱海銀座出發！
告別伊豆，奔向湘南海岸！
(湘南の風になれ！君が好きだと叫びたい！)

[Verse 1 - 漢文]
清晨沿著國道一百三十五號北上相模灣
果斷切入神奈川縣道七百四十號柑橘景觀道
徹底避開大貨車奔馳的江之浦暗黑長隧道！
在半山腰的蜜柑果園間爬升，居高臨下俯瞰蔚藍太平洋

[Verse 2 - 日本語]
難攻不落の名城、小田原城の天守閣へ
お堀の周り、鮮やかな紅葉が揺れる
アジフライ定食で パワーをフル充電
ここからは平坦な 相模湾の道
湘南海岸の防風林、専用サイクリングロードへ

[Pre-Chorus - 雙語交織]
耳邊響起《灌籃高手》熟悉的吉他旋律 (流川が走った 海沿いのハイウェイ)
想像流川楓戴著耳機在海風中破風飛馳！(潮風を受けて スピードを上げろ！)
輪胎在柏油路上尖叫，衝刺！(ペダルを回せ、誰にも負けない！)

[Chorus - 雙語高亢合唱]
奔向湘南海岸！迎著金色海浪！(湘南の風になれ！黄金の波を目指して)
早雲柑橘道的清香，與太平洋海風交織成歌 (みかんの香りと 潮風のハーモニー)
小田原城後的六十公里坦途，全速衝刺！(小田原を越えて 江の島へまっしぐら！)
江之島海燈塔已在夕陽下閃耀！(夕陽に輝く シーキャンドルの光！)
Ride on the Shonan coastal highway!

[Guitar Solo]
(Classic 90s screaming melodic rock guitar solo)

[Bridge - 日本語]
「海街diary」の四姉妹が暮らす 極楽寺の町
僕たちはペダルを踏んで その物語をなぞる
潮風が運ぶ 懐かしい青春の香り

[Chorus - 雙語熱血爆發]
奔向湘南海岸！迎著金色海浪！(誰にも譲らない 熱い想いを乗せて)
征服了伊豆半島的所有高山峠道 (峠を越えて、平坦な海辺を突っ走れ)
在平坦的海岸防風林裡享受極速快感 (防風林を抜けて 広がる大海原)
今晚在江之島，品嚐熱騰騰吻仔魚丼！(今夜は江の島、しらす丼で乾杯だ！)

[Outro]
江之島的日落把相模灣染成一片金紅
江の島の夕陽よ、明日も晴れろ！
(Final heavy rock drum fill and guitar chord)"""
    },
    {
        "track": 13,
        "day": "Day 13 (11/25 三)",
        "title": "高校前的命運路口 (Destiny Crossing at Kamakura High)",
        "theme": "《灌籃高手》世紀平交道 ✕《倒數第二次戀愛》✕ 柏尾川綠道 ➔ 橫濱",
        "style": "Nostalgic J-Rock, melodic pop punk, ringing acoustic-electric guitar, emotional singalong chorus, ASIAN KUNG-FU GENERATION vibe, youth memories, coastal railroad, 158 BPM",
        "lyrics": """[Intro]
(Ding-ding-ding railroad bell into fast AJIKAN style guitar!)
鎌倉高校前！
綠色江之電正緩緩駛過！
(江ノ電の踏切で、僕らは出会う！)

[Verse 1 - 漢文]
清晨七點半，抵達全亞洲最著名的平交道口
碧藍大海與七里濱的浪花作為背景
彷彿看見櫻木花道背著球鞋、晴子在對面揮手
三十年的青春熱血，在這一刻與現實世界重疊！

[Verse 2 - 日本語]
長谷寺の境内で 十一面観音に手を合わせ
庭園の池に映る 深紅の紅葉を愛でる
極楽寺駅の改札、「最後から二番目の恋」
柏尾川のプロムナード、川沿いの専用道へ
信号のない平坦路、横浜へと真っ直ぐ続く

[Pre-Chorus - 雙語交織]
柏尾川專用道一路無紅綠燈向北延伸 (戸塚を抜けて みなとみらいへ)
穿過戶塚進入橫濱港未來二十一區 (横浜の風が 街へと誘う)
摩天大樓與巨型摩天輪在天際線拔地而起！(観覧車のネオンが 僕たちを迎える！)

[Chorus - 雙語高亢合唱]
在命運的平交道口向青春致敬！(運命の踏切で 青春に手を振ろう！)
江之電的鈴聲喚醒了心底不滅的熱血 (江ノ電のベルが 呼び覚ます情熱)
沿著柏尾川水岸綠道順暢滑進橫濱港 (川沿いの緑道を 滑り込む横浜の夜)
連住東京灣台場基地，免行李暢快漫騎！(お台場の拠点へ、軽やかに走れ！)
Cross the line into Yokohama's skyline!

[Guitar Solo]
(Catchy melodic indie rock guitar duel)

[Bridge - 日本語]
黒船が来航した 開港の歴史の街
鎌倉の古都から 近代の港へとペダルは進む
時代を駆け抜ける サイクリストの夢

[Chorus - 雙語熱血爆發]
在命運的平交道口向青春致敬！(未来へのリライト、新しい景色へ！)
三十公里的平坦水岸巡航，輕鬆愜意 (海と川を繋ぐ 快適なクルージング)
東京灣的海風吹散了連日的疲勞 (東京湾の風が 疲れを吹き飛ばす)
今夜在摩天輪下，為後半段的黃金篇章舉杯！(観覧車の下で、乾杯しよう！)

[Outro]
橫濱港未來的霓虹燈在海面跳躍
横浜の夜景に 乾杯しよう！
(Railroad bell chime fades into ambient city sounds)"""
    },
    {
        "track": 14,
        "day": "Day 14 (11/26 四)",
        "title": "獨角獸與彩虹之橋 (Unicorn on the Rainbow Bridge)",
        "theme": "《機動戰士鋼彈 UC》獨角獸 ✕《大搜查線》彩虹大橋 ✕ 台場水岸巡航",
        "style": "Epic Sawano-style Electronic Orchestral Rock, dramatic drop, powerful synth brass, intense heavy drums, Hiroyuki Sawano Gundam UC style, Odaiba futuristic bay, 148 BPM",
        "lyrics": """[Intro]
(Sawano-style dramatic electronic drop with epic orchestral brass)
Destruction Mode... 啟動！
在東京灣的彩虹之上破風飛翔！
(可能性の獣、レインボーブリッジを翔ける！)

[Verse 1 - 漢文]
橫濱山下公園漫步，百年銀杏落滿黃金地毯
歷史郵輪冰川丸號靜靜泊在蔚藍港灣
第一京濱平坦寬闊，輕裝無行李自由馳騁
穿越羽田水岸，切入豐洲大橋專用自行車道！

[Verse 2 - 日本語]
五メートル幅の広い道、オリンピックのウォーターフロント
目の前に広がる レインボーブリッジの雄姿
「レインボーブリッジを封鎖できません！」青島の声が響く
ダイバーシティ東京、実物大のユニコーンガンダム
デストロイモードに変形し、紅く輝くサイコフレーム

[Pre-Chorus - 雙語交織]
免行李的純粹自由，讓雙輪快如閃電 (荷物を降ろして 風のように駆け抜ける)
《戀愛世代》水晶蘋果在海風中閃爍 (クリスタルアップルの 輝く海辺)
在台場海濱公園的夕陽下，見證未來之城！(お台場の海に 沈む夕陽を見つめて)

[Chorus - 雙語高亢合唱]
跨越彩虹大橋！奔向鋼彈的誓言！(虹の橋を越えて！可能性の獣よ！)
東京灣的蔚藍天際線在眼前展開 (東京湾のスカイライン、広がる未来)
免行李的純粹自由，讓雙輪快如閃電 (解き放たれた翼で 駆け抜ける海風)
在台場海濱公園的夕陽下，見證未來之城！(ベイエリアの夜に 酔いしれるんだ！)
Unicorn awaken on Tokyo Bay!

[Guitar & Synth Solo]
(Sawano-style heavy drop with shredding electric guitar and dubstep-orchestral fusion)

[Bridge - 日本語]
幕末の台場砲台が 現代のリゾートへ
変わりゆく大都市の 海岸線を駆け抜けて
僕たちの旅も 未来へと加速する

[Chorus - 雙語熱血爆發]
跨越彩虹大橋！奔向鋼彈的誓言！(希望の光を 掴み取るために！)
三十八公里的海灣巡航，一馬平川 (快適な水辺の道、どこまでも走れ)
今晚連住東京灣水岸基地，盡情享受下町前奏 (お台場のホテルで ゆったりと寛ぎ)
明天，前往兩津勘吉的葛飾故鄉！(明日は下町、葛飾の町へ出発だ！)

[Outro]
獨角獸鋼彈頭部天線緩緩閉合
明日は下町、葛飾の町へ！
(Dramatic orchestral chord resonating into distance)"""
    },
    {
        "track": 15,
        "day": "Day 15 (11/27 五)",
        "title": "葛飾下町的昭和人情 (Shitamachi Memories of Katsushika)",
        "theme": "《烏龍派出所》兩津勘吉 ✕《男人真命苦》車寅次郎 ➔ 柴又 ➔ 金町花庵",
        "style": "Nostalgic Upbeat Shitamachi Pop, bouncy brass and accordion, energetic ska-punk rhythm, cheerful retro J-Pop, Kochikame opening vibe, lively street banter, 150 BPM",
        "lyrics": """[Intro]
(Lively Kochikame style whistle and brass stabs!)
「大家注意啦！我是葛飾區龜有公園前派出所的兩津勘吉！」
出發！前往人情味滿滿的葛飾下町！
(わしが両さんだ！葛飾へいらっしゃい！)

[Verse 1 - 漢文]
告別台場海濱，穿過葛西臨海公園
直徑一百一十七米巨大鑽石摩天輪旋轉在藍天
切入中川水岸自行車道，避開所有市區紅綠燈與車潮
河堤兩旁秋草金黃，下町清涼微風撲面而來

[Verse 2 - 日本語]
柴又帝釈天の参道、寅さんの銅像に挨拶
草だんごの甘い香りと 鰻の蒲焼き
矢切の渡し舟、江戸川をゆっくり渡る
葛飾金町・花庵にチェックイン
「自転車歓迎」の宿、二連泊の安らぎ

[Pre-Chorus - 雙語交織]
穿過純樸的昭和懷舊商店街 (昭和レトロな 商店街を抜けて)
中川的水流長又長，滿滿的下町人情 (中川の流れ、温かい昭和の人情味)
抵達葛飾金町「花庵旅舍」，官方確認可放單車！(花庵の暖簾を くぐれば笑顔が待つ！)

[Chorus - 雙語高亢合唱]
葛飾下町的昭和人情味！(葛飾ラプソディー！おいでよ亀有へ)
沒有摩天大樓的冷漠，只有居酒屋的溫暖笑聲 (ビルの谷間を離れ、温かい笑い声の中へ)
兩津的自行車又在河堤上全力狂奔 (両さんのチャリが 堤防を駆け抜ける)
入住水元公園旁的花庵，享受悠閒的下町慢活！(花庵の畳で 旅の夜を楽しもう！)
Shitamachi memories flowing with love!

[Accordion & Brass Solo]
(Jovial and bouncy ska-pop solo with laughing whistles)

[Bridge - 日本語]
「秒速五センチメートル」の踏切の音
常磐線の高架下に 焼き鳥の煙が立ち上る
路地裏の温もりが 旅人の心を包む

[Chorus - 雙語熱血爆發]
葛飾下町的昭和人情味！(人情溢れる 下町の風！)
避開市中心擁擠嘈雜，選擇水岸旁的隱世基地 (都会の喧騒を離れ、川沿いの隠れ家へ)
今晚免收行李，在下町居酒屋乾一杯生啤酒 (冷えた生ビールで 乾杯しよう)
明天輕裝出擊，江戶川水岸無重力暢騎！(明日は手ぶらで、江戸川クルージング！)

[Outro]
「阿兩！又偷懶去騎單車啦！」
明日は手ぶらで、江戸川クルージング！
(Lively brass fanfare finish!)"""
    },
    {
        "track": 16,
        "day": "Day 16 (11/28 六)",
        "title": "江戶川無重力巡航 (Zero-Gravity Cruise on Edogawa)",
        "theme": "《四月是你的謊言》水岸 ✕《烏龍派出所》江戶川巡邏 ➔ 週末輕裝巡航",
        "style": "Breezy Acoustic J-Pop, fingerstyle acoustic guitar, uplifting flute, light percussion, relaxing indie pop, weekend cycling cruise, crystal blue sky, 122 BPM",
        "lyrics": """[Intro]
(Peaceful acoustic guitar with gentle river breeze and bird chirping)
免收行李的週六早晨...
全車卸下重負，像羽毛一樣輕盈。
(荷物を降ろして、風と一体になる週末...)

[Verse 1 - 漢文]
從金町花庵旅舍出發，車架上沒有沈重的馬鞍包
切入江戶川專用自行車道，寬闊河堤一望無際
秋日澄澈的藍天倒映在平靜水面上
正如《四月是你的謊言》水岸堤防上的夕陽騎行

[Verse 2 - 日本語]
麗子と中川が 凧揚げをしたあの土手で
ギアを軽くして、ペダルを回し続ける
江戸の利根川東遷、先人の知恵が拓いた大地
流山の古い町並みで ハンドドリップの珈琲を
週末の手ぶらポタリング、贅沢な時間の贈り物

[Pre-Chorus - 雙語交織]
不用換飯店，不用趕進度 (宿を変えずに、のんびり走る)
把身心交給金黃色的河堤 (土手のススキが 風に揺れている)
這是一場與自己靈魂的輕盈對話！(心がふわりと 空へ舞い上がる！)

[Chorus - 雙語高亢合唱]
在江戶川水岸享受無重力巡航！(江戸川の風と遊ぶ 無重力クルーズ！)
沒有馬鞍包的負擔，雙輪輕快如飛 (荷物のない軽やかさ、鳥のように飛べる)
輪胎輕快地滾動，心靈如白鷺般自由飛翔 (白鷺が舞う 川面を見つめて)
今夜回到花庵連住，下町居酒屋依然溫暖！(今夜も花庵で、下町の人情に乾杯！)
Floating on the river breeze.

[Acoustic & Flute Solo]
(Breezy indie folk solo with sweet acoustic melodies)

[Bridge - 日本語]
走ることだけが旅じゃない、立ち止まることも旅なんだ
西の空が茜色に染まり、川面が金色に輝く
川沿いのベンチで 夕暮れを見送る

[Chorus - 雙語熱血爆發]
在江戶川水岸享受無重力巡航！(心軽やかに、秋の日を慈しむ)
這不是競賽，而是一場與自己的深度對話 (急ぐ必要なんてない、この瞬間を味わおう)
看著落日把江戶川染成一片金紅 (夕陽に染まる 穏やかな水辺)
明天清晨，水元公園萬棵水杉即將震撼登場！(明日は水元公園、黄金のメタセコイアへ！)

[Outro]
江戶川夕陽漸沉，晚風微涼
江戸川の夕暮れよ、ありがとう...
(Acoustic strumming slowly fading into quiet river sounds)"""
    },
    {
        "track": 17,
        "day": "Day 17 (11/29 日)",
        "title": "萬棵水杉的黃金童話 (Golden Fairy Tale of Metasequoia)",
        "theme": "《鬼滅之刃》大正淺草 ✕ 水元公園 1,800 棵水杉黃金森林見頃 ➔ 淺草",
        "style": "Ethereal Cinematic Folk Pop, acoustic guitar picking, lush cello and violin, warm choral hums, fairy-tale autumn forest, Studio Ghibli meets modern J-Pop, 116 BPM",
        "lyrics": """[Intro]
(Dreamy harp and cello arpeggio with ethereal choral humming)
清晨六點半，騎車五分鐘...
走進全東京最大的黃金森林。
(朝霧の奥に広がる、黄金色のメタセコイアの森...)

[Verse 1 - 漢文]
水元公園的薄霧還在水面上輕輕飄蕩
一千八百棵水杉巨木拔地參天，倒映在清澈水鄉
十一月底見頃最盛期，整座森林轉為濃郁的金黃與紅褐色
宛如走進北歐童話世界，美得令人屏息凝神！

[Verse 2 - 日本語]
黄金の森を抜けて 隅田川の水辺へ
雷門の赤い大提灯、浅草寺の境内へ
「鬼滅の刃」炭治郎が 鬼舞辻無惨に出会った街
仲見世通りの賑わい、人形焼きの甘い匂い
「浅草キッド」の夢が息づく フランス座の記憶

[Pre-Chorus - 雙語交織]
從童話水鄉走進江戶最繁華的大正古剎 (水郷の静寂から 浅草の熱気へ)
仲見世通飄著現烤煎餅的香氣 (香ばしい煎餅の 懐かしい香り)
東京深秋的魔幻穿越在眼前展開！(時空を超えた 東京の秋の物語！)

[Chorus - 雙語高亢合唱]
萬棵水杉織就的黃金童話！(メタセコイアの森、黄金のファンタジー！)
晨霧中的金黃紅褐，是東京最深沉的秘境 (朝霧に浮かぶ 紅褐色の巨木たち)
從靜謐水鄉騎進繁華古剎淺草雷門 (静かな森から 雷門の大提灯へ)
一場跨越童話與歷史的奇幻巡禮！(歴史と夢が 交差するステージ！)
Golden forest whispering in the morning mist!

[Violin & Cello Solo]
(Sweeping emotional string solo filled with autumn nostalgia)

[Bridge - 日本語]
隅田川の水上バスが ゆっくりと波を立てる
スカイツリーが 夕陽を浴びてそびえ立つ
大都市の真ん中に息づく 下町の心

[Chorus - 雙語熱血爆發]
萬棵水杉織就的黃金童話！(黄金の光に 包まれた一日)
十六公里的短程漫騎，沉浸在深秋的畫卷中 (のんびり走る 贅沢な東京ポタリング)
明天，東京金秋的最高潮——神宮外苑與東大銀杏 (明日は神宮外苑、黄金のイチョウ並木へ！)
即將為這趟騎旅寫下最輝煌的篇章！(旅のフィナーレが、輝きを放つ！)

[Outro]
淺草寺的暮鐘在夜空中悠揚迴盪
明日はいよいよ、神宮外苑の銀杏並木へ！
(Temple bell resonating into peaceful silence)"""
    },
    {
        "track": 18,
        "day": "Day 18 (11/30 一)",
        "title": "神宮外苑的黃金雨 (Golden Rain at Jingu Gaien)",
        "theme": "《東京愛情故事》莉香名場面 ✕《東大特訓班》赤門 ✕ 神宮外苑銀杏大道",
        "style": "Iconic 90s J-Pop Anthem, shimmering chorus guitar, expressive saxophone solo, passionate emotional melody, Kazumasa Oda / Love Story wa Totsuzen ni vibe, golden falling leaves, 124 BPM",
        "lyrics": """[Intro]
(Legendary 90s J-Pop piano chords and electric guitar hook)
何から伝えればいいのか...
在神宮外苑的黃金雨中，與東京相遇！
(君に逢えて 本当によかった...)

[Verse 1 - 漢文]
東京大學本鄉校區，加賀藩赤門古樸莊嚴
《東大特訓班》阿部寬熱血激勵的百年學府
安田講堂前，參天巨大銀杏樹鋪滿厚厚黃金地毯
每一步踩在落葉上，都發出金秋清脆的沙沙聲

[Verse 2 - 日本語]
皇居のお堀を巡り、二重橋を眺めて
明治神宮外苑、三百メートルの黄金トンネルへ
百四十六本のイチョウが 空を黄色に埋め尽くす
「東京ラブストーリー」リカとカンチが別れた場所
「HERO」の久利生公平が 歩いた並木道

[Pre-Chorus - 雙語交織]
落葉紛飛如漫天黃金雨，飄落在車把與肩膀上 (舞い散るイチョウの葉、黄金のシャワー)
十九天的汗水在此刻化為純金的記憶！(十九日間の記憶が、黄金に輝く！)
這座城市正在展現它最浪漫的容顏！(東京がくれた 最高のフィナーレ！)

[Chorus - 雙語高亢合唱]
在神宮外苑淋一場黃金雨！(ラブ・ストーリーは突然に！神宮外苑の黄金雨)
三百米金黃隧道，落葉紛飛如夢似幻 (黄色いトンネルを 駆け抜ける喜び)
東大赤門的古韻，皇居的威嚴，與外苑的浪漫 (赤門の歴史と 外苑のロマンス)
這是東京秋天獻給騎士最深情的告白！(東京の秋がくれた 最高のプレゼント！)
Dancing in the golden ginkgo rain!

[Saxophone Solo]
(Passionate and expressive 90s J-Pop saxophone solo)

[Bridge - 日本語]
高山を越え、海を渡り、ついにここまで走ってきた
十九日間のすべての道が ここに繋がっていた
秋葉原のスタート地点が 僕たちを待っている

[Chorus - 雙語熱血爆發]
在神宮外苑淋一場黃金雨！(黄金色に輝く 奇跡の並木道！)
金秋的東京，為這趟壯遊披上最華麗的告別長袍 (最高の想い出を 胸に焼き付けて)
回到秋葉原的起點，心底湧動著滿滿的感動 (ペダルを止めて、空を見上げれば)
明天，七百七十六公里的世界線即將圓滿閉環！(明日はゴール、世界線を繋ぐんだ！)

[Outro]
東京的秋天，謝謝你！
ありがとう、黄金色に輝く東京よ...
(Saxophone and guitar soaring together as leaves fall)"""
    },
    {
        "track": 19,
        "day": "Day 19 (12/01 二)",
        "title": "776公里的世界線閉環 (Closing the 776km World Line)",
        "theme": "《Love Live!》神田明神 ✕《命運石之門》閉環 ✕ 776km 完騎圓滿返台",
        "style": "Triumphant Anisong Finale, celebratory stadium rock, full brass section, soaring vocal harmonies, fast double-time chorus, emotional graduation anthem, Love Live style, 178 BPM",
        "lyrics": """[Intro]
(Epic triumphant brass fanfare with fast double-time drums)
七百七十六公里！
十九天的冒險，在今天畫下完美句點！
All riders, hands in the air!
(僕らの奇跡！七百七十六キロ、完全完騎！)

[Verse 1 - 漢文]
最後一個清晨，來到江戶總鎮守神田明神
《Love Live!》μ's 少女們奔跑特訓的神社石階
在平將門命的神前深深一躬，祈求平安圓滿
感恩十九天萬里無雲的恩賜，感恩一路平安的守護

[Verse 2 - 日本語]
サイクル・トリップ・ベースへ、無事に愛車を返却
大垂水峠、朝霧の坂、冷川峠を越えた相棒
ありがとう、お疲れ様と フレームを撫でる
日暮里駅から スカイライナーに顔認証で乗車
わずか三十六分、成田空港へと列車は走る

[Pre-Chorus - 雙語交織]
窗外飛速掠過的關東平原，回憶如潮水湧上心頭 (車窓を流れる 関東平野の景色)
京成 Skyliner 載著滿滿的回憶 (思い出を乗せて 駆け抜ける特急)
七百七十六公里的軌跡，在今天畫下句點！(七百七十六キロの 奇跡のプロローグ！)

[Chorus - 雙語高亢合唱]
七百七十六公里的世界線圓滿閉環！(僕らの奇跡！七百七十六キロの世界線)
從秋葉原出發，穿過多摩川、翻越大垂水 (秋葉原から 多摩川、大垂水を越えて)
在河口湖看見紅葉，在本棲湖遇見逆富士 (河口湖の紅葉、本栖湖の逆さ富士)
駿河灣的海堤、修善寺的古湯、熱海的花火與外苑的銀杏 (花火と温泉と 黄金の銀杏並木！)
這不是夢境，是我們用雙腳寫下的壯麗史詩！(僕たちが走った、輝く日々の物語！)
We made it! The ultimate journey is complete!

[Guitar & Brass Climax Solo]
(Massive stadium rock solo with all instruments firing in celebration)

[Bridge - 日本語]
成田の滑走路、飛び立つ翼の窓から
白い富士山が「またおいで」と手を振っている
心の中に 永遠に消えない炎を灯して

[Chorus - 雙語熱血爆發]
七百七十六公里的世界線圓滿閉環！(ありがとう、すべての出会いと道に！)
滿載十九天的回憶、感動與榮耀，平安返回溫暖的家 (たくさんの想い出を 抱きしめて帰ろう)
這趟騎旅永遠不會結束，它將成為心中永恆的力量 (この旅は終わらない、心の中で輝き続ける)
下一次的冒險，我們路上再見！(次の冒險へ、またいつか逢う日まで！)
Ride forever into the golden sky!

[Outro]
東京・富士・伊豆 19日秋季單車騎旅 —— 完全完騎！
(Mission Accomplished - Complete!)
ありがとう、すべての出会いと道に。また会う日まで！
(Grand final chord, celebratory crowd cheering and fireworks echo fading)"""
    }
]

# Generate master HTML
html_content = '''<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>東京・富士五湖・伊豆・東京灣 19日單車騎旅 ｜ 19首 Suno AI 官方台日雙語全量音樂詞庫 (50:50 中日平衡版・一鍵複製)</title>
    <style>
        :root {
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
        }

        * {
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }

        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
            background-color: var(--bg-dark);
            color: var(--text-light);
            line-height: 1.6;
            padding: 16px;
        }

        .container {
            max-width: 1280px;
            margin: 0 auto;
        }

        header {
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
        }

        .header-title h1 {
            font-size: 24px;
            font-weight: 800;
            color: #FFFFFF;
            margin-bottom: 6px;
        }

        .header-title p {
            font-size: 14px;
            color: #CBD5E1;
        }

        .nav-links {
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
        }

        .nav-btn {
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
        }

        .nav-btn:hover {
            background: rgba(255, 255, 255, 0.25);
            transform: translateY(-1px);
        }

        .nav-btn.primary {
            background: var(--primary);
            border-color: #3B82F6;
        }

        .quick-nav-bar {
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
        }

        .track-nav-btn {
            background: #1E293B;
            border: 1px solid #334155;
            color: #94A3B8;
            padding: 6px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            text-decoration: none;
            transition: all 0.15s ease;
        }

        .track-nav-btn:hover {
            background: #2563EB;
            color: #FFFFFF;
            border-color: #60A5FA;
        }

        .track-card {
            background: var(--card-bg);
            border: 1px solid var(--border);
            border-radius: 16px;
            padding: 22px;
            margin-bottom: 24px;
            transition: all 0.2s ease;
        }

        .track-card:hover {
            border-color: #3B82F6;
            box-shadow: 0 8px 24px rgba(37, 99, 235, 0.15);
        }

        .track-header {
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 12px;
            border-bottom: 1px solid var(--border);
            padding-bottom: 14px;
            margin-bottom: 16px;
        }

        .track-title-box h2 {
            font-size: 19px;
            font-weight: 800;
            color: #F8FAFC;
            display: flex;
            align-items: center;
            gap: 8px;
        }

        .track-badge {
            background: #2563EB;
            color: #FFFFFF;
            padding: 3px 8px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 800;
        }

        .track-day {
            font-size: 13px;
            color: var(--accent);
            font-weight: 700;
            margin-top: 4px;
        }

        .track-theme {
            background: rgba(168, 85, 247, 0.1);
            border: 1px solid rgba(168, 85, 247, 0.3);
            color: #D8B4FE;
            padding: 8px 12px;
            border-radius: 8px;
            font-size: 12.5px;
            margin-bottom: 14px;
        }

        .prompt-box {
            background: #0F172A;
            border: 1px solid #334155;
            border-left: 4px solid var(--accent);
            border-radius: 8px;
            padding: 12px 14px;
            margin-bottom: 16px;
            position: relative;
        }

        .prompt-header {
            font-size: 12px;
            font-weight: 700;
            color: var(--accent);
            margin-bottom: 6px;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }

        .prompt-text {
            font-family: ui-monospace, SFMono-Regular, Menlo, Monaco, Consolas, monospace;
            font-size: 12px;
            color: #E2E8F0;
            word-break: break-all;
        }

        .copy-btn {
            background: #334155;
            color: #F8FAFC;
            border: 1px solid #475569;
            padding: 6px 14px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 700;
            cursor: pointer;
            transition: all 0.15s ease;
            display: inline-flex;
            align-items: center;
            gap: 6px;
        }

        .copy-btn:hover {
            background: #2563EB;
            border-color: #3B82F6;
            transform: translateY(-1px);
        }

        .copy-lyrics-btn {
            background: #0284C7;
            border-color: #38BDF8;
            color: #FFFFFF;
        }

        .copy-lyrics-btn:hover {
            background: #0369A1;
            border-color: #7DD3FC;
        }

        .lyrics-section {
            margin-top: 14px;
        }

        .lyrics-header {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }

        .lyrics-header-title {
            font-size: 13.5px;
            font-weight: 700;
            color: #38BDF8;
            display: flex;
            align-items: center;
            gap: 6px;
        }

        .lyrics-box {
            background: #090D16;
            border: 1px solid #1E293B;
            border-radius: 10px;
            padding: 18px;
            font-family: inherit;
            font-size: 13.5px;
            color: #CBD5E1;
            line-height: 1.75;
            white-space: pre-line;
        }

        .toast {
            position: fixed;
            bottom: 24px;
            right: 24px;
            background: #10B981;
            color: #FFFFFF;
            padding: 14px 22px;
            border-radius: 8px;
            font-size: 14.5px;
            font-weight: 700;
            box-shadow: 0 8px 24px rgba(0,0,0,0.5);
            display: none;
            z-index: 9999;
        }
    </style>
</head>
<body>

<div class="container">
    <header>
        <div class="header-title">
            <h1>東京・富士五湖・伊豆・東京灣 19日秋季單車騎旅</h1>
            <p>🎵 19首 Suno AI 官方雙語音樂詞庫 ｜ 50:50 中日平衡版 ✕ 一鍵複製提示詞與全曲歌詞 ✕ J-POP ✕ Anime Rock</p>
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
    track_no = t["track"]
    html_content += f'        <a href="#track-{track_no}" class="track-nav-btn">T{track_no:02d}: Day {track_no}</a>\n'

html_content += '''    </div>

    <!-- 19 首曲目詳細卡片 (含風格提示詞與歌詞一鍵複製) -->
'''

for t in tracks:
    track_no = t["track"]
    title = t["title"]
    day = t["day"]
    theme = t["theme"]
    style = t["style"]
    lyrics = t["lyrics"]

    html_content += f'''    <div class="track-card" id="track-{track_no}">
        <div class="track-header">
            <div class="track-title-box">
                <h2><span class="track-badge">Track {track_no:02d}</span> 《{title}》</h2>
                <div class="track-day">📅 {day}</div>
            </div>
        </div>

        <div class="track-theme">
            🎬 <strong>影視動漫與歷史意象：</strong> {theme}
        </div>

        <div class="prompt-box">
            <div class="prompt-header">
                <span>🎛️ Suno AI Style of Music (風格提示詞)</span>
                <button class="copy-btn" onclick="copyText('prompt-{track_no}', this)">📋 複製風格提示詞</button>
            </div>
            <div class="prompt-text" id="prompt-{track_no}">{style}</div>
        </div>

        <div class="lyrics-section">
            <div class="lyrics-header">
                <span class="lyrics-header-title">📜 Suno AI 雙語結構化歌詞 (Lyrics - 可直接貼上創作)</span>
                <button class="copy-btn copy-lyrics-btn" onclick="copyText('lyrics-{track_no}', this)">📋 複製全曲歌詞</button>
            </div>
            <div class="lyrics-box" id="lyrics-{track_no}">{lyrics}</div>
        </div>
    </div>
'''

html_content += '''</div>

<div id="toast" class="toast"></div>

<script>
function copyText(elementId, btnElement) {
    const text = document.getElementById(elementId).innerText;
    navigator.clipboard.writeText(text).then(() => {
        const originalText = btnElement.innerText;
        btnElement.innerText = "✅ 已複製！";
        btnElement.style.background = "#10B981";
        btnElement.style.borderColor = "#34D399";
        
        showToast(elementId.startsWith('prompt') ? "🎵 已成功複製風格提示詞 (Style Prompt)！" : "📜 已成功複製全曲雙語歌詞 (Lyrics)！");

        setTimeout(() => {
            btnElement.innerText = originalText;
            btnElement.style.background = "";
            btnElement.style.borderColor = "";
        }, 2000);
    });
}

function showToast(msg) {
    let toast = document.getElementById('toast');
    if (!toast) {
        toast = document.createElement('div');
        toast.id = 'toast';
        toast.className = 'toast';
        document.body.appendChild(toast);
    }
    toast.innerText = msg;
    toast.style.display = 'block';
    setTimeout(() => {
        toast.style.display = 'none';
    }, 2500);
}
</script>

</body>
</html>'''

with open("C:/Users/ymero/Downloads/suno_cycling_soundtrack_19days.html", "w", encoding="utf-8") as f:
    f.write(html_content)

with open("d:/2026東京單車騎旅/suno_cycling_soundtrack_19days.html", "w", encoding="utf-8") as f:
    f.write(html_content)

print("Master 19-Track Suno Soundtrack rebuilt successfully with 1-click COPY for BOTH style prompt and lyrics!")
