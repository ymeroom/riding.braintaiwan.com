import sys, json

tracks = [
    {
        "day": 1,
        "date": "11/13 (五)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "世界線の起点：逆流する多摩川の風 (跨越世界線的啟程)",
        "title_en": "Starting Line: Cross the Worldline on Tama River",
        "vibe": "J-Rock Duet / 172bpm / 速度感與啟程熱血",
        "anime": "《命運石之門 Steins;Gate》（秋葉原 Radio會館、世界線跳躍）、《飆速宅男》",
        "drama": "《悠長假期》《求婚大作戰》（多摩川堤防夕陽奔跑名場面）",
        "history": "德川家康開創「六鄉渡口」東海道出城門戶；鎌倉倒幕傳奇「分倍河原之戰」",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (warm, resonant, grounded) and 30yo clear Japanese female vocal (sweet, melodic, energetic anime style), J-Rock, fast tempo 172bpm, driving bassline, bright electric guitar, synth arpeggios, Tokyo city pop vibes, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Fast drum roll, energetic distorted guitar riff, retro synth arpeggio)
[Female Vocal - 日本語]
El Psy Kongroo...
新しい世界線が、いま動き出す！

[Verse 1 - Male Vocal (中文)]
跨上單車 轉動四十歲沈澱的齒輪
離開秋葉原霓虹 逃離日常的喧囂與圍困
踩過銀座的晨光 第一京濱寬廣的路塵
這不是逃避 是一場蓄謀已久的追尋

[Verse 1 - Female Vocal (日本語)]
六郷橋を渡れば 目の前に広がる水面
ビル街のノイズを 背中に振り切って
信号のない一本道 多摩川の風が吹く
迷いはすべて この川に置いてゆこう

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 像日劇長假裡的夕陽 奔跑在河堤之上
[Female (日本語)] 『ロングバケーション』の空が 私たちを照らしている
[Male (中文)] 鏈條咬合的聲音 唱著不服輸的倔強
[Female (日本語)] ペダルを踏み込んで、未来へ！

[Chorus - Duet (中日雙語合唱)]
[Duet]
多摩川の風を裂いて 逆流のペダルを回せ！
(破開多摩川的逆風 踩下滾燙的車輪)
止まらない鼓動が叫ぶ 僕たちのプロローグ
(停不下來的心跳 宣告著旅程的序章)
[Male (中文)] 沿著德川家康開創的古道 逆流而上！
[Female (日本語)] どこまでも遠く、どこまでも熱く！
[Duet]
世界線を変えるスピードで 駆け抜けろ！
(用改變世界線的速度 奔向遠方！)

[Verse 2 - Male Vocal (中文)]
經過二子玉川 漸漸染紅的深大寺林木
分倍河原古戰場 彷彿聽見鎌倉武士的征途
汗水滑過臉頰 呼吸與心跳同步
這條五十公里的起點 是給自己的禮物

[Verse 2 - Female Vocal (日本語)]
夕暮れの調布の空 富士の影がうっすら揺れる
スプロケットが刻む 確かな二人のリズム
「諦めたら そこでレースは終わりだよ」
風の中に聴こえる 懐かしいエール

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 歲月磨平了棱角 卻磨不滅眼裡的星火
[Female (日本語)] 坂道の向こうに、新しい明日の光がある
[Duet]
握緊發燙的車把 向著遠方的山巒 繼續破風！

[Chorus - Duet (中日雙語合唱)]
[Duet]
多摩川の風を裂いて 逆流のペダルを回せ！
(破開多摩川的逆風 踩下滾燙的車輪)
止まらない鼓動が叫ぶ 僕たちのプロローグ
(停不下來的心跳 宣告著旅程的序章)
[Male (中文)] 沿著德川家康開創的古道 逆流而上！
[Female (日本語)] どこまでも遠く、どこまでも熱く！
[Duet]
世界線を変えるスピードで 駆け抜けろ！
(用改變世界線的速度 奔向遠方！)

[Outro]
[Female (日本語)] 調布の街に、茜色の夕焼け
[Male (中文)] 第一天，我們順利抵達
[Duet]
Day One, Complete...
(Guitar solo fading out with bell chimes)"""
    },
    {
        "day": 2,
        "date": "11/14 (六)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "誠の風、秋山街道の静寂 (誠字風骨・秋山靜谷)",
        "title_en": "The Wind of Makoto: Silence of Akiyama Highway",
        "vibe": "Melodic J-Rock Duet / 和風三味線搖滾 / 155bpm",
        "anime": "《Persona 5》（八王子轉運站）、《搖曳露營△》（山梨林道出發）",
        "drama": "《孤獨的美食家》（高尾山名物蕎麥麵與山間茶屋的療癒）",
        "history": "新選組副長土方歲三故鄉（天然理心流日野宿）；武田信玄重臣小山田氏谷村城",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (husky, gritty rock tone) and 30yo Japanese female rock vocal (powerful, crisp, melodic), Shamisen and heavy electric guitar fusion, 155bpm, driving bass, dramatic anime battle OST style, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Sharp shamisen solo melody, exploding into powerful rock rhythm with heavy guitar)

[Verse 1 - Male Vocal (中文)]
告別城市的平坦 淺川水聲推著前輪向前
八王子的老街裡 藏著天然理心流的刀劍
避開國道轟鳴的大車 尋找一條幽靜的生路
土方歲三的誠字旗 彷彿在山風中獵獵作響

[Verse 1 - Female Vocal (日本語)]
津久井湖の波紋が 静かに鏡のように揺れる
県道三十五号の木漏れ日 山が深く抱きしめる
大垂水の喧騒を 鮮やかにかわして
孤独なサイクリストを 迎える秋の谷間

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 鏈條切換至最大飛輪 汗水滴在冷涼的柏油路
[Female (日本語)] 坂道は苦しみじゃない、魂を研ぎ澄ます砥石
[Male (中文)] 像孤獨的美食家 在山間茶屋喝一口甘洌的清泉
[Female (日本語)] 一歩ずつ、峠の頂へ！

[Chorus - Duet (中日雙語合唱)]
[Duet]
秋山街道の谷間を 誇り高く駆け抜けろ！
(在秋山街道的幽谷中 驕傲地破風前行！)
[Male (中文)] 爬坡不是逞強 而是與中年自我的和解
[Female (日本語)] 武田の騎馬隊が駆けた、甲斐の山並みへ！
[Duet]
ギアを落とし 呼吸を整え 限界のその先へ！
(變換齒比 調勻呼吸 踏破極限的彼方！)

[Verse 2 - Male Vocal (中文)]
谷村城的古老石階 記錄著武田氏最後的殘陽
兩側深秋的山林 染上了金黃與赭紅的盛裝
六百米的累積爬升 雙腿發酸卻無比滾燙
四十歲男人的浪漫 就在這無人打擾的深谷道旁

[Verse 2 - Female Vocal (日本語)]
都留の街の灯りが 夕暮れの中に近づく
冷たい秋風が ほてった頬を優しく撫でる
静寂の中で見つけた 自分だけの誇り
誰も邪魔できない、二人の冒険路

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 不走大路 才能看見最澄澈的風景
[Female (日本語)] 険しい坂を越えた者だけが、本当の自由を知る
[Duet]
踏み抜いたペダルの重さだけ 明日の僕らは強くなる！
(踏過踏板的每一次沈重 都將化作明天的堅強！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
秋山街道の谷間を 誇り高く駆け抜けろ！
(在秋山街道的幽谷中 驕傲地破風前行！)
[Male (中文)] 爬坡不是逞強 而是與中年自我的和解
[Female (日本語)] 武田の騎馬隊が駆けた、甲斐の山並みへ！
[Duet]
ギアを落とし 呼吸を整え 限界のその先へ！
(變換齒比 調勻呼吸 踏破極限的彼方！)

[Outro]
[Male (中文)] 暮色降臨都留 聽見棘輪清脆的歌唱
[Female (日本語)] 山を越えた静かな歓喜、都留の夜へ
[Duet]
(Shamisen outro phrase, heavy rock chord fading out)"""
    },
    {
        "day": 3,
        "date": "11/15 (日)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "神宿る金鳥居：千メートルの夕焼け (金鳥居的晚霞・千米靈峰)",
        "title_en": "The Golden Torii: Sunset at 1000 Meters",
        "vibe": "Epic J-Pop Duet / Atmospheric Synth-Rock / 140bpm",
        "anime": "《搖曳露營△》（山中湖夕陽露營、溫泉煮麵）",
        "drama": "《First Love 初戀》（富士山下的命中註定回憶）",
        "history": "江戶時代平民信仰「富士講」；富士吉田金鳥居靈山結界",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (warm, emotive, cinematic) and 30yo sweet Japanese female vocal (pure, soaring, atmospheric), Epic J-Pop, Atmospheric Synth-Rock, 140bpm, acoustic piano intro, expansive string arrangement, uplifting stadium chorus, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Gentle acoustic piano, distant train bell, atmospheric pad swelling)
[Female Vocal - 日本語]
富士の神様、どうか私たちの旅を見守って...

[Verse 1 - Male Vocal (中文)]
沿著富士急行線 騎進桂川旁的鄉間小路
避開大車的喧囂 伴著清泉一路平緩爬升
穿過富士吉田老街 抬頭看見巍峨的金鳥居
江戶時代富士講的朝聖者 也曾在這裡仰望神靈

[Verse 1 - Female Vocal (日本語)]
富士吉田の金鳥居をくぐれば 空が近くなる
標高千メートルの冷気が 白い息に変わる
『First Love』の記憶のように 突然現れた霊峰
雪を戴いた白い冠が 夕日に輝いている

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 氣溫降到十度以下 穿上防風外套拉緊拉鍊
[Female (日本語)] 志摩リンが焚き火を灯した 山中湖の渚へ
[Male (中文)] 疲憊的雙腿 在看見富士山頂那一刻融化
[Female (日本語)] 見てごらん、これが私たちの登ってきた道！

[Chorus - Duet (中日雙語合唱)]
[Duet]
夕焼けの渚 山中湖が紅に染まりゆく！
(夕陽照耀的湖渚 山中湖正燃燒著晚霞！)
[Male (中文)] 踩著厚厚的落葉紅毯 抵達海拔一千米的高原
[Female (日本語)] 富士の峰が茜色の光を浴びて微笑む
[Duet]
初恋の温もりを抱きしめて 天空の湖へ！
(擁抱初戀般的溫熱 抵達這天空之湖！)

[Verse 2 - Male Vocal (中文)]
湖畔的露營場 飄來熱湯與柴火的香氣
像《搖曳露營》裡的悠閒 煮一碗熱騰騰的麵條
夕陽把湖水染成了深邃的金紅
所有的辛苦 都在這面水鏡前得到了補償

