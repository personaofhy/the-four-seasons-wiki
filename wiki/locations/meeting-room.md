---
title: "政治家の家・応接間"
type: location
location_id: meeting-room
chapter: 01-spring
decision_default: canon
decision_states:
  prompt: draft  # spec から生成した初版・未検証
  image: open    # 未生成
tags: [location, chapter/01-spring]
---

# 📍 政治家の家・応接間

**登場章:** [[chapters/01-spring/index|01-spring]]　／　**決定状態:** `canon`

> [!info] 改訂（2026-09-09）— 「窓のない会議室」から「家の応接間」へ
> 旧版は企業の会議室（windowless meeting room / long table / leather chairs）の仕様だったが、
> 第1章の canon は**山道を長時間かけて向かった田舎の政治家の家**であり、
> **「田舎者特有の長話＝家の蘊蓄自慢」**が破綻の一因になっている。会議室では成立しない。
>
> **昭和的な応接セットのある座敷続きの応接間**へ改訂する。
> 圧迫感（出口が見えない・息苦しい）は、**襖と障子で閉じられた部屋**として維持できる。

> [!important] 座面は合皮。液体は色ではなく、光の反射で見える
> 桃香のスラックスはポリエステル混で吸わず（[[characters/momoka/index|cpt-a6c2]]）、
> 合皮のソファも吸わない。**液体は座面に溜まる。**
>
> **黒か焦茶の座面に透明な液体が乗っても、色差はほぼ出ない。**
> 見えるのは**照明の反射だけ——そこだけが光っている。**
> 誰かが気づくとしたら、染みを見つけるのではなく**光り方の違いに気づく。**
>
> ソファは座面が広く低く、**深く沈む。立ち上がるのに時間がかかる。**
> そして合皮なので、**立ち上がるときに音が出る。** 逃げにくく、動けば鳴る。

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | formal reception room in a rural politician's house, shoji and fusuma closed on all sides, no view outside, tatami visible beyond the threshold, oppressively low ceiling |
| **表面・素材** | dark brown faux-leather sofa set, low glass-topped coffee table, display cabinet with awards and local souvenirs |
| **光** | a single warm ceiling light, no daylight, **highlights catching on the vinyl seat surface** |
| **空気・音・匂い** | stale overwarm air from a kerosene heater, no circulation, faint smell of tobacco and tatami |
| **小道具** | tea cups on the table, one of them already half empty, a closed document folder, a wall clock |
| **カメラ** | eye level, medium wide, slight wide-angle compression toward the closed fusuma |
| **トーン** | spring chapter palette, low contrast, desaturated |

---

## 🖼️ 参照画像

| 背景 | 意図 |
| :---: | :--- |
| ![[placeholder_full.jpg]] | **`open`／未生成。**人物を含まない背景単体。上記スロットのとおり。<br>**用途:** この場所で起きる全シーンの背景基準。キャラ画像と合成するため**カメラ設定を固定**して生成すること。 |

---

## 🎨 プロンプト

```text
formal reception room in a rural politician's house, shoji and fusuma closed on all sides, no view outside, tatami visible beyond the threshold, oppressively low ceiling, dark brown faux-leather sofa set, low glass-topped coffee table, display cabinet with awards and local souvenirs, a single warm ceiling light, no daylight, highlights catching on the vinyl seat surface, stale overwarm air from a kerosene heater, no circulation, faint smell of tobacco and tatami, tea cups on the table one of them already half empty, a closed document folder, a wall clock, eye level, medium wide, slight wide-angle compression toward the closed fusuma, spring chapter palette, low contrast, desaturated
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

