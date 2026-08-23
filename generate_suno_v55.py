import sys, json

# Define the 19 tracks with Suno v5.5 standard metadata
tracks_v55 = [
    {
        "day": 1,
        "date": "11/13 (五)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "世界線の起点：逆流する多摩川の風 (跨越世界線的啟程)",
        "title_en": "Starting Line: Cross the Worldline on Tama River",
        "vibe": "J-Rock Duet / 172 BPM / E Major",
        "anime": "《命運石之門 Steins;Gate》（秋葉原 Radio會館、世界線跳躍）、《飆速宅男》",
        "drama": "《悠長假期》《求婚大作戰》（多摩川堤防夕陽奔跑名場面）",
        "history": "德川家康開創「六鄉渡口」東海道出城門戶；鎌倉倒幕傳奇「分倍河原之戰」",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Mature, Warm, Resonant) & 30yo Japanese Female Soprano (Sweet, Clear, Energetic Anime Style)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: J-Rock, Energetic Anime Opening, Tokyo City Pop]
[Tempo: 172 BPM]
[Key: E Major]
[Instrumentation: Distorted Electric Guitar Riffs, Driving Bassline, Punchy Rock Drums, Bright Synth Arpeggios]
[Mood: Triumphant, Nostalgic, Energetic, Adventurous]
[Production: Modern High Fidelity, Dynamic Vocal Separation, Wide Stereo Field, Crisp Master]""",
        "lyrics": """[Intro: Fast drum roll, energetic guitar riff, retro synth arpeggios]
[Voice: Female Vocal - Japanese]
El Psy Kongroo...
新しい世界線が、いま動き出す！

[Verse 1: Male Lead - Mandarin Chinese]
跨上單車 轉動四十歲沈澱的齒輪
離開秋葉原霓虹 逃離日常的喧囂與圍困
踩過銀座的晨光 第一京濱寬廣的路塵
這不是逃避 是一場蓄謀已久的追尋

[Verse 1: Female Lead - Japanese]
六郷橋を渡れば 目の前に広がる水面
ビル街のノイズを 背中に振り切って
信号のない一本道 多摩川の風が吹く
迷いはすべて この川に置いてゆこう

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 像日劇長假裡的夕陽 奔跑在河堤之上
[Voice: Female Vocal - Japanese] 『ロングバケーション』の空が 私たちを照らしている
[Voice: Male Vocal - Mandarin] 鏈條咬合的聲音 唱著不服輸的倔強
[Voice: Female Vocal - Japanese] ペダルを踏み込んで、未来へ！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
多摩川の風を裂いて 逆流のペダルを回せ！
(破開多摩川的逆風 踩下滾燙的車輪)
止まらない鼓動が叫ぶ 僕たちのプロローグ
(停不下來的心跳 宣告著旅程的序章)
[Voice: Male Lead - Mandarin] 沿著德川家康開創的古道 逆流而上！
[Voice: Female Lead - Japanese] どこまでも遠く、どこまでも熱く！
[Voice: Duet / Harmony]
世界線を変えるスピードで 駆け抜けろ！
(用改變世界線的速度 奔向遠方！)

[Verse 2: Male Lead - Mandarin Chinese]
經過二子玉川 漸漸染紅的深大寺林木
分倍河原古戰場 彷彿聽見鎌倉武士的征途
汗水滑過臉頰 呼吸與心跳同步
這條五十公里的起點 是給自己的禮物

[Verse 2: Female Lead - Japanese]
夕暮れの調布の空 富士の影がうっすら揺れる
スプロケットが刻む 確かな二人のリズム
「諦めたら そこでレースは終わりだよ」
風の中に聴こえる 懐かしいエール

[Instrumental Break: Melodic Electric Guitar Solo]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 歲月磨平了棱角 卻磨不滅眼裡的星火
[Voice: Female Vocal - Japanese] 坂道の向こうに、新しい明日の光がある
[Voice: Duet / Harmony]
握緊發燙的車把 向著遠方的山巒 繼續破風！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
多摩川の風を裂いて 逆流のペダルを回せ！
(破開多摩川的逆風 踩下滾燙的車輪)
止まらない鼓動が叫ぶ 僕たちのプロローグ
(停不下來的心跳 宣告著旅程的序章)
[Voice: Male Lead - Mandarin] 沿著德川家康開創的古道 逆流而上！
[Voice: Female Lead - Japanese] どこまでも遠く、どこまでも熱く！
[Voice: Duet / Harmony]
世界線を変えるスピードで 駆け抜けろ！
(用改變世界線的速度 奔向遠方！)

[Outro: Soft Vocal Ad-lib & Guitar Outro]
[Voice: Female Vocal - Japanese] 高尾山の麓、Base Camp の灯り
[Voice: Male Vocal - Mandarin] 泡進極樂湯溫泉 第一天七十八公里順利抵達
[Voice: Duet / Harmony]
Day One Complete, Mt. Takao Base Camp...
[End]"""
    },
    {
        "day": 2,
        "date": "11/14 (六)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "誠の風、秋山街道の静寂 (誠字風骨・秋山靜谷)",
        "title_en": "The Wind of Makoto: Silence of Akiyama Highway",
        "vibe": "Shamisen Rock Duet / 155 BPM / D Minor",
        "anime": "《Persona 5》（八王子轉運站）、《搖曳露營△》（山梨林道出發）",
        "drama": "《孤獨的美食家》（高尾山名物蕎麥麵與山間茶屋的療癒）",
        "history": "新選組副長土方歲三故鄉（天然理心流日野宿）；武田信玄重臣小山田氏谷村城",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Gritty, Resonant, Heroic) & 30yo Japanese Female Vocal (Crisp, High Energy Rock Soprano)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Melodic J-Rock, Shamisen Rock Fusion, Anime Battle OST]
[Tempo: 155 BPM]
[Key: D Minor]
[Instrumentation: Traditional Shamisen Solo, Heavy Distortion Guitar, Punchy Slap Bass, Epic Taiko & Rock Drums]
[Mood: Dramatic, Honorable, Focused, Energetic]
[Production: High Definition Dynamic Mixing, Cinematic Soundstage, Tight Punchy Low End]""",
        "lyrics": """[Intro: Sharp shamisen solo melody, exploding into heavy rock rhythm with taiko drums]
[Voice: Female Vocal - Japanese]
誠の旗を掲げて、峠の向こうへ！

[Verse 1: Male Lead - Mandarin Chinese]
告別城市的平坦 淺川水聲推著前輪向前
八王子的老街裡 藏著天然理心流的刀劍
避開國道轟鳴的大車 尋找一條幽靜的生路
土方歲三的誠字旗 彷彿在山風中獵獵作響

[Verse 1: Female Lead - Japanese]
津久井湖の波紋が 静かに鏡のように揺れる
県道三十五号の木漏れ日 山が深く抱きしめる
大垂水の喧騒を 鮮やかにかわして
孤独なサイクリストを 迎える秋の谷間

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 鏈條切換至最大飛輪 汗水滴在冷涼的柏油路
[Voice: Female Vocal - Japanese] 坂道は苦しみじゃない、魂を研ぎ澄ます砥石！
[Voice: Male Vocal - Mandarin] 像孤獨的美食家 在山間茶屋喝一口甘洌的清泉
[Voice: Female Vocal - Japanese] 一歩ずつ、峠の頂へ！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
秋山街道の谷間を 誇り高く駆け抜けろ！
(在秋山街道的幽谷中 驕傲地破風前行！)
[Voice: Male Lead - Mandarin] 爬坡不是逞強 而是與中年自我的和解
[Voice: Female Lead - Japanese] 武田の騎馬隊が駆けた、甲斐の山並みへ！
[Voice: Duet / Harmony]
ギアを落とし 呼吸を整え 限界のその先へ！
(變換齒比 調勻呼吸 踏破極限的彼方！)

[Verse 2: Male Lead - Mandarin Chinese]
谷村城的古老石階 記錄著武田氏最後的殘陽
兩側深秋的山林 染上了金黃與赭紅的盛裝
六百米的累積爬升 雙腿發酸卻無比滾燙
四十歲男人的浪漫 就在這無人打擾的深谷道旁

[Verse 2: Female Lead - Japanese]
都留の街の灯りが 夕暮れの中に近づく
冷たい秋風が ほてった頬を優しく撫でる
静寂の中で見つけた 自分だけの誇り
誰も邪魔できない、二人の冒険路

[Instrumental Break: Shamisen and Electric Guitar Battle Duet]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 不走大路 才能看見最澄澈的風景
[Voice: Female Vocal - Japanese] 険しい坂を越えた者だけが、本当の自由を知る
[Voice: Duet / Harmony]
踏み抜いたペダルの重さだけ 明日の僕らは強くなる！
(踏過踏板的每一次沈重 都將化作明天的堅強！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
秋山街道の谷間を 誇り高く駆け抜けろ！
(在秋山街道的幽谷中 驕傲地破風前行！)
[Voice: Male Lead - Mandarin] 爬坡不是逞強 而是與中年自我的和解
[Voice: Female Lead - Japanese] 武田の騎馬隊が駆けた、甲斐の山並みへ！
[Voice: Duet / Harmony]
ギアを落とし 呼吸を整え 限界のその先へ！
(變換齒比 調勻呼吸 踏破極限的彼方！)

[Outro: Shamisen Outro Phrase & Fade]
[Voice: Male Vocal - Mandarin] 翻越大垂水與秋山 抵達由加利旅館的溫暖
[Voice: Female Vocal - Japanese] 都留の町、由加利旅館で乾杯！
[Voice: Duet / Harmony]
(Shamisen outro phrase trailing into peaceful night wind)
[End]"""
    },
    {
        "day": 3,
        "date": "11/15 (日)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "神宿る金鳥居：千メートルの夕焼け (金鳥居的晚霞・千米靈峰)",
        "title_en": "The Golden Torii: Sunset at 1000 Meters",
        "vibe": "Epic Synth-Rock Duet / 140 BPM / G Major",
        "anime": "《搖曳露營△》（山中湖夕陽露營、溫泉煮麵）",
        "drama": "《First Love 初戀》（富士山下的命中註定回憶）",
        "history": "江戶時代平民信仰「富士講」；富士吉田金鳥居靈山結界",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Emotive, Cinematic, Warm) & 30yo Japanese Female Soprano (Pure, Ethereal, Inspiring)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Epic J-Pop, Atmospheric Synth-Rock, Cinematic Soundtrack]
[Tempo: 140 BPM]
[Key: G Major]
[Instrumentation: Grand Acoustic Piano Intro, Sweeping Symphonic Strings, Ambient Synth Pads, Distant Train Bell FX]
[Mood: Majestic, Emotional, Awe-Inspiring, Uplifting]
[Production: Expansive Reverb, Stadium Scale Soundstage, Crystal Clear Vocal Air]""",
        "lyrics": """[Intro: Gentle acoustic piano solo, distant train bell, atmospheric synth swelling]
[Voice: Female Vocal - Japanese]
富士の神様、どうか私たちの旅を見守って...

[Verse 1: Male Lead - Mandarin Chinese]
沿著富士急行線 騎進桂川旁的鄉間小路
避開大車的喧囂 伴著清泉一路平緩爬升
穿過富士吉田老街 抬頭看見巍峨的金鳥居
江戶時代富士講的朝聖者 也曾在這裡仰望神靈

[Verse 1: Female Lead - Japanese]
富士吉田の金鳥居をくぐれば 空が近くなる
標高千メートルの冷気が 白い息に変わる
『First Love』の記憶のように 突然現れた霊峰
雪を戴いた白い冠が 夕日に輝いている

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 氣溫降到十度以下 穿上防風外套拉緊拉鍊
[Voice: Female Vocal - Japanese] 志摩リンが焚き火を灯した 山中湖の渚へ
[Voice: Male Vocal - Mandarin] 疲憊的雙腿 在看見富士山頂那一刻融化
[Voice: Female Vocal - Japanese] 見てごらん、これが私たちの登ってきた道！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
夕焼けの渚 山中湖が紅に染まりゆく！
(夕陽照耀的湖渚 山中湖正燃燒著晚霞！)
[Voice: Male Lead - Mandarin] 踩著厚厚的落葉紅毯 抵達海拔一千米的高原
[Voice: Female Lead - Japanese] 富士の峰が茜色の光を浴びて微笑む
[Voice: Duet / Harmony]
初恋の温もりを抱きしめて 天空の湖へ！
(擁抱初戀般的溫熱 抵達這天空之湖！)

[Verse 2: Male Lead - Mandarin Chinese]
湖畔的露營場 飄來熱湯與柴火的香氣
像《搖曳露營》裡的悠閒 煮一碗熱騰騰的麵條
夕陽把湖水染成了深邃的金紅
所有的辛苦 都在這面水鏡前得到了補償

[Verse 2: Female Lead - Japanese]
波音が静かに 湖畔の紅葉を揺らしている
星空がゆっくりと 天空から降りてくるころ
言葉はいらない ただ静寂に寄り添って
二つの車輪が描いた軌跡を 噛みしめる