[Verse 2 - Female Vocal (日本語)]
波音が静かに 湖畔の紅葉を揺らしている
星空がゆっくりと 天空から降りてくるころ
言葉はいらない ただ静寂に寄り添って
二つの車輪が描いた軌跡を 噛みしめる

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 經歷了前半生的風雨 才能讀懂這座靈山的沉靜
[Female (日本語)] 登りきった者だけが出逢える、圧倒的な奇跡
[Duet]
この冷たい空気の中で、心はずっと熱いまま！
(在這冰涼的高原空氣中 內心卻無比熾熱！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
夕焼けの渚 山中湖が紅に染まりゆく！
(夕陽照耀的湖渚 山中湖正燃燒著晚霞！)
[Male (中文)] 踩著厚厚的落葉紅毯 抵達海拔一千米的高原
[Female (日本語)] 富士の峰が茜色の光を浴びて微笑む
[Duet]
初恋の温もりを抱きしめて 天空の湖へ！
(擁抱初戀般的溫熱 抵達這天空之湖！)

[Outro]
[Female (日本語)] 静かな湖畔、満天の星空
[Male (中文)] 今夜，山中湖在星光下睡去
[Duet]
Good night, Mt. Fuji...
(Piano solo trailing off into night wind ambience)"""
    },
    {
        "day": 4,
        "date": "11/16 (一)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "紅葉回廊のシンフォニー (楓葉迴廊的交響詩)",
        "title_en": "Symphony of the Momiji Corridor",
        "vibe": "Emotional Piano Ballad Duet / 125bpm / 深情見頃",
        "anime": "《名偵探柯南：往天國的倒數計時》（富士五湖雙塔倒影）、《搖曳露營△》",
        "drama": "《silent》（湖畔靜謐而深情的深秋手語獨白）",
        "history": "忍野八海——數百年火山熔岩過濾之神之湧泉，修驗道聖地",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (deep, gentle, romantic) and 30yo Japanese female vocal (crystal clear, emotional, poignant), Piano Ballad, Orchestral J-Pop, 125bpm, expressive violin, acoustic guitar, silent drama vibes, cinematic climax, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Gentle piano melody with falling leaves ambience, tender violin solo)
[Female Vocal - 日本語]
言葉にできない想い、紅葉の風に乗せて...

[Verse 1 - Male Vocal (中文)]
清晨走過忍野八海 泉水澄澈得像一眼望穿千年
八百年的雪融伏流 在池底悄悄訴說著時間
轉動踏板騎上湖北 View Line
微涼的湖風 拂過河口湖平靜的岸邊

[Verse 1 - Female Vocal (日本語)]
湖北ビューラインを 滑るように走る朝
湖面を渡る風が 黄金の秋を連れてくる
『silent』の静けさのように 声を出さなくても
紅葉の回廊が 心の奥を優しく満たす

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 六百株古木楓樹 在今天迎來了最盛期
[Female (日本語)] 深紅に燃え盛るトンネル 空を覆い尽くしてゆく
[Male (中文)] 不需要多餘的言語 手指觸碰飄落的紅葉
[Female (日本語)] この一瞬を、ずっと忘れないで

[Chorus - Duet (中日雙語合唱)]
[Duet]
もみじ回廊！ 燃え盛る光のトンネルを抜けて！
(穿過紅葉迴廊 漫天燃燒的光之隧道！)
[Male (中文)] 紅與金的落葉 在車輪旁飛舞如花雨
[Female (日本語)] 今日この日、満開の見頃に出逢えた奇跡
[Duet]
息を呑むほどの深紅の中で 愛の言葉を奏でよう！
(在屏息凝神的深紅之中 奏響愛的交響詩！)

[Verse 2 - Male Vocal (中文)]
大石公園的岸邊 掃帚草染上了成熟的酒紅
湖面倒映著完美的富士 像柯南電影裡的終極謎題
停下單車 坐在長椅上喝一口熱咖啡
這份深秋的奢侈 治癒了中年所有的疲憊

[Verse 2 - Female Vocal (日本語)]
湖面に揺れる 逆さ富士のシルエット
落ち葉が車輪に触れて カサリと音を立てる
旅はまだ続くけれど 今日のこの景色は
私たちの心に 永遠の宝物になる

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 如果秋天是一首詩 這裡就是最動人的副歌
[Female (日本語)] 赤く染まる夜のライトアップ、夢のような光の海
[Duet]
ペダルを止めて、ただこの美しさに抱かれよう
(停下踏板 靜靜沉醉在這份極致的美麗中)

[Chorus - Duet (中日雙語合唱)]
[Duet]
もみじ回廊！ 燃え盛る光のトンネルを抜けて！
(穿過紅葉迴廊 漫天燃燒的光之隧道！)
[Male (中文)] 紅與金的落葉 在車輪旁飛舞如花雨
[Female (日本語)] 今日この日、満開の見頃に出逢えた奇跡
[Duet]
息を呑むほどの深紅の中で 愛の言葉を奏でよう！
(在屏息凝神的深紅之中 奏響愛的交響詩！)

[Outro]
[Female (日本語)] 夜の回廊に、灯る赤い光
[Male (中文)] 河口湖的紅葉，晚安
[Duet]
(Violin and piano duet softly fading out)"""
    },
    {
        "day": 5,
        "date": "11/17 (二)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "千円札の蒼い鏡：青木ヶ原の風 (千圓紙幣上的逆富士)",
        "title_en": "The Thousand-Yen Mirror: Aoki Forest Wind",
        "vibe": "Chillhop Duet / Lo-Fi 吉他 / 110bpm",
        "anime": "《搖曳露營△》第一集浩庵露營場逆富士、《蟲師》（青木原樹海生命之息）",
        "drama": "《在世界中心呼喊愛》《四重奏》（深山湖畔的隱逸詩意）",
        "history": "西元864年「貞觀大噴發」熔岩分開古代剗之海；岡田紅陽「湖畔之春」千圓逆富士",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (laid-back, warm, contemplative) and 30yo Japanese female vocal (airy, soft, cozy indie tone), Chillhop, Dreamy Indie Pop, Lo-Fi Electric Guitar, 110bpm, ambient synth pads, mellow brass, cozy autumn vibe, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Vinyl crackle, warm jazzy guitar chords, soft acoustic drum beat)
[Male Vocal - 中文]
拿出皮夾裡的千圓紙幣...
[Female Vocal - 日本語]
あの青い湖畔へ、行こう...

[Verse 1 - Male Vocal (中文)]
穿過西湖療癒之里的茅草屋頂
貞觀大噴發的古老熔岩 孕育了青木原樹海的寂靜
像《蟲師》走過的靈山小徑 遠離主幹道的車流
車胎碾過金黃松針 奏出節奏舒適的迴響

[Verse 1 - Female Vocal (日本語)]
精進湖の畔で出逢う 『子抱き富士』の優しさ
小さな山を抱きしめる 静かなシルエット
千年の歴史が育んだ 蒼い四つの湖
風が木々を揺らし 旅人の心を洗ってゆく

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 來到本棲湖浩庵營地 拿出千圓紙幣對齊地平線
[Female (日本語)] お札の裏側の景色が、いま目の前に広がっている
[Male (中文)] 泡一碗熱騰騰的咖哩泡麵 撫慰微涼的指尖
[Female (日本語)] 志摩リンと撫子が出逢った、あの朝のように

[Chorus - Duet (中日雙語合唱)]
[Duet]
浩庵の湖畔に広がる 完璧な逆さ富士！
(浩庵湖畔展開的 完美無瑕的逆富士！)
[Male (中文)] 平靜如鏡的藍色水面 倒映著雪白的富士冠頂
[Female (日本語)] 波ひとつない蒼い鏡、千円札の奇跡！
[Duet]
世界の中心で 自然がくれた詩を聴いている
(在世界中心 聆聽大自然寫下的詩行)

[Verse 2 - Male Vocal (中文)]
湖北岸的起伏坡道 像《四重奏》般優雅悠揚
沒有趕路的焦慮 只有齒輪與湖水的合唱
四十歲的旅行 不再追求速度與里程
而是把這份純粹的孤獨 釀成一壺陳年佳釀

[Verse 2 - Female Vocal (日本語)]
観光客の消えた夕暮れ 本棲湖の深い青
富士山と私たちだけの 贅沢な時間が流れる
タイヤが刻んだ四十九キロ 穏やかな達成感
心の中に広がる、あたたかな余韻

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 這張千圓紙幣上的風景 今天變成了永恆的記憶
[Female (日本語)] 溶岩の森を抜けて、私たちは自由になった
[Duet]
静けさこそが、いちばん贅沢なご馳走
(這份靜謐 才是旅程中最奢華的盛宴)

[Chorus - Duet (中日雙語合唱)]
[Duet]
浩庵の湖畔に広がる 完璧な逆さ富士！
(浩庵湖畔展開的 完美無瑕的逆富士！)
[Male (中文)] 平靜如鏡的藍色水面 倒映著雪白的富士冠頂
[Female (日本語)] 波ひとつない蒼い鏡、千円札の奇跡！
[Duet]
世界の中心で 自然がくれた詩を聴いている
(在世界中心 聆聽大自然寫下的詩行)

