---
title: "屋上のプール"
type: location
location_id: rooftop-pool
chapter: 02-summer
decision_default: canon
decision_states:
  prompt: draft  # spec から生成した初版・未検証
  image: open    # 未生成
tags: [location, chapter/02-summer]
---

# 📍 屋上のプール

**登場章:** [[chapters/02-summer/index|02-summer]]　／　**決定状態:** `canon`

> [!abstract] この場所の役割
> **発端の舞台。**ここで水着の紐とフェンスが南京錠で繋がれる。フェンスが「囲い」として機能し、逃げ場がないことを画で示す。犯人は描かない。

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | open rooftop swimming pool of a school, chain-link fence enclosing the whole roof, city rooftops beyond, no shade |
| **表面・素材** | wet pale blue tiled poolside, still chlorinated water, hot concrete, galvanised chain-link and a padlock |
| **光** | brutal high midday summer sun straight overhead, glare off the water, short hard shadows |
| **空気・音・匂い** | blazing heat, chlorine and sunscreen, cicadas, absolute stillness of a closed summer school |
| **小道具** | a padlock clipped through the fence, a discarded swimsuit strap, a folded towel |
| **カメラ** | eye level, wide, strong sun flare |
| **トーン** | summer chapter palette, bleached highlights, deep blue shadow |

---

## 🖼️ 参照画像

| 背景 | 意図 |
| :---: | :--- |
| ![[placeholder_full.jpg]] | **`open`／未生成。**人物を含まない背景単体。上記スロットのとおり。<br>**用途:** この場所で起きる全シーンの背景基準。キャラ画像と合成するため**カメラ設定を固定**して生成すること。 |

---

## 🎨 プロンプト

```text
open rooftop swimming pool of a school, chain-link fence enclosing the whole roof, city rooftops beyond, no shade, wet pale blue tiled poolside, still chlorinated water, hot concrete, galvanised chain-link and a padlock, brutal high midday summer sun straight overhead, glare off the water, short hard shadows, blazing heat, chlorine and sunscreen, cicadas, absolute stillness of a closed summer school, a padlock clipped through the fence, a discarded swimsuit strap, a folded towel, eye level, wide, strong sun flare, summer chapter palette, bleached highlights, deep blue shadow
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

