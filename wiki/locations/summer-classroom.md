---
title: "補習授業中の教室・カーテン裏"
type: location
location_id: summer-classroom
chapter: 02-summer
decision_default: canon
decision_states:
  prompt: draft  # spec から生成した初版・未検証
  image: open    # 未生成
tags: [location, chapter/02-summer]
---

# 📍 補習授業中の教室・カーテン裏

**登場章:** [[chapters/02-summer/index|02-summer]]　／　**決定状態:** `canon`

> [!abstract] この場所の役割
> **破綻の舞台。**カメラを**屋外（校庭側）に置く**のが最重要。教室側からの画ではなく、**カーテン裏の身体が窓ガラス越しに見えている**構図が第2章の核。

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | occupied high school classroom during summer supplementary lessons, desks filled, tall window wall along one side, heavy curtains half drawn |
| **表面・素材** | large window glass, worn curtain fabric, scuffed wooden floor, chalk dust |
| **光** | hard summer daylight pouring through the window wall, the curtain glowing translucent from behind, silhouettes readable through the fabric |
| **空気・音・匂い** | hot humid air, ceiling fan, the drone of a lesson, schoolyard noise from outside |
| **小道具** | a half-drawn curtain, the window glass, rows of occupied desks |
| **カメラ** | from outside the window looking in, eye level, medium - the schoolyard vantage point |
| **トーン** | summer chapter palette, low contrast, harsh backlight |

---

## 🖼️ 参照画像

| 背景 | 意図 |
| :---: | :--- |
| ![未生成](../assets/templates/placeholder_full.jpg) | **`open`／未生成。**人物を含まない背景単体。上記スロットのとおり。<br>**用途:** この場所で起きる全シーンの背景基準。キャラ画像と合成するため**カメラ設定を固定**して生成すること。 |

---

## 🎨 プロンプト

```text
occupied high school classroom during summer supplementary lessons, desks filled, tall window wall along one side, heavy curtains half drawn, large window glass, worn curtain fabric, scuffed wooden floor, chalk dust, hard summer daylight pouring through the window wall, the curtain glowing translucent from behind, silhouettes readable through the fabric, hot humid air, ceiling fan, the drone of a lesson, schoolyard noise from outside, a half-drawn curtain, the window glass, rows of occupied desks, from outside the window looking in, eye level, medium - the schoolyard vantage point, summer chapter palette, low contrast, harsh backlight
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