[Outro]
[Female (日本語)] 藍色に暮れゆく本棲湖
[Male (中文)] 逆富士的倒影，收進心底
[Duet]
(Guitar riff fading out with soft synth chime)"""
    },
    {
        "day": 6,
        "date": "11/18 (三)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "新倉山絵葉書：五重塔と富士の休日 (新倉山明信片・富士休整日)",
        "title_en": "Arakurayama Postcard: The Pagoda and Rest Day",
        "vibe": "City Pop Duet / 放克律動 / 118bpm",
        "anime": "《你的名字。》（時空交錯鳥居）、《進擊的巨人》（孤傲俯瞰視角）",
        "drama": "《First Love 初戀》（富士吉田本町通巨大富士街景）、《重啟人生》",
        "history": "新倉山淺間公園忠靈塔；富士吉田傳承數百年「甲斐絹」織物宿場文化",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (relaxed, smooth, warm) and 30yo Japanese female vocal (sweet, breezy, stylish City Pop tone), Japanese City Pop, Relaxed Groove, 118bpm, smooth saxophone solo, funky bass, vintage electric piano, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Funky bassline, bright electric piano chords, silky smooth saxophone)
[Female Vocal - 日本語]
今日はペダルをお休みして、のんびり歩こう！

[Verse 1 - Male Vocal (中文)]
踩上三百九十八階石梯 今天把單車停在山下
不趕路的日子 腳步變得輕快而悠然
登上新倉山頂 轉身的那一個瞬間
全世界最經典的明信片 在眼前化作真實

[Verse 1 - Female Vocal (日本語)]
朱塗りの五重塔と 燃え盛る紅葉のグラデーション
背後にそびえ立つ 堂々たる白い富士山
『First Love』の本町通りを 見下ろせば
昭和レトロな街並みが 映画のように広がっている

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 走進老街咖啡館 喝一杯手沖熱咖啡
[Female (日本語)] 甲斐絹の機織りの音が、どこか懐かしく響く
[Male (中文)] 檢查煞車皮與鏈條油 準備明天的長下坡
[Female (日本語)] シャッターを切るたび、笑顔がこぼれる

[Chorus - Duet (中日雙語合唱)]
[Duet]
シャッターを切るたび 永遠になる秋の午後！
(每次按下快門 這秋日午後便化作永恆！)
[Male (中文)] 急著奔跑的半生 在這裡學會了停下腳步
[Female (日本語)] 急がない旅だから、見つけられた宝物
[Duet]
五重塔と紅葉富士 最高のご褒美ホリデー！
(五重塔與紅葉富士 最棒的犒賞假期！)

[Verse 2 - Male Vocal (中文)]
河口湖南岸漫步 陽光灑在微波粼粼的湖面
微風吹落幾片紅葉 落在中年男人的肩頭
給自己一天的留白 感受肌肉的放鬆與沉澱
明天要從一千米高原 直衝駿河灣的蔚藍海邊

[Verse 2 - Female Vocal (日本語)]
テラス席でおしゃべり 甘いアップルパイの香り
休養日があるから 長い旅はもっと輝く
夕暮れの本町通り 街灯が優しく灯るころ
明日へのエネルギーが 胸いっぱいに満ちてゆく

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 完美的旅行 需要汗水也需要這杯咖啡的香氣
[Female (日本語)] 富士山に見守られて、心のリセットボタンを押す
[Duet]
明日は駿河湾へ！ 風になる準備はできたかい？
(明天奔向駿河灣！你準備好化作一陣風了嗎？)

[Chorus - Duet (中日雙語合唱)]
[Duet]
シャッターを切るたび 永遠になる秋の午後！
(每次按下快門 這秋日午後便化作永恆！)
[Male (中文)] 急著奔跑的半生 在這裡學會了停下腳步
[Female (日本語)] 急がない旅だから、見つけられた宝物
[Duet]
五重塔と紅葉富士 最高のご褒美ホリデー！
(五重塔與紅葉富士 最棒的犒賞假期！)

[Outro]
[Female (日本語)] 富士吉田の夜に、乾杯！
[Male (中文)] 充飽電，明天出發！
[Duet]
(Saxophone solo trailing off smoothly)"""
    },
    {
        "day": 7,
        "date": "11/19 (四)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "標高差一千メートルの風：駿河湾へダイブ！ (千米落差俯衝・直奔駿河灣)",
        "title_en": "A Thousand Meters Descent: Dive into Suruga Bay",
        "vibe": "Surf Rock Duet / Upbeat J-Pop / 168bpm / 疾速俯衝",
        "anime": "《Love Live! Sunshine!!》（Aqours沼津港、千本松原海堤）、《銀之匙》",
        "drama": "《義經》（大河劇瀧澤秀明主演，源賴朝與義經富士野大卷狩）",
        "history": "1193年源賴朝富士之卷狩與曾我兄弟復仇；德川家康還願之淺間大社總本社",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (energetic, shouting with excitement, husky rock) and 30yo Japanese female vocal (high energy anime idol style, bright, cheering), High-Energy Surf Rock, Upbeat J-Pop, 168bpm, fast acoustic strumming, thunderous drum fills, driving electric guitar, triumphant brass section, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Fast acoustic guitar strumming, soaring trumpet fanfare, countdown: 3, 2, 1, GO!)
[Female Vocal - 日本語]
標高一千メートルから、海へ飛び込めーー！

[Verse 1 - Male Vocal (中文)]
清晨朝霧高原 氣溫只有冰涼的兩度
穿齊防風手套與風衣 展開十八公里的自由落體！
重力拉著車輪飛馳 標高指針一路狂跌
風在耳邊尖嘯 像飛鳥掠過鳴澤的林野

[Verse 1 - Female Vocal (日本語)]
白糸の滝の水しぶきが 紅葉を鮮やかに濡らす
源頼朝が狩りをした 富士の巻狩りの古戦場
浅間大社の湧玉池で 旅の安全を祈ったら
潤井川のサイクリングロードを 海へ一直線！

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 避開危險的國道一號 駛進田子之浦港
[Female (日本語)] 千本松原の堤防ロード、車が一台もいない！
[Male (中文)] 專用海堤筆直展開 駿河灣的潮香撲鼻而來
[Female (日本語)] Aqoursの風を感じて、沼津へ突っ走れ！

[Chorus - Duet (中日雙語合唱)]
[Duet]
標高差一千メートル！ 駿河湾の海風へダイブ！
(標高差一千公尺！一頭躍入駿河灣的海風！)
[Male (中文)] 右手是無垠的太平洋 回頭依然是巍峨的富士山！
[Female (日本語)] 振り返れば、圧倒的な雪富士が見守っている！
[Duet]
海堤專用道上的狂飆 這是屬於我們的黃金路線！
(海堤専用ロードの疾走、最高のゴールデンルート！)

[Verse 2 - Male Vocal (中文)]
在沼津港大口吃下 新鮮美味的生魚片海鮮丼
從高原的寒冬 瞬間切換到伊豆溫暖的陽光
千本黑松在海風中搖曳 擋住沙塵與喧囂
這就是單車旅行 才能體會的極致落差與震撼

[Verse 2 - Female Vocal (日本語)]
『Love Live! Sunshine!!』の 聖地の風が吹く
港の賑わいと カモメたちの白い翼
三島へ向かう平坦路 ペダルが羽のように軽い
山から海へ繋いだ 七十二キロの凱旋！

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 幾小時前還在雪山腳下 現在已經擁抱大海
[Female (日本語)] 標高差千メートルの風を、二本の足で駆け抜けた
[Duet]
これだから単車旅は、やめられない！
(正因如此 單車旅行才讓人如此著迷！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
標高差一千メートル！ 駿河湾の海風へダイブ！
(標高差一千公尺！一頭躍入駿河灣的海風！)
[Male (中文)] 右手是無垠的太平洋 回頭依然是巍峨的富士山！
[Female (日本語)] 振り返れば、圧倒的な雪富士が見守っている！
[Duet]
海堤專用道上的狂飆 這是屬於我們的黃金路線！
(海堤専用ロードの疾走、最高のゴールデンルート！)

[Outro]
[Female (日本語)] 三島大社に響く、夕暮れの鐘
[Male (中文)] 從雪山到大海，完美達成！
[Duet]
(Surf rock guitar tremolo finish)"""
    },
    {
        "day": 8,
        "date": "11/20 (五)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "逃げ恥の足音：修善寺・竹林の小径 (月薪嬌妻的足音・修善寺竹林)",
        "title_en": "Footsteps of Escape: Shuzenji Bamboo Path",
        "vibe": "Traditional Japanese Jazz-Pop Duet / 115bpm / 溫泉浪漫",
        "anime": "《夏目友人帳》（名湯竹林與妖怪和風物語）",
        "drama": "《月薪嬌妻 / 逃避雖可恥但有用》（新垣結衣與星野源蜜月溫泉之旅修善寺桂橋）",
        "history": "西元807年弘法大師空海開山獨鈷之湯；鎌倉二代將軍源賴家幽禁修禪寺物語",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (warm, gentle, romantic crooner) and 30yo Japanese female vocal (sweet, whispering, elegant Japanese tone), Modern Japanese Enka-Pop fusion, Lo-Fi Lounge, 115bpm, bamboo flute Shakuhachi, plucked Shamisen, warm double bass, cozy onsen atmosphere, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Gentle river sound, bamboo flute melody, soothing electric piano chords)
[Female Vocal - 日本語]
赤い橋を渡れば、恋の足音がする...

[Verse 1 - Male Vocal (中文)]
沿著狩野川自行車專用道 悠閒平緩地巡航
二十公里的輕鬆路程 穿過伊豆之國的田庄
三島出發一個半小時 便抵達伊豆最古老的名湯
把單車靠在溫泉旅館前 卸下一身行囊

[Verse 1 - Female Vocal (日本語)]
桂川にかかる 朱塗りの桂橋
『逃げるは恥だが役に立つ』の 二人のように
少し照れながら でも確かに手をつないで
竹林の小径の丸いベンチに 腰を下ろす

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 弘法大師擊出的獨鈷之湯 升起千年的白霧蒸氣
[Female (日本語)] 修禅寺の鐘の音が、静かに秋の山に染みわたる
[Male (中文)] 朱紅色的拱橋 映襯著兩側深紅的楓葉與翠竹
[Female (日本語)] 疲れた脚を名湯に沈めて、ふぅっとため息

[Chorus - Duet (中日雙語合唱)]
[Duet]
修善寺温泉 紅葉が湯煙に揺れている！
(修善寺溫泉 紅葉在溫泉白煙中搖曳！)
[Male (中文)] 換上日式浴衣 走在石疊街道的黃昏
[Female (日本語)] 虹の郷の紅葉が、雅やかな夜を連れてくる
[Duet]
恋する古湯のぬくもり 今夜は夢の中へ溶けてゆこう
(墜入戀愛的名湯溫熱 今夜就融化在夢鄉之中)

[Verse 2 - Male Vocal (中文)]
源賴家的哀愁歷史 如今都化作溫柔的秋色
吃一盤現磨的山葵冰淇淋 辛香中帶著清甜
三連休前夕的溫泉街 安靜得只聽見溪水流淌
這就是中年男人 最嚮往的避世安寧

[Verse 2 - Female Vocal (日本語)]
竹の葉が風にささやく 『夏目友人帳』の森のように
優しい妖怪たちが どこかで見守っているのかな
浴衣の袖を揺らして 温泉街の灯篭を巡る
心までぽかぽかに温まる、贅沢な夜

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 逃避雖可恥但有用 暫時逃離現實又何妨
[Female (日本語)] 休むことは弱さじゃない、明日をもっと愛するため
[Duet]
名湯に身体を預けて、深い眠りへ
(將身心託付給溫泉 沉入甜美的夢鄉)

[Chorus - Duet (中日雙語合唱)]
[Duet]
修善寺温泉 紅葉が湯煙に揺れている！
(修善寺溫泉 紅葉在溫泉白煙中搖曳！)
[Male (中文)] 換上日式浴衣 走在石疊街道的黃昏
[Female (日本語)] 虹の郷の紅葉が、雅やかな夜を連れてくる
[Duet]
恋する古湯のぬくもり 今夜は夢の中へ溶けてゆこう
(墜入戀愛的名湯溫熱 今夜就融化在夢鄉之中)

[Outro]
[Female (日本語)] 川のせせらぎ、おやすみなさい
[Male (中文)] 修善寺的溫泉夜，晚安
[Duet]
(Shakuhachi fading out with gentle stream sound)"""
    },
    {
        "day": 9,
        "date": "11/21 (六)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "火曜サスペンスの断崖：城ヶ崎の白波 (懸疑劇場斷崖・城崎驚濤)",
        "title_en": "Suspense Cliff: The White Waves of Jogasaki",
        "vibe": "Dramatic Symphonic Rock Duet / 148bpm / 壯闊懸疑",
        "anime": "《名偵探柯南》（崖邊真相大白名場面）、《藍海少女！Amanchu!》",
        "drama": "《火曜懸疑劇場》（國民懸疑劇聖地——門脇吊橋與懸崖最後自白）、《華麗一族》",
        "history": "4000年前大室山火山噴發熔岩海岸柱狀節理；川端康成《伊豆的舞孃》漫步之道",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (dramatic, powerful, intense) and 30yo Japanese female rock vocal (soaring, theatrical, dramatic soprano), Dramatic Symphonic Rock, Mysterious, 148bpm, heavy electric guitar riffs, grand orchestral strings, gothic organ accents, cinematic anime OST, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Crashing ocean waves, suspenseful orchestral strings, dramatic heavy guitar chord)