[Instrumental Break: Sweeping Orchestral Strings & Ambient Piano]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 經歷了前半生的風雨 才能讀懂這座靈山的沉靜
[Voice: Female Vocal - Japanese] 登りきった者だけが出逢える、圧倒的な奇跡
[Voice: Duet / Harmony]
この冷たい空気の中で、心はずっと熱いまま！
(在這冰涼的高原空氣中 內心卻無比熾熱！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
夕焼けの渚 山中湖が紅に染まりゆく！
(夕陽照耀的湖渚 山中湖正燃燒著晚霞！)
[Voice: Male Lead - Mandarin] 踩著厚厚的落葉紅毯 抵達海拔一千米的高原
[Voice: Female Lead - Japanese] 富士の峰が茜色の光を浴びて微笑む
[Voice: Duet / Harmony]
初恋の温もりを抱きしめて 天空の湖へ！
(擁抱初戀般的溫熱 抵達這天空之湖！)

[Outro: Soft Piano Trailing into Wind]
[Voice: Female Vocal - Japanese] 河口湖北岸、Orange Cabin の温もり
[Voice: Male Vocal - Mandarin] 紅葉迴廊旁的木屋 今夜在富士山下安眠
[Voice: Duet / Harmony]
Good night, Orange Cabin and Mt. Fuji...
[End]"""
    },
    {
        "day": 4,
        "date": "11/16 (一)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "紅葉回廊のシンフォニー (楓葉迴廊的交響詩)",
        "title_en": "Symphony of the Momiji Corridor",
        "vibe": "Orchestral J-Pop Duet / 125 BPM / C# Minor",
        "anime": "《名偵探柯南：往天國的倒數計時》（富士五湖雙塔倒影）、《搖曳露營△》",
        "drama": "《silent》（湖畔靜謐而深情的深秋手語獨白）",
        "history": "忍野八海——數百年火山熔岩過濾之神之湧泉，修驗道聖地",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Deep, Gentle, Tender) & 30yo Japanese Female Soprano (Crystal Clear, Poignant, Melodic)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Emotional Piano Ballad, Orchestral J-Pop, J-Drama Soundtrack]
[Tempo: 125 BPM]
[Key: C# Minor]
[Instrumentation: Solo Concert Violin, Grand Piano, Fingerpicked Acoustic Guitar, Lush String Orchestra]
[Mood: Poignant, Romantic, Breathtaking, Majestic]
[Production: Warm Studio Master, Intimate Vocal Presence, Rich String Harmonics]""",
        "lyrics": """[Intro: Tender solo piano melody, falling leaves sound FX, expressive solo violin]
[Voice: Female Vocal - Japanese]
言葉にできない想い、紅葉の風に乗せて...

[Verse 1: Male Lead - Mandarin Chinese]
清晨走過忍野八海 泉水澄澈得像一眼望穿千年
八百年的雪融伏流 在池底悄悄訴說著時間
轉動踏板騎上湖北 View Line
微涼的湖風 拂過河口湖平靜的岸邊

[Verse 1: Female Lead - Japanese]
湖北ビューラインを 滑るように走る朝
湖面を渡る風が 黄金の秋を連れてくる
『silent』の静けさのように 声を出さなくても
紅葉の回廊が 心の奥を優しく満たす

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 六百株古木楓樹 在今天迎來了最盛期
[Voice: Female Vocal - Japanese] 深紅に燃え盛るトンネル 空を覆い尽くしてゆく
[Voice: Male Vocal - Mandarin] 不需要多餘的言語 手指觸碰飄落的紅葉
[Voice: Female Vocal - Japanese] この一瞬を、ずっと忘れないで

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
もみじ回廊！ 燃え盛る光のトンネルを抜けて！
(穿過紅葉迴廊 漫天燃燒的光之隧道！)
[Voice: Male Lead - Mandarin] 紅與金的落葉 在車輪旁飛舞如花雨
[Voice: Female Lead - Japanese] 今日この日、満開の見頃に出逢えた奇跡
[Voice: Duet / Harmony]
息を呑むほどの深紅の中で 愛の言葉を奏でよう！
(在屏息凝神的深紅之中 奏響愛的交響詩！)

[Verse 2: Male Lead - Mandarin Chinese]
大石公園的岸邊 掃帚草染上了成熟的酒紅
湖面倒映著完美的富士 像柯南電影裡的終極謎題
停下單車 坐在長椅上喝一口熱咖啡
這份深秋的奢侈 治癒了中年所有的疲憊

[Verse 2: Female Lead - Japanese]
湖面に揺れる 逆さ富士のシルエット
落ち葉が車輪に触れて カサリと音を立てる
旅はまだ続くけれど 今日のこの景色は
私たちの心に 永遠の宝物になる

[Instrumental Break: Soaring Solo Violin & Piano Duet]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 如果秋天是一首詩 這裡就是最動人的副歌
[Voice: Female Vocal - Japanese] 赤く染まる夜のライトアップ、夢のような光の海
[Voice: Duet / Harmony]
ペダルを止めて、ただこの美しさに抱かれよう
(停下踏板 靜靜沉醉在這份極致的美麗中)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
もみじ回廊！ 燃え盛る光のトンネルを抜けて！
(穿過紅葉迴廊 漫天燃燒的光之隧道！)
[Voice: Male Lead - Mandarin] 紅與金的落葉 在車輪旁飛舞如花雨
[Voice: Female Lead - Japanese] 今日この日、満開の見頃に出逢えた奇跡
[Voice: Duet / Harmony]
息を呑むほどの深紅の中で 愛の言葉を奏でよう！
(在屏息凝神的深紅之中 奏響愛的交響詩！)

[Outro: Violin and Piano Duet Softly Fading]
[Voice: Female Vocal - Japanese] 夜の回廊に灯る赤い光、Orange Cabin 連泊の贅沢
[Voice: Male Vocal - Mandarin] 免收行李的第二晚，河口湖紅葉迴廊，晚安
[Voice: Duet / Harmony]
(Violin and piano trailing off into serene lake silence)
[End]"""
    },
    {
        "day": 5,
        "date": "11/17 (二)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "湖畔の休息：青木ヶ原と癒しの里 (湖畔休整・樹海與療癒之里)",
        "title_en": "Lakeside Rest: Aoki Forest & Healing Village",
        "vibe": "Chillhop Lo-Fi Duet / 110 BPM / F Major",
        "anime": "《搖曳露營△》第一集浩庵露營場逆富士、《蟲師》（青木原樹海生命之息）",
        "drama": "《在世界中心呼喊愛》《四重奏》（深山湖畔的隱逸詩意）",
        "history": "西元864年「貞觀大噴發」熔岩分開古代剗之海；岡田紅陽「湖畔之春」千圓逆富士",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Laid-Back, Warm, Contemplative) & 30yo Japanese Female Vocal (Airy, Cozy, Dreamy Indie Tone)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Chillhop, Dreamy Indie Pop, Lo-Fi Guitar Lounge]
[Tempo: 110 BPM]
[Key: F Major]
[Instrumentation: Clean Electric Guitar Chords, Fender Rhodes, Lo-Fi Vinyl Crackle, Mellow Flute, Relaxed Hip-Hop Drums]
[Mood: Relaxing, Nostalgic, Serene, Reflective]
[Production: Warm Analog Tape Saturation, Intimate Close-Mic Vocals, Lush Spatial Stereo]""",
        "lyrics": """[Intro: Vinyl crackle, warm jazzy guitar chords, relaxed acoustic beat]
[Voice: Male Vocal - Mandarin] 拿出皮夾裡的千圓紙幣...
[Voice: Female Vocal - Japanese] あの青い湖畔へ、行こう...

[Verse 1: Male Lead - Mandarin Chinese]
穿過西湖療癒之里的茅草屋頂
貞觀大噴發的古老熔岩 孕育了青木原樹海的寂靜
像《蟲師》走過的靈山小徑 遠離主幹道的車流
車胎碾過金黃松針 奏出節奏舒適的迴響

[Verse 1: Female Lead - Japanese]
精進湖の畔で出逢う 『子抱き富士』の優しさ
小さな山を抱きしめる 静かなシルエット
千年の歴史が育んだ 蒼い四つの湖
風が木々を揺らし 旅人の心を洗ってゆく

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 來到本棲湖浩庵營地 拿出千圓紙幣對齊地平線
[Voice: Female Vocal - Japanese] お札の裏側の景色が、いま目の前に広がっている
[Voice: Male Vocal - Mandarin] 泡一碗熱騰騰的咖哩泡麵 撫慰微涼的指尖
[Voice: Female Vocal - Japanese] 志摩リンと撫子が出逢った、あの朝のように

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
浩庵の湖畔に広がる 完璧な逆さ富士！
(浩庵湖畔展開的 完美無瑕的逆富士！)
[Voice: Male Lead - Mandarin] 平靜如鏡的藍色水面 倒映著雪白的富士冠頂
[Voice: Female Lead - Japanese] 波ひとつない蒼い鏡、千円札の奇跡！
[Voice: Duet / Harmony]
世界の中心で 自然がくれた詩を聴いている
(在世界中心 聆聽大自然寫下的詩行)

[Verse 2: Male Lead - Mandarin Chinese]
湖北岸的起伏坡道 像《四重奏》般優雅悠揚
沒有趕路的焦慮 只有齒輪與湖水的合唱
四十歲的旅行 不再追求速度與里程
而是把這份純粹的孤獨 釀成一壺陳年佳釀

[Verse 2: Female Lead - Japanese]
観光客の消えた夕暮れ 本棲湖の深い青
富士山と私たちだけの 贅沢な時間が流れる
タイヤが刻んだ四十九キロ 穏やかな達成感
心の中に広がる、あたたかな余韻

[Instrumental Break: Lo-Fi Mellow Guitar & Rhodes Solo]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 這張千圓紙幣上的風景 今天變成了永恆的記憶
[Voice: Female Vocal - Japanese] 溶岩の森を抜けて、私たちは自由になった
[Voice: Duet / Harmony]
静けさこそが、いちばん贅沢なご馳走
(這份靜謐 才是旅程中最奢華的盛宴)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
浩庵の湖畔に広がる 完璧な逆さ富士！
(浩庵湖畔展開的 完美無瑕的逆富士！)
[Voice: Male Lead - Mandarin] 平靜如鏡的藍色水面 倒映著雪白的富士冠頂
[Voice: Female Lead - Japanese] 波ひとつない蒼い鏡、千円札の奇跡！
[Voice: Duet / Harmony]
世界の中心で 自然がくれた詩を聴いている
(在世界中心 聆聽大自然寫下的詩行)

[Outro: Lo-Fi Guitar Riff & Fading Synth Chime]
[Voice: Female Vocal - Japanese] 藍色に暮れゆく本棲湖
[Voice: Male Vocal - Mandarin] 逆富士的倒影，收進心底
[Voice: Duet / Harmony]
(Guitar riff fading out with vinyl hiss)
[End]"""
    },
    {
        "day": 6,
        "date": "11/18 (三)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "千円札の蒼い鏡：朝霧高原ダウンヒル (千圓逆富士・朝霧高原俯衝之章)",
        "title_en": "Thousand-Yen Mirror: Asagiri Plateau Downhill",
        "vibe": "Japanese City Pop Duet / 118 BPM / A Major",
        "anime": "《你的名字。》（時空交錯鳥居）、《進擊的巨人》（孤傲俯瞰視角）",
        "drama": "《First Love 初戀》（富士吉田本町通巨大富士街景）、《重啟人生》",
        "history": "新倉山淺間公園忠靈塔；富士吉田傳承數百年「甲斐絹」織物宿場文化",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Smooth, Relaxed, Soulful) & 30yo Japanese Female Vocal (Breezy, Sweet, Stylish 80s City Pop Diva)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Japanese City Pop, Funk Groove, Shibuya-Kei]
[Tempo: 118 BPM]
[Key: A Major]
[Instrumentation: Smooth Alto Saxophone, Funky Slap Bass, Fender Rhodes Piano, Crisp Rhythmic Electric Guitar]
[Mood: Sunny, Carefree, Sophisticated, Relaxed]
[Production: Crisp Studio Master, Punchy Bass Groove, Silky Vocal Shimmer]""",
        "lyrics": """[Intro: Funky slap bass groove, bright electric piano chords, silky smooth saxophone]
[Voice: Female Vocal - Japanese]
今日はペダルをお休みして、のんびり歩こう！

[Verse 1: Male Lead - Mandarin Chinese]
踩上三百九十八階石梯 今天把單車停在山下
不趕路的日子 腳步變得輕快而悠然
登上新倉山頂 轉身的那一個瞬間
全世界最經典的明信片 在眼前化作真實

[Verse 1: Female Lead - Japanese]
朱塗りの五重塔と 燃え盛る紅葉のグラデーション
背後にそびえ立つ 堂々たる白い富士山
『First Love』の本町通りを 見下ろせば
昭和レトロな街並みが 映画のように広がっている

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 走進老街咖啡館 喝一杯手沖熱咖啡
[Voice: Female Vocal - Japanese] 甲斐絹の機織りの音が、どこか懐かしく響く
[Voice: Male Vocal - Mandarin] 檢查煞車皮與鏈條油 準備明天的長下坡
[Voice: Female Vocal - Japanese] シャッターを切るたび、笑顔がこぼれる

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
シャッターを切るたび 永遠になる秋の午後！
(每次按下快門 這秋日午後便化作永恆！)
[Voice: Male Lead - Mandarin] 急著奔跑的半生 在這裡學會了停下腳步
[Voice: Female Lead - Japanese] 急がない旅だから、見つけられた宝物
[Voice: Duet / Harmony]
五重塔と紅葉富士 最高のご褒美ホリデー！
(五重塔與紅葉富士 最棒的犒賞假期！)

[Verse 2: Male Lead - Mandarin Chinese]
河口湖南岸漫步 陽光灑在微波粼粼的湖面
微風吹落幾片紅葉 落在中年男人的肩頭
給自己一天的留白 感受肌肉的放鬆與沉澱
明天要從一千米高原 直衝駿河灣的蔚藍海邊

[Verse 2: Female Lead - Japanese]
テラス席でおしゃべり 甘いアップルパイの香り
休養日があるから 長い旅はもっと輝く
夕暮れの本町通り 街灯が優しく灯るころ
明日へのエネルギーが 胸いっぱいに満ちてゆく

[Instrumental Break: Searing Silky Saxophone Solo & Funky Guitar]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 完美的旅行 需要汗水也需要這杯咖啡的香氣
[Voice: Female Vocal - Japanese] 富士山に見守られて、心のリセットボタンを押す
[Voice: Duet / Harmony]
明日は駿河湾へ！ 風になる準備はできたかい？
(明天奔向駿河灣！你準備好化作一陣風了嗎？)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
シャッターを切るたび 永遠になる秋の午後！
(每次按下快門 這秋日午後便化作永恆！)
[Voice: Male Lead - Mandarin] 急著奔跑的半生 在這裡學會了停下腳步
[Voice: Female Lead - Japanese] 急がない旅だから、見つけられた宝物
[Voice: Duet / Harmony]
五重塔と紅葉富士 最高のご褒美ホリデー！
(五重塔與紅葉富士 最棒的犒賞假期！)

[Outro: Saxophone Trailing off into City Lights]
[Voice: Female Vocal - Japanese] 富士吉田の夜に、乾杯！
[Voice: Male Vocal - Mandarin] 充飽電，明天出發！
[Voice: Duet / Harmony]
(Saxophone solo smoothly fading out)
[End]"""
    },
    {
        "day": 7,
        "date": "11/19 (四)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "標高差一千メートルの風：駿河湾へダイブ！ (千米落差俯衝・直奔駿河灣)",
        "title_en": "A Thousand Meters Descent: Dive into Suruga Bay",
        "vibe": "Surf Rock Duet / 168 BPM / D Major",
        "anime": "《Love Live! Sunshine!!》（Aqours沼津港、千本松原海堤）、《銀之匙》",
        "drama": "《義經》（大河劇瀧澤秀明主演，源賴朝與義經富士野大卷狩）",
        "history": "1193年源賴朝富士之卷狩與曾我兄弟復仇；德川家康還願之淺間大社總本社",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Excited, Husky Rock Tone, Shouting Hook) & 30yo Japanese Female Vocal (High-Energy Anime Idol Soprano)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: High-Energy Surf Rock, Upbeat J-Pop, Anime Action Theme]
