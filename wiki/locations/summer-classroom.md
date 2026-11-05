---
title: "集中講義中の視聴覚室・カーテン裏"
type: location
location_id: summer-classroom
chapter: 02-summer
decision_default: canon
decision_states:
  prompt: draft  # spec から生成した初版・未検証
  image: open    # 未生成
tags: [location, chapter/02-summer]
---

# 📍 集中講義中の視聴覚室・カーテン裏

**登場章:** [[chapters/02-summer/index|02-summer]]　／　**学内の位置:** [[locations/himawari-university|向日葵の大学]]　／　**決定状態:** `canon`

> [!abstract] この場所の役割
> **破綻の舞台。**カメラを**屋外（中庭側）に置く**のが最重要。教室側からの画ではなく、**カーテン裏の身体が窓ガラス越しに見えている**構図が第2章の核。
>
> **旧校舎1階の、6列60席の階段状の視聴覚室。** 窓は西向きで中庭に面する。遮光のため床が半地下気味に沈み、窓が高い位置にある。着替えに使う言い訳が立つ部屋であり（プールでの撮影は教員に内緒）、同時に**段の上の全員が彼女を見下ろす客席**になる。
>
> 窓ガラスに体を押し付けたまま下がる時の物理は [[rules/glass-press-physics|ガラスに押し付けた体の物理]]（`draft`、採用は未決）。

---

## 📐 寸法 — この部屋は数字で決まっている

**内外の到達可否を分けている変数は「床の沈み込み」だけ**であり、他に調整の余地がない。

| 項目 | 値 | 意味 |
| :--- | :--- | :--- |
| 床が外の地面より低い分 | **60cm** | 内と外の差を作る唯一の変数 |
| 窓台の高さ（床から） | **145cm** | 視聴覚室の高窓。遮光にも合う |
| 窓台の高さ（外の地面から） | 85cm | 145 − 60 |
| **股の高さ（外の地面から）** | **165cm** | **唯香が背伸びで届く** |
| **股の高さ（教室の床から）** | **225cm** | **素手では届かない** |
| 必要な天井高 | **3.3m以上** | 145 + 170（頭頂）＋余裕 → 傾斜つきの部屋を要求する |
| 彼女の立ち位置 | **前後の中ほど** | 最後方は床が高く、外から手が届かなくなる |

> [!important] 三つの要求が一つの寸法から出ている
> ① 中庭側からは**唯香が背伸びで手が届く** ② 教室側からは**素手では届かない**
> ③ その部屋で**唯一届く物が箒になる**——これらは別々の演出上の願いだったが、
> 上の寸法を満たすと**同時に成立する**。
>
> **高さが時間を作る。** 足場を探して運んでくるまでの間、干渉は道具越しに留まる。
> ただし**段の上の席は彼女とほぼ同じ高さに来る**ため、段を上れば手が届く——
> 建築そのものがエスカレーションの経路を用意している。

> [!note] 尿の流れも傾斜が決める
> 彼女の足元から**最前列（低い側）へ向かって下っていく**。したがって
> [[chapters/02-summer/index|幕引き]]（尿が奥津の椅子へ近づく）が成立するには、
> **奥津の席は彼女より前方＝低い側**でなければならない。

---

## 🏛️ 部屋のつくり（2026-11-05 作者決定）

旧校舎は**平成施工で古びた印象はない**。