[Female Vocal - 日本語]
犯人は... この断崖の向こうにいる！

[Verse 1 - Male Vocal (中文)]
翻過冷川峠的幽靜九十九拐
避開天城峠的險峻 將爬升鎖定在五百米之內
一碧湖被稱為伊豆之瞳 湖面平靜如鏡
倒映著深紅水杉 隨後空氣漸漸透出大海的鹹味

[Verse 1 - Female Vocal (日本語)]
四千年前 大室山の溶岩が海へ流れ込み
造り出した溶岩の芸術 門脇埼灯台
サスペンス劇場のラストシーンのように
白い怒濤が 黒い絶壁に激しく牙を剥く

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 走上二十三米高的門脇吊橋 腳下是翻騰的太平洋
[Female (日本語)] 火曜サスペンスの音楽が、頭の中で鳴り響く！
[Male (中文)] 像柯南在懸崖邊揭開真相 所有的線索在此交匯
[Female (日本語)] 真実はいつもひとつ！

[Chorus - Duet (中日雙語合唱)]
[Duet]
城ヶ崎の吊橋を 渡れば足がすくむ！
(踏上城崎海岸的吊橋 腳下不禁陣陣發麻！)
[Male (中文)] 驚濤駭浪拍打著四千年熔岩 怒吼著大自然的力量
[Female (日本語)] 犯人の告白を呑み込むような、轟音の白波！
[Duet]
越過山嶺來到海之涯 這是屬於勇敢者的冒險！
(山を越え海へ辿り着いた、勇者たちのアドベンチャー！)

[Verse 2 - Male Vocal (中文)]
《藍海少女》裡那片蔚藍的伊東海岸
三連休的車陣被單車甩在身後
海風呼嘯著吹過頭盔 帶走所有的疲憊
四十歲的胸膛 依然跳動著冒險的野心

[Verse 2 - Female Vocal (日本語)]
夕日が水平線に 沈んでゆく瞬間
断崖の溶岩が 黄金色に輝きだす
川端康成が歩いた 伊豆の旅路
海と山が織りなす 壮大なクライマックス

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 在懸崖的邊緣 才能看清大海真正的壯闊
[Female (日本語)] 恐れを乗り越えた先に、言葉のない感動がある
[Duet]
太平洋の風を胸いっぱいに吸い込んで！
(把太平洋的浩瀚海風 深深吸入胸膛！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
城ヶ崎の吊橋を 渡れば足がすくむ！
(踏上城崎海岸的吊橋 腳下不禁陣陣發麻！)
[Male (中文)] 驚濤駭浪拍打著四千年熔岩 怒吼著大自然的力量
[Female (日本語)] 犯人の告白を呑み込むような、轟音の白波！
[Duet]
越過山嶺來到海之涯 這是屬於勇敢者的冒險！
(山を越え海へ辿り着いた、勇者たちのアドベンチャー！)

[Outro]
[Female (日本語)] 門脇灯台の光が、夜の海を照らす
[Male (中文)] 城崎海岸的浪聲，今夜不休
[Duet]
(Heavy guitar chord ringing out over ocean waves)"""
    },
    {
        "day": 10,
        "date": "11/22 (日)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "熱海月夜：日本一遅い紅葉と金色夜叉 (熱海月夜・最遲紅葉與金色夜叉)",
        "title_en": "Atami Moonlight: The Late Foliage and Golden Demon",
        "vibe": "80s City Pop Duet / 120bpm / 復古浪漫",
        "anime": "《狂賭之淵》《蠟筆小新：溫泉青春大決戰》",
        "drama": "《熱海的搜查官》（小田切讓奇幻探案）、《長假》（木村拓哉）",
        "history": "明治尾崎紅葉《金色夜叉》貫一宮之松訣別；德川家康命人快遞熱海溫泉水至江戶",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (smooth, nostalgic, retro crooner) and 30yo Japanese female vocal (sensual, elegant 80s City Pop style), 80s Japanese City Pop, Nostalgic Synth-Wave, 120bpm, melancholic trumpet solo, groovy slap bass, shimmering vintage synthesizers, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Nostalgic synth pads, groovy 80s drum beat, soulful muted trumpet solo)
[Female Vocal - 日本語]
今夜の月は、私たちの涙で曇らせない...

[Verse 1 - Male Vocal (中文)]
清晨七點半早早出發 避開觀光的大車潮
在網代市區果斷拐進 幽靜的生活舊街道
漁船靜靜泊在港灣 避開了幽暗狹窄的長隧道
海風吹過三十公里的波浪起伏 順利抵達熱海的海邊

[Verse 1 - Female Vocal (日本語)]
お宮の松の前に立てば 貫一の叫びが聴こえる
金色夜叉の哀愁を 潮騒が優しく包み込む
熱海サンビーチのヤシの木 ネオンが揺れる夕暮れ
昭和のロマンが息づく 温泉の港町

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 走進熱海梅園 迎來全日本最遲的紅葉祭
[Female (日本語)] 深紅のモミジと 早咲きの白梅が手をつなぐ奇跡
[Male (中文)] 德川家康曾用木桶快遞這溫泉到江戶城
[Female (日本語)] 浴衣に着替えて、昭和の路地裏を歩こう

[Chorus - Duet (中日雙語合唱)]
[Duet]
熱海梅園 日本で一番遅い紅葉が咲き誇る！
(熱海梅園 全日本最遲的紅葉正燦爛綻放！)
[Male (中文)] 穿過危險隧道的騎士 在溫泉熱氣中慶祝勝利
[Female (日本語)] さよならの涙さえ 恋しくなる熱海の月夜
[Duet]
昭和のネオンに照らされて 二人の夜曲を歌おう！
(在昭和霓虹映照下 唱響屬於我們的夜曲！)

[Verse 2 - Male Vocal (中文)]
如果不願冒險 還有JR伊東線兩鐵輪行的備案
聰明地避開危險 才是成熟旅人的最高哲學
湯前神社的古老源泉 升騰起滾燙的白煙
吃一口現蒸的溫泉饅頭 甜意融化在舌尖

[Verse 2 - Female Vocal (日本語)]
『熱海の捜査官』のように 不思議な魅力あふれる街
海岸通りのムーンロードが 海面に金色の道を描く
三連休の賑わいの中 二人の自転車が休んでいる
旅の半分を越えて、心はますます通い合う

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 貫一與宮的眼淚 已隨時代遠去
[Female (日本語)] 今夜の月は、私たちの笑顔を照らしている
[Duet]
熱海の夜風よ、この幸せを運んでおくれ
(熱海的夜風啊 請把這份幸福帶向遠方)

[Chorus - Duet (中日雙語合唱)]
[Duet]
熱海梅園 日本で一番遅い紅葉が咲き誇る！
(熱海梅園 全日本最遲的紅葉正燦爛綻放！)
[Male (中文)] 穿過危險隧道的騎士 在溫泉熱氣中慶祝勝利
[Female (日本語)] さよならの涙さえ 恋しくなる熱海の月夜
[Duet]
昭和のネオンに照らされて 二人の夜曲を歌おう！
(在昭和霓虹映照下 唱響屬於我們的夜曲！)

[Outro]
[Female (日本語)] 熱海湾に浮かぶ、月の道
[Male (中文)] 熱海月夜，晚安
[Duet]
(Muted trumpet solo fading out softly)"""
    },
    {
        "day": 11,
        "date": "11/23 (一)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "蜜柑色の坂道：難攻不落の小田原城 (柑橘坡道・小田原開城之章)",
        "title_en": "Mandarin Orange Slopes: Impregnable Odawara",
        "vibe": "Brass Rock Duet / Upbeat J-Pop / 145bpm / 凱旋朝陽",
        "anime": "《飆速宅男》（箱根學園起點、小田原出發衝刺）、《頭文字D》",
        "drama": "《真田丸》《軍師官兵衛》（黑田官兵衛說降北條氏政、小田原征伐）",
        "history": "1590年豐臣秀吉小田原征伐滅後北條氏天下統一；縣道740號俯瞰白糸川鐵橋",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (bright, triumphant, bold) and 30yo Japanese female vocal (cheerful, ringing, energetic brass rock style), Upbeat J-Pop, Brass Rock, 145bpm, punchy horn section, driving electric rhythm guitar, sunny coastal vibe, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Punchy brass fanfare, crisp electric guitar groove, upbeat drums)
[Female Vocal - 日本語]
真鶴駅前、左折！ 絶景ロードへGO！

[Verse 1 - Male Vocal (中文)]
離開熱海溫泉 沿著伊豆山緩緩爬升
騎到真鶴站前 果斷左轉切入縣道七四零！
徹底繞開國道危險的江之浦暗黑隧道
沿著山腰的柑橘園 展開神級景觀的巡航

[Verse 1 - Female Vocal (日本語)]
たわわに実る 黄金色の温州みかん
相模湾の青い海を どこまでも見下ろして
白糸川橋梁を渡る 東海道線の電車
まるで絵画のような 根府川の絶景パノラマ

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 四到六度的平緩坡道 踩起來輕鬆愉快
[Female (日本語)] 『弱虫ペダル』の箱根学園が 駆け抜けた風を感じて
[Male (中文)] 早川漁港傳來 炸竹筴魚的酥脆香氣
[Female (日本語)] 難攻不落の小田原城へ、凱旋のラストスパート！

[Chorus - Duet (中日雙語合唱)]
[Duet]
蜜柑色の坂道を 軽やかに駆け上がれ！
(在金黃柑橘的坡道上 輕快地奔馳而上！)
[Male (中文)] 豐臣秀吉二十二萬大軍 小田原開城的天下一統！
[Female (日本語)] 白壁の天守閣とお濠に、紅葉が美しく映える！
[Duet]
伊豆半島を走破した 誇らしき二本の足で！
(用征服伊豆半島的雙腿 驕傲地踏入小田原！)