[Tempo: 168 BPM]
[Key: D Major]
[Instrumentation: Surf Rock Tremolo Guitar, Punchy Horn Fanfare, Fast Acoustic Strumming, Thunderous Rock Drums]
[Mood: Exhilarating, Triumphant, Fast-Paced, Celebratory]
[Production: Punchy High Voltage Master, Bright Open Cymbals, Dynamic Stereo Panning]""",
        "lyrics": """[Intro: Fast acoustic guitar strumming, soaring trumpet fanfare, countdown: 3, 2, 1, GO!]
[Voice: Female Vocal - Japanese]
標高一千メートルから、海へ飛び込めーー！

[Verse 1: Male Lead - Mandarin Chinese]
清晨朝霧高原 氣溫只有冰涼的兩度
穿齊防風手套與風衣 展開十八公里的自由落體！
重力拉著車輪飛馳 標高指針一路狂跌
風在耳邊尖嘯 像飛鳥掠過鳴澤的林野

[Verse 1: Female Lead - Japanese]
白糸の滝の水しぶきが 紅葉を鮮やかに濡らす
源頼朝が狩りをした 富士の巻狩りの古戦場
浅間大社の湧玉池で 旅の安全を祈ったら
潤井川のサイクリングロードを 海へ一直線！

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 避開危險的國道一號 駛進田子之浦港
[Voice: Female Vocal - Japanese] 千本松原の堤防ロード、車が一台もいない！
[Voice: Male Vocal - Mandarin] 專用海堤筆直展開 駿河灣的潮香撲鼻而來
[Voice: Female Vocal - Japanese] Aqoursの風を感じて、沼津へ突っ走れ！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
標高差一千メートル！ 駿河湾の海風へダイブ！
(標高差一千公尺！一頭躍入駿河灣的海風！)
[Voice: Male Lead - Mandarin] 右手是無垠的太平洋 回頭依然是巍峨的富士山！
[Voice: Female Lead - Japanese] 振り返れば、圧倒的な雪富士が見守っている！
[Voice: Duet / Harmony]
海堤專用道上的狂飆 這是屬於我們的黃金路線！
(海堤専用ロードの疾走、最高のゴールデンルート！)

[Verse 2: Male Lead - Mandarin Chinese]
在沼津港大口吃下 新鮮美味的生魚片海鮮丼
從高原的寒冬 瞬間切換到伊豆溫暖的陽光
千本黑松在海風中搖曳 擋住沙塵與喧囂
這就是單車旅行 才能體會的極致落差與震撼

[Verse 2: Female Lead - Japanese]
『Love Live! Sunshine!!』の 聖地の風が吹く
港の賑わいと カモメたちの白い翼
三島へ向かう平坦路 ペダルが羽のように軽い
山から海へ繋いだ 七十二キロの凱旋！

[Instrumental Break: Wild Surf Rock Tremolo Guitar Solo & Brass Riffs]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 幾小時前還在雪山腳下 現在已經擁抱大海
[Voice: Female Vocal - Japanese] 標高差千メートルの風を、二本の足で駆け抜けた
[Voice: Duet / Harmony]
これだから単車旅は、やめられない！
(正因如此 單車旅行才讓人如此著迷！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
標高差一千メートル！ 駿河湾の海風へダイブ！
(標高差一千公尺！一頭躍入駿河灣的海風！)
[Voice: Male Lead - Mandarin] 右手是無垠的太平洋 回頭依然是巍峨的富士山！
[Voice: Female Lead - Japanese] 振り返れば、圧倒的な雪富士が見守っている！
[Voice: Duet / Harmony]
海堤專用道上的狂飆 這是屬於我們的黃金路線！
(海堤専用ロードの疾走、最高のゴールデンルート！)

[Outro: Surf Guitar Tremolo Finish]
[Voice: Female Vocal - Japanese] 三島大社に響く、夕暮れの鐘
[Voice: Male Vocal - Mandarin] 從雪山到大海，完美達成！
[Voice: Duet / Harmony]
(Brass and guitar crash finish)
[End]"""
    },
    {
        "day": 8,
        "date": "11/20 (五)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "逃げ恥の足音：修善寺・竹林の小径 (月薪嬌妻的足音・修善寺竹林)",
        "title_en": "Footsteps of Escape: Shuzenji Bamboo Path",
        "vibe": "Japanese Jazz-Pop Duet / 115 BPM / B Minor",
        "anime": "《夏目友人帳》（名湯竹林與妖怪和風物語）",
        "drama": "《月薪嬌妻 / 逃避雖可恥但有用》（新垣結衣與星野源蜜月溫泉之旅修善寺桂橋）",
        "history": "西元807年弘法大師空海開山獨鈷之湯；鎌倉二代將軍源賴家幽禁修禪寺物語",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Warm, Gentle, Intimate Crooner) & 30yo Japanese Female Vocal (Whispering, Sweet, Elegant Japanese Onsen Tone)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Modern Japanese Enka-Pop Fusion, Lo-Fi Jazz Lounge, Traditional Folk]
[Tempo: 115 BPM]
[Key: B Minor]
[Instrumentation: Shakuhachi Bamboo Flute, Plucked Shamisen, Upright Double Bass, Gentle Flowing Stream FX]
[Mood: Romantic, Soothing, Cozy, Peaceful]
[Production: Natural Acoustic Warmth, Intimate Vocal Proximity, Organic Stereo Reverb]""",
        "lyrics": """[Intro: Gentle river sound, bamboo flute melody, soothing electric piano chords]
[Voice: Female Vocal - Japanese]
赤い橋を渡れば、恋の足音がする...

[Verse 1: Male Lead - Mandarin Chinese]
沿著狩野川自行車專用道 悠閒平緩地巡航
二十公里的輕鬆路程 穿過伊豆之國的田庄
三島出發一個半小時 便抵達伊豆最古老的名湯
把單車靠在溫泉旅館前 卸下一身行囊

[Verse 1: Female Lead - Japanese]
桂川にかかる 朱塗りの桂橋
『逃げるは恥だが役に立つ』の 二人のように
少し照れながら でも確かに手をつないで
竹林の小径の丸いベンチに 腰を下ろす

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 弘法大師擊出的獨鈷之湯 升起千年的白霧蒸氣
[Voice: Female Vocal - Japanese] 修禅寺の鐘の音が、静かに秋の山に染みわたる
[Voice: Male Vocal - Mandarin] 朱紅色的拱橋 映襯著兩側深紅的楓葉與翠竹
[Voice: Female Vocal - Japanese] 疲れた脚を名湯に沈めて、ふぅっとため息

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
修善寺温泉 紅葉が湯煙に揺れている！
(修善寺溫泉 紅葉在溫泉白煙中搖曳！)
[Voice: Male Lead - Mandarin] 換上日式浴衣 走在石疊街道的黃昏
[Voice: Female Lead - Japanese] 虹の郷の紅葉が、雅やかな夜を連れてくる
[Voice: Duet / Harmony]
恋する古湯のぬくもり 今夜は夢の中へ溶けてゆこう
(墜入戀愛的名湯溫熱 今夜就融化在夢鄉之中)

[Verse 2: Male Lead - Mandarin Chinese]
源賴家的哀愁歷史 如今都化作溫柔的秋色
吃一盤現磨的山葵冰淇淋 辛香中帶著清甜
三連休前夕的溫泉街 安靜得只聽見溪水流淌
這就是中年男人 最嚮往的避世安寧

[Verse 2: Female Lead - Japanese]
竹の葉が風にささやく 『夏目友人帳』の森のように
優しい妖怪たちが どこかで見守っているのかな
浴衣の袖を揺らして 温泉街の灯篭を巡る
心までぽかぽかに温まる、贅沢な夜

[Instrumental Break: Shakuhachi and Shamisen Melodic Interlude]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 逃避雖可恥但有用 暫時逃離現實又何妨
[Voice: Female Vocal - Japanese] 休むことは弱さじゃない、明日をもっと愛するため
[Voice: Duet / Harmony]
名湯に身体を預けて、深い眠りへ
(將身心託付給溫泉 沉入甜美的夢鄉)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
修善寺温泉 紅葉が湯煙に揺れている！
(修善寺溫泉 紅葉在溫泉白煙中搖曳！)
[Voice: Male Lead - Mandarin] 換上日式浴衣 走在石疊街道的黃昏
[Voice: Female Lead - Japanese] 虹の郷の紅葉が、雅やかな夜を連れてくる
[Voice: Duet / Harmony]
恋する古湯のぬくもり 今夜は夢の中へ溶けてゆこう
(墜入戀愛的名湯溫熱 今夜就融化在夢鄉之中)

[Outro: River Sound FX and Shakuhachi Fade]
[Voice: Female Vocal - Japanese] 川のせせらぎ、おやすみなさい
[Voice: Male Vocal - Mandarin] 修善寺的溫泉夜，晚安
[Voice: Duet / Harmony]
(Bamboo flute softly trailing into water sound)
[End]"""
    },
    {
        "day": 9,
        "date": "11/21 (六)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "火曜サスペンスの断崖：城ヶ崎の白波 (懸疑劇場斷崖・城崎驚濤)",
        "title_en": "Suspense Cliff: The White Waves of Jogasaki",
        "vibe": "Symphonic Rock Duet / 148 BPM / C Minor",
        "anime": "《名偵探柯南》（崖邊真相大白名場面）、《藍海少女！Amanchu!》",
        "drama": "《火曜懸疑劇場》（國民懸疑劇聖地——門脇吊橋與懸崖最後自白）、《華麗一族》",
        "history": "4000年前大室山火山噴發熔岩海岸柱狀節理；川端康成《伊豆的舞孃》漫步之道",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Intense, Dramatic, Powerful) & 30yo Japanese Female Rock Soprano (Soaring, Theatrical, Gothic Drama)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Dramatic Symphonic Rock, Mystery Anime Soundtrack, Gothic Rock]
[Tempo: 148 BPM]
[Key: C Minor]
[Instrumentation: Heavy Distortion Guitar Riffs, Grand Symphonic Strings, Church Organ, Crashing Ocean Waves FX]
[Mood: Suspenseful, Dramatic, Fierce, Epic]
[Production: Wall-of-Sound Production, Heavy Orchestral Dynamics, Crystal Highs]""",
        "lyrics": """[Intro: Crashing ocean waves, suspenseful orchestral strings, dramatic heavy guitar chord]
[Voice: Female Vocal - Japanese]
犯人は... この断崖の向こうにいる！

[Verse 1: Male Lead - Mandarin Chinese]
翻過冷川峠的幽靜九十九拐
避開天城峠的險峻 將爬升鎖定在五百米之內
一碧湖被稱為伊豆之瞳 湖面平靜如鏡
倒映著深紅水杉 隨後空氣漸漸透出大海的鹹味

[Verse 1: Female Lead - Japanese]
四千年前 大室山の溶岩が海へ流れ込み
造り出した溶岩の芸術 門脇埼灯台
サスペンス劇場のラストシーンのように
白い怒濤が 黒い絶壁に激しく牙を剥く

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 走上二十三米高的門脇吊橋 腳下是翻騰的太平洋
[Voice: Female Vocal - Japanese] 火曜サスペンスの音楽が、頭の中で鳴り響く！
[Voice: Male Vocal - Mandarin] 像柯南在懸崖邊揭開真相 所有的線索在此交匯
[Voice: Female Vocal - Japanese] 真実はいつもひとつ！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
城ヶ崎の吊橋を 渡れば足がすくむ！
(踏上城崎海岸的吊橋 腳下不禁陣陣發麻！)
[Voice: Male Lead - Mandarin] 驚濤駭浪拍打著四千年熔岩 怒吼著大自然的力量
[Voice: Female Lead - Japanese] 犯人の告白を呑み込むような、轟音の白波！
[Voice: Duet / Harmony]
越過山嶺來到海之涯 這是屬於勇敢者的冒險！
(山を越え海へ辿り着いた、勇者たちのアドベンチャー！)

[Verse 2: Male Lead - Mandarin Chinese]
《藍海少女》裡那片蔚藍的伊東海岸
三連休的車陣被單車甩在身後
海風呼嘯著吹過頭盔 帶走所有的疲憊
四十歲的胸膛 依然跳動著冒險的野心

