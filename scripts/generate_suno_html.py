import sys, json

tracks = [
    {
        "day": 1,
        "date": "11/13 (五)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "世界線の起点：逆流する多摩川の風",
        "title_en": "Starting Line: Riding Against the Tama River",
        "vibe": "J-Rock / 172bpm / 速度感與啟程熱血",
        "anime": "《命運石之門 Steins;Gate》（秋葉原 Radio會館、世界線跳躍）、《飆速宅男》",
        "drama": "《悠長假期》《求婚大作戰》（多摩川堤防夕陽奔跑名場面）",
        "history": "德川家康開創「六鄉渡口」東海道出城門戶；鎌倉倒幕傳奇「分倍河原之戰」",
        "style_prompt": "J-Rock, energetic anime opening, fast tempo 172bpm, driving bassline, bright electric guitar riffs, emotional female vocal, synth arpeggios, Tokyo city pop vibes, powerful drums",
        "lyrics": """[Intro]
(Fast drum roll, energetic distorted guitar riff, retro synth arpeggio)
El Psy Kongroo...
世界線が、いま動き出す！

[Verse 1]
秋葉原 ラジオ会館の影を抜けて
交差点で踏み込む ペダルが音を立てる
ビル街のノイズを 背中に振り切って
銀座から第一京浜 海の匂いへ走る

[Pre-Chorus]
六郷橋を渡れば 目の前に広がる水面
信号のない一本道 遮るものは何もない
まるで『ロングバケーション』の夕暮れのように
胸の奥のモヤモヤが 風にほどけてゆく

[Chorus]
多摩川の風を裂いて 逆流のペダルを回せ！
止まらない鼓動が叫ぶ 僕たちのプロローグ
家康が開いた 古き街道の先へ
どこまでも遠く どこまでも熱く
世界線を変えるスピードで 駆け抜けろ！

[Verse 2]
二子玉川の緑を越えて 府中の杜へ
分倍河原の古戦場 武士たちの夢の跡
スプロケットが刻む 確かなリズム
夕暮れの川面に 富士の影がうっすら揺れる

[Bridge]
「諦めたら そこでレースは終わりだ」
あの日のアニメの言葉が 胸でリフレインする
汗に濡れたハンドルを ギュッと握り直して
明日の峠へ 坂道へ 思いを馳せる

[Chorus]
多摩川の風を裂いて 逆流のペダルを回せ！
止まらない鼓動が叫ぶ 僕たちのプロローグ
家康が開いた 古き街道の先へ
どこまでも遠く どこまでも熱く
世界線を変えるスピードで 駆け抜けろ！

[Outro]
調布の空が 茜色に染まる
五十キロの軌跡を 称えるように
(Guitar solo fading out with bell chimes)
Day One, Complete..."""
    },
    {
        "day": 2,
        "date": "11/14 (六)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "誠の風、秋山街道の静寂",
        "title_en": "The Wind of Makoto: Silence of Akiyama Highway",
        "vibe": "Melodic J-Rock / 和風三味線搖滾 / 155bpm",
        "anime": "《Persona 5》（八王子轉運站）、《搖曳露營△》（山梨林道出發）",
        "drama": "《孤獨的美食家》（高尾山名物蕎麥麵與山間茶屋的療癒）",
        "history": "新選組副長土方歲三故鄉（天然理心流日野宿）；武田信玄重臣小山田氏谷村城",
        "style_prompt": "Melodic J-Rock, Shamisen and heavy electric guitar fusion, 155bpm, driving bass, heroic male vocal, atmospheric, emotional soaring chorus, dramatic anime battle OST style",
        "lyrics": """[Intro]
(Sharp shamisen solo melody, exploding into powerful rock rhythm)

[Verse 1]
浅川のせせらぎに 背中を押され
高尾の山の端が 黄金に色づいてゆく
日野の宿に眠る 『誠』の旗の記憶
土方歳三の残像が 冷たい風を斬る

[Pre-Chorus]
大垂水の喧騒を 鮮やかにかわして
津久井湖の静寂へ 県道三十五号
湖面に映る紅葉が 鏡のように揺れる
孤独なサイクリストを 山が深く迎え入れる

[Chorus]
秋山街道の谷間を 誇り高く駆け抜けろ！
登り坂は苦しみじゃない 魂を研ぎ澄ます砥石だ
武田の騎馬隊が駆けた 甲斐の山並みへ
ギアを落とし 呼吸を整え
限界のその先へ ペダルを踏み込め！

[Verse 2]
木漏れ日がアスファルトに 縞模様を描く
澄み切った秋の空 吸い込まれそうだ
茶屋の蕎麦の香りが どこか懐かしくて
五百メートルの標高差が 誇らしく胸を満たす

[Bridge]
谷村城の石垣が 都留の街で待っている
誰もいない山道で 自分の心と語り合った
風の音だけが 最高のBGM

[Chorus]
秋山街道の谷間を 誇り高く駆け抜けろ！
登り坂は苦しみじゃない 魂を研ぎ澄ます砥石だ
武田の騎馬隊が駆けた 甲斐の山並みへ
ギアを落とし 呼吸を整え
限界のその先へ ペダルを踏み込め！

[Outro]
夕暮れの都留に 響くフリーハブの音
山を越えた者だけが知る 静かな歓喜
(Shamisen outro phrase, soft fade)"""
    },
    {
        "day": 3,
        "date": "11/15 (日)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "神宿る金鳥居：千メートルの夕焼け",
        "title_en": "The Golden Torii: Sunset at 1000 Meters",
        "vibe": "Epic J-Pop / Atmospheric Synth-Rock / 140bpm",
        "anime": "《搖曳露營△》（山中湖夕陽露營、溫泉煮麵）",
        "drama": "《First Love 初戀》（富士山下的命中註定回憶）",
        "history": "江戶時代平民信仰「富士講」；富士吉田金鳥居靈山結界",
        "style_prompt": "Epic J-Pop, Atmospheric Synth-Rock, Inspiring, 140bpm, powerful emotional female vocal, acoustic piano intro, expansive string arrangement, uplifting stadium chorus",
        "lyrics": """[Intro]
(Gentle acoustic piano, distant train bell, atmospheric pad swelling)

[Verse 1]
富士急行の線路沿い 桂川の裏道
澄み切った清流が 坂道を潤してゆく
農道の曲がり角 視界が開けた瞬間
巨大な金鳥居が 青空を貫いていた

[Pre-Chorus]
江戸の昔から 祈りを捧げた富士講の道
標高千メートルの冷気が 頬を刺すけれど
『First Love』の記憶のように
白雪を戴く霊峰が 圧倒的な姿で迫る

[Chorus]
夕焼けの渚 山中湖が紅に染まりゆく！
落葉の絨毯を踏みしめて 辿り着いた天空の湖
湖畔の紅葉祭りが 灯りを灯すころ
富士の頂が 茜色の光を浴びて微笑む
「見てごらん、これが僕たちの登ってきた道だ！」

[Verse 2]
キャンプ場の片隅から 漂う焚き火の匂い
コッヘルで沸かす珈琲が 冷えた身体を包む
志摩リンが見つめた あの星空の下で
ペダルを止めて 静寂に耳を澄ませる

[Bridge]
息を吐くたび 白く輝くクリスタル
登りきった足の痛みが 確かな誇りになる
山中湖の波音が 優しく夜を連れてくる

[Chorus]
夕焼けの渚 山中湖が紅に染まりゆく！
落葉の絨毯を踏みしめて 辿り着いた天空の湖
湖畔の紅葉祭りが 灯りを灯すころ
富士の頂が 茜色の光を浴びて微笑む
「見てごらん、これが僕たちの登ってきた道だ！」

[Outro]
静まり返る湖畔、満天の星
標高千メートルの夜が 更けてゆく
(Piano solo trailing off into night wind ambience)"""
    },
    {
        "day": 4,
        "date": "11/16 (一)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "紅葉回廊のシンフォニー",
        "title_en": "Symphony of the Momiji Corridor",
        "vibe": "Emotional Piano Ballad / Orchestral J-Pop / 125bpm",
        "anime": "《名偵探柯南：往天國的倒數計時》（富士五湖雙塔倒影）、《搖曳露營△》",
        "drama": "《silent》（湖畔靜謐而深情的深秋手語獨白）",
        "history": "忍野八海——數百年火山熔岩過濾之神之湧泉，修驗道聖地",
        "style_prompt": "Emotional Piano Ballad, Orchestral J-Pop, 125bpm, expressive solo violin, acoustic guitar picking, pure melodic vocal, silent drama vibes, cinematic climax",
        "lyrics": """[Intro]
(Gentle piano melody with falling leaves ambience, tender violin solo)

[Verse 1]
忍野八海の底を覗けば
八百年の雪解け水が 碧く透き通っている
湖北ビューラインを 滑るように走る
湖面を渡る風が 黄金の秋を運んでくる

[Pre-Chorus]
言葉にできない 美しさがある
『silent』の静寂が 教えてくれたように
声を出さなくても 心が通い合う
深紅に燃える 六百本の古木の下で

[Chorus]
もみじ回廊！ 燃え盛る光のトンネルを抜けて
赤と金の花吹雪が ホイールを包み込む
今日この日、最高の見頃に出逢えた奇跡
息を呑むほどの鮮やかさに 涙がこぼれそうになる
この深紅の記憶を 永遠に胸に焼き付けて

[Verse 2]
大石公園のコキアが 茜色に揺れて
対岸にそびえる富士が 威厳を放っている
コナンが見上げた 左右対称の完璧な稜線
誰もが立ち止まり 空を見上げる湖畔の午後

[Bridge]
風がひと吹き 赤い葉が水面を流れてゆく
言葉はいらない ただペダルをゆっくり回すだけで
生きてることのすべてが 祝福されている気がした

[Chorus]
もみじ回廊！ 燃え盛る光のトンネルを抜けて
赤と金の花吹雪が ホイールを包み込む
今日この日、最高の見頃に出逢えた奇跡
息を呑むほどの鮮やかさに 涙がこぼれそうになる
この深紅の記憶を 永遠に胸に焼き付けて

[Outro]
夕闇のライトアップが 湖を紅く染める
夢のような一日が 静かに幕を閉じる
(Violin and piano duet softly fading out)"""
    },
    {
        "day": 5,
        "date": "11/17 (二)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "千円札の蒼い鏡：青木ヶ原の風",
        "title_en": "The Thousand-Yen Mirror: Aoki Forest Wind",
        "vibe": "Chillhop / Dreamy Indie Pop / 110bpm",
        "anime": "《搖曳露營△》第一集浩庵露營場逆富士、《蟲師》（青木原樹海生命之息）",
        "drama": "《在世界中心呼喊愛》《四重奏》（深山湖畔的隱逸詩意）",
        "history": "西元864年「貞觀大噴發」熔岩分開古代剗之海；岡田紅陽「湖畔之春」千圓逆富士",
        "style_prompt": "Chillhop, Dreamy Indie Pop, Lo-Fi Electric Guitar, 110bpm, soft male vocal, ambient synth pads, mellow brass, relaxing groove, cozy autumn vibe",
        "lyrics": """[Intro]
(Vinyl crackle, warm jazzy guitar chords, soft acoustic drum beat)
あの千円札の景色へ...

[Verse 1]
西湖いやしの里 茅葺き屋根の懐かしさ
貞観の噴火が分けた 古代の湖の物語
青木ヶ原樹海の 溶岩の隙間から
生命の息吹が 蒼い苔を撫でてゆく

[Pre-Chorus]
精進湖の畔で 見つけた『子抱き富士』
小さな山を抱きしめる 優しいシルエット
財布からそっと取り出した 千円札をかざせば
目の前の本棲湖と ピタリと重なり合う

[Chorus]
浩庵の湖畔に広がる 完璧な逆さ富士！
波ひとつない水面が 蒼い鏡になる瞬間
カレー麺の湯気と 澄んだ冷気の中で
僕らは世界で一番 贅沢な孤独を知る
「千円札の裏側に隠された、僕たちの秘密基地！」

[Verse 2]
湖北のワインディングを 軽やかにトレースして
落ち葉を踏みしめる サクサクという足音
『四重奏』のメロディが どこからか聴こえるような
静かで、美しくて、少し切ない湖水巡礼

[Bridge]
観光バスのいない裏道 湖と語り合う時間
チェーンのオイルの匂いと 針葉樹の深いアロマ
この瞬間だけは 世界が僕のために止まっている

[Chorus]
浩庵の湖畔に広がる 完璧な逆さ富士！
波ひとつない水面が 蒼い鏡になる瞬間
カレー麺の湯気と 澄んだ冷気の中で
僕らは世界で一番 贅沢な孤独を知る
「千円札の裏側に隠された、僕たちの秘密基地！」

[Outro]
本棲湖の青が 藍色へと深まってゆく
水面に揺れる富士山、心の中の宝物
(Guitar riff fading out with soft synth chime)"""
    },
    {
        "day": 6,
        "date": "11/18 (三)",
        "stage": "stage1",
        "stage_name": "第一階段：多摩川出城 ➔ 富士五湖賞楓",
        "title": "新倉山絵葉書：五重塔と富士の休日",
        "title_en": "Arakurayama Postcard: The Pagoda and Rest Day",
        "vibe": "City Pop / Relaxed Groove / 118bpm",
        "anime": "《你的名字。》（時空交錯鳥居）、《進擊的巨人》（孤傲俯瞰視角）",
        "drama": "《First Love 初戀》（富士吉田本町通巨大富士街景）、《重啟人生》",
        "history": "新倉山淺間公園忠靈塔；富士吉田傳承數百年「甲斐絹」織物宿場文化",
        "style_prompt": "Japanese City Pop, Relaxed Groove, 118bpm, smooth saxophone solo, funky bass, vintage electric piano, breezy female vocal, sunny nostalgic vibe",
        "lyrics": """[Intro]
(Funky bassline, bright electric piano chords, silky smooth saxophone)

[Verse 1]
三百九十八段の 階段を一歩ずつ
今日はペダルを休めて スニーカーで登る丘
新倉山の頂で 振り返った瞬間に
世界が息を呑んだ 絵葉書が動き出す

[Pre-Chorus]
朱塗りの忠霊塔と 燃え盛る紅葉のグラデーション
その背後にそびえ立つ 堂々たる白雪の富士
『First Love』の本町通を 見下ろせば
レトロな看板の向こうに 暮らしの息づかい

[Chorus]
シャッターを切るたび 永遠になる秋の午後！
急がない旅だから 見つけられた宝物
甲斐絹の機織りの音が どこか懐かしくて
チェーンを磨いて ブレーキを確かめて
明日へのエネルギーを 満タンにチャージしよう！

[Verse 2]
河口湖のカフェのテラス あたたかいチャイを飲む
湖面を渡る遊覧船が 白い航跡を描く
休養日があるからこそ 長い旅は輝く
靴底の土を払って のんびり笑顔を交わす

[Bridge]
明日は朝霧高原 千メートルのダウンヒル
駿河湾の潮風が 僕らを待っている
でも今日だけは この富士山を独り占め

[Chorus]
シャッターを切るたび 永遠になる秋の午後！
急がない旅だから 見つけられた宝物
甲斐絹の機織りの音が どこか懐かしくて
チェーンを磨いて ブレーキを確かめて
明日へのエネルギーを 満タンにチャージしよう！

[Outro]
本町通の夕暮れに 街灯が灯りだす
完璧な休日に、乾杯！
(Saxophone solo trailing off smoothly)"""
    },
    {
        "day": 7,
        "date": "11/19 (四)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "標高差一千メートルの風：駿河湾へダイブ！",
        "title_en": "A Thousand Meters Descent: Dive into Suruga Bay",
        "vibe": "High-Energy Surf Rock / Upbeat J-Pop / 168bpm",
        "anime": "《Love Live! Sunshine!!》（Aqours沼津港、千本松原海堤）、《銀之匙》",
        "drama": "《義經》（大河劇瀧澤秀明主演，源賴朝與義經富士野大卷狩）",
        "history": "1193年源賴朝富士之卷狩與曾我兄弟復仇；德川家康還願之淺間大社總本社",
        "style_prompt": "High-Energy Surf Rock, Upbeat J-Pop, 168bpm, fast acoustic strumming, thunderous drum fills, driving electric guitar, triumphant brass section, euphoric chorus",
        "lyrics": """[Intro]
(Fast acoustic guitar strumming, soaring trumpet fanfare, countdown: 3, 2, 1, GO!)

[Verse 1]
朝霧高原の朝は白い 朝露が光る牧場
気温二度の冷気を切り裂いて ダウンヒルが始まる！
鳴沢を抜けて ぐんぐん落ちてゆく標高計
ブレーキをコントロールして 重力とダンスする

[Pre-Chorus]
白糸の滝の水しぶきが 紅葉を濡らしている
源頼朝が狩りをした 富士の巻狩りの古戦場
浅間大社の湧玉池で 旅の安全を祈ったら
潤井川のサイクリングロードを 海へ一直線！

[Chorus]
標高差一千メートル！ 駿河湾の海風へ飛び込め！
田子の浦の港から 千本松原の堤防ロード
車が一台もいない 僕たちだけの専用コース
右手にはどこまでも青い太平洋
振り返れば 圧倒的な富士山が見送ってくれる！

[Verse 2]
『Love Live! Sunshine!!』の Aqoursが走った道
沼津港の潮の香りと 新鮮な海鮮丼
危険な国道バイパスを 鮮やかに迂回して
千本の黒松が並ぶ 砂浜の道を駆け抜ける

[Bridge]
高原の寒さから 駿河のあたたかな陽光へ
わずか数時間で 世界がガラリと変わる
このダイナミックな変化こそ 単車の旅の真骨頂！

[Chorus]
標高差一千メートル！ 駿河湾の海風へ飛び込め！
田子の浦の港から 千本松原の堤防ロード
車が一台もいない 僕たちだけの専用コース
右手にはどこまでも青い太平洋
振り返れば 圧倒的な富士山が見送ってくれる！

[Outro]
三島大社の杜に 夕暮れの鐘が鳴る
山から海へ、最高の七十二キロ！
(Surf rock guitar tremolo finish)"""
    },
    {
        "day": 8,
        "date": "11/20 (五)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "逃げ恥の足音：修善寺・竹林の小径",
        "title_en": "Footsteps of Escape: Shuzenji Bamboo Path",
        "vibe": "Traditional Japanese Enka-Pop / Lo-Fi Lounge / 115bpm",
        "anime": "《夏目友人帳》（名湯竹林與妖怪和風物語）",
        "drama": "《月薪嬌妻 / 逃避雖可恥但有用》（新垣結衣與星野源蜜月溫泉之旅修善寺桂橋）",
        "history": "西元807年弘法大師空海開山獨鈷之湯；鎌倉二代將軍源賴家幽禁修禪寺物語",
        "style_prompt": "Modern Japanese Enka-Pop fusion, Lo-Fi Lounge, 115bpm, bamboo flute Shakuhachi, plucked Shamisen, warm double bass, sweet romantic vocal, cozy onsen atmosphere",
        "lyrics": """[Intro]
(Gentle river sound, bamboo flute melody, soothing electric piano chords)

[Verse 1]
狩野川のサイクリングロード 水鳥が羽ばたく
三島から修善寺へ 緩やかな川沿いルート
アンダーパスをくぐり抜け 伊豆の奥座敷へ
坂道を感じさせない 穏やかな秋のポタリング

[Pre-Chorus]
桂川にかかる 朱塗りの桂橋
『逃げるは恥だが役に立つ』の みくりと平匡のように
少しぎこちなく でも確かに寄り添って
竹林の小径の丸いベンチに 腰を下ろす

[Chorus]
修善寺温泉 紅葉が湯煙に揺れている
空海が突いた 独鈷の湯の温もり
源氏の哀しい歴史も 今は優しい秋の色
温泉旅館の暖簾をくぐって 浴衣に着替えたら
疲れた脚を名湯に沈めて 最高の至福へ！

[Verse 2]
虹の郷の紅葉が イギリス村を染め上げる
古刹・修禅寺の境内に 響く鐘の音
伊豆の小京都が魅せる 雅やかな深秋
急ぐ理由なんて ここには何一つない

[Bridge]
三連休の前夜 静寂が街を包み込む
温泉街の灯篭に ぽっと明かりが灯るころ
ペダルを置いた旅人は 夢の中へと溶けてゆく

[Chorus]
修善寺温泉 紅葉が湯煙に揺れている
空海が突いた 独鈷の湯の温もり
源氏の哀しい歴史も 今は優しい秋の色
温泉旅館の暖簾をくぐって 浴衣に着替えたら
疲れた脚を名湯に沈めて 最高の至福へ！

[Outro]
川のせせらぎ、竹の葉のささやき
おやすみなさい、伊豆の秋
(Shakuhachi fading out with gentle stream sound)"""
    },
    {
        "day": 9,
        "date": "11/21 (六)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "火曜サスペンスの断崖：城ヶ崎の白波",
        "title_en": "Suspense Cliff: The White Waves of Jogasaki",
        "vibe": "Dramatic Symphonic Rock / Mysterious / 148bpm",
        "anime": "《名偵探柯南》（崖邊真相大白名場面）、《藍海少女！Amanchu!》",
        "drama": "《火曜懸疑劇場》（國民懸疑劇聖地——門脇吊橋與懸崖最後自白）、《華麗一族》",
        "history": "4000年前大室山火山噴發熔岩海岸柱狀節理；川端康成《伊豆的舞孃》漫步之道",
        "style_prompt": "Dramatic Symphonic Rock, Mysterious, 148bpm, heavy electric guitar riffs, grand orchestral strings, gothic organ accents, powerful intense vocal, cinematic anime OST",
        "lyrics": """[Intro]
(Crashing ocean waves, suspenseful orchestral strings, dramatic heavy guitar chord)

[Verse 1]
冷川峠の九十九折り 静かに高度を上げてゆく
天城越えの険しさをかわし 中伊豆を横断する
一碧湖の『伊豆の瞳』に 映る紅葉の赤
鏡のような水面を過ぎれば 潮の香りが濃くなる

[Pre-Chorus]
四千年前 大室山の溶岩が海へ流れ込み
造り出した溶岩の彫刻 門脇埼灯台
サスペンス劇場のラストシーンのように
波しぶきが 断崖絶壁に牙を剥く

[Chorus]
城ヶ崎の吊橋を 渡れば足がすくむ！
高さ二十三メートル 眼下に渦巻く太平洋
犯人の告白を呑み込むような 轟音の白波
冷川峠を越えてきた僕らの 誇らしいアドベンチャー
「真実はいつも、このペダルの先にある！」

[Verse 2]
『あまんちゅ！』の少女たちが 潜った伊豆の海
吸い込まれそうなコバルトブルーが どこまでも広がる
三連休の車の列を 横目に眺めながら
自由な二輪の軌跡を 海岸線に刻みつける

[Bridge]
夕日が水平線に 沈んでゆく瞬間
断崖の溶岩が 黄金色に輝きだす
自然が創り出した 圧倒的なドラマ

[Chorus]
城ヶ崎の吊橋を 渡れば足がすくむ！
高さ二十三メートル 眼下に渦巻く太平洋
犯人の告白を呑み込むような 轟音の白波
冷川峠を越えてきた僕らの 誇らしいアドベンチャー
「真実はいつも、このペダルの先にある！」

[Outro]
波の咆哮と 門脇灯台の白い光
伊豆高原の夜が 幕を開ける
(Heavy guitar chord ringing out over ocean waves)"""
    },
    {
        "day": 10,
        "date": "11/22 (日)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "熱海月夜：日本一遅い紅葉と金色夜叉",
        "title_en": "Atami Moonlight: The Late Foliage and Golden Demon",
        "vibe": "80s City Pop / Nostalgic Synth-Wave / 120bpm",
        "anime": "《狂賭之淵》《蠟筆小新：溫泉青春大決戰》",
        "drama": "《熱海的搜查官》（小田切讓奇幻探案）、《長假》（木村拓哉）",
        "history": "明治尾崎紅葉《金色夜叉》貫一宮之松訣別；德川家康命人快遞熱海溫泉水至江戶",
        "style_prompt": "80s Japanese City Pop, Nostalgic Synth-Wave, 120bpm, melancholic trumpet solo, groovy slap bass, shimmering vintage synthesizers, smooth emotional male/female duet",
        "lyrics": """[Intro]
(Nostalgic synth pads, groovy 80s drum beat, soulful muted trumpet solo)

[Verse 1]
朝七時半 宇佐美の海を静かに出発する
魔のトンネルを賢くかわして 網代港の旧街道
漁船が並ぶ生活道路 潮風が心地いい
伊東から熱海へと 繋がる海岸のプロムナード

[Pre-Chorus]
お宮の松の前に立てば 貫一の叫びが聴こえる
「来年の今月今夜の この月を僕の涙で曇らせてみせる」
金色夜叉の哀愁を 潮騒が優しく包み
サンビーチのヤシの木が ネオンに照らされる

[Chorus]
熱海梅園 日本で一番遅い紅葉が咲き誇る！
深紅のモミジと 早咲きの白梅が手をつなぐ奇跡
家康公も愛した 熱海の名湯に身を委ねて
昭和のレトロな街並みを 浴衣で歩く夜
「さよならの涙さえ 恋しくなる熱海の月！」

[Verse 2]
危険な国道をクリアした サイクリストの勝利宣言
JR伊東線の輪行という 秘密のカードをポケットに
無理をせず、賢く安全に 旅を紡いでゆく
これこそが大人の 自由な冒険スタイル

[Bridge]
湯前神社の源泉から 立ち上る白い蒸気
温泉まんじゅうの甘さが 身体中に染み渡る
昭和と令和が交差する 不思議な熱海の夜

[Chorus]
熱海梅園 日本で一番遅い紅葉が咲き誇る！
深紅のモミジと 早咲きの白梅が手をつなぐ奇跡
家康公も愛した 熱海の名湯に身を委ねて
昭和のレトロな街並みを 浴衣で歩く夜
「さよならの涙さえ 恋しくなる熱海の月！」

[Outro]
熱海湾に浮かぶ 月の道（ムーンロード）
波音に溶けてゆく トランペットの余韻
(Muted trumpet solo fading out softly)"""
    },
    {
        "day": 11,
        "date": "11/23 (一)",
        "stage": "stage2",
        "stage_name": "第二階段：朝霧駿河灣海堤 ➔ 伊豆名湯紅葉祭",
        "title": "蜜柑色の坂道：難攻不落の小田原城",
        "title_en": "Mandarin Orange Slopes: Impregnable Odawara",
        "vibe": "Upbeat J-Pop / Brass Rock / 145bpm",
        "anime": "《飆速宅男》（箱根學園起點、小田原出發衝刺）、《頭文字D》",
        "drama": "《真田丸》《軍師官兵衛》（黑田官兵衛說降北條氏政、小田原征伐）",
        "history": "1590年豐臣秀吉小田原征伐滅後北條氏天下統一；縣道740號俯瞰白糸川鐵橋",
        "style_prompt": "Upbeat J-Pop, Brass Rock, 145bpm, punchy horn section, driving electric rhythm guitar, cheerful energetic vocal, bright triumphant chorus, sunny coastal vibe",
        "lyrics": """[Intro]
(Punchy brass fanfare, crisp electric guitar groove, upbeat drums)

[Verse 1]
熱海を抜けて 湯河原の坂を越えてゆく
真鶴駅前で見逃すな 神奈川県道七四零！
危険なトンネルをすべて 眼下に見下ろしながら
山腹の絶景ロードへと ハンドルを切る

[Pre-Chorus]
たわわに実る 黄金色の温州みかん
潮風を浴びて 太陽の光を吸い込んでいる
白糸川橋梁を 渡る東海道線の電車
まるでジオラマのような 相模湾の青いパノラマ

[Chorus]
蜜柑色の坂道を 軽やかに駆け上がれ！
斜度五パーセントの坂は 絶景へのプロムナード
『弱虫ペダル』の箱根学園が 駆けた風を感じて
難攻不落の小田原城へ 凱旋のペダルを回せ！
「天下一統の城が、僕らを待っている！」

[Verse 2]
早川漁港の賑わい アジフライの香ばしさ
小田原城址公園の お濠に映る天守閣
官兵衛が説き伏せた 北條五代の栄華の夢
白壁と紅葉が 晴天の空に美しく映える

[Bridge]
真鶴道路の車の渋滞を 完全に迂回した爽快感
地元のチャリダーが愛する 秘密の裏ルート
知恵と勇気があれば 旅は百倍楽しくなる！

[Chorus]
蜜柑色の坂道を 軽やかに駆け上がれ！
斜度五パーセントの坂は 絶景へのプロムナード
『弱虫ペダル』の箱根学園が 駆けた風を感じて
難攻不落の小田原城へ 凱旋のペダルを回せ！
「天下一統の城が、僕らを待っている！」

[Outro]
小田原城の天守に 翻る風
明日は湘南の海へ！
(Triumphant brass coda, big cymbal crash)"""
    },
    {
        "day": 12,
        "date": "11/24 (二)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "烏帽子岩の風：スラムダンクの海岸線",
        "title_en": "Eboshi Rock Breeze: The Slam Dunk Coastline",
        "vibe": "90s Anime Pop-Rock / ZARD / WANDS style / 138bpm",
        "anime": "《灌籃高手 SLAM DUNK》（流川楓湘南海岸晨騎）、《青春豬頭少年不會夢到兔女郎學姐》",
        "drama": "《有喜歡的人》（湘南海岸浪漫物語）、《海灘男孩 Beach Boys》",
        "history": "歌川廣重東海道五十三次（平塚、大磯宿）；南方之星桑田佳祐故鄉茅崎烏帽子岩",
        "style_prompt": "90s Anime Pop-Rock, ZARD style, 138bpm, bright overdrive guitar chords, driving bass, nostalgic pop melody, clear inspiring female/male vocal, uplifting summer/autumn seaside vibe",
        "lyrics": """[Intro]
(Classic 90s guitar intro melody, catchy straight rock drum beat)

[Verse 1]
小田原を出て 国道一号線の広い路肩
大磯の宿場町を抜けて 湘南の海へ出る
防風林の松並木が 海風を遮って
国道百三十四号線 平坦なクルージング

[Pre-Chorus]
砂浜のサイクリングロード 砂を避けて走る
ヘッドホンから流れる 懐かしいあのメロディ
茅ヶ崎の沖合に浮かぶ 烏帽子岩のシルエット
桑田佳祐が歌った 青春の海が広がる

[Chorus]
波音に合わせて ペダルを回せ！ 湘南の風になれ！
遠く江ノ島のシーキャンドルが 呼んでいる
流川が自転車で走った あの海岸線
真っ直ぐな青空と どこまでも続く水平線
「世界が終わるまでは、この道を走り続けたい！」

[Verse 2]
江ノ島大橋を渡れば 弁天様の島
『青ブタ』の聖地に 舞い降りるカモメの影
しらす丼の湯気が 潮風に混ざり合って
平坦路三十八キロの 心地よい達成感

[Bridge]
冬の透明な空気の向こう
相模湾越しに見える 富士山の白い冠
海と富士山を同時に抱きしめる 贅沢な湘南ライド

[Chorus]
波音に合わせて ペダルを回せ！ 湘南の風になれ！
遠く江ノ島のシーキャンドルが 呼んでいる
流川が自転車で走った あの海岸線
真っ直ぐな青空と どこまでも続く水平線
「世界が終わるまでは、この道を走り続けたい！」

[Outro]
江ノ島の夕焼けが 相模湾を染めてゆく
明日は古都・鎌倉へ
(Guitar solo fading out with gentle ocean surf)"""
    },
    {
        "day": 13,
        "date": "11/25 (三)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "いざ、鎌倉！踏切の晴子と柏尾川",
        "title_en": "Iza Kamakura! Haruko at the Crossing & Kashio River",
        "vibe": "Indie Folk / J-Acoustic Pop / 128bpm",
        "anime": "《灌籃高手》（鎌倉高校前平交道世紀揮手）、《孤獨搖滾！》《海街日記》",
        "drama": "《倒數第二次戀愛》（小泉今日子極樂寺長谷寺浪漫）、《海街日記》（四姊妹梅酒）",
        "history": "1185年源賴朝創立鎌倉幕府（「いざ、鎌倉！」）；鶴岡八幡宮；柏尾川水岸步道",
        "style_prompt": "Indie Folk, J-Acoustic Pop, 128bpm, acoustic guitar fingerpicking, melodic upright piano, warm cello lines, gentle nostalgic vocal, breezy autumn city vibe",
        "lyrics": """[Intro]
(Acoustic guitar strumming, bell chime of a railroad crossing: dang-dang-dang)

[Verse 1]
朝八時の 鎌倉高校前踏切
まだ観光客のいない 静かな七里ヶ浜
江ノ電の緑の車体が カタコト通り過ぎて
遮断機が上がった瞬間 海がキラリと光った

[Pre-Chorus]
晴子さんが手を振っていた あの伝説の場所
長谷寺の紅葉と 極楽寺の古き切通し
『最後から二番目の恋』の 大人の時間が流れる
鶴岡八幡宮の段葛を 厳かに通り抜ける

[Chorus]
「いざ、鎌倉！」 武士たちの誇りを胸に刻み
北鎌倉の古刹から 大船へ抜け出そう
危険な峠を避けて 柏尾川プロムナードへ
川沿いの平坦な緑道が 横浜へと僕らを導く
「踏切を越えたら、新しい物語が走り出す！」

[Verse 2]
戸塚を抜けて 旧東海道の緩やかな坂
保土ヶ谷の宿場を越えれば 空港の匂いが近づく
みなとみらいの観覧車が ランドマークタワーの横で
夕暮れの空に レインボーの光を灯す

[Bridge]
古都の静寂から 近未来の港町へ
タイムスリップするように 景色が移り変わる
三十三キロの道程が あっという間に過ぎてゆく

[Chorus]
「いざ、鎌倉！」 武士たちの誇りを胸に刻み
北鎌倉の古刹から 大船へ抜け出そう
危険な峠を避けて 柏尾川プロムナードへ
川沿いの平坦な緑道が 横浜へと僕らを導く
「踏切を越えたら、新しい物語が走り出す！」

[Outro]
横浜港の潮風と 輝くベイブリッジ
明日は東京湾へ帰還する
(Acoustic guitar chord fading out with foghorn in distance)"""
    },
    {
        "day": 14,
        "date": "11/26 (四)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "踊る大捜査線：豊洲大橋とガンダムの空",
        "title_en": "Bayside Line: Toyosu Bridge & Gundam Skyline",
        "vibe": "Modern Electro-Pop / Synth-Pop / 130bpm",
        "anime": "《機動戰士鋼彈》（台場獨角獸立像）、《數碼寶貝》（富士電視台大激戰）、《文豪野犬》",
        "drama": "《大搜查線》（「無法封鎖彩虹大橋！」經典台詞）、《戀愛可以持續到天長地久》",
        "history": "1853年培里黑船來航橫濱開港；江戶末期防衛黑船之品川砲台（台場）；現代豐洲大橋",
        "style_prompt": "Modern Electro-Pop, Synth-Pop, 130bpm, driving synth bass, infectious 808 beats, sparkling futuristic synthesizers, bright energetic female vocal, Tokyo skyline vibe (Yoasobi / Perfume style)",
        "lyrics": """[Intro]
(Futuristic synth arpeggio, punchy four-on-the-floor beat, sweeping filter)
「レインボーブリッジ、封鎖できません！」
でも、僕らには豊洲大橋がある！

[Verse 1]
山下公園の銀杏が 金色に舞い散る朝
ペリーの黒船が来た 横浜港に別れを告げて
鶴見を越えて 羽田の大鳥居へ
多摩川の河口で 海の匂いと再会する

[Pre-Chorus]
勝どき橋を渡り 築地の熱気を感じながら
レインボーブリッジの押し歩きはパスして
最新の豊洲大橋 自転車専用レーンへ！
遮るもののない 東京湾のパノラマへ駆け上がる

[Chorus]
お台場の空へ！ 未来都市のハイウェイを突き抜けろ！
フジテレビの球体が 夕日を浴びて輝く
等身大のガンダムが 僕らを見下ろしている
黒船を防いだ砲台の島は 今や未来のワンダーランド
「レインボーブリッジを渡らなくても、僕らの道は繋がっている！」

[Verse 2]
有明のモダンな建築群 タイヤのスキール音
都会の風を切り裂いて走る この爽快感
夜になれば 摩天楼の灯りが海に反射して
まるで映画の主人公になったような気分

[Bridge]
十七日間の旅が 都会の真ん中で光り輝く
ペダルを回す脚には もう恐れる坂はない
東京湾の天際線が 僕たちを歓迎している

[Chorus]
お台場の空へ！ 未来都市のハイウェイを突き抜けろ！
フジテレビの球体が 夕日を浴びて輝く
等身大のガンダムが 僕らを見下ろしている
黒船を防いだ砲台の島は 今や未来のワンダーランド
「レインボーブリッジを渡らなくても、僕らの道は繋がっている！」

[Outro]
台場海浜公園の夜景、輝く自由の女神
都会の夜が、きらめいている
(Synth arpeggio echoing away into electronic beats)"""
    },
    {
        "day": 15,
        "date": "11/27 (五)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "荒川アンダー・ザ・ブリッジ：金八先生の土手",
        "title_en": "Arakawa Under the Bridge: Kinpachi Sunset Path",
        "vibe": "Quirky J-Rock / Upbeat Ska-Punk / 160bpm",
        "anime": "《荒川爆笑團》（小招與小珊荒川橋下戀愛）、《魔法少女小圓》（葛西臨海公園齒輪）",
        "drama": "《3年B組金八先生》（荒川堤防夕陽奔跑國民記憶）、《山田孝之的東京都北區赤羽》",
        "history": "1911-1930年青山士主持世界級荒川放水路治水大工程；百年岩淵赤水門",
        "style_prompt": "Quirky J-Rock, Upbeat Ska-Punk, 160bpm, walking bassline, punchy ska brass chords, humorous yet energetic vocal, driving drums, cheerful riverside anthem",
        "lyrics": """[Intro]
(Punchy ska brass intro, upbeat guitar upstrokes, cheerful whistle)
荒川右岸！ 車止めは減速だ！

[Verse 1]
葛西臨海公園 ゼロキロポストから
荒川放水路の壮大な ドラマが始まる
清砂大橋を渡って 指名打ちの『右岸』へ！
左岸の砂利道をかわして 完璧なアスファルト

[Pre-Chorus]
橋の下を覗けば 河童の村長がいるのかな？
金星から来た美少女が 笑っているのかな？
『金八先生』が走った あの夕暮れの土手で
ススキの穂が 金色に波打っている

[Chorus]
荒川アンダー・ザ・ブリッジ！ どこまでも続く河川敷！
車止めパイプは 無理せずゆっくり下車してパス
群馬からの赤城おろし 逆風さえも楽しんで
赤羽の赤水門へ 青山士の夢の跡へ
「僕らのペダルは、誰も止められない！」

[Verse 2]
スカイツリーが右手に ずっと付いてくる
野球少年の元気な声と 犬の散歩の長閑さ
山田孝之が愛した 赤羽のディープな街へ
一番街の赤提灯が 旅人を誘っている

[Bridge]
大洪水を防ぐために 掘られた命の川
百年の歴史が育てた サイクリストの聖地
広い空の下を走れる 都会のオアシス

[Chorus]
荒川アンダー・ザ・ブリッジ！ どこまでも続く河川敷！
車止めパイプは 無理せずゆっくり下車してパス
群馬からの赤城おろし 逆風さえも楽しんで
赤羽の赤水門へ 青山士の夢の跡へ
「僕らのペダルは、誰も止められない！」

[Outro]
赤水門の向こうに 沈む大きな夕日
赤羽の夜に、乾杯！
(Ska brass fanfare with cheerful laugh)"""
    },
    {
        "day": 16,
        "date": "11/28 (六)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "月がきれい：小江戸川越・時の鐘",
        "title_en": "The Moon is Beautiful: Little Edo Kawagoe",
        "vibe": "Emotional Anime OST Ballad / 132bpm",
        "anime": "《月色真美》（安曇小太郎與水野茜純愛聖地、冰川神社風鈴）、《元氣少女緣結神》",
        "drama": "《JIN 仁醫》（江戶防火藏造黑瓦老街風貌）、晨間劇《つばさ》",
        "history": "川越藩主松平信綱城下町；喜多院藏有江戶城唯一留存「德川家光誕生之間」「春日局化妝之間」",
        "style_prompt": "Emotional Anime OST Ballad, 132bpm, acoustic guitar arpeggios, melodic grand piano, sweet expressive strings, heartfelt vocal, nostalgic Japanese town atmosphere",
        "lyrics": """[Intro]
(Gentle chime of the Toki no Kane bell, tender piano melody, soft wind chimes)

[Verse 1]
荒川右岸から 入間川の専用道へ
埼玉の田園風景を 抜けてゆく一本道
黒漆喰の蔵造りが 並ぶ一番街
タイムスリップしたような 小江戸の街並みへ

[Pre-Chorus]
『月がきれい』の二人が 歩いた菓子屋横丁
氷川神社の大銀杏が 黄金の雨を降らせる
時の鐘がゴーンと響き 街に時を告げる
茜さんの笑顔が どこかに揺れているような

[Chorus]
「月がきれいですね」 あの純粋な告白のように
喜多院の紅葉山庭園 真っ赤に染まる秋
徳川家光が生まれた 江戸城の部屋のぬくもり
五十六キロの長い道も 愛おしい思い出になる
「時を越えて響く鐘の音に、僕らの青春を重ねて！」

[Verse 2]
蔵造りのスタバの庭で ひと息つく贅沢
太麺焼きそばの湯気が 食欲をそそる
帰りの入間川は 追い風が背中を押してくれる
夕暮れの荒川へと スムーズに滑り込む

[Bridge]
急ぐ旅じゃないから 寄り道が一番楽しい
小江戸の風情を 心のアルバムにしまって
茜色の空に向かって ペダルを踏み出す

[Chorus]
「月がきれいですね」 あの純粋な告白のように
喜多院の紅葉山庭園 真っ赤に染まる秋
徳川家光が生まれた 江戸城の部屋のぬくもり
五十六キロの長い道も 愛おしい思い出になる
「時を越えて響く鐘の音に、僕らの青春を重ねて！」

[Outro]
夜空に浮かぶ 澄み切った満月
「今夜の月は、本当にきれいだ」
(Piano solo trailing off with distant bell toll)"""
    },
    {
        "day": 17,
        "date": "11/29 (日)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "メタセコイアの黄金森：寅さんと両さんの下町",
        "title_en": "Golden Metasequoia Forest: Tora-san & Ryotsu Downtown",
        "vibe": "Nostalgic Folk-Pop / Accordion & Acoustic Guitar / 122bpm",
        "anime": "《烏龍派出所》（兩津勘吉故鄉葛飾柴又、淺草回憶）、《鬼滅之刃》（大正繁華淺草）",
        "drama": "《男人真命苦 / 寅次郎的故事》（渥美清國民電影殿堂、柴又帝釋天參道草餅）",
        "history": "東京最大水鄉「葛飾水元公園」一萬棵水杉林；江戶將軍鷹狩地；淺草寺町人文化",
        "style_prompt": "Nostalgic Folk-Pop, Accordion and Acoustic Guitar, 122bpm, cheerful whistling, warm walking bass, heartwarming male/female vocal, retro downtown Tokyo vibe",
        "lyrics": """[Intro]
(Warm accordion melody, acoustic guitar strumming, cheerful whistle melody)

[Verse 1]
荒川を南下して 葛飾の水郷へ
水元公園のゲートをくぐった 瞬間の息を呑む静寂
一万本のメタセコイアが レンガ色に染まり
小合溜の水面に 完璧な黄金の森を映す

[Pre-Chorus]
柴又帝釋天の参道 草団子の甘い香り
「私、生まれも育ちも葛飾柴又です」
寅さんがトランクを持って 歩いたあの木橋
両津勘吉の破天荒な 笑い声が響いてくる

[Chorus]
メタセコイアの黄金の森 下町の温もりに抱かれて！
東京の果てで見つけた おとぎ話のような世界
隅田川の風に吹かれて 浅草の雷門へ
大正ロマンの匂い残る 浅草寺の赤い灯籠
「男はつらいよ、だけど旅はこんなにも素晴らしい！」

[Verse 2]
吾妻橋から見上げる アサヒビールの金の炎
スカイツリーが夕暮れの空に 紫に点灯する
昭和情話と現代が 仲良く手をつなぐ街
下町のチャリ散歩は どこか優しくて温かい

[Bridge]
水杉の落ち葉をサクサク 踏みしめた車輪
江戸の粋と 庶民の笑顔がくれた元気
旅の終わりが近づく 切なさを包み込んでくれる

[Chorus]
メタセコイアの黄金の森 下町の温もりに抱かれて！
東京の果てで見つけた おとぎ話のような世界
隅田川の風に吹かれて 浅草の雷門へ
大正ロマンの匂い残る 浅草寺の赤い灯籠
「男はつらいよ、だけど旅はこんなにも素晴らしい！」

[Outro]
浅草の夜風に 揺れる赤提灯
寅さん、今日もいい旅だったよ
(Accordion outro melody with cheerful whistle)"""
    },
    {
        "day": 18,
        "date": "11/30 (一)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "神宮外苑イチョウ並木：カンチ、バイバイ！",
        "title_en": "Jingu Gaien Gingko Avenue: Kanchi, Bye-bye!",
        "vibe": "Classic 90s City Pop / Romantic Big Band J-Pop / 126bpm",
        "anime": "《東大特訓班 / 龍櫻》（阿部寬帶領考取東大赤門）、《天氣之子》（新海誠神宮外苑）",
        "drama": "《東京愛情故事》（赤名莉香神宮外苑銀杏下經典訣別）、《HERO》（木村拓哉檢察官大道）",
        "history": "東京大學加賀藩前田家赤門（1827年迎娶德川將軍之女建）；神宮外苑繪畫館；皇居江戶城跡",
        "style_prompt": "Classic 90s City Pop, Romantic Big Band J-Pop, 126bpm, Tatsuro Yamashita style, lush brass arrangement, sparkling electric piano, soaring saxophone solo, emotional triumphant vocal",
        "lyrics": """[Intro]
(Lush brass fanfare, sparkling electric piano chords, groovy 90s drum groove)
「ねえ、カンチ！ 好きって言ったじゃん！」

[Verse 1]
上野の森を抜けて 本郷の東京大学へ
加賀藩前田家の 赤門をくぐり抜ける
『ドラゴン桜』の生徒たちが 見上げた大銀杏
黄色い絨毯が キャンパスを埋め尽くしている

[Pre-Chorus]
皇居のお濠沿い パレスサイドを滑らかに巡り
ついに辿り着いた 青山・明治神宮外苑
三百メートルの銀杏並木が 円錐形の黄金のトンネル
『HERO』の久利生公平のように 前を向いて歩き出す

[Chorus]
「カンチ、バイバイ！」 あの名シーンのイチョウ並木で！
頭上から降り注ぐ 眩い黄金のシャワー
七百四十キロを 走り抜いてきた僕らの脚が
この黄金の絨毯の上で 誇らしげに輝いている
「東京の秋の最高峰、いま僕らはその中心にいる！」

[Verse 2]
絵画館のクラシックなドーム 晴天の青空とのコントラスト
『天気の子』の雨上がりのように 澄み切った都心の午後
秋葉原へと戻る道 すべての景色が愛おしい
十九日間の冒険が クライマックスを迎える

[Bridge]
最初は遠かった 富士山も、伊豆の海も、湘南の波も
全部この二本の足で 繋いできたんだ
自分を少しだけ 好きになれた気がするよ

[Chorus]
「カンチ、バイバイ！」 あの名シーンのイチョウ並木で！
頭上から降り注ぐ 眩い黄金のシャワー
七百四十キロを 走り抜いてきた僕らの脚が
この黄金の絨毯の上で 誇らしげに輝いている
「東京の秋の最高峰、いま僕らはその中心にいる！」

[Outro]
イチョウの葉が 一枚、肩に舞い落ちる
最高のフィナーレへ、ラストスパート！
(Saxophone solo soaring over big band brass climax)"""
    },
    {
        "day": 19,
        "date": "12/01 (二)",
        "stage": "stage3",
        "stage_name": "第三階段：湘南海岸 ➔ 古都鎌倉 ➔ 都心黃金銀杏",
        "title": "エル・プサイ・コングルゥ：帰還のスカイライナー",
        "title_en": "El Psy Kongroo: Skyliner of Return",
        "vibe": "Epic Anime Ending / Emotional Rock & Piano / 142bpm",
        "anime": "《命運石之門 Steins;Gate》（世界線收斂終點與新起點「El Psy Kongroo」）、《Love Live!》",
        "drama": "《電車男》（秋葉原純愛奇蹟）、《空中急診英雄 Code Blue》（成田疾馳）",
        "history": "秋葉原從明治鎮火神社演變為全球次文化聖地；京成Skyliner 160km/h直達成田完成圓滿閉環",
        "style_prompt": "Epic Anime Ending, Emotional Rock & Piano Outro, 142bpm, uplifting strings, driving drums, distorted guitar chords, passionate triumphant male/female vocal, cinematic finale",
        "lyrics": """[Intro]
(Gentle acoustic piano playing Day 1 theme, then swelling with epic strings and rock drums)
神田明神の石段で 合掌...
すべての道に、ありがとう。

[Verse 1]
神田明神に立ち寄り 旅の無事を感謝して
秋葉原の裏通り 懐かしい景色の中へ
CycleTrip Base の看板が見えてくる
十九日間、苦楽を共にした 相棒のロードバイク

[Pre-Chorus]
チェーンの油汚れも タイヤの細かな傷も
すべてが僕たちの かけがえのない勲章だ
バイクを返却して 輪行袋をたたんだら
日暮里のホームで スカイライナーを待つ

[Chorus]
エル・プサイ・コングルゥ！ 世界線はここに収束した！
時速百六十キロ 成田空港へ滑空する窓の外
富士五湖の紅葉も 伊豆の温泉も 湘南の風も
走馬灯のように 胸の中で永遠に回り続ける
「さようなら、そしてありがとう！ 最高の日本単車旅！」

[Verse 2]
『電車男』が生まれた街から 『コード・ブルー』の空へ
夕暮れの成田の滑走路 飛行機が飛び立ってゆく
パスポートを握りしめ ゲートへと歩き出す
足の筋肉の心地よい張りが 旅の余韻を教えてくれる

[Bridge]
終わるんじゃない これは新しい始まりなんだ
日常に戻っても 僕たちの胸には
あの富士山の圧倒的な姿と 仲間たちの笑顔がある

[Chorus]
エル・プサイ・コングルゥ！ 世界線はここに収束した！
時速百六十キロ 成田空港へ滑空する窓の外
富士五湖の紅葉も 伊豆の温泉も 湘南の風も
走馬灯のように 胸の中で永遠に回り続ける
「さようなら、そしてありがとう！ 最高の日本単車旅！」

[Outro]
飛行機が雲を突き抜けて 星空へ舞い上がる
(Piano solo reprises the Day 1 main theme)
十九日間のすべての瞬間に...
エル・プサイ・コングルゥ。
[End]"""
    }
]

