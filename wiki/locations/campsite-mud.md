---
title: "社内キャンプ場・紅葉の泥"
type: location
location_id: campsite-mud
chapter: 03-autumn
decision_default: canon
decision_states:
  prompt: draft  # spec から生成した初版・未検証
  image: open    # 未生成
tags: [location, chapter/03-autumn]
---

# 📍 社内キャンプ場・紅葉の泥

**登場章:** [[chapters/03-autumn/index|03-autumn]]　／　**決定状態:** `canon`

> [!abstract] この場所の役割
> **破綻の舞台。**泥の色を秋のキャラパレットに近づけ、楓の輪郭が背景に飲み込まれるように。

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | outdoor company retreat campsite clearing in deep autumn woods, toilet block visible but too far |
| **表面・素材** | churned brown mud, wet fallen leaves, exposed tree roots |
| **光** | low overcast afternoon light, no direct sun, flat and grey |
| **空気・音・匂い** | cold damp air, smell of wet earth and rot, distant water |
| **小道具** | a single dark brown pump half sunk in mud, scattered maple leaves, a washstand in the background |
| **カメラ** | low angle near ground level, close, shallow depth of field |
| **トーン** | autumn chapter palette, medium contrast, mud tones close to the character palette |

---

## 🖼️ 参照画像

| 背景 | 意図 |
| :---: | :--- |
| ![未生成](../assets/templates/placeholder_full.jpg) | **`open`／未生成。**人物を含まない背景単体。上記スロットのとおり。<br>**用途:** この場所で起きる全シーンの背景基準。キャラ画像と合成するため**カメラ設定を固定**して生成すること。 |

---

## 🎨 プロンプト

```text
outdoor company retreat campsite clearing in deep autumn woods, toilet block visible but too far, churned brown mud, wet fallen leaves, exposed tree roots, low overcast afternoon light, no direct sun, flat and grey, cold damp air, smell of wet earth and rot, distant water, a single dark brown pump half sunk in mud, scattered maple leaves, a washstand in the background, low angle near ground level, close, shallow depth of field, autumn chapter palette, medium contrast, mud tones close to the character palette
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

