---
title: "補習授業中の視聴覚室・カーテン裏"
type: location
location_id: summer-classroom
chapter: 02-summer
decision_default: canon
decision_states:
  prompt: draft  # spec から生成した初版・未検証
  image: open    # 未生成
tags: [location, chapter/02-summer]
---

# 📍 補習授業中の視聴覚室・カーテン裏

**登場章:** [[chapters/02-summer/index|02-summer]]　／　**決定状態:** `canon`

> [!abstract] この場所の役割
> **破綻の舞台。**カメラを**屋外（校庭側）に置く**のが最重要。教室側からの画ではなく、**カーテン裏の身体が窓ガラス越しに見えている**構図が第2章の核。
>
> **旧校舎1階の、緩やかに傾斜した視聴覚室。** 遮光のため床が半地下気味に沈み、窓が高い位置にある。着替えに使う言い訳が立つ部屋であり（プールでの撮影は教師に内緒）、同時に**段の上の全員が彼女を見下ろす客席**になる。

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
> ① 校庭側からは**唯香が背伸びで手が届く** ② 教室側からは**素手では届かない**
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

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | occupied high school audio-visual lecture room during summer supplementary lessons, gently tiered floor stepping down toward the front, floor set slightly below the outside ground level, high window band along one side, heavy blackout curtains half drawn, high ceiling |
| **表面・素材** | large window glass, heavy worn curtain fabric, narrow window ledge, scuffed wooden tiers, chalk dust |
| **光** | hard summer daylight pouring through the high window band, the curtain glowing translucent from behind, silhouettes readable through the fabric |
| **空気・音・匂い** | hot humid air, ceiling fan, the drone of a lesson, schoolyard noise from outside |
| **小道具** | a half-drawn curtain, the window glass, the narrow ledge, rows of occupied tiered desks, a broom, a spilled cup of coffee |
| **カメラ** | from outside the window looking in, eye level, medium - the schoolyard vantage point |
| **トーン** | summer chapter palette, low contrast, harsh backlight |

---

## 🖼️ 参照画像

| 背景 | 意図 |
| :---: | :--- |
| ![[placeholder_full.jpg]] | **`open`／未生成。**人物を含まない背景単体。上記スロットのとおり。<br>**用途:** この場所で起きる全シーンの背景基準。キャラ画像と合成するため**カメラ設定を固定**して生成すること。 |

---

## 🎨 プロンプト

```text
occupied high school audio-visual lecture room during summer supplementary lessons, gently tiered floor stepping down toward the front, floor set slightly below the outside ground level, high window band along one side, heavy blackout curtains half drawn, high ceiling, large window glass, heavy worn curtain fabric, narrow window ledge, scuffed wooden tiers, chalk dust, hard summer daylight pouring through the high window band, the curtain glowing translucent from behind, silhouettes readable through the fabric, hot humid air, ceiling fan, the drone of a lesson, schoolyard noise from outside, a broom, a spilled cup of coffee, rows of occupied tiered desks, from outside the window looking in, eye level, medium - the schoolyard vantage point, summer chapter palette, low contrast, harsh backlight
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