[Verse 2: Female Lead - Japanese]
夕日が水平線に 沈んでゆく瞬間
断崖の溶岩が 黄金色に輝きだす
川端康成が歩いた 伊豆の旅路
海と山が織りなす 壮大なクライマックス

[Instrumental Break: Epic Symphonic Strings & Searing Guitar Solo]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 在懸崖的邊緣 才能看清大海真正的壯闊
[Voice: Female Vocal - Japanese] 恐れを乗り越えた先に、言葉のない感動がある
[Voice: Duet / Harmony]
太平洋の風を胸いっぱいに吸い込んで！
(把太平洋的浩瀚海風 深深吸入胸膛！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
城ヶ崎の吊橋を 渡れば足がすくむ！
(踏上城崎海岸的吊橋 腳下不禁陣陣發麻！)
[Voice: Male Lead - Mandarin] 驚濤駭浪拍打著四千年熔岩 怒吼著大自然的力量
[Voice: Female Lead - Japanese] 犯人の告白を呑み込むような、轟音の白波！
[Voice: Duet / Harmony]
越過山嶺來到海之涯 這是屬於勇敢者的冒險！
(山を越え海へ辿り着いた、勇者たちのアドベンチャー！)

[Outro: Heavy Guitar Riffs over Crashing Waves]
[Voice: Female Vocal - Japanese] 門脇灯台の光が、夜の海を照らす
[Voice: Male Vocal - Mandarin] 城崎海岸的浪聲，今夜不休
[Voice: Duet / Harmony]
(Heavy guitar chord ringing out over ocean waves)
[End]"""
    },
    {
        "day": 10,
        "date": "11/22 (日)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "熱海月夜：日本一遅い紅葉と金色夜叉 (熱海月夜・最遲紅葉與金色夜叉)",
        "title_en": "Atami Moonlight: The Late Foliage and Golden Demon",
        "vibe": "80s Synth-Wave Duet / 120 BPM / Bb Major",
        "anime": "《狂賭之淵》《蠟筆小新：溫泉青春大決戰》",
        "drama": "《熱海的搜查官》（小田切讓奇幻探案）、《長假》（木村拓哉）",
        "history": "明治尾崎紅葉《金色夜叉》貫一宮之松訣別；德川家康命人快遞熱海溫泉水至江戶",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Smooth, Retro Crooner, Warm) & 30yo Japanese Female Vocal (Sensual, Melancholic 80s City Pop Diva)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: 80s Japanese City Pop, Nostalgic Synth-Wave, Midnight Lounge]
[Tempo: 120 BPM]
[Key: Bb Major]
[Instrumentation: Soulful Muted Trumpet Solo, Analog Synthesizer Pads, Slap Bass, 80s Drum Machine]
[Mood: Nostalgic, Romantic, Melancholic, Retro]
[Production: Vintage Reverb, Silky Vocal Blend, Warm Analog Master]""",
        "lyrics": """[Intro: Nostalgic synth pads, groovy 80s drum beat, soulful muted trumpet solo]
[Voice: Female Vocal - Japanese]
今夜の月は、私たちの涙で曇らせない...

[Verse 1: Male Lead - Mandarin Chinese]
清晨七點半早早出發 避開觀光的大車潮
在網代市區果斷拐進 幽靜的生活舊街道
漁船靜靜泊在港灣 避開了幽暗狹窄的長隧道
海風吹過三十公里的波浪起伏 順利抵達熱海的海邊

[Verse 1: Female Lead - Japanese]
お宮の松の前に立てば 貫一の叫びが聴こえる
金色夜叉の哀愁を 潮騒が優しく包み込む
熱海サンビーチのヤシの木 ネオンが揺れる夕暮れ
昭和のロマンが息づく 温泉の港町

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 走進熱海梅園 迎來全日本最遲的紅葉祭
[Voice: Female Vocal - Japanese] 深紅のモミジと 早咲きの白梅が手をつなぐ奇跡
[Voice: Male Vocal - Mandarin] 德川家康曾用木桶快遞這溫泉到江戶城
[Voice: Female Vocal - Japanese] 浴衣に着替えて、昭和の路地裏を歩こう

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
熱海梅園 日本で一番遅い紅葉が咲き誇る！
(熱海梅園 全日本最遲的紅葉正燦爛綻放！)
[Voice: Male Lead - Mandarin] 穿過危險隧道的騎士 在溫泉熱氣中慶祝勝利
[Voice: Female Lead - Japanese] さよならの涙さえ 恋しくなる熱海の月夜
[Voice: Duet / Harmony]
昭和のネオンに照らされて 二人の夜曲を歌おう！
(在昭和霓虹映照下 唱響屬於我們的夜曲！)

[Verse 2: Male Lead - Mandarin Chinese]
如果不願冒險 還有JR伊東線兩鐵輪行的備案
聰明地避開危險 才是成熟旅人的最高哲學
湯前神社的古老源泉 升騰起滾燙的白煙
吃一口現蒸的溫泉饅頭 甜意融化在舌尖

[Verse 2: Female Lead - Japanese]
『熱海の捜査官』のように 不思議な魅力あふれる街
海岸通りのムーンロードが 海面に金色の道を描く
三連休の賑わいの中 二人の自転車が休んでいる
旅の半分を越えて、心はますます通い合う

[Instrumental Break: Muted Trumpet & Jazzy Guitar Duet]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 貫一與宮的眼淚 已隨時代遠去
[Voice: Female Vocal - Japanese] 今夜の月は、私たちの笑顔を照らしている
[Voice: Duet / Harmony]
熱海の夜風よ、この幸せを運んでおくれ
(熱海的夜風啊 請把這份幸福帶向遠方)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
熱海梅園 日本で一番遅い紅葉が咲き誇る！
(熱海梅園 全日本最遲的紅葉正燦爛綻放！)
[Voice: Male Lead - Mandarin] 穿過危險隧道的騎士 在溫泉熱氣中慶祝勝利
[Voice: Female Lead - Japanese] さよならの涙さえ 恋しくなる熱海の月夜
[Voice: Duet / Harmony]
昭和のネオンに照らされて 二人の夜曲を歌おう！
(在昭和霓虹映照下 唱響屬於我們的夜曲！)

[Outro: Muted Trumpet Trailing Over Ocean Moonroad]
[Voice: Female Vocal - Japanese] 南熱海の長浜海岸、波の音が優しい
[Voice: Male Vocal - Mandarin] Apt南熱海的海景公寓，今夜安眠
[Voice: Duet / Harmony]
(Trumpet solo fading out softly over quiet waves)
[End]"""
    },
    {
        "day": 11,
        "date": "11/23 (一)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "熱海海上花火：相模湾の夜空に咲く大輪 (熱海海上花火・夜空璀璨之章)",
        "title_en": "Atami Sea Fireworks: Blossoms in Sagami Night Sky",
        "vibe": "Brass Rock Duet / 145 BPM / F# Major",
        "anime": "《飆速宅男》（箱根學園起點、小田原出發衝刺）、《頭文字D》",
        "drama": "《真田丸》《軍師官兵衛》（黑田官兵衛說降北條氏政、小田原征伐）",
        "history": "1590年豐臣秀吉小田原征伐滅後北條氏天下統一；縣道740號俯瞰白糸川鐵橋",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Triumphant, Bold, Ringing) & 30yo Japanese Female Vocal (Cheerful, Punchy Brass Pop Vocal)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Upbeat J-Pop, Brass Rock, Anime Sports Theme]
[Tempo: 145 BPM]
[Key: F# Major]
[Instrumentation: Punchy Horn Section, Bright Electric Rhythm Guitar, Marching Drum Fills, Driving Bass]
[Mood: Triumphant, Bright, Cheerful, Victorious]
[Production: Punchy Modern Pop Master, Crisp Brass Dynamics, Clear Vocal Layering]""",
        "lyrics": """[Intro: Punchy brass fanfare, crisp electric guitar groove, upbeat drums]
[Voice: Female Vocal - Japanese]
真鶴駅前、左折！ 絶景ロードへGO！

[Verse 1: Male Lead - Mandarin Chinese]
離開熱海溫泉 沿著伊豆山緩緩爬升
騎到真鶴站前 果斷左轉切入縣道七四零！
徹底繞開國道危險的江之浦暗黑隧道
沿著山腰的柑橘園 展開神級景觀的巡航

[Verse 1: Female Lead - Japanese]
たわわに実る 黄金色の温州みかん
相模湾の青い海を どこまでも見下ろして
白糸川橋梁を渡る 東海道線の電車
まるで絵画のような 根府川の絶景パノラマ

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 四到六度的平緩坡道 踩起來輕鬆愉快
[Voice: Female Vocal - Japanese] 『弱虫ペダル』の箱根学園が 駆け抜けた風を感じて
[Voice: Male Vocal - Mandarin] 早川漁港傳來 炸竹筴魚的酥脆香氣
[Voice: Female Vocal - Japanese] 難攻不落の小田原城へ、凱旋のラストスパート！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
蜜柑色の坂道を 軽やかに駆け上がれ！
(在金黃柑橘的坡道上 輕快地奔馳而上！)
[Voice: Male Lead - Mandarin] 豐臣秀吉二十二萬大軍 小田原開城的天下一統！
[Voice: Female Lead - Japanese] 白壁の天守閣とお濠に、紅葉が美しく映える！
[Voice: Duet / Harmony]
伊豆半島を走破した 誇らしき二本の足で！
(用征服伊豆半島的雙腿 驕傲地踏入小田原！)

[Verse 2: Male Lead - Mandarin Chinese]
黑田官兵衛單騎入城 說降北條氏政的傳奇
小田原城護城河畔 銀杏與楓葉正初初染紅
連假最後一天的收官日 我們跨越了山海的考驗
二十三公里的短程 留下最甜美的蜜柑香氣

[Verse 2: Female Lead - Japanese]
難攻不落の城は今 私たちを優しく迎える
真鶴道路の渋滞を 完全に迂回した爽快感
知恵とルート選びがあれば 自転車は最強の翼
天守閣の上から 走ってきた相模湾を望む

[Instrumental Break: Brass Fanfare & Upbeat Guitar Riffs]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 告別了伊豆的名湯與懸崖 前方就是湘南海岸
[Voice: Female Vocal - Japanese] 蜜柑の甘酸っぱさが、疲れた身体を癒してくれる
[Voice: Duet / Harmony]
明日はスラムダンクの海へ！ 風は止まらない！
(明天奔向灌籃高手的海岸！風絕不停歇！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
蜜柑色の坂道を 軽やかに駆け上がれ！
(在金黃柑橘的坡道上 輕快地奔馳而上！)
[Voice: Male Lead - Mandarin] 豐臣秀吉二十二萬大軍 小田原開城的天下一統！
[Voice: Female Lead - Japanese] 白壁の天守閣とお濠に、紅葉が美しく映える！
[Voice: Duet / Harmony]
伊豆半島を走破した 誇らしき二本の足で！
(用征服伊豆半島的雙腿 驕傲地踏入小田原！)

[Outro: Triumphant Brass Coda]
[Voice: Female Vocal - Japanese] 熱海湾の大花火、胸に響く轟音
[Voice: Male Vocal - Mandarin] 下多賀 Izu Kansya 的夜空，花火祭圓滿落幕！
[Voice: Duet / Harmony]
(Triumphant fireworks booming and brass coda)
[End]"""
    },
    {
        "day": 12,
        "date": "11/24 (二)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "烏帽子岩の風：スラムダンクの海岸線 (烏帽子岩海風・灌籃高手的海岸)",
        "title_en": "Eboshi Rock Breeze: The Slam Dunk Coastline",
        "vibe": "90s Anime Pop-Rock Duet / 138 BPM / E Major",
        "anime": "《灌籃高手 SLAM DUNK》（流川楓湘南海岸晨騎）、《青春豬頭少年不會夢到兔女郎學姐》",
        "drama": "《有喜歡的人》（湘南海岸浪漫物語）、《海灘男孩 Beach Boys》",
        "history": "歌川廣重東海道五十三次（平塚、大磯宿）；南方之星桑田佳祐故鄉茅崎烏帽子岩",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Passionate, Nostalgic 90s Rock Vocal) & 30yo Japanese Female Vocal (Clear, Inspiring, ZARD Style Pop-Rock)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: 90s Anime Pop-Rock, ZARD Style, J-Rock Coastal Anthem]
[Tempo: 138 BPM]
[Key: E Major]
[Instrumentation: Bright Overdriven Guitar Riffs, Driving Bassline, Catchy Pop Drum Beat, Distant Ocean Waves FX]
[Mood: Uplifting, Nostalgic, Youthful, Inspiring]
[Production: Punchy 90s Vintage Master, Crisp Guitars, Wide Stereo Chorus]""",
        "lyrics": """[Intro: Classic 90s guitar intro melody, catchy straight rock drum beat]
[Voice: Female Vocal - Japanese]
あの頃の夢を、もう一度ペダルに乗せて！

[Verse 1: Male Lead - Mandarin Chinese]
從小田原出發 沿著國道一號寬廣的路肩
大磯平塚的古老驛站 迎來相模灣清澈的海藍
遇到積沙就切出 改騎一三四號專用車道
耳機裡響起《直到世界盡頭》 彷彿回到十七歲那年

[Verse 1: Female Lead - Japanese]
茅ヶ崎の沖合に浮かぶ 烏帽子岩のシルエット
桑田佳祐が歌った サザンオールスターズの海
松林の防風林が 冷たい海風を遮って
真っ直ぐに伸びる海岸線を スピードに乗ってゆく

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 像流川楓戴著耳機 在湘南海岸晨騎破風
[Voice: Female Vocal - Japanese] 『青ブタ』の江ノ島弁天橋 カモメが空を舞う
[Voice: Male Vocal - Mandarin] 秋冬乾燥透明的空氣 隔著海灣清晰看見富士冠頂
[Voice: Female Vocal - Japanese] 世界が終わるまでは、離れる事もない！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
波音に合わせて ペダルを回せ！ 湘南の風になれ！
(伴著海浪的節奏 轉動踏板！化作湘南的風！)
[Voice: Male Lead - Mandarin] 遠方江之島的海燭燈塔 在陽光下召喚著我們
[Voice: Female Lead - Japanese] 流川が自転車で走った、あの眩しい海岸線！
[Voice: Duet / Harmony]
平坦な三十八キロ 青春の熱さを取り戻せ！
(平坦的三十八公里 找回那份熾熱的青春！)

[Verse 2: Male Lead - Mandarin Chinese]
騎上江之島大橋 弁財天的海島在眼前展開
點一碗滿滿的吻仔魚海鮮丼 犒賞奔馳的雙腿
海風吹拂著微熱的臉龐 沒有中年危機的焦慮
只有太平洋的浪花 與單車鏈條清脆的律動

[Verse 2: Female Lead - Japanese]
江ノ電の音が遠くから カタコト聴こえてくる
海辺のカフェのテラスで 夕日を待つ時間
四十代の青春は まだまだ始まったばかり
二本の足で刻んだ 確かな湘南の記憶

[Instrumental Break: 90s Melodic Rock Guitar Solo]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 年少時看過的漫畫 如今真真切切在車輪下展開
[Voice: Female Vocal - Japanese] どこまでも青い空、どこまでも続く水平線
[Voice: Duet / Harmony]
あの日の情熱は、ずっと胸の中で燃えている！
(那一天的熱血 一直在心中熊魁燃燒！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
波音に合わせて ペダルを回せ！ 湘南の風になれ！
(伴著海浪的節奏 轉動踏板！化作湘南的風！)
[Voice: Male Lead - Mandarin] 遠方江之島的海燭燈塔 在陽光下召喚著我們
[Voice: Female Lead - Japanese] 流川が自転車で走った、あの眩しい海岸線！
[Voice: Duet / Harmony]
平坦な三十八キロ 青春の熱さを取り戻せ！
(平坦的三十八公里 找回那份熾熱的青春！)

[Outro: Guitar Solo with Ocean Waves FX]
[Voice: Female Vocal - Japanese] 江ノ島の夕暮れ、富士の影
[Voice: Male Vocal - Mandarin] 湘南的海風，永遠年輕！
[Voice: Duet / Harmony]
(Guitar chord fading into gentle ocean surf)
[End]"""
    },
    {
        "day": 13,
        "date": "11/25 (三)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "いざ、鎌倉！踏切の晴子と柏尾川 (前進鎌倉！平交道晴子與柏尾川)",
        "title_en": "Iza Kamakura! Haruko at the Crossing & Kashio River",
        "vibe": "Indie Folk Duet / 128 BPM / D Major",
        "anime": "《灌籃高手》（鎌倉高校前平交道世紀揮手）、《孤獨搖滾！》《海街日記》",
        "drama": "《倒數第二次戀愛》（小泉今日子極樂寺長谷寺浪漫）、《海街日記》（四姊妹梅酒）",
        "history": "1185年源賴朝創立鎌倉幕府（「いざ、鎌倉！」）；鶴岡八幡宮；柏尾川水岸步道",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Warm, Storyteller, Gentle) & 30yo Japanese Female Vocal (Sweet, Nostalgic Indie Singer)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Indie Folk, J-Acoustic Pop, Cinematic Nostalgia]