| 項目 | 内容 | 状態 |
| :--- | :--- | :--- |
| 席 | 6列×10席の60席。固定の長机＋跳ね上げ椅子 | `canon` |
| 床 | 濃色の木質フロア、半艶。液体は吸わず段を伝う | `canon` |
| 壁と天井 | 温色の有孔木パネル、白い吸音天井 | `canon` |
| 窓 | 大判のFIXガラス5枚＋黒い細枠。西向き。窓台は濃色の人工大理石の桟 | `canon` |
| 窓の下 | 機器を置かない。壁だけ | `canon` |
| カーテン | 新しめの厚い濃色。**止まっている時は足元が隠れ、揺れた時だけ裸足が見える長さ** | `canon` |
| 前の壁 | 電動スクリーン＋上下黒板。教卓に操作パネル | `canon` |
| 棚 | 後ろの壁の扉付き棚。扉を開けないと中は見えない。善意②で荷物が移される場所 | `canon` |
| 空調 | 天井エアコン＋天井扇風機。暑いのは入室直後でまだ効いていないため | `canon` |
| 奥津の席 | 3列目の窓側の端 | `canon` |
| 光 | 普段の部屋に光は入らないのが視聴覚室として自然。決壊の時は、向日葵のいた所のカーテンが引かれて光が入る | `canon` |
| 時刻 | 8月20日ごろの17:30、黄金の夕陽（太陽の高さ約18°） | `canon` |
| カーテンの普段の範囲 | 動かせるので固定しない | `draft` |
| 寸法 | 段は奥行100cm・蹴上げ20cm。部屋は幅10m×奥行10.8m。前の平場 -120、4列目 -60、後ろの通路 ±0、天井 +280 | `draft` |
| カーテンの裾 | +78cm（外の地面から）。桟より7cm下 | `draft` |
| 窓の高さ | +85〜+265cm。上の30cmは排煙の小窓 | `draft` |
| 前の扉 | 廊下 ±0 の扉の内側に踊り場と7段 | `canon` |

> [!note] 夕陽が落ちる範囲
> カーテンをどけた所では、4列目の高さの床に窓から456〜988cmまで光が落ちる。**17:30の光は廊下側の壁を登らない。**机と床を照らす。

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | modern university audio-visual lecture room in a well-kept Heisei-era building, 60 fixed seats in six rows stepping down toward the front, floor set slightly below the outside ground level, high west-facing window band along one side, thick dark curtains drawn across most of it, projector screen and sliding blackboards at the front |
| **表面・素材** | large fixed window glass in slim black frames, thick new dark curtain fabric hanging past a narrow dark engineered-stone ledge, dark semi-gloss wooden tiers, warm perforated wood wall panels above dark wood wainscot, white acoustic ceiling |
| **光** | golden low western sun at 5:30 pm stopped by the curtains, the room kept dim as an audio-visual room should be, a hard blade of gold where the curtain is pulled aside |
| **空気・音・匂い** | hot humid air, air conditioning only just switched on, ceiling fans turning, the drone of a lecture, voices from the courtyard outside |
| **小道具** | a curtain pulled aside, the window glass, the narrow ledge, rows of occupied fixed desks with folding seats, a broom, a spilled cup of coffee |
| **カメラ** | from outside the window looking in, eye level, medium - the campus courtyard vantage point |
| **トーン** | summer chapter palette, warm gold against dark wood, harsh backlight |

---

## 🖼️ 参照画像

| 背景 | 意図 |
| :---: | :--- |
| ![[placeholder_full.jpg]] | **`open`／未生成。**人物を含まない背景単体。上記スロットのとおり。<br>**用途:** この場所で起きる全シーンの背景基準。キャラ画像と合成するため**カメラ設定を固定**して生成すること。 |

---

## 🎨 プロンプト

```text
modern university audio-visual lecture room in a well-kept Heisei-era building, 60 fixed seats in six rows stepping down toward the front, floor set slightly below the outside ground level, high west-facing window band along one side, thick dark curtains drawn across most of it, projector screen and sliding blackboards at the front, large fixed window glass in slim black frames, thick new dark curtain fabric hanging past a narrow dark engineered-stone ledge, dark semi-gloss wooden tiers, warm perforated wood wall panels above dark wood wainscot, white acoustic ceiling, golden low western sun at 5:30 pm stopped by the curtains, the room kept dim as an audio-visual room should be, a hard blade of gold where the curtain is pulled aside, hot humid air, air conditioning only just switched on, ceiling fans turning, the drone of a lecture, voices from the courtyard outside, a curtain pulled aside, the window glass, the narrow ledge, rows of occupied fixed desks with folding seats, a broom, a spilled cup of coffee, from outside the window looking in, eye level, medium - the campus courtyard vantage point, summer chapter palette, warm gold against dark wood, harsh backlight
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

