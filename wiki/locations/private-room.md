---
title: "静まり返った自室・炬燵"
type: location
location_id: private-room
chapter: 04-winter
decision_default: canon
decision_states:
  prompt: draft  # spec から生成した初版・未検証
  image: open    # 未生成
  role: draft    # 2026-08-15 全面改訂により役割が変更。要検証
tags: [location, chapter/04-winter]
---

# 📍 静まり返った自室・炬燵

**登場章:** [[chapters/04-winter/index|04-winter]]　／　**決定状態:** `canon`（下記「役割」は `draft`）

> [!warning] 役割変更（2026-08-15）
> **旧: 破綻の場所。新: 準備段階の場所。** 破綻本体は
> `locations/ferris-wheel-queue`（遊園地・観覧車待機列）へ移動した。
> ここは柊が児童用下着を試着し、これから行う再演に向けて覚悟を固める場面として使う。
> 炬燵は破綻の道具ではなく、**視覚的には隠れているが体感的には露出している**という
> 倒錯を演出する小道具として、劇中の配置は未定のまま残っている（[[rules/decision-states]]）。
> 下記スロット仕様（空間・小道具など）はこの新しい役割のもとでも概ね流用できる。

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | small cold single-room apartment, curtains drawn, door shut, nowhere to be seen and nobody coming |
| **表面・素材** | tatami or thin carpet, a kotatsu with a heavy quilt, cold bare floor beyond its edge |
| **光** | weak grey winter daylight through drawn curtains, the kotatsu glowing faintly orange underneath |
| **空気・音・匂い** | freezing still air outside the quilt, silence, faint hum of the heater |
| **小道具** | discarded tights and skirt beside the kotatsu, an unwatched screen, a mug gone cold |
| **カメラ** | low floor level, close, intimate |
| **トーン** | winter chapter palette, highest contrast, cold blue against the orange pocket of warmth |

---

## 🖼️ 参照画像

| 背景 | 意図 |
| :---: | :--- |
| ![[placeholder_full.jpg]] | **`open`／未生成。**人物を含まない背景単体。上記スロットのとおり。<br>**用途:** この場所で起きる全シーンの背景基準。キャラ画像と合成するため**カメラ設定を固定**して生成すること。 |

---

## 🎨 プロンプト

```text
small cold single-room apartment, curtains drawn, door shut, nowhere to be seen and nobody coming, tatami or thin carpet, a kotatsu with a heavy quilt, cold bare floor beyond its edge, weak grey winter daylight through drawn curtains, the kotatsu glowing faintly orange underneath, freezing still air outside the quilt, silence, faint hum of the heater, discarded tights and skirt beside the kotatsu, an unwatched screen, a mug gone cold, low floor level, close, intimate, winter chapter palette, highest contrast, cold blue against the orange pocket of warmth
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