[Tempo: 128 BPM]
[Key: D Major]
[Instrumentation: Fingerpicked Acoustic Guitar, Melodic Upright Piano, Warm Cello, Railroad Crossing Bell FX]
[Mood: Nostalgic, Bittersweet, Gentle, Heartwarming]
[Production: Acoustic Intimacy, Spatial Reverb, Organic Wooden Tone]""",
        "lyrics": """[Intro: Acoustic guitar strumming, bell chime of a railroad crossing: dang-dang-dang]
[Voice: Female Vocal - Japanese]
朝八時の踏切、江ノ電が通り過ぎる...

[Verse 1: Male Lead - Mandarin Chinese]
早上八點準時抵達 鎌倉高校前平交道
沒有吵雜的觀光客 只有波光粼粼的七里濱
綠色的江之電 伴著清脆叮咚聲緩緩駛過
柵欄升起的那一刻 彷彿看見晴子在對面揮手

[Verse 1: Female Lead - Japanese]
長谷寺の紅葉と 極楽寺の切通し
『最後から二番目の恋』の 大人の時間が流れる
鶴岡八幡宮の段葛 武士たちの古都・鎌倉
歴史の静寂が 私たちのペダルを包み込む

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 避開砂石車密集的朝比奈峠 切入大船與柏尾川
[Voice: Female Vocal - Japanese] 柏尾川プロムナード、平坦な水辺の緑道へ！
[Voice: Male Vocal - Mandarin] 沿著河岸平整綠道 輕鬆滑向戶塚與保土谷
[Voice: Female Vocal - Japanese] 「いざ、鎌倉！」から 横浜港の未来へ！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
踏切の遮断機が上がれば 青春の続きが走り出す！
(當平交道的柵欄升起 青春的續篇便開始奔馳！)
[Voice: Male Lead - Mandarin] 長谷寺的庭園楓紅 點亮了八百年的古寺簷角
[Voice: Female Lead - Japanese] 柏尾川の風に吹かれて、横浜みなとみらいへ！
[Voice: Duet / Harmony]
古都から未来の港町へ 完璧なプロムナード！
(從古都直通未來港灣 最完美的濱水綠道！)

[Verse 2: Male Lead - Mandarin Chinese]
穿過戶塚的舊東海道 緩坡騎起來毫不費力
橫濱地標塔與摩天輪 在天際線上漸漸升起
從千年前武家政權的起源 騎進現代港灣的繁華
這三十三公里的穿越 像一場優雅的時空對話

[Verse 2: Female Lead - Japanese]
みなとみらいの観覧車 夕暮れの空に光りだす
山下公園の銀杏が 金色の絨毯を敷き詰めて
赤レンガ倉庫のカフェで 温かいラテを飲む
都会の夜風が 優しく旅人を迎える

[Instrumental Break: Fingerstyle Guitar & Cello Duet]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 告別了湘南的浪花 走進橫濱璀璨的夜景
[Voice: Female Vocal - Japanese] 古い歴史と新しい夢が、この道で繋がっている
[Voice: Duet / Harmony]
車輪が紡いだ物語、フィナーレへと向かってゆく
(車輪紡織的物語 正在向著終曲前行)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
踏切の遮断機が上がれば 青春の続きが走り出す！
(當平交道的柵欄升起 青春的續篇便開始奔馳！)
[Voice: Male Lead - Mandarin] 長谷寺的庭園楓紅 點亮了八百年的古寺簷角
[Voice: Female Lead - Japanese] 柏尾川の風に吹かれて、横浜みなとみらいへ！
[Voice: Duet / Harmony]
古都から未来の港町へ 完璧なプロムナード！
(從古都直通未來港灣 最完美的濱水綠道！)

[Outro: Acoustic Guitar with Distant Foghorn FX]
[Voice: Female Vocal - Japanese] 横浜港の汽笛と、ベイブリッジの光
[Voice: Male Vocal - Mandarin] 鎌倉與橫濱，青春不散場
[Voice: Duet / Harmony]
(Guitar chord fading into night air)
[End]"""
    },
    {
        "day": 14,
        "date": "11/26 (四)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "踊る大捜査線：豊洲大橋とガンダムの空 (大搜查線・豐洲大橋與鋼彈天空)",
        "title_en": "Bayside Line: Toyosu Bridge & Gundam Skyline",
        "vibe": "Modern Electro-Pop Duet / 130 BPM / G# Minor",
        "anime": "《機動戰士鋼彈》（台場獨角獸立像）、《數碼寶貝》（富士電視台大激戰）、《文豪野犬》",
        "drama": "《大搜查線》（「無法封鎖彩虹大橋！」經典台詞）、《戀愛可以持續到天長地久》",
        "history": "1853年培里黑船來航橫濱開港；江戶末期防衛黑船之品川砲台（台場）；現代豐洲大橋",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Urban, Crisp, Confident) & 30yo Japanese Female Vocal (Sweet, Energetic, Modern Tokyo Electro-Pop Diva like Yoasobi / Perfume)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Modern Electro-Pop, Futuristic Synth-Pop, Tokyo Skyline Electronic]
[Tempo: 130 BPM]
[Key: G# Minor]
[Instrumentation: Pulsing Synth Bass, 808 Trap Beats, Sparkly Arpeggiators, Futuristic Vocoder Glitches]
[Mood: Futuristic, Exhilarating, Urban, Romantic]
[Production: Punchy Modern Electronic Master, Dynamic Stereo Panning, Spatial Vocals]""",
        "lyrics": """[Intro: Futuristic synth arpeggio, punchy four-on-the-floor beat, sweeping filter]
[Voice: Female Vocal - Japanese]
「レインボーブリッジ、封鎖できません！」
[Voice: Male Vocal - Mandarin]
沒關係，我們有豐洲大橋！

[Verse 1: Male Lead - Mandarin Chinese]
告別黑船來航的橫濱港 沿著多摩川出海口北上
羽田大鳥居在海風中守望 飛機從頭頂呼嘯掠過
穿過勝鬨橋 感受築地的生機與過往
彩虹大橋禁止騎乘 我們直奔全新的豐洲大橋！

[Verse 1: Female Lead - Japanese]
豊洲大橋の専用レーン 東京湾のパノラマへ
遮るもののない 青いハイウェイを駆け上がる
お台場のフジテレビの球体が 夕日を浴びて輝く
等身大のガンダムが 私たちを見下ろしている

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 江戶末期防衛黑船的砲台 今日已是未來的海濱公園
[Voice: Female Vocal - Japanese] 『デジモン』の選ばれし子供たちが、戦ったあの空！
[Voice: Male Vocal - Mandarin] 寬闊平穩的跨海大橋 免下車推行直通台場
[Voice: Female Vocal - Japanese] 都会の風を切り裂いて、未来都市へ！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
お台場の空へ！ 未来都市のハイウェイを突き抜けろ！
(奔向台場的天空！穿透未來都市的跨海高架！)
[Voice: Male Lead - Mandarin] 摩天大樓在海面投下倒影 自由女神在夜色中微笑
[Voice: Female Lead - Japanese] レインボーブリッジを渡らなくても、私たちの道は繋がっている！
[Voice: Duet / Harmony]
東京湾の天際線 我們用車輪封鎖了今夜最美的奇蹟！
(東京湾のスカイライン、今夜最高の奇跡を駆け抜けろ！)

[Verse 2: Male Lead - Mandarin Chinese]
有明現代建築的幾何線條 映襯著黃昏的紫霞
十四天的磨練 雙腿早已習慣了任何坡度與風向
在台場海濱公園停下單車 望著對岸東京鐵塔的橘光
四十歲的成熟與浪漫 在這座未來之城綻放

[Verse 2: Female Lead - Japanese]
『恋はつづくよどこまでも』の 観覧車の光の下で
潮風が心地よく 二人の汗を乾かしてゆく
大都会のど真ん中を 自転車で駆け抜ける爽快感
世界で一番輝く 夜景の特等席

[Instrumental Break: Futuristic Synth Solo with Glitch FX]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 從古老神社到未來鋼彈 這座城市包容了所有夢想
[Voice: Female Vocal - Japanese] 長い旅路を走ってきた私たちに、東京が微笑んでいる
[Voice: Duet / Harmony]
未来へのペダルは、まだまだ止まらない！
(通往未來的踏板 依然絕不停歇！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
お台場の空へ！ 未来都市のハイウェイを突き抜けろ！
(奔向台場的天空！穿透未來都市的跨海高架！)
[Voice: Male Lead - Mandarin] 摩天大樓在海面投下倒影 自由女神在夜色中微笑
[Voice: Female Lead - Japanese] レインボーブリッジを渡らなくても、私たちの道は繋がっている！
[Voice: Duet / Harmony]
東京湾の天際線 我們用車輪封鎖了今夜最美的奇蹟！
(東京湾のスカイライン、今夜最高の奇跡を駆け抜けろ！)

[Outro: Electronic Beats Fading with Night Ambiance]
[Voice: Female Vocal - Japanese] お台場の夜景、輝く自由の女神
[Voice: Male Vocal - Mandarin] 今夜，東京灣屬於我們
[Voice: Duet / Harmony]
(Synth arpeggio echoing away into electronic beats)
[End]"""
    },
    {
        "day": 15,
        "date": "11/27 (五)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "荒川アンダー・ザ・ブリッジ：金八先生の土手 (荒川橋下・金八老師的河堤)",
        "title_en": "Arakawa Under the Bridge: Kinpachi Sunset Path",
        "vibe": "Ska-Punk Duet / 160 BPM / C Major",
        "anime": "《荒川爆笑團》（小招與小珊荒川橋下戀愛）、《魔法少女小圓》（葛西臨海公園齒輪）",
        "drama": "《3年B組金八先生》（荒川堤防夕陽奔跑國民記憶）、《山田孝之的東京都北區赤羽》",
        "history": "1911-1930年青山士主持世界級荒川放水路治水大工程；百年岩淵赤水門",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Humorous, Playful, Energetic) & 30yo Japanese Female Vocal (Quirky, Lively, Punchy Ska-Rock Singer)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Ska-Punk, Quirky J-Rock, Upbeat Riverside Anthem]
[Tempo: 160 BPM]
[Key: C Major]
[Instrumentation: Punchy Ska Brass Horns, Upstroke Electric Guitar Chords, Walking Bass, Cheerful Whistle]
[Mood: Playful, Cheerful, Energetic, Comedic]
[Production: Punchy Live Sound, Crisp Horn Attacks, Bouncy Rhythm Section]""",
        "lyrics": """[Intro: Punchy ska brass intro, upbeat guitar upstrokes, cheerful whistle]