[Verse 2 - Male Vocal (中文)]
黑田官兵衛單騎入城 說降北條氏政的傳奇
小田原城護城河畔 銀杏與楓葉正初初染紅
連假最後一天的收官日 我們跨越了山海的考驗
二十三公里的短程 留下最甜美的蜜柑香氣

[Verse 2 - Female Vocal (日本語)]
難攻不落の城は今 私たちを優しく迎える
真鶴道路の渋滞を 完全に迂回した爽快感
知恵とルート選びがあれば 自転車は最強の翼
天守閣の上から 走ってきた相模湾を望む

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 告別了伊豆的名湯與懸崖 前方就是湘南海岸
[Female (日本語)] 蜜柑の甘酸っぱさが、疲れた身体を癒してくれる
[Duet]
明日はスラムダンクの海へ！ 風は止まらない！
(明天奔向灌籃高手的海岸！風絕不停歇！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
蜜柑色の坂道を 軽やかに駆け上がれ！
(在金黃柑橘的坡道上 輕快地奔馳而上！)
[Male (中文)] 豐臣秀吉二十二萬大軍 小田原開城的天下一統！
[Female (日本語)] 白壁の天守閣とお濠に、紅葉が美しく映える！
[Duet]
伊豆半島を走破した 誇らしき二本の足で！
(用征服伊豆半島的雙腿 驕傲地踏入小田原！)

[Outro]
[Female (日本語)] 小田原城の天守に、翻る秋風
[Male (中文)] 伊豆征程，圓滿收官！
[Duet]
(Triumphant brass coda, big cymbal crash)"""
    },
    {
        "day": 12,
        "date": "11/24 (二)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "烏帽子岩の風：スラムダンクの海岸線 (烏帽子岩海風・灌籃高手的海岸)",
        "title_en": "Eboshi Rock Breeze: The Slam Dunk Coastline",
        "vibe": "90s Anime Pop-Rock Duet / ZARD style / 138bpm",
        "anime": "《灌籃高手 SLAM DUNK》（流川楓湘南海岸晨騎）、《青春豬頭少年不會夢到兔女郎學姐》",
        "drama": "《有喜歡的人》（湘南海岸浪漫物語）、《海灘男孩 Beach Boys》",
        "history": "歌川廣重東海道五十三次（平塚、大磯宿）；南方之星桑田佳祐故鄉茅崎烏帽子岩",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (nostalgic, passionate, 90s rock tone) and 30yo Japanese female vocal (clear, energetic, ZARD / anime pop style), 90s Anime Pop-Rock, 138bpm, bright overdrive guitar chords, driving bass, nostalgic pop melody, uplifting seaside vibe, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Classic 90s guitar intro melody, catchy straight rock drum beat)
[Female Vocal - 日本語]
あの頃の夢を、もう一度ペダルに乗せて！

[Verse 1 - Male Vocal (中文)]
從小田原出發 沿著國道一號寬廣的路肩
大磯平塚的古老驛站 迎來相模灣清澈的海藍
遇到積沙就切出 改騎一三四號專用車道
耳機裡響起《直到世界盡頭》 彷彿回到十七歲那年

[Verse 1 - Female Vocal (日本語)]
茅ヶ崎の沖合に浮かぶ 烏帽子岩のシルエット
桑田佳祐が歌った サザンオールスターズの海
松林の防風林が 冷たい海風を遮って
真っ直ぐに伸びる海岸線を スピードに乗ってゆく

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 像流川楓戴著耳機 在湘南海岸晨騎破風
[Female (日本語)] 『青ブタ』の江ノ島弁天橋 カモメが空を舞う
[Male (中文)] 秋冬乾燥透明的空氣 隔著海灣清晰看見富士冠頂
[Female (日本語)] 世界が終わるまでは、離れる事もない！

[Chorus - Duet (中日雙語合唱)]
[Duet]
波音に合わせて ペダルを回せ！ 湘南の風になれ！
(伴著海浪的節奏 轉動踏板！化作湘南的風！)
[Male (中文)] 遠方江之島的海燭燈塔 在陽光下召喚著我們
[Female (日本語)] 流川が自転車で走った、あの眩しい海岸線！
[Duet]
平坦な三十八キロ 青春の熱さを取り戻せ！
(平坦的三十八公里 找回那份熾熱的青春！)

[Verse 2 - Male Vocal (中文)]
騎上江之島大橋 弁財天的海島在眼前展開
點一碗滿滿的吻仔魚海鮮丼 犒賞奔馳的雙腿
海風吹拂著微熱的臉龐 沒有中年危機的焦慮
只有太平洋的浪花 與單車鏈條清脆的律動

[Verse 2 - Female Vocal (日本語)]
江ノ電の音が遠くから カタコト聴こえてくる
海辺のカフェのテラスで 夕日を待つ時間
四十代の青春は まだまだ始まったばかり
二本の足で刻んだ 確かな湘南の記憶

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 年少時看過的漫畫 如今真真切切在車輪下展開
[Female (日本語)] どこまでも青い空、どこまでも続く水平線
[Duet]
あの日の情熱は、ずっと胸の中で燃えている！
(那一天的熱血 一直在心中熊熊燃燒！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
波音に合わせて ペダルを回せ！ 湘南の風になれ！
(伴著海浪的節奏 轉動踏板！化作湘南的風！)
[Male (中文)] 遠方江之島的海燭燈塔 在陽光下召喚著我們
[Female (日本語)] 流川が自転車で走った、あの眩しい海岸線！
[Duet]
平坦な三十八キロ 青春の熱さを取り戻せ！
(平坦的三十八公里 找回那份熾熱的青春！)

[Outro]
[Female (日本語)] 江ノ島の夕暮れ、富士の影
[Male (中文)] 湘南的海風，永遠年輕！
[Duet]
(Guitar solo fading out with gentle ocean surf)"""
    },
    {
        "day": 13,
        "date": "11/25 (三)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "いざ、鎌倉！踏切の晴子と柏尾川 (前進鎌倉！平交道晴子與柏尾川)",
        "title_en": "Iza Kamakura! Haruko at the Crossing & Kashio River",
        "vibe": "Indie Folk Duet / J-Acoustic Pop / 128bpm / 青春回憶",
        "anime": "《灌籃高手》（鎌倉高校前平交道世紀揮手）、《孤獨搖滾！》《海街日記》",
        "drama": "《倒數第二次戀愛》（小泉今日子極樂寺長谷寺浪漫）、《海街日記》（四姊妹梅酒）",
        "history": "1185年源賴朝創立鎌倉幕府（「いざ、鎌倉！」）；鶴岡八幡宮；柏尾川水岸步道",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (warm, storytelling tone, acoustic) and 30yo Japanese female vocal (sweet, gentle, nostalgic indie folk), Indie Folk, J-Acoustic Pop, 128bpm, acoustic guitar fingerpicking, melodic upright piano, warm cello lines, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Acoustic guitar strumming, bell chime of a railroad crossing: dang-dang-dang)
[Female Vocal - 日本語]
朝八時の踏切、江ノ電が通り過ぎる...

[Verse 1 - Male Vocal (中文)]
早上八點準時抵達 鎌倉高校前平交道
沒有吵雜的觀光客 只有波光粼粼的七里濱
綠色的江之電 伴著清脆叮咚聲緩緩駛過
柵欄升起的那一刻 彷彿看見晴子在對面揮手

[Verse 1 - Female Vocal (日本語)]
長谷寺の紅葉と 極楽寺の切通し
『最後から二番目の恋』の 大人の時間が流れる
鶴岡八幡宮の段葛 武士たちの古都・鎌倉
歴史の静寂が 私たちのペダルを包み込む

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 避開砂石車密集的朝比奈峠 切入大船與柏尾川
[Female (日本語)] 柏尾川プロムナード、平坦な水辺の緑道へ！
[Male (中文)] 沿著河岸平整綠道 輕鬆滑向戶塚與保土谷
[Female (日本語)] 「いざ、鎌倉！」から 横浜港の未来へ！

[Chorus - Duet (中日雙語合唱)]
[Duet]
踏切の遮断機が上がれば 青春の続きが走り出す！
(當平交道的柵欄升起 青春的續篇便開始奔馳！)
[Male (中文)] 長谷寺的庭園楓紅 點亮了八百年的古寺簷角
[Female (日本語)] 柏尾川の風に吹かれて、横浜みなとみらいへ！
[Duet]
古都から未来の港町へ 完璧なプロムナード！
(從古都直通未來港灣 最完美的濱水綠道！)

[Verse 2 - Male Vocal (中文)]
穿過戶塚的舊東海道 緩坡騎起來毫不費力
橫濱地標塔與摩天輪 在天際線上漸漸升起
從千年前武家政權的起源 騎進現代港灣的繁華
這三十三公里的穿越 像一場優雅的時空對話

[Verse 2 - Female Vocal (日本語)]
みなとみらいの観覧車 夕暮れの空に光りだす
山下公園の銀杏が 金色の絨毯を敷き詰めて
赤レンガ倉庫のカフェで 温かいラテを飲む
都会の夜風が 優しく旅人を迎える

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 告別了湘南的浪花 走進橫濱璀璨的夜景
[Female (日本語)] 古い歴史と新しい夢が、この道で繋がっている
[Duet]
車輪が紡いだ物語、フィナーレへと向かってゆく
(車輪紡織的物語 正在向著終曲前行)

[Chorus - Duet (中日雙語合唱)]
[Duet]
踏切の遮断機が上がれば 青春の続きが走り出す！
(當平交道的柵欄升起 青春的續篇便開始奔馳！)
[Male (中文)] 長谷寺的庭園楓紅 點亮了八百年的古寺簷角
[Female (日本語)] 柏尾川の風に吹かれて、横浜みなとみらいへ！
[Duet]
古都から未来の港町へ 完璧なプロムナード！
(從古都直通未來港灣 最完美的濱水綠道！)