html_template = f"""<!DOCTYPE html>
<html lang="zh-TW">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>東京・富士・伊豆・東京灣 單車騎旅 19日 Suno AI 音樂創作專屬提示詞庫</title>
    <style>
        :root {{
            --primary: #8C2D19;
            --primary-light: #FDF6F0;
            --secondary: #2B4C59;
            --secondary-light: #EBF3F5;
            --accent: #D97724;
            --text-dark: #1E293B;
            --text-muted: #64748B;
            --bg-body: #0F172A;
            --card-bg: #1E293B;
            --card-border: #334155;
            --code-bg: #0B1120;
            --code-border: #1E293B;
            --success-color: #10B981;
            --btn-copy: #3B82F6;
            --btn-copy-hover: #2563EB;
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
            max-width: 1150px;
            margin: 0 auto;
        }}

        /* Header */
        .hero {{
            background: linear-gradient(135deg, #1E1B4B 0%, #31102E 50%, #451A03 100%);
            border: 1px solid #475569;
            border-radius: 20px;
            padding: 40px 32px;
            margin-bottom: 28px;
            text-align: center;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.4);
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
            max-width: 850px;
            margin: 0 auto 20px auto;
            line-height: 1.6;
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

        /* Quick Navigation Filter */
        .nav-filter {{
            display: flex;
            gap: 10px;
            margin-bottom: 24px;
            flex-wrap: wrap;
            justify-content: center;
        }}

        .filter-btn {{
            background: #1E293B;
            color: #94A3B8;
            border: 1px solid #334155;
            padding: 8px 18px;
            border-radius: 12px;
            font-size: 13.5px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
        }}

        .filter-btn:hover, .filter-btn.active {{
            background: var(--accent);
            color: #FFFFFF;
            border-color: var(--accent);
            transform: translateY(-1px);
        }}

        /* Day Selector Grid */
        .day-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(52px, 1fr));
            gap: 8px;
            margin-bottom: 30px;
            background: #1E293B;
            padding: 16px;
            border-radius: 16px;
            border: 1px solid #334155;
        }}

        .day-quick-btn {{
            background: #0F172A;
            border: 1px solid #334155;
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
            box-shadow: 0 8px 20px rgba(0, 0, 0, 0.25);
            transition: border-color 0.2s ease;
        }}

        .track-card:hover {{
            border-color: #64748B;
        }}

        .track-header {{
            display: flex;
            justify-content: space-between;
            align-items: flex-start;
            flex-wrap: wrap;
            gap: 12px;
            border-bottom: 1px solid #334155;
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

        /* Badges list */
        .badge-list {{
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
            gap: 10px;
            margin-bottom: 20px;
        }}

        .info-pill {{
            background: #0F172A;
            border: 1px solid #334155;
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
            background: #334155;
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
            line-height: 1.6;
            max-height: 380px;
            overflow-y: auto;
        }}

        .code-box.style-box {{
            color: #38BDF8;
            max-height: 100px;
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
            border-top: 1px solid #334155;
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
        <h2 style="font-size: 16px; font-weight: 500; color: #FCD34D; margin-bottom: 12px;">Suno AI 每日音樂創作全套提示詞庫 (19-Track Concept Album)</h2>
        <p>每一天皆深度融合【日本動漫 × 經典日劇 × 歷史人物事件】，內建完整歌詞結構（Verse / Chorus / Bridge）與精準曲風標籤，提供一鍵複製功能，直接貼入 Suno.com 即刻生成專屬旅行單曲！</p>
        <div class="hero-tags">
            <span class="hero-tag">🚲 19 天完整概念專輯</span>
            <span class="hero-tag">🎸 J-Rock / City Pop / Anime OST / Lo-Fi</span>
            <span class="hero-tag">📋 一鍵複製 Style + Full Lyrics</span>
            <span class="hero-tag">🚀 支援 Suno v3.5 / v4</span>
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
                <button class="super-copy-btn" onclick='copyText({all_json}, "已複製 Day {t['day']} 全套 Prompt（標題+曲風+歌詞）！")'>
                    📋 一鍵複製全套 Suno Prompt
                </button>
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
                    <span class="prompt-label">🎹 Suno Style of Music (音樂風格標籤)</span>
                    <button class="copy-btn" onclick='copyText({style_json}, "已複製 Style of Music 標籤！")'>
                        📋 複製 Style
                    </button>
                </div>
                <div class="code-box style-box">{t['style_prompt']}</div>
            </div>

            <!-- Prompt Box 2: Full Lyrics -->
            <div class="prompt-section">
                <div class="prompt-header">
                    <span class="prompt-label">📝 Suno Lyrics (結構化完整歌詞)</span>
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
        <p>東京・富士五湖・富士宮・伊豆・東京灣 19日秋季單車騎行 ｜ Suno AI 音樂創作全套提示詞庫 (19-Track Album)</p>
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

print("HTML Generator script written successfully!")