[Voice: Female Vocal - Japanese]
荒川右岸！ 車止めは減速だよー！
[Voice: Male Vocal - Mandarin]
收到！減速牽行，安全第一！

[Verse 1: Male Lead - Mandarin Chinese]
從葛西臨海公園 荒川零公里起點出發
過清砂大橋 一律切入全柏油的荒川右岸！
避開左岸的碎石斷點 享受這條專用紅地毯
遇到極窄的防機車鐵管路擋 乖乖減速牽過絕不硬闖

[Verse 1: Female Lead - Japanese]
橋の下を覗き込めば カッパの村長がいるのかな？
金星から来た美少女が 笑っているのかな？
『金八先生』が走った あの夕暮れの土手で
ススキの穂が 金色に波打っている

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 提早出發 避開午後群馬吹來的西北落山風
[Voice: Female Vocal - Japanese] スカイツリーが右手に ずっと私たちを見守っている
[Voice: Male Vocal - Mandarin] 百年前青山士主持的世界級治水工程 守護著整座東京
[Voice: Female Vocal - Japanese] 赤羽の百年・岩淵赤水門へ！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
荒川アンダー・ザ・ブリッジ！ どこまでも続く河川敷！
(荒川橋下的狂想曲！一望無際的寬廣河濱！)
[Voice: Male Lead - Mandarin] 金色芒草在風中敬禮 像金八老師當年的熱血奔跑
[Voice: Female Lead - Japanese] 車止めパイプも笑顔でクリア！ 自由な土手を突き進め！
[Voice: Duet / Harmony]
河川敷のパラダイス 誰も僕らのペダルを止められない！
(河濱的高灘地樂園 誰也阻擋不了我們的車輪！)

[Verse 2: Male Lead - Mandarin Chinese]
棒球少年清脆的擊球聲 在開闊的河堤迴響
騎進山田孝之深愛的赤羽一番街
紅燈籠在黃昏點亮 居酒屋飄出串燒香氣
三十八公里的平路 騎得輕鬆又暢快淋漓

[Verse 2: Female Lead - Japanese]
赤水門の赤いアーチ 大正の誇りを今に伝える
都会の真ん中に広がる 空の広さに息をのむ
無理をせず、笑い合って、ペダルを回す午後
これが大人の、最高のサイクリング！

[Instrumental Break: Wild Ska Horns & Walking Bass Jam]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 就算遇到逆風 只要放慢踩踏節奏依然能向前
[Voice: Female Vocal - Japanese] 橋の下にも、土手の上にも、たくさんのドラマがある
[Voice: Duet / Harmony]
赤羽の夜風に乾杯！ 明日は川越へ！
(敬赤羽的夜風一杯！明天前進川越！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
荒川アンダー・ザ・ブリッジ！ どこまでも続く河川敷！
(荒川橋下的狂想曲！一望無際的寬廣河濱！)
[Voice: Male Lead - Mandarin] 金色芒草在風中敬禮 像金八老師當年的熱血奔跑
[Voice: Female Lead - Japanese] 車止めパイプも笑顔でクリア！ 自由な土手を突き進め！
[Voice: Duet / Harmony]
河川敷のパラダイス 誰も僕らのペダルを止められない！
(河濱的高灘地樂園 誰也阻擋不了我們的車輪！)

[Outro: Ska Horn Fanfare with Laugh]
[Voice: Female Vocal - Japanese] 赤羽の一番街で、乾杯！
[Voice: Male Vocal - Mandarin] 荒川河畔，晚安！
[Voice: Duet / Harmony]
(Brass fanfare with cheerful laughter)
[End]"""
    },
    {
        "day": 16,
        "date": "11/28 (六)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "月がきれい：小江戸川越・時の鐘 (月色真美・小江戶川越之鐘)",
        "title_en": "The Moon is Beautiful: Little Edo Kawagoe",
        "vibe": "Anime OST Duet / 132 BPM / Eb Major",
        "anime": "《月色真美》（安曇小太郎與水野茜純愛聖地、冰川神社風鈴）、《元氣少女緣結神》",
        "drama": "《JIN 仁醫》（江戶防火藏造黑瓦老街風貌）、晨間劇《つばさ》",
        "history": "川越藩主松平信綱城下町；喜多院藏有江戶城唯一留存「德川家光誕生之間」「春日局化妝之間」",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Poetic, Gentle, Tender) & 30yo Japanese Female Vocal (Innocent, Sweet, Pure Anime OST Vocalist)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Emotional Anime OST Ballad, Japanese Pure Romance Theme]
[Tempo: 132 BPM]
[Key: Eb Major]
[Instrumentation: Grand Acoustic Piano, Lush String Orchestra, Japanese Wind Chimes, Distant Temple Bell FX]
[Mood: Pure, Romantic, Nostalgic, Tender]
[Production: Delicate Studio Reverb, Clear Intimate Vocals, Warm String Acoustics]""",
        "lyrics": """[Intro: Gentle chime of the Toki no Kane bell, tender piano melody, soft wind chimes]
[Voice: Female Vocal - Japanese]
「月がきれいですね」...
[Voice: Male Vocal - Mandarin]
風也溫柔...

[Verse 1: Male Lead - Mandarin Chinese]
從荒川切入入間川專用自行車道
田園風光伴著平坦柏油 一路向北延伸
黑漆防火的藏造建築 映入眼簾的一番街
像走進《仁醫》的江戶 穿越回三百年前的城下町

[Verse 1: Female Lead - Japanese]
『月がきれい』の二人が 歩いた菓子屋横丁
氷川神社の大銀杏が 金色の雨を降らせる
時の鐘がゴーンと響き 街に時を告げる
茜さんの笑顔が どこかで揺れているような午後

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 走進喜多院 欣賞紅葉山庭園的深紅楓景
[Voice: Female Vocal - Japanese] 徳川家光が生まれた 江戸城の部屋がここに眠る
[Voice: Male Vocal - Mandarin] 春日局的化妝室 藏著幕府時代的優雅與幽玄
[Voice: Female Vocal - Japanese] 五十六キロの道のりも、愛おしい思い出に変わる

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
「月がきれいですね」 あの純粋な告白のように！
(「今夜月色真美」 宛如那句最純粹的告白！)
[Voice: Male Lead - Mandarin] 時之鐘敲響了古今交錯的清脆與悠揚
[Voice: Female Lead - Japanese] 喜多院の紅葉山庭園、真っ赤に染まる秋！
[Voice: Duet / Harmony]
小江戸の風情に抱かれて 青春の時間を巻き戻そう！
(沉醉在小江戶的風情中 倒帶屬於青春的時光！)

[Verse 2: Male Lead - Mandarin Chinese]
在藏造星巴克的日式庭園 喝一口暖心熱茶
川越太麵炒麵的香氣 驅散了騎行的微疲
回程入間川微風吹拂 順著平坦路道滑行
這座小江戶 用沉靜的黑瓦治癒了趕路的心

[Verse 2: Female Lead - Japanese]
夕暮れの荒川へと スムーズに滑り込む
茜色に染まる土手 二つの影が寄り添う
急ぐ旅じゃないから 寄り道が一番楽しい
心のアルバムに刻まれた、優しい小江戸の日

[Instrumental Break: Tender Grand Piano and Wind Chime Interlude]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 年少時不懂的隱忍與深情 在川越老街找到了答案
[Voice: Female Vocal - Japanese] 時の鐘が響く街で、二人の想いが重なり合う
[Voice: Duet / Harmony]
今夜の月は、本当にきれいだね
(今夜的月色 真的無比美麗啊)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
「月がきれいですね」 あの純粋な告白のように！
(「今夜月色真美」 宛如那句最純粹的告白！)
[Voice: Male Lead - Mandarin] 時之鐘敲響了古今交錯的清脆與悠揚
[Voice: Female Lead - Japanese] 喜多院の紅葉山庭園、真っ赤に染まる秋！
[Voice: Duet / Harmony]
小江戸の風情に抱かれて 青春の時間を巻き戻そう！
(沉醉在小江戶的風情中 倒帶屬於青春的時光！)

[Outro: Toki no Kane Bell Chime & Fading Piano]
[Voice: Female Vocal - Japanese] 時の鐘の余韻、夜空に浮かぶ満月
[Voice: Male Vocal - Mandarin] 川越小江戶，晚安
[Voice: Duet / Harmony]
(Piano solo trailing off with distant bell toll)
[End]"""
    },
    {
        "day": 17,
        "date": "11/29 (日)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "メタセコイアの黄金森：寅さんと両さんの下町 (水杉黃金森林・寅次郎與阿兩的下町)",
        "title_en": "Golden Metasequoia Forest: Tora-san & Ryotsu Downtown",
        "vibe": "Nostalgic Folk Duet / 122 BPM / G Major",
        "anime": "《烏龍派出所》（兩津勘吉故鄉葛飾柴又、淺草回憶）、《鬼滅之刃》（大正繁華淺草）",
        "drama": "《男人真命苦 / 寅次郎的故事》（渥美清國民電影殿堂、柴又帝釋天參道草餅）",
        "history": "東京最大水鄉「葛飾水元公園」一萬棵水杉林；江戶將軍鷹狩地；淺草寺町人文化",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Heartwarming, Rustic, Cheerful) & 30yo Japanese Female Vocal (Sweet, Sunny, Melodic Japanese Folk Singer)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Nostalgic Folk-Pop, Retro Downtown Tokyo, Acoustic Whistle Anthem]
[Tempo: 122 BPM]
[Key: G Major]
[Instrumentation: Acoustic Accordion, Fingerstyle Acoustic Guitar, Upright Bass, Cheerful Whistling]
[Mood: Heartwarming, Cheerful, Nostalgic, Whimsical]
[Production: Warm Analog Acoustic Tone, Open Natural Soundstage, Intimate Vocals]""",
        "lyrics": """[Intro: Warm accordion melody, acoustic guitar strumming, cheerful whistle melody]
[Voice: Female Vocal - Japanese]
「私、生まれも育ちも葛飾柴又です！」
[Voice: Male Vocal - Mandarin]
走！去看看一萬棵水杉的黃金森林！

[Verse 1: Male Lead - Mandarin Chinese]
荒川一路南下 切入葛飾的水鄉小徑
走進水元公園 迎面而來的是震撼的寧靜
一萬棵高聳入雲的水杉 染上了深邃的磚紅與金橙
小合溜的水面倒映著 這全東京最壯觀的森林

[Verse 1: Female Lead - Japanese]
柴又帝釈天の参道 草団子の甘い香り
寅さんがトランクを提げて 歩いたあの木橋
『こち亀』の両津勘吉の 破天荒な笑い声が
下町の路地裏から 聴こえてくるような温もり

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 江戶將軍曾在此鷹狩 如今是市民騎行的世外桃源
[Voice: Female Vocal - Japanese] 隅田川の風に吹かれて、浅草の雷門へ！
[Voice: Male Vocal - Mandarin] 穿過吾妻橋 看見大正浪漫與晴空塔交相輝映
[Voice: Female Vocal - Japanese] 「男はつらいよ」、だけど旅は最高に楽しい！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
メタセコイアの黄金の森 下町の温もりに抱かれて！
(水杉的黃金森林 沉醉在下町的溫暖懷抱中！)
[Voice: Male Lead - Mandarin] 一萬棵水杉在水面鋪成 宛如北歐童話的黃金倒影
[Voice: Female Lead - Japanese] 浅草寺の赤い灯籠、大正ロマンの光が灯る！
[Voice: Duet / Harmony]
庶民の笑顔がくれた元気 どこまでも温かい下町散歩！
(平民的笑容給予我們力量 無比溫暖的下町漫步！)

[Verse 2: Male Lead - Mandarin Chinese]
車輪碾過水杉掉落的柔軟針葉 沙沙作響
淺草寺前的紅燈籠 映照著四百年町人文化的繁華
《鬼滅之刃》裡炭治郎驚嘆的繁華街角
如今在我們的車把前 展現著現代與古樸的交融

[Verse 2: Female Lead - Japanese]
スカイツリーが夕暮れの空に 紫に点灯する
アサヒビールの金の炎が 隅田川を照らして
下町の人情が 旅の終わりの寂しさを包む
三十六キロのポタリング、心満たされる午後