[Outro]
[Female (日本語)] 横浜港の汽笛と、ベイブリッジの光
[Male (中文)] 鎌倉與橫濱，青春不散場
[Duet]
(Acoustic guitar chord fading out with foghorn in distance)"""
    },
    {
        "day": 14,
        "date": "11/26 (四)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "踊る大捜査線：豊洲大橋とガンダムの空 (大搜查線・豐洲大橋與鋼彈天空)",
        "title_en": "Bayside Line: Toyosu Bridge & Gundam Skyline",
        "vibe": "Modern Electro-Pop Duet / 130bpm / 未來天際線",
        "anime": "《機動戰士鋼彈》（台場獨角獸立像）、《數碼寶貝》（富士電視台大激戰）、《文豪野犬》",
        "drama": "《大搜查線》（「無法封鎖彩虹大橋！」經典台詞）、《戀愛可以持續到天長地久》",
        "history": "1853年培里黑船來航橫濱開港；江戶末期防衛黑船之品川砲台（台場）；現代豐洲大橋",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (urban, crisp, stylish) and 30yo Japanese female vocal (sweet, energetic, modern Tokyo electro-pop style like Yoasobi / Perfume), Modern Electro-Pop, Synth-Pop, 130bpm, driving synth bass, infectious 808 beats, sparkling futuristic synthesizers, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Futuristic synth arpeggio, punchy four-on-the-floor beat, sweeping filter)
[Female Vocal - 日本語]
「レインボーブリッジ、封鎖できません！」
[Male Vocal - 中文]
沒關係，我們有豐洲大橋！

[Verse 1 - Male Vocal (中文)]
告別黑船來航的橫濱港 沿著多摩川出海口北上
羽田大鳥居在海風中守望 飛機從頭頂呼嘯掠過
穿過勝鬨橋 感受築地的生機與過往
彩虹大橋禁止騎乘 我們直奔全新的豐洲大橋！

[Verse 1 - Female Vocal (日本語)]
豊洲大橋の専用レーン 東京湾のパノラマへ
遮るもののない 青いハイウェイを駆け上がる
お台場のフジテレビの球体が 夕日を浴びて輝く
等身大のガンダムが 私たちを見下ろしている

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 江戶末期防衛黑船的砲台 今日已是未來的海濱公園
[Female (日本語)] 『デジモン』の選ばれし子供たちが、戦ったあの空！
[Male (中文)] 寬闊平穩的跨海大橋 免下車推行直通台場
[Female (日本語)] 都会の風を切り裂いて、未来都市へ！

[Chorus - Duet (中日雙語合唱)]
[Duet]
お台場の空へ！ 未来都市のハイウェイを突き抜けろ！
(奔向台場的天空！穿透未來都市的跨海高架！)
[Male (中文)] 摩天大樓在海面投下倒影 自由女神在夜色中微笑
[Female (日本語)] レインボーブリッジを渡らなくても、私たちの道は繋がっている！
[Duet]
東京湾の天際線 我們用車輪封鎖了今夜最美的奇蹟！
(東京湾のスカイライン、今夜最高の奇跡を駆け抜けろ！)

[Verse 2 - Male Vocal (中文)]
有明現代建築的幾何線條 映襯著黃昏的紫霞
十四天的磨練 雙腿早已習慣了任何坡度與風向
在台場海濱公園停下單車 望著對岸東京鐵塔的橘光
四十歲的成熟與浪漫 在這座未來之城綻放

[Verse 2 - Female Vocal (日本語)]
『恋はつづくよどこまでも』の 観覧車の光の下で
潮風が心地よく 二人の汗を乾かしてゆく
大都会のど真ん中を 自転車で駆け抜ける爽快感
世界で一番輝く 夜景の特等席

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 從古老神社到未來鋼彈 這座城市包容了所有夢想
[Female (日本語)] 長い旅路を走ってきた私たちに、東京が微笑んでいる
[Duet]
未来へのペダルは、まだまだ止まらない！
(通往未來的踏板 依然絕不停歇！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
お台場の空へ！ 未来都市のハイウェイを突き抜けろ！
(奔向台場的天空！穿透未來都市的跨海高架！)
[Male (中文)] 摩天大樓在海面投下倒影 自由女神在夜色中微笑
[Female (日本語)] レインボーブリッジを渡らなくても、私たちの道は繋がっている！
[Duet]
東京湾の天際線 我們用車輪封鎖了今夜最美的奇蹟！
(東京湾のスカイライン、今夜最高の奇跡を駆け抜けろ！)

[Outro]
[Female (日本語)] お台場の夜景、輝く自由の女神
[Male (中文)] 今夜，東京灣屬於我們
[Duet]
(Synth arpeggio echoing away into electronic beats)"""
    },
    {
        "day": 15,
        "date": "11/27 (五)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "荒川アンダー・ザ・ブリッジ：金八先生の土手 (荒川橋下・金八老師的河堤)",
        "title_en": "Arakawa Under the Bridge: Kinpachi Sunset Path",
        "vibe": "Ska-Punk Duet / Quirky J-Rock / 160bpm / 荒川狂想",
        "anime": "《荒川爆笑團》（小招與小珊荒川橋下戀愛）、《魔法少女小圓》（葛西臨海公園齒輪）",
        "drama": "《3年B組金八先生》（荒川堤防夕陽奔跑國民記憶）、《山田孝之的東京都北區赤羽》",
        "history": "1911-1930年青山士主持世界級荒川放水路治水大工程；百年岩淵赤水門",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (playful, energetic, humorous) and 30yo Japanese female vocal (quirky, lively, punchy ska-rock style), Quirky J-Rock, Upbeat Ska-Punk, 160bpm, walking bassline, punchy ska brass chords, driving drums, cheerful riverside anthem, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Punchy ska brass intro, upbeat guitar upstrokes, cheerful whistle)
[Female Vocal - 日本語]
荒川右岸！ 車止めは減速だよー！
[Male Vocal - 中文]
收到！減速牽行，安全第一！

[Verse 1 - Male Vocal (中文)]
從葛西臨海公園 荒川零公里起點出發
過清砂大橋 一律切入全柏油的荒川右岸！
避開左岸的碎石斷點 享受這條專用紅地毯
遇到極窄的防機車鐵管路擋 乖乖減速牽過絕不硬闖

[Verse 1 - Female Vocal (日本語)]
橋の下を覗き込めば カッパの村長がいるのかな？
金星から来た美少女が 笑っているのかな？
『金八先生』が走った あの夕暮れの土手で
ススキの穂が 金色に波打っている

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 提早出發 避開午後群馬吹來的西北落山風
[Female (日本語)] スカイツリーが右手に ずっと私たちを見守っている
[Male (中文)] 百年前青山士主持的世界級治水工程 守護著整座東京
[Female (日本語)] 赤羽の百年・岩淵赤水門へ！

[Chorus - Duet (中日雙語合唱)]
[Duet]
荒川アンダー・ザ・ブリッジ！ どこまでも続く河川敷！
(荒川橋下的狂想曲！一望無際的寬廣河濱！)
[Male (中文)] 金色芒草在風中敬禮 像金八老師當年的熱血奔跑
[Female (日本語)] 車止めパイプも笑顔でクリア！ 自由な土手を突き進め！
[Duet]
河川敷のパラダイス 誰も僕らのペダルを止められない！
(河濱的高灘地樂園 誰也阻擋不了我們的車輪！)

[Verse 2 - Male Vocal (中文)]
棒球少年清脆的擊球聲 在開闊的河堤迴響
騎進山田孝之深愛的赤羽一番街
紅燈籠在黃昏點亮 居酒屋飄出串燒香氣
三十八公里的平路 騎得輕鬆又暢快淋漓

[Verse 2 - Female Vocal (日本語)]
赤水門の赤いアーチ 大正の誇りを今に伝える
都会の真ん中に広がる 空の広さに息をのむ
無理をせず、笑い合って、ペダルを回す午後
これが大人の、最高のサイクリング！

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 就算遇到逆風 只要放慢踩踏節奏依然能向前
[Female (日本語)] 橋の下にも、土手の上にも、たくさんのドラマがある
[Duet]
赤羽の夜風に乾杯！ 明日は川越へ！
(敬赤羽的夜風一杯！明天前進川越！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
荒川アンダー・ザ・ブリッジ！ どこまでも続く河川敷！
(荒川橋下的狂想曲！一望無際的寬廣河濱！)
[Male (中文)] 金色芒草在風中敬禮 像金八老師當年的熱血奔跑
[Female (日本語)] 車止めパイプも笑顔でクリア！ 自由な土手を突き進め！
[Duet]
河川敷のパラダイス 誰も僕らのペダルを止められない！
(河濱的高灘地樂園 誰也阻擋不了我們的車輪！)

[Outro]
[Female (日本語)] 赤羽の一番街で、乾杯！
[Male (中文)] 荒川河畔，晚安！
[Duet]
(Ska brass fanfare with cheerful laugh)"""
    },
    {
        "day": 16,
        "date": "11/28 (六)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "月がきれい：小江戸川越・時の鐘 (月色真美・小江戶川越之鐘)",
        "title_en": "The Moon is Beautiful: Little Edo Kawagoe",
        "vibe": "Emotional Anime OST Duet / 132bpm / 鐘聲純愛",
        "anime": "《月色真美》（安曇小太郎與水野茜純愛聖地、冰川神社風鈴）、《元氣少女緣結神》",
        "drama": "《JIN 仁醫》（江戶防火藏造黑瓦老街風貌）、晨間劇《つばさ》",
        "history": "川越藩主松平信綱城下町；喜多院藏有江戶城唯一留存「德川家光誕生之間」「春日局化妝之間」",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (gentle, tender, poetic) and 30yo Japanese female vocal (sweet, innocent, pure anime OST vocal), Emotional Anime OST Ballad, 132bpm, acoustic guitar arpeggios, melodic grand piano, sweet expressive strings, heartfelt nostalgic atmosphere, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Gentle chime of the Toki no Kane bell, tender piano melody, soft wind chimes)
[Female Vocal - 日本語]
「月がきれいですね」...
[Male Vocal - 中文]
風也溫柔...

[Verse 1 - Male Vocal (中文)]
從荒川切入入間川專用自行車道
田園風光伴著平坦柏油 一路向北延伸
黑漆防火的藏造建築 映入眼簾的一番街
像走進《仁醫》的江戶 穿越回三百年前的城下町

[Verse 1 - Female Vocal (日本語)]
『月がきれい』の二人が 歩いた菓子屋横丁
氷川神社の大銀杏が 金色の雨を降らせる
時の鐘がゴーンと響き 街に時を告げる
茜さんの笑顔が どこかで揺れているような午後

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 走進喜多院 欣賞紅葉山庭園的深紅楓景
[Female (日本語)] 徳川家光が生まれた 江戸城の部屋がここに眠る
[Male (中文)] 春日局的化妝室 藏著幕府時代的優雅與幽玄
[Female (日本語)] 五十六キロの道のりも、愛おしい思い出に変わる

[Chorus - Duet (中日雙語合唱)]
[Duet]
「月がきれいですね」 あの純粋な告白のように！
(「今夜月色真美」 宛如那句最純粹的告白！)
[Male (中文)] 時之鐘敲響了古今交錯的清脆與悠揚
[Female (日本語)] 喜多院の紅葉山庭園、真っ赤に染まる秋！
[Duet]
小江戸の風情に抱かれて 青春の時間を巻き戻そう！
(沉醉在小江戶的風情中 倒帶屬於青春的時光！)

[Verse 2 - Male Vocal (中文)]
在藏造星巴克的日式庭園 喝一口暖心熱茶
川越太麵炒麵的香氣 驅散了騎行的微疲
回程入間川微風吹拂 順著平坦路道滑行
這座小江戶 用沉靜的黑瓦治癒了趕路的心

[Verse 2 - Female Vocal (日本語)]
夕暮れの荒川へと スムーズに滑り込む
茜色に染まる土手 二つの影が寄り添う
急ぐ旅じゃないから 寄り道が一番楽しい
心のアルバムに刻まれた、優しい小江戸の日

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 年少時不懂的隱忍與深情 在川越老街找到了答案
[Female (日本語)] 時の鐘が響く街で、二人の想いが重なり合う
[Duet]
今夜の月は、本当にきれいだね
(今夜的月色 真的無比美麗啊)

[Chorus - Duet (中日雙語合唱)]
[Duet]
「月がきれいですね」 あの純粋な告白のように！
(「今夜月色真美」 宛如那句最純粹的告白！)
[Male (中文)] 時之鐘敲響了古今交錯的清脆與悠揚
[Female (日本語)] 喜多院の紅葉山庭園、真っ赤に染まる秋！
[Duet]
小江戸の風情に抱かれて 青春の時間を巻き戻そう！
(沉醉在小江戶的風情中 倒帶屬於青春的時光！)

[Outro]
[Female (日本語)] 時の鐘の余韻、夜空に浮かぶ満月
[Male (中文)] 川越小江戶，晚安
[Duet]
(Piano solo trailing off with distant bell toll)"""
    },
    {
        "day": 17,
        "date": "11/29 (日)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "メタセコイアの黄金森：寅さんと両さんの下町 (水杉黃金森林・寅次郎與阿兩的下町)",
        "title_en": "Golden Metasequoia Forest: Tora-san & Ryotsu Downtown",
        "vibe": "Nostalgic Folk-Pop Duet / 122bpm / 溫馨童話",
        "anime": "《烏龍派出所》（兩津勘吉故鄉葛飾柴又、淺草回憶）、《鬼滅之刃》（大正繁華淺草）",
        "drama": "《男人真命苦 / 寅次郎的故事》（渥美清國民電影殿堂、柴又帝釋天參道草餅）",
        "history": "東京最大水鄉「葛飾水元公園」一萬棵水杉林；江戶將軍鷹狩地；淺草寺町人文化",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (heartwarming, rustic, cheerful) and 30yo Japanese female vocal (sweet, sunny, cheerful folk style), Nostalgic Folk-Pop, Accordion and Acoustic Guitar, 122bpm, cheerful whistling, warm walking bass, retro downtown Tokyo vibe, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Warm accordion melody, acoustic guitar strumming, cheerful whistle melody)
