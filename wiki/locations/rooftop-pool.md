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

**登場章:** [[chapters/02-summer/index|02-summer]]　／　**学内の位置:** [[locations/himawari-university|向日葵の大学]]　／　**決定状態:** `canon`

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

## 📐 建物と寸法（2026-11-05 作者決定）

旧校舎は**平成施工で耐震も十分**であり、古びた印象はない。「旧」は新校舎に対する呼び名にすぎない。屋上は4階建ての上、+1560cm（中庭の地面が0）。

| 項目 | 内容 | 状態 |
| :--- | :--- | :--- |
| プールの収まり | 水槽を4階の天井に沈める。プールサイドと屋上の床は同じ高さ、水面は床の15cm下 | `canon` |
| 金網 | 床から30cmの立ち上がり＋高さ3mの亜鉛めっき菱形金網。屋上の全周 | `canon` |
| プールの入り口 | 塔屋（南階段）の前を金網で仕切り、門を鎖と南京錠で閉める。南京錠はこの門の備品 | `canon` |
| 屋上へ出る階段 | 南階段だけ | `canon` |
| 周りの街 | 東と北の間近は3階建てまで。80m以上先にビル | `canon` |
| 見下ろし | 新校舎の北面は窓なし（壁面緑化）、北棟5階の南面は窓なしの書庫 | `canon` |
| プールの寸法 | 25m×10m、5コース、水深110cm | `draft` |
| 水槽の下の4階 | 天井高210cmの機械室。4階の部屋は南北に分かれる | `draft` |
| 更衣室 | 屋上には置かない。視聴覚室で着替える理由を保つ。4階にあるかは `open` | `open` |

> [!warning] 80m先のビルからは屋上まで視線が通る
> 距離で人の見分けがつきにくいことを前提にしている。寄りのカットでビルの窓を映さないこと。

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | open rooftop swimming pool of a modern, well-kept Heisei-era university building in the city centre, 25 metre pool sunk flush with the roof deck, galvanised chain-link fence on a low concrete upstand enclosing the whole roof, stair tower and a chained fence gate at one end, city rooftops beyond, no shade |
| **表面・素材** | wet pale blue tiled poolside, still chlorinated water, hot concrete beyond the tile, galvanised diamond chain-link and a padlock |
| **光** | brutal high midday summer sun straight overhead, glare off the water, short hard shadows |
| **空気・音・匂い** | blazing heat, chlorine and sunscreen, cicadas, absolute stillness of a university campus during summer break |
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
open rooftop swimming pool of a modern, well-kept Heisei-era university building in the city centre, 25 metre pool sunk flush with the roof deck, galvanised chain-link fence on a low concrete upstand enclosing the whole roof, stair tower and a chained fence gate at one end, city rooftops beyond, no shade, wet pale blue tiled poolside, still chlorinated water, hot concrete beyond the tile, galvanised diamond chain-link and a padlock, brutal high midday summer sun straight overhead, glare off the water, short hard shadows, blazing heat, chlorine and sunscreen, cicadas, absolute stillness of a university campus during summer break, a padlock clipped through the chain-link fence, a discarded swimsuit strap, a drink bottle left beside an empty poolside spot, a smartphone, eye level, wide, strong sun flare, summer chapter palette, bleached highlights, deep blue shadow
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