[Instrumental Break: Whistling and Accordion Folk Solo]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 走過繁華都心 走過崇山峻嶺 最打動人心的依然是人間煙火
[Voice: Female Vocal - Japanese] 寅さんの笑顔のように、私たちは前を向いて走る
[Voice: Duet / Harmony]
旅のゴールはもうすぐ、一歩一歩を大切に！
(終點就在眼前 珍惜這每一踏步的美好！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
メタセコイアの黄金の森 下町の温もりに抱かれて！
(水杉的黃金森林 沉醉在下町的溫暖懷抱中！)
[Voice: Male Lead - Mandarin] 一萬棵水杉在水面鋪成 宛如北歐童話的黃金倒影
[Voice: Female Lead - Japanese] 浅草寺の赤い灯籠、大正ロマンの光が灯る！
[Voice: Duet / Harmony]
庶民の笑顔がくれた元気 どこまでも温かい下町散歩！
(平民的笑容給予我們力量 無比溫暖的下町漫步！)

[Outro: Accordion Melodic Outro with Whistle]
[Voice: Female Vocal - Japanese] 浅草の夜風に、揺れる赤提灯
[Voice: Male Vocal - Mandarin] 寅次郎與阿兩，感謝你們的陪伴
[Voice: Duet / Harmony]
(Accordion outro trailing off cheerful whistle)
[End]"""
    },
    {
        "day": 18,
        "date": "11/30 (一)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "神宮外苑イチョウ並木：カンチ、バイバイ！ (神宮外苑銀杏大道・莉香的完結篇)",
        "title_en": "Jingu Gaien Gingko Avenue: Kanchi, Bye-bye!",
        "vibe": "90s Big Band City Pop Duet / 126 BPM / A Major",
        "anime": "《東大特訓班 / 龍櫻》（阿部寬帶領考取東大赤門）、《天氣之子》（新海誠神宮外苑）",
        "drama": "《東京愛情故事》（赤名莉香神宮外苑銀杏下經典訣別）、《HERO》（木村拓哉檢察官大道）",
        "history": "東京大學加賀藩前田家赤門（1827年迎娶德川將軍之女建）；神宮外苑繪畫館；皇居江戶城跡",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Romantic, Soulful, Resonant) & 30yo Japanese Female Vocal (Passionate, Sweet, Iconic 90s J-Pop Diva Tone like Matsutoya Yumi / Oda Kazumasa)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Classic 90s City Pop, Romantic Big Band J-Pop, Tokyo Autumn Anthem]
[Tempo: 126 BPM]
[Key: A Major]
[Instrumentation: Lush Brass Section, Sparkling Electric Piano, Searing Alto Saxophone Solo, Groovy Drum Rhythm]
[Mood: Triumphant, Romantic, Bittersweet, Grand]
[Production: Polished High-Gloss 90s Master, Wide Stereo Horns, Rich Vocal Reverb]""",
        "lyrics": """[Intro: Lush brass fanfare, sparkling electric piano chords, groovy 90s drum groove]
[Voice: Female Vocal - Japanese]
「ねえ、カンチ！ 好きって言ったじゃん！」
[Voice: Male Vocal - Mandarin]
莉香，這一次，我們在黃金地毯上微笑告別！

[Verse 1: Male Lead - Mandarin Chinese]
從上野之森出發 騎進東京大學本鄉校區
加賀藩前田家建立的百年赤門 莊嚴肅穆
《龍櫻》學生們奮鬥的大銀杏樹下
厚厚一層金黃地毯 鋪滿了整個校園的步道

[Verse 1: Female Lead - Japanese]
皇居のお濠沿い パレスサイドを滑らかに巡り
青山・明治神宮外苑へと ハンドルを向ける
三百メートルのイチョウ並木が 円錐形の黄金トンネル
『HERO』の久利生公平のように 前を向いて歩き出す

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 十一月的最後一天 迎來了全東京最盛大的黃金雨
[Voice: Female Vocal - Japanese] 『東京ラブストーリー』の 赤名リカの笑顔のように
[Voice: Male Vocal - Mandarin] 頭頂飄落著片片金黃 落在四十歲滄桑的肩頭
[Voice: Female Vocal - Japanese] 七百四十キロを走り抜いた脚が、誇らしく輝く！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
「カンチ、バイバイ！」 あの名シーンのイチョウ並木で！
(「完治，再見！」 在那名場景的銀杏大道下！)
[Voice: Male Lead - Mandarin] 漫天灑落的黃金雨 為十九天的單車旅程加冕
[Voice: Female Lead - Japanese] 頭上から降り注ぐ、眩い黄金のシャワー！
[Voice: Duet / Harmony]
東京の秋の最高峰 いま僕らはその中心で輝いている！
(東京秋日的最高峰 此刻我們正在其中心閃耀！)

[Verse 2: Male Lead - Mandarin Chinese]
聖德紀念繪畫館的經典圓頂 在艷陽下閃閃發光
像《天氣之子》雨過天晴後的萬里無雲
騎向皇居外苑 轉回秋葉原的起點
當初看似遙不可及的富士山與伊豆海 如今已全在輪下

[Verse 2: Female Lead - Japanese]
最初は遠く見えた 富士五湖も、伊豆の海も、湘南の波も
全部この二本の足で 繋いできた奇跡
銀杏の葉を一枚 ポケットにそっと忍ばせて
明日へのラストスパート、笑顔で駆け抜けよう！

[Instrumental Break: Searing Big Band Saxophone Solo over Lush Horns]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 敬這趟無怨無悔的旅程 敬那個永不言退的自己
[Voice: Female Vocal - Japanese] さよならじゃなくて、新しい始まりのバイバイ
[Voice: Duet / Harmony]
黄金色のトンネルを抜けて、最高のフィナーレへ！
(穿過金黃色的並木隧道 奔向最完美的終曲！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
「カンチ、バイバイ！」 あの名シーンのイチョウ並木で！
(「完治，再見！」 在那名場景的銀杏大道下！)
[Voice: Male Lead - Mandarin] 漫天灑落的黃金雨 為十九天的單車旅程加冕
[Voice: Female Lead - Japanese] 頭上から降り注ぐ、眩い黄金のシャワー！
[Voice: Duet / Harmony]
東京の秋の最高峰 いま僕らはその中心で輝いている！
(東京秋日的最高峰 此刻我們正在其中心閃耀！)

[Outro: Saxophone Soaring over Big Band Climax]
[Voice: Female Vocal - Japanese] カンチ、バイバイ！ ありがとう！
[Voice: Male Vocal - Mandarin] 明治神宮外苑，黃金滿開！
[Voice: Duet / Harmony]
(Big band brass hit with triumphant cymbal)
[End]"""
    },
    {
        "day": 19,
        "date": "12/01 (二)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "エル・プサイ・コングルゥ：帰還のスカイライナー (命運閉環・歸還的Skyliner)",
        "title_en": "El Psy Kongroo: Skyliner of Return",
        "vibe": "Epic Symphonic Ending Duet / 142 BPM / E Major",
        "anime": "《命運石之門 Steins;Gate》（世界線收斂終點與新起點「El Psy Kongroo」）、《Love Live!》",
        "drama": "《電車男》（秋葉原純愛奇蹟）、《空中急診英雄 Code Blue》（成田疾馳）",
        "history": "秋葉原從明治鎮火神社演變為全球次文化聖地；京成Skyliner 160km/h直達成田完成圓滿閉環",
        "style_prompt": """[Vocals: Duet - 40yo Chinese Male Baritone (Triumphant, Deeply Moved, Resonant Rock Tone) & 30yo Japanese Female Vocal (Soaring, Angelic, Emotional Anime Diva)]
[Language: Bilingual Mandarin Chinese and Japanese]
[Genre: Epic Anime Ending, Symphonic Rock Outro, Cinematic Finale]
[Tempo: 142 BPM]
[Key: E Major]
[Instrumentation: Grand Symphonic Strings, Driving Stadium Rock Drums, Distorted Guitar Chords, Concert Piano]
[Mood: Triumphant, Epic, Emotional, Grateful]
[Production: Wall of Sound Master, Huge Cinematic Dynamic Range, Wide Spatial Stereo]""",
        "lyrics": """[Intro: Gentle acoustic piano playing Day 1 theme, then swelling with epic strings and rock drums]
[Voice: Female Vocal - Japanese]
神田明神の石段で、合掌...
[Voice: Male Vocal - Mandarin]
還清了這十九天的晴空與微風。
[Voice: Duet / Harmony]
すべての道に、ありがとう！

[Verse 1: Male Lead - Mandarin Chinese]
走進神田明神 雙手合十感謝一路平安
秋葉原的巷弄依舊熱鬧 CycleTrip Base 的門市就在眼前
把洗淨的愛車交還 檢查這七百四十五公里的勳章
鏈條上的油垢與細痕 都是中年最驕傲的印記

[Verse 1: Female Lead - Japanese]
バイクを返却して 輪行袋をたたんだら
日暮里のホームへ スカイライナーが滑り込んでくる
時速百六十キロ 成田空港へ滑空する窓の外
十九日間の景色が 走馬灯のように駆け巡る

[Pre-Chorus: Call & Response - Bilingual]
[Voice: Male Vocal - Mandarin] 多摩川的晨光、秋山街道的靜谷、富士山腳下的紅葉迴廊
[Voice: Female Vocal - Japanese] 朝霧高原の風、修善寺の湯煙、城ヶ崎の白波、湘南の海！
[Voice: Male Vocal - Mandarin] 《電車男》誕生的秋葉原 直通《Code Blue》的成田天空
[Voice: Female Vocal - Japanese] 世界線はここに収束し、新しい旅立ちへ！

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
エル・プサイ・コングルゥ！ 世界線はここに収束した！
(El Psy Kongroo！ 世界線在這一刻完美收斂！)
[Voice: Male Lead - Mandarin] 七百四十五公里的輪印 銘刻進四十歲男人的靈魂
[Voice: Female Lead - Japanese] 富士の紅葉も、伊豆の海も、永遠に胸の中で生き続ける！
[Voice: Duet / Harmony]
さようなら、そしてありがとう！ 最高の日本単車旅！
(再見了，還有謝謝！ 這趟最棒的日本單車騎旅！)

[Verse 2: Male Lead - Mandarin Chinese]
在成田機場的登機門前 握著護照回望夕陽
腿部肌肉隱隱的酸脹 是這段冒險最真實的烙印
這不是終點 而是人生下一個階段的起點
心中裝滿了富士雪與相模浪 還有什麼困難不能跨越？

[Verse 2: Female Lead - Japanese]
飛行機が夕暮れの滑走路を 飛び立ってゆく
雲を突き抜けて 星空の海へと舞い上がる
日常に戻っても 私たちの胸には
あの圧倒的な富士山の姿と、風の歌がある

[Instrumental Break: Epic Guitar and Symphonic Strings Grand Reprise]

[Bridge: Emotional Duet Climax - Bilingual]
[Voice: Male Vocal - Mandarin] 踏板停下了 夢想卻在更大的世界裡旋轉
[Voice: Female Vocal - Japanese] 二人で走った軌跡は、消えない光になって輝く
[Voice: Duet / Harmony]
十九日間のすべての瞬間に、心からの感謝を！
(對這十九天的每一個瞬間，致以最深沉的感謝！)

[Chorus: Full Duet Harmony - Bilingual]
[Voice: Duet / Harmony]
エル・プサイ・コングルゥ！ 世界線はここに収束した！
(El Psy Kongroo！ 世界線在這一刻完美收斂！)
[Voice: Male Lead - Mandarin] 七百四十五公里的輪印 銘刻進四十歲男人的靈魂
[Voice: Female Lead - Japanese] 富士の紅葉も、伊豆の海も、永遠に胸の中で生き続ける！
[Voice: Duet / Harmony]
さようなら、そしてありがとう！ 最高の日本単車旅！
(再見了，還有謝謝！ 這趟最棒的日本單車騎旅！)

[Outro: Piano Solo Reprises Day 1 Theme, Epic Grand Finish]
[Voice: Male Vocal - Mandarin] 登機廣播響起，準備回家
[Voice: Female Vocal - Japanese] またいつか、この道で逢おうね
[Voice: Duet / Harmony]
十九日間のすべての奇跡に...
エル・プサイ・コングルゥ。
(El Psy Kongroo.)
[End]"""
    }
]