[Female Vocal - 日本語]
「私、生まれも育ちも葛飾柴又です！」
[Male Vocal - 中文]
走！去看看一萬棵水杉的黃金森林！

[Verse 1 - Male Vocal (中文)]
荒川一路南下 切入葛飾的水鄉小徑
走進水元公園 迎面而來的是震撼的寧靜
一萬棵高聳入雲的水杉 染上了深邃的磚紅與金橙
小合溜的水面倒映著 這全東京最壯觀的森林

[Verse 1 - Female Vocal (日本語)]
柴又帝釈天の参道 草団子の甘い香り
寅さんがトランクを提げて 歩いたあの木橋
『こち亀』の両津勘吉の 破天荒な笑い声が
下町の路地裏から 聴こえてくるような温もり

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 江戶將軍曾在此鷹狩 如今是市民騎行的世外桃源
[Female (日本語)] 隅田川の風に吹かれて、浅草の雷門へ！
[Male (中文)] 穿過吾妻橋 看見大正浪漫與晴空塔交相輝映
[Female (日本語)] 「男はつらいよ」、だけど旅は最高に楽しい！

[Chorus - Duet (中日雙語合唱)]
[Duet]
メタセコイアの黄金の森 下町の温もりに抱かれて！
(水杉的黃金森林 沉醉在下町的溫暖懷抱中！)
[Male (中文)] 一萬棵水杉在水面鋪成 宛如北歐童話的黃金倒影
[Female (日本語)] 浅草寺の赤い灯籠、大正ロマンの光が灯る！
[Duet]
庶民の笑顔がくれた元気 どこまでも温かい下町散歩！
(平民的笑容給予我們力量 無比溫暖的下町漫步！)

[Verse 2 - Male Vocal (中文)]
車輪碾過水杉掉落的柔軟針葉 沙沙作響
淺草寺前的紅燈籠 映照著四百年町人文化的繁華
《鬼滅之刃》裡炭治郎驚嘆的繁華街角
如今在我們的車把前 展現著現代與古樸的交融

[Verse 2 - Female Vocal (日本語)]
スカイツリーが夕暮れの空に 紫に点灯する
アサヒビールの金の炎が 隅田川を照らして
下町の人情が 旅の終わりの寂しさを包む
三十六キロのポタリング、心満たされる午後

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 走過繁華都心 走過崇山峻嶺 最打動人心的依然是人間煙火
[Female (日本語)] 寅さんの笑顔のように、私たちは前を向いて走る
[Duet]
旅のゴールはもうすぐ、一歩一歩を大切に！
(終點就在眼前 珍惜這每一踏步的美好！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
メタセコイアの黄金の森 下町の温もりに抱かれて！
(水杉的黃金森林 沉醉在下町的溫暖懷抱中！)
[Male (中文)] 一萬棵水杉在水面鋪成 宛如北歐童話的黃金倒影
[Female (日本語)] 浅草寺の赤い灯籠、大正ロマンの光が灯る！
[Duet]
庶民の笑顔がくれた元気 どこまでも温かい下町散歩！
(平民的笑容給予我們力量 無比溫暖的下町漫步！)

[Outro]
[Female (日本語)] 浅草の夜風に、揺れる赤提灯
[Male (中文)] 寅次郎與阿兩，感謝你們的陪伴
[Duet]
(Accordion outro melody with cheerful whistle)"""
    },
    {
        "day": 18,
        "date": "11/30 (一)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "神宮外苑イチョウ並木：カンチ、バイバイ！ (神宮外苑銀杏大道・莉香的完結篇)",
        "title_en": "Jingu Gaien Gingko Avenue: Kanchi, Bye-bye!",
        "vibe": "Classic 90s City Pop Duet / 126bpm / 都會浪漫最高峰",
        "anime": "《東大特訓班 / 龍櫻》（阿部寬帶領考取東大赤門）、《天氣之子》（新海誠神宮外苑）",
        "drama": "《東京愛情故事》（赤名莉香神宮外苑銀杏下經典訣別）、《HERO》（木村拓哉檢察官大道）",
        "history": "東京大學加賀藩前田家赤門（1827年迎娶德川將軍之女建）；神宮外苑繪畫館；皇居江戶城跡",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (romantic, soulful, resonant) and 30yo Japanese female vocal (passionate, sweet, iconic 90s J-Pop diva tone like Oda Kazumasa / Matsutoya Yumi style), Classic 90s City Pop, Romantic Big Band J-Pop, 126bpm, lush brass arrangement, sparkling electric piano, soaring saxophone solo, emotional triumphant climax, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Lush brass fanfare, sparkling electric piano chords, groovy 90s drum groove)
[Female Vocal - 日本語]
「ねえ、カンチ！ 好きって言ったじゃん！」
[Male Vocal - 中文]
莉香，這一次，我們在黃金地毯上微笑告別！

[Verse 1 - Male Vocal (中文)]
從上野之森出發 騎進東京大學本鄉校區
加賀藩前田家建立的百年赤門 莊嚴肅穆
《龍櫻》學生們奮鬥的大銀杏樹下
厚厚一層金黃地毯 鋪滿了整個校園的步道

[Verse 1 - Female Vocal (日本語)]
皇居のお濠沿い パレスサイドを滑らかに巡り
青山・明治神宮外苑へと ハンドルを向ける
三百メートルのイチョウ並木が 円錐形の黄金トンネル
『HERO』の久利生公平のように 前を向いて歩き出す

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 十一月的最後一天 迎來了全東京最盛大的黃金雨
[Female (日本語)] 『東京ラブストーリー』の 赤名リカの笑顔のように
[Male (中文)] 頭頂飄落著片片金黃 落在四十歲滄桑的肩頭
[Female (日本語)] 七百四十キロを走り抜いた脚が、誇らしく輝く！

[Chorus - Duet (中日雙語合唱)]
[Duet]
「カンチ、バイバイ！」 あの名シーンのイチョウ並木で！
(「完治，再見！」 在那名場景的銀杏大道下！)
[Male (中文)] 漫天灑落的黃金雨 為十九天的單車旅程加冕
[Female (日本語)] 頭上から降り注ぐ、眩い黄金のシャワー！
[Duet]
東京の秋の最高峰 いま僕らはその中心で輝いている！
(東京秋日的最高峰 此刻我們正在其中心閃耀！)

[Verse 2 - Male Vocal (中文)]
聖德紀念繪畫館的經典圓頂 在艷陽下閃閃發光
像《天氣之子》雨過天晴後的萬里無雲
騎向皇居外苑 轉回秋葉原的起點
當初看似遙不可及的富士山與伊豆海 如今已全在輪下

[Verse 2 - Female Vocal (日本語)]
最初は遠く見えた 富士五湖も、伊豆の海も、湘南の波も
全部この二本の足で 繋いできた奇跡
銀杏の葉を一枚 ポケットにそっと忍ばせて
明日へのラストスパート、笑顔で駆け抜けよう！

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 敬這趟無怨無悔的旅程 敬那個永不言退的自己
[Female (日本語)] さよならじゃなくて、新しい始まりのバイバイ
[Duet]
黄金色のトンネルを抜けて、最高のフィナーレへ！
(穿過金黃色的並木隧道 奔向最完美的終曲！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
「カンチ、バイバイ！」 あの名シーンのイチョウ並木で！
(「完治，再見！」 在那名場景的銀杏大道下！)
[Male (中文)] 漫天灑落的黃金雨 為十九天的單車旅程加冕
[Female (日本語)] 頭上から降り注ぐ、眩い黄金のシャワー！
[Duet]
東京の秋の最高峰 いま僕らはその中心で輝いている！
(東京秋日的最高峰 此刻我們正在其中心閃耀！)

[Outro]
[Female (日本語)] カンチ、バイバイ！ ありがとう！
[Male (中文)] 明治神宮外苑，黃金滿開！
[Duet]
(Saxophone solo soaring over big band brass climax)"""
    },
    {
        "day": 19,
        "date": "12/01 (二)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "エル・プサイ・コングルゥ：帰還のスカイライナー (命運閉環・歸還的Skyliner)",
        "title_en": "El Psy Kongroo: Skyliner of Return",
        "vibe": "Epic Anime Ending Duet / 142bpm / 史詩圓滿終曲",
        "anime": "《命運石之門 Steins;Gate》（世界線收斂終點與新起點「El Psy Kongroo」）、《Love Live!》",
        "drama": "《電車男》（秋葉原純愛奇蹟）、《空中急診英雄 Code Blue》（成田疾馳）",
        "history": "秋葉原從明治鎮火神社演變為全球次文化聖地；京成Skyliner 160km/h直達成田完成圓滿閉環",
        "style_prompt": "Duet, mature 40yo Chinese male baritone (triumphant, deeply moved, epic rock vocal) and 30yo Japanese female vocal (emotional, soaring, angelic anime diva), Epic Anime Ending, Emotional Rock & Piano Outro, 142bpm, uplifting strings, driving drums, distorted guitar chords, cinematic grand finale, bilingual Mandarin and Japanese lyrics",
        "lyrics": """[Intro]
(Gentle acoustic piano playing Day 1 theme, then swelling with epic strings and rock drums)
[Female Vocal - 日本語]
神田明神の石段で、合掌...
[Male Vocal - 中文]
還清了這十九天的晴空與微風。
[Duet]
すべての道に、ありがとう！

[Verse 1 - Male Vocal (中文)]
走進神田明神 雙手合十感謝一路平安
秋葉原的巷弄依舊熱鬧 CycleTrip Base 的門市就在眼前
把洗淨的愛車交還 檢查這七百四十五公里的勳章
鏈條上的油垢與細痕 都是中年最驕傲的印記

[Verse 1 - Female Vocal (日本語)]
バイクを返却して 輪行袋をたたんだら
日暮里のホームへ スカイライナーが滑り込んでくる
時速百六十キロ 成田空港へ滑空する窓の外
十九日間の景色が 走馬灯のように駆け巡る

[Pre-Chorus - Male & Female (中日對唱)]
[Male (中文)] 多摩川的晨光、秋山街道的靜谷、富士山腳下的紅葉迴廊
[Female (日本語)] 朝霧高原の風、修善寺の湯煙、城ヶ崎の白波、湘南の海！
[Male (中文)] 《電車男》誕生的秋葉原 直通《Code Blue》的成田天空
[Female (日本語)] 世界線はここに収束し、新しい旅立ちへ！

[Chorus - Duet (中日雙語合唱)]
[Duet]
エル・プサイ・コングルゥ！ 世界線はここに収束した！
(El Psy Kongroo！ 世界線在這一刻完美收斂！)
[Male (中文)] 七百四十五公里的輪印 銘刻進四十歲男人的靈魂
[Female (日本語)] 富士の紅葉も、伊豆の海も、永遠に胸の中で生き続ける！
[Duet]
さようなら、そしてありがとう！ 最高の日本単車旅！
(再見了，還有謝謝！ 這趟最棒的日本單車騎旅！)

[Verse 2 - Male Vocal (中文)]
在成田機場的登機門前 握著護照回望夕陽
腿部肌肉隱隱的酸脹 是這段冒險最真實的烙印
這不是終點 而是人生下一個階段的起點
心中裝滿了富士雪與相模浪 還有什麼困難不能跨越？

[Verse 2 - Female Vocal (日本語)]
飛行機が夕暮れの滑走路を 飛び立ってゆく
雲を突き抜けて 星空の海へと舞い上がる
日常に戻っても 私たちの胸には
あの圧倒的な富士山の姿と、風の歌がある

[Bridge - Duet (中日和聲交織)]
[Male (中文)] 踏板停下了 夢想卻在更大的世界裡旋轉
[Female (日本語)] 二人で走った軌跡は、消えない光になって輝く
[Duet]
十九日間のすべての瞬間に、心からの感謝を！
(對這十九天的每一個瞬間，致以最深沉的感謝！)

[Chorus - Duet (中日雙語合唱)]
[Duet]
エル・プサイ・コングルゥ！ 世界線はここに収束した！
(El Psy Kongroo！ 世界線在這一刻完美收斂！)
[Male (中文)] 七百四十五公里的輪印 銘刻進四十歲男人的靈魂
[Female (日本語)] 富士の紅葉も、伊豆の海も、永遠に胸の中で生き続ける！
[Duet]
さようなら、然後謝謝！ 最高の日本単車旅！
(再見了，還有謝謝！ 這趟最棒的日本單車騎旅！)

[Outro]
[Male (中文)] 登機廣播響起，準備回家
[Female (日本語)] またいつか、この道で逢おうね
[Duet]
十九日間のすべての奇跡に...
エル・プサイ・コングルゥ。
(El Psy Kongroo.)
(Piano solo reprises the Day 1 main theme, epic grand finish)
[End]"""
    }
]

