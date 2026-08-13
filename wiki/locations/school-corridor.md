---
title: "学校・トイレ前の廊下"
type: location
location_id: school-corridor
chapter: 05-re-spring
decision_default: canon
decision_states:
  prompt: draft  # spec から生成した初版・未検証
  image: open    # 未生成
tags: [location, chapter/05-re-spring]
---

# 📍 学校・トイレ前の廊下

**登場章:** [[chapters/05-re-spring/index|05-re-spring]]　／　**決定状態:** `canon`

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | school corridor outside the toilets, long straight sightline, students able to appear from either end |
| **表面・素材** | polished linoleum reflecting the windows, painted concrete walls, a row of lockers |
| **光** | flat spring daylight from a window wall, even and unforgiving, nothing to hide in |
| **空気・音・匂い** | mild air, distant noise of a class, footsteps |
| **小道具** | a toilet door standing ajar, a notice board, a wooden hanger |
| **カメラ** | eye level, long lens down the corridor, deep focus |
| **トーン** | spring chapter palette returning, low contrast, brighter than chapter 1 |

---

## 🖼️ 参照画像

| 背景 | 意図 |
| :---: | :--- |
| ![[placeholder_full.jpg]] | **`open`／未生成。**人物を含まない背景単体。上記スロットのとおり。<br>**用途:** この場所で起きる全シーンの背景基準。キャラ画像と合成するため**カメラ設定を固定**して生成すること。 |

---

## 🎨 プロンプト

```text
school corridor outside the toilets, long straight sightline, students able to appear from either end, polished linoleum reflecting the windows, painted concrete walls, a row of lockers, flat spring daylight from a window wall, even and unforgiving, nothing to hide in, mild air, distant noise of a class, footsteps, a toilet door standing ajar, a notice board, a wooden hanger, eye level, long lens down the corridor, deep focus, spring chapter palette returning, low contrast, brighter than chapter 1
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