html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>東京・富士・伊豆・東京灣 單車騎旅 19日 Suno v5.5 中日雙語男女對唱提示詞庫</title>
    <style>
        :root {{
            --primary: #8C2D19;
            --secondary: #2B4C59;
            --accent: #D97724;
            --bg-body: #070A13;
            --card-bg: #111827;
            --card-border: #1F2937;
            --code-bg: #030712;
            --code-border: #1E293B;
            --btn-copy: #2563EB;
            --btn-copy-hover: #1D4ED8;
            --male-color: #38BDF8;
            --female-color: #F472B6;
            --duet-color: #FBBF24;
            --v55-color: #10B981;
        }}

        * {{
            box-sizing: border-box;
            margin: 0;
            padding: 0;
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, "PingFang TC", "Microsoft JhengHei", sans-serif;
            background-color: var(--bg-body);
            color: #F1F5F9;
            line-height: 1.6;
            padding: 24px 16px;
        }}

        .container {{
            max-width: 1200px;
            margin: 0 auto;
        }}

        /* Header */
        .hero {{
            background: linear-gradient(135deg, #0F172A 0%, #311042 45%, #451A03 100%);
            border: 1px solid #4F46E5;
            border-radius: 20px;
            padding: 40px 32px;
            margin-bottom: 28px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.6);
            position: relative;
        }}

        .hero h1 {{
            font-size: 26px;
            font-weight: 800;
            letter-spacing: 0.5px;
            color: #F8FAFC;
            margin-bottom: 10px;
        }}

        .v55-pill {{
            display: inline-block;
            background: linear-gradient(135deg, #10B981 0%, #059669 100%);
            color: #FFFFFF;
            padding: 3px 12px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 800;
            margin-bottom: 12px;
            box-shadow: 0 2px 8px rgba(16, 185, 129, 0.3);
        }}

        .hero p {{
            font-size: 14.5px;
            color: #CBD5E1;
            max-width: 920px;
            margin: 0 auto 16px auto;
            line-height: 1.65;
        }}

        .duet-badge-banner {{
            display: inline-flex;
            align-items: center;
            gap: 12px;
            background: rgba(3, 7, 18, 0.8);
            border: 1px solid #4F46E5;
            padding: 8px 20px;
            border-radius: 30px;
            margin-top: 10px;
            font-size: 13px;
            font-weight: 600;
        }}

        .hero-tags {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
            margin-top: 18px;
        }}

        .hero-tag {{
            background: rgba(255, 255, 255, 0.08);
            border: 1px solid rgba(255, 255, 255, 0.15);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 12.5px;
            color: #E2E8F0;
            backdrop-filter: blur(5px);
        }}

        /* Quick Navigation Filter */
        .nav-filter {{
            display: flex;
            gap: 10px;
            margin-bottom: 20px;
            flex-wrap: wrap;
            justify-content: center;
        }}

        .filter-btn {{
            background: var(--card-bg);
            color: #94A3B8;
            border: 1px solid var(--card-border);
            padding: 8px 18px;
            border-radius: 12px;
            font-size: 13.5px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .filter-btn:hover, .filter-btn.active {{
            background: #D97724;
            color: #FFFFFF;
            border-color: #D97724;
            transform: translateY(-1px);
        }}

        /* Day Selector Grid */
        .day-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(54px, 1fr));
            gap: 8px;
            margin-bottom: 30px;
            background: var(--card-bg);
            padding: 16px;
            border-radius: 16px;
            border: 1px solid var(--card-border);
        }}

        .day-quick-btn {{
            background: var(--code-bg);
            border: 1px solid var(--card-border);
            color: #CBD5E1;
            padding: 8px 0;
            border-radius: 8px;
            font-size: 12.5px;
            font-weight: 700;
            text-align: center;
            text-decoration: none;
            transition: all 0.15s ease;
        }}

        .day-quick-btn:hover {{
            background: var(--btn-copy);
            color: #FFFFFF;
            border-color: var(--btn-copy);
        }}

        /* Track Card */
        .track-card {{
            background: var(--card-bg);
            border: 1px solid var(--card-border);
            border-radius: 18px;
            margin-bottom: 28px;
            padding: 26px;
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.4);
            transition: border-color 0.2s ease;
        }}

        .track-card:hover {{
            border-color: #475569;
        }}

        .track-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 12px;
            border-bottom: 1px solid var(--card-border);
            padding-bottom: 16px;
            margin-bottom: 18px;
        }}

        .track-meta {{
            display: flex;
            flex-direction: column;
            gap: 4px;
        }}

        .track-num-badge {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            font-size: 12px;
            font-weight: 700;
            color: #F59E0B;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}

        .track-title {{
            font-size: 20px;
            font-weight: 800;
            color: #F8FAFC;
        }}

        .track-title-en {{
            font-size: 13.5px;
            color: #94A3B8;
            font-weight: 400;
        }}

        .super-copy-btn {{
            background: linear-gradient(135deg, #2563EB 0%, #1D4ED8 100%);
            color: #FFFFFF;
            border: none;
            padding: 10px 18px;
            border-radius: 10px;
            font-size: 13px;
            font-weight: 700;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 6px;
            transition: all 0.2s ease;
            box-shadow: 0 4px 12px rgba(37, 99, 235, 0.3);
        }}

        .super-copy-btn:hover {{
            background: linear-gradient(135deg, #1D4ED8 0%, #1E40AF 100%);
            transform: translateY(-2px);
            box-shadow: 0 6px 16px rgba(37, 99, 235, 0.4);
        }}

        /* Vocalist Guide Pill */
        .vocal-guide {{
            display: flex;
            gap: 10px;
            flex-wrap: wrap;
            margin-bottom: 14px;
            padding: 10px 14px;
            background: var(--code-bg);
            border-radius: 8px;
            border: 1px solid var(--code-border);
            font-size: 12.5px;
        }}

        .vocal-tag-m {{
            color: var(--male-color);
            font-weight: 600;
        }}

        .vocal-tag-f {{
            color: var(--female-color);
            font-weight: 600;
        }}

        .vocal-tag-d {{
            color: var(--duet-color);
            font-weight: 600;
        }}

        /* Badges list */
        .badge-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 10px;
            margin-bottom: 20px;
        }}

        .info-pill {{
            background: var(--code-bg);
            border: 1px solid var(--card-border);
            padding: 9px 13px;
            border-radius: 8px;
            font-size: 12.8px;
            color: #E2E8F0;
            line-height: 1.45;
        }}

        .info-pill strong {{
            color: #F59E0B;
            font-weight: 600;
        }}

        /* Prompt Box */
        .prompt-section {{
            margin-top: 16px;
        }}

        .prompt-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-bottom: 8px;
        }}

        .prompt-label {{
            font-size: 13px;
            font-weight: 700;
            color: #94A3B8;
            text-transform: uppercase;
            letter-spacing: 0.5px;
            display: flex;
            align-items: center;
            gap: 6px;
        }}

        .copy-btn {{
            background: #1E293B;
            color: #F8FAFC;
            border: 1px solid #475569;
            padding: 4px 12px;
            border-radius: 6px;
            font-size: 12px;
            font-weight: 600;
            cursor: pointer;
            display: inline-flex;
            align-items: center;
            gap: 4px;
            transition: all 0.15s ease;
        }}

        .copy-btn:hover {{
            background: var(--btn-copy);
            border-color: var(--btn-copy);
        }}

        .code-box {{
            background: var(--code-bg);
            border: 1px solid var(--code-border);
            border-radius: 10px;
            padding: 14px 16px;
            font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace;
            font-size: 13px;
            color: #E2E8F0;
            white-space: pre-wrap;
            word-break: break-word;
            line-height: 1.65;
            max-height: 420px;
            overflow-y: auto;
        }}

        .code-box.style-box {{
            color: #38BDF8;
            max-height: 150px;
            font-weight: 500;
        }}

        /* Toast Notification */
        .toast {{
            position: fixed;
            bottom: 30px;
            right: 30px;
            background: linear-gradient(135deg, #10B981 0%, #059669 100%);
            color: #FFFFFF;
            padding: 14px 24px;
            border-radius: 12px;
            font-size: 14px;
            font-weight: 700;
            box-shadow: 0 10px 25px rgba(0, 0, 0, 0.4);
            opacity: 0;
            transform: translateY(20px);
            transition: all 0.3s cubic-bezier(0.68, -0.55, 0.265, 1.55);
            z-index: 9999;
            display: flex;
            align-items: center;
            gap: 8px;
            pointer-events: none;
        }}

        .toast.show {{
            opacity: 1;
            transform: translateY(0);
        }}

        /* Footer */
        footer {{
            text-align: center;
            padding: 30px 0;
            color: #64748B;
            font-size: 13px;
            border-top: 1px solid var(--card-border);
            margin-top: 40px;
        }}

        @media (max-width: 768px) {{
            body {{
                padding: 16px 10px;
            }}
            .hero {{
                padding: 28px 18px;
            }}
            .track-card {{
                padding: 18px;
            }}
            .track-header {{
                flex-direction: column;
                align-items: stretch;
            }}
            .super-copy-btn {{
                width: 100%;
                justify-content: center;
            }}
        }}
    </style>
</head>
<body>

<div class="container">
    <!-- Hero Banner -->
    <header class="hero">
        <div class="v55-pill">⚡ Suno v5.5 深度神經聲學標準規範</div>
        <h1>🎵 東京・富士・伊豆・東京灣 19日單車騎旅</h1>
        <h2 style="font-size: 16px; font-weight: 600; color: #FCD34D; margin-bottom: 10px;">Suno v5.5 中日雙語男女對唱概念專輯 (19-Track Concept Album)</h2>
        <p>全面升級為 Suno v5.5 最新提示詞規範！採用【Bracketed Descriptor 模組化風格架構】與【Voice-Steering 聲線引導標籤】，精準鎖定 40歲中文熟男音與 30歲清亮日語女聲的聲線分離與和聲交織！</p>
        
        <div class="duet-badge-banner">
            <span class="vocal-tag-m">👨 [Voice: Male Lead - Mandarin]（40歲成熟中文男聲・破風敘事）</span>
            <span>✖</span>
            <span class="vocal-tag-f">👩 [Voice: Female Lead - Japanese]（30歲清亮日語女聲・動漫J-Pop）</span>
        </div>

        <div class="hero-tags">
            <span class="hero-tag">🚀 支援 Suno v5.5 / v5 / v4 自訂模式</span>
            <span class="hero-tag">🎹 模組化 [Vocals] [Genre] [Key] [Tempo] [Production]</span>
            <span class="hero-tag">🎙️ 聲線防串音 [Voice-Steering] 標籤</span>
            <span class="hero-tag">📋 一鍵複製全套 Prompt</span>
        </div>
    </header>

    <!-- Quick Filter -->
    <div class="nav-filter">
        <button class="filter-btn active" onclick="filterStage('all', this)">全部 19 天 (All Tracks)</button>
        <button class="filter-btn" onclick="filterStage('stage1', this)">第一階段：富士五湖賞楓 (Day 1-6)</button>
        <button class="filter-btn" onclick="filterStage('stage2', this)">第二階段：伊豆名湯海岸 (Day 7-11)</button>
        <button class="filter-btn" onclick="filterStage('stage3', this)">第三階段：湘南都心銀杏 (Day 12-19)</button>
    </div>

    <!-- Day Quick Jumper -->
    <div class="day-grid">
"""

for t in tracks_v55:
    html_template += f'        <a href="#day-{t["day"]}" class="day-quick-btn">D{t["day"]}</a>\n'

html_template += """    </div>

    <!-- Track List -->
    <div class="track-list">
"""

for t in tracks_v55:
    lyrics_json = json.dumps(t["lyrics"])
    style_json = json.dumps(t["style_prompt"])
    all_json = json.dumps(f"【Song Title】: {t['title']}\n\n【Style of Music (Suno v5.5)】:\n{t['style_prompt']}\n\n【Lyrics (Suno v5.5)】:\n{t['lyrics']}")
    
    html_template += f"""
        <!-- Day {t['day']} -->
        <article class="track-card" id="day-{t['day']}" data-stage="{t['stage']}">
            <div class="track-header">
                <div class="track-meta">
                    <div class="track-num-badge">
                        <span>💿 Track {t['day']:02d}</span>
                        <span>•</span>
                        <span>{t['date']}</span>
                        <span>•</span>
                        <span style="color: #10B981;">⚡ Suno v5.5 Optimized</span>
                        <span>•</span>
                        <span>{t['vibe']}</span>
                    </div>
                    <h3 class="track-title">{t['title']}</h3>
                    <div class="track-title-en">{t['title_en']}</div>
                </div>
                <button class="super-copy-btn" onclick='copyText({all_json}, "已複製 Day {t['day']} Suno v5.5 全套 Prompt！")'>
                    📋 一鍵複製全套 v5.5 Prompt
                </button>
            </div>

            <!-- Vocalist Setup Guide -->
            <div class="vocal-guide">
                <span class="vocal-tag-m">👨 [Voice: Male Lead - Mandarin]：40歲成熟中文男聲</span>
                <span>｜</span>
                <span class="vocal-tag-f">👩 [Voice: Female Lead - Japanese]：30歲清亮日語女聲</span>
                <span>｜</span>
                <span class="vocal-tag-d">🗣️ [Voice: Duet / Harmony]：雙語和聲合唱</span>
            </div>

            <!-- Three Pillars of Culture -->
            <div class="badge-list">
                <div class="info-pill">
                    <strong>🎬 動漫連結：</strong>{t['anime']}
                </div>
                <div class="info-pill">
                    <strong>📺 日劇/電影：</strong>{t['drama']}
                </div>
                <div class="info-pill">
                    <strong>📜 歷史人物/事件：</strong>{t['history']}
                </div>
            </div>

            <!-- Prompt Box 1: Style of Music -->
            <div class="prompt-section">
                <div class="prompt-header">
                    <span class="prompt-label">🎹 Suno v5.5 Style of Music (模組化提示詞)</span>
                    <button class="copy-btn" onclick='copyText({style_json}, "已複製 v5.5 Style 標籤！")'>
                        📋 複製 Style
                    </button>
                </div>
                <div class="code-box style-box">{t['style_prompt']}</div>
            </div>

            <!-- Prompt Box 2: Full Lyrics -->
            <div class="prompt-section">
                <div class="prompt-header">
                    <span class="prompt-label">📝 Suno v5.5 Lyrics (聲線引導結構化歌詞)</span>
                    <button class="copy-btn" onclick='copyText({lyrics_json}, "已複製完整歌詞！")'>
                        📋 複製 Lyrics
                    </button>
                </div>
                <div class="code-box">{t['lyrics']}</div>
            </div>
        </article>
"""

html_template += """
    </div>

    <!-- Toast Notification -->
    <div id="toast" class="toast">✨ 已成功複製到剪貼簿！可直接貼入 Suno v5.5 生成歌曲！</div>

    <footer>
        <p>東京・富士五湖・富士宮・伊豆・東京灣 19日秋季單車騎行 ｜ Suno v5.5 中日雙語男女對唱提示詞庫 (19-Track Album)</p>
    </footer>
</div>

<script>
function copyText(text, successMsg) {
    if (navigator.clipboard && window.isSecureContext) {
        navigator.clipboard.writeText(text).then(() => {
            showToast(successMsg || "✨ 已成功複製到剪貼簿！");
        }).catch(err => {
            fallbackCopy(text, successMsg);
        });
    } else {
        fallbackCopy(text, successMsg);
    }
}

function fallbackCopy(text, successMsg) {
    const textArea = document.createElement("textarea");
    textArea.value = text;
    textArea.style.position = "fixed";
    textArea.style.left = "-999999px";
    textArea.style.top = "-999999px";
    document.body.appendChild(textArea);
    textArea.focus();
    textArea.select();
    try {
        document.execCommand('copy');
        showToast(successMsg || "✨ 已成功複製到剪貼簿！");
    } catch (err) {
        alert('複製失敗，請手動選取複製');
    }
    document.body.removeChild(textArea);
}

function showToast(msg) {
    const toast = document.getElementById("toast");
    toast.textContent = msg;
    toast.classList.add("show");
    setTimeout(() => {
        toast.classList.remove("show");
    }, 2500);
}

function filterStage(stage, btn) {
    document.querySelectorAll(".filter-btn").forEach(b => b.classList.remove("active"));
    btn.classList.add("active");
    
    const cards = document.querySelectorAll(".track-card");
    cards.forEach(card => {
        if (stage === 'all' || card.getAttribute("data-stage") === stage) {
            card.style.display = "block";
        } else {
            card.style.display = "none";
        }
    });
}
</script>

</body>
</html>
"""

with open("C:/Users/ymero/Downloads/suno_cycling_soundtrack_19days.html", "w", encoding="utf-8") as f:
    f.write(html_template)

with open("d:/2026東京單車騎旅/suno_cycling_soundtrack_19days.html", "w", encoding="utf-8") as f:
    f.write(html_template)

print("Suno v5.5 HTML successfully generated!")