html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>東京・富士・伊豆・東京灣 單車騎旅 19日 Suno AI 中日雙語男女對唱提示詞庫</title>
    <style>
        :root {{
            --primary: #8C2D19;
            --primary-light: #FDF6F0;
            --secondary: #2B4C59;
            --secondary-light: #EBF3F5;
            --accent: #D97724;
            --text-dark: #1E293B;
            --text-muted: #64748B;
            --bg-body: #0B0F19;
            --card-bg: #151D2E;
            --card-border: #2B3952;
            --code-bg: #070B14;
            --code-border: #1F293D;
            --success-color: #10B981;
            --btn-copy: #2563EB;
            --btn-copy-hover: #1D4ED8;
            --male-color: #38BDF8;
            --female-color: #F472B6;
            --duet-color: #FBBF24;
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
            max-width: 1180px;
            margin: 0 auto;
        }}

        /* Header */
        .hero {{
            background: linear-gradient(135deg, #1E1B4B 0%, #3B0764 45%, #431407 100%);
            border: 1px solid #4338CA;
            border-radius: 20px;
            padding: 40px 32px;
            margin-bottom: 28px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
            position: relative;
            overflow: hidden;
        }}

        .hero h1 {{
            font-size: 26px;
            font-weight: 800;
            letter-spacing: 0.5px;
            color: #F8FAFC;
            margin-bottom: 12px;
        }}

        .hero p {{
            font-size: 14.5px;
            color: #CBD5E1;
            max-width: 900px;
            margin: 0 auto 20px auto;
            line-height: 1.65;
        }}

        .hero-tags {{
            display: flex;
            justify-content: center;
            flex-wrap: wrap;
            gap: 10px;
        }}

        .hero-tag {{
            background: rgba(255, 255, 255, 0.1);
            border: 1px solid rgba(255, 255, 255, 0.2);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 12.5px;
            color: #E2E8F0;
            backdrop-filter: blur(5px);
        }}

        .duet-badge-banner {{
            display: inline-flex;
            align-items: center;
            gap: 12px;
            background: rgba(15, 23, 42, 0.8);
            border: 1px solid #6366F1;
            padding: 8px 18px;
            border-radius: 30px;
            margin-top: 14px;
            font-size: 13px;
            font-weight: 600;
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
            background: #151D2E;
            color: #94A3B8;
            border: 1px solid #2B3952;
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
            background: #151D2E;
            padding: 16px;
            border-radius: 16px;
            border: 1px solid #2B3952;
        }}

        .day-quick-btn {{
            background: #0B0F19;
            border: 1px solid #2B3952;
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
            box-shadow: 0 8px 25px rgba(0, 0, 0, 0.35);
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
            border-bottom: 1px solid #2B3952;
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
            background: #0B0F19;
            border-radius: 8px;
            border: 1px solid #1F293D;
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
            background: #0B0F19;
            border: 1px solid #2B3952;
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
            background: #2B3952;
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
            max-height: 110px;
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
            border-top: 1px solid #2B3952;
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
        <h1>🎵 東京・富士・伊豆・東京灣 19日單車騎旅</h1>
        <h2 style="font-size: 16px; font-weight: 600; color: #FCD34D; margin-bottom: 12px;">Suno AI 中日雙語・男女對唱概念專輯 (19-Track Duet Concept Album)</h2>
        <p>專為【40歲成熟中文男聲 × 30歲清亮日語女聲】量身定制！深度融合【日本動漫 × 經典日劇 × 歷史人物事件】，包含完整的段落對唱、副歌合唱與精準 Suno v3.5/v4 提示詞，一鍵複製即刻生成！</p>
        
        <div class="duet-badge-banner">
            <span class="vocal-tag-m">👨 40歲中文熟男音（沉穩敘事・成熟滄桑・破風騎手）</span>
            <span>✖</span>
            <span class="vocal-tag-f">👩 30歲日語甜美音（清亮純淨・動漫J-Pop・文化嚮導）</span>
        </div>

        <div class="hero-tags" style="margin-top: 16px;">
            <span class="hero-tag">🚲 19 天完整中日雙語對唱</span>
            <span class="hero-tag">📋 一鍵複製 Style + Full Lyrics</span>
            <span class="hero-tag">🎸 結構化標籤 [Male] / [Female] / [Duet]</span>
            <span class="hero-tag">🚀 支援 Suno v3.5 / v4 自訂模式</span>
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

for t in tracks:
    html_template += f'        <a href="#day-{t["day"]}" class="day-quick-btn">D{t["day"]}</a>\n'

html_template += """    </div>

    <!-- Track List -->
    <div class="track-list">
"""

for t in tracks:
    lyrics_json = json.dumps(t["lyrics"])
    style_json = json.dumps(t["style_prompt"])
    all_json = json.dumps(f"【Song Title】: {t['title']}\n\n【Style of Music】:\n{t['style_prompt']}\n\n【Lyrics】:\n{t['lyrics']}")
    
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
                        <span>{t['vibe']}</span>
                    </div>
                    <h3 class="track-title">{t['title']}</h3>
                    <div class="track-title-en">{t['title_en']}</div>
                </div>
                <button class="super-copy-btn" onclick='copyText({all_json}, "已複製 Day {t['day']} 全套中日雙語對唱 Prompt！")'>
                    📋 一鍵複製全套 Suno Prompt
                </button>
            </div>

            <!-- Vocalist Setup Guide -->
            <div class="vocal-guide">
                <span class="vocal-tag-m">👨 [Male - 中文]：40歲成熟中文男聲</span>
                <span>｜</span>
                <span class="vocal-tag-f">👩 [Female - 日本語]：30歲清亮日語女聲</span>
                <span>｜</span>
                <span class="vocal-tag-d">🗣️ [Duet - 合唱]：中日雙語合唱交織</span>
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
                    <span class="prompt-label">🎹 Suno Style of Music (男女對唱與風格標籤)</span>
                    <button class="copy-btn" onclick='copyText({style_json}, "已複製 Style of Music 標籤！")'>
                        📋 複製 Style
                    </button>
                </div>
                <div class="code-box style-box">{t['style_prompt']}</div>
            </div>

            <!-- Prompt Box 2: Full Lyrics -->
            <div class="prompt-section">
                <div class="prompt-header">
                    <span class="prompt-label">📝 Suno Lyrics (中日雙語結構化歌詞)</span>
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
    <div id="toast" class="toast">✨ 已成功複製到剪貼簿！可直接貼入 Suno 生成歌曲！</div>

    <footer>
        <p>東京・富士五湖・富士宮・伊豆・東京灣 19日秋季單車騎行 ｜ Suno AI 中日雙語男女對唱提示詞庫 (19-Track Album)</p>
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

print("Bilingual Duet HTML successfully generated!")
