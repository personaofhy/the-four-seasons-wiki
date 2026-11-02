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
> **発端の舞台。**ここで**水着の肩紐とフェンスの金網**が南京錠で繋がれる。フェンスが「囲い」として機能し、逃げ場がないことを画で示す。犯人は描かない。

> [!important] 小道具の増減 — タオルは無く、飲み物がある
> * **南京錠はプールの入り口を塞ぐための備品。** 犯人が持ち込んだ道具ではない（＝計画性の痕跡を残さない）
> * **タオルは画に入れない。** 唯香たちが善意で持ち去った後の状態を描く。**「タオルがあったはずの空白」**として置く
> * **うたた寝の傍らに飲み物を置く。** 誰が置いたかも、どれだけ飲んだかも書かない。尿意の理由づけであり、同時に読者が勝手に線を引くための余白になる（作中の誰にも疑わせないこと）
> * 手元に残るのは**スマートフォン**と紐付きのボトルだけ
>
> うたた寝の姿勢は**フェンスに背をあずける体勢**で固定する。肩紐が金網に触れていることが拘束の前提。

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | open rooftop swimming pool of a school, chain-link fence enclosing the whole roof, city rooftops beyond, no shade |
| **表面・素材** | wet pale blue tiled poolside, still chlorinated water, hot concrete, galvanised chain-link and a padlock |
| **光** | brutal high midday summer sun straight overhead, glare off the water, short hard shadows |
| **空気・音・匂い** | blazing heat, chlorine and sunscreen, cicadas, absolute stillness of a closed summer school |
| **小道具** | a padlock clipped through the chain-link fence, a discarded swimsuit strap, a drink bottle left beside an empty poolside spot, a smartphone |
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
open rooftop swimming pool of a school, chain-link fence enclosing the whole roof, city rooftops beyond, no shade, wet pale blue tiled poolside, still chlorinated water, hot concrete, galvanised chain-link and a padlock, brutal high midday summer sun straight overhead, glare off the water, short hard shadows, blazing heat, chlorine and sunscreen, cicadas, absolute stillness of a closed summer school, a padlock clipped through the chain-link fence, a discarded swimsuit strap, a drink bottle left beside an empty poolside spot, a smartphone, eye level, wide, strong sun flare, summer chapter palette, bleached highlights, deep blue shadow
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

