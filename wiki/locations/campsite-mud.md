---
title: "寂れた自然公園・トイレ棟の前"
type: location
location_id: campsite-mud
chapter: 03-autumn
decision_default: canon
decision_states:
  prompt: draft  # spec から生成した初版・未検証
  image: open    # 未生成
tags: [location, chapter/03-autumn]
---

# 📍 寂れた自然公園・トイレ棟の前

**登場章:** [[chapters/03-autumn/index|03-autumn]]　／　**決定状態:** `canon`

> [!abstract] この場所の役割
> **破綻の舞台。**出張の道中、トイレを求めて紛れ込んだ**バブル期の遺物**。**管理は名目だけの市営施設**で、
> 管理者は常駐せず、看板だけが古い。水道だけが止められていない。**誰も来ない場所であることの理由が、景色に書いてある**状態にする。
> 画の端に**遠くの人影**だけがある（助けを求められる距離ではなく、表情も見えない）。
> 人影は決壊の場面から歩行の場面まで、遠景としてのみ置く。

> [!important] 破綻面は泥ではなく、タイル
> 決壊が起きるのは**男女共用のトイレ棟（電話ボックス二つ分ほどの据え置き型）の目前**。
> **泥は吸うが、タイルは吸わない**——土の上なら数分で消える痕跡が、人工の床では広がって
> 残る。しかも**あと数歩だった距離**が、その広がりと一緒に画に入る。
>
> 泥は[[chapters/03-autumn/index|道中の装飾]]に降格しており、**決壊の舞台ではない**。

> [!note] カメラは背後から
> 高木は後ろから見ている。**楓の顔は最後まで画に入らない。** 彼が一生忘れないのは表情
> ではなく、**床に広がる跡と、ワンピースの尻から跳ねる軌跡**である。

---

## 🧩 スロット別仕様

| スロット | 内容 |
| :--- | :--- |
| **空間** | derelict rural nature park from the bubble era, long abandoned, a small freestanding unisex toilet block the size of two phone booths, forked path leading up through autumn woods, sea visible far below through the trees |
| **表面・素材** | cracked pale tiles in front of the toilet block, weeds through the joints, wet fallen leaves, faded painted signage |
| **光** | low overcast afternoon light, no direct sun, flat and grey |
| **空気・音・匂い** | cold damp air, smell of wet earth and rot, distant water |
| **小道具** | a rusted map board, scattered maple leaves, a single dark brown pump left on the tiles, a washstand inside the block |
| **カメラ** | from behind at standing height, the toilet block a few steps ahead |
| **トーン** | autumn chapter palette, medium contrast, pale tiles catching what little light there is |

---

## 🖼️ 参照画像

| 背景 | 意図 |
| :---: | :--- |
| ![[placeholder_full.jpg]] | **`open`／未生成。**人物を含まない背景単体。上記スロットのとおり。<br>**用途:** この場所で起きる全シーンの背景基準。キャラ画像と合成するため**カメラ設定を固定**して生成すること。 |

---

## 🎨 プロンプト

```text
derelict rural nature park from the bubble era, long abandoned, a small freestanding unisex toilet block the size of two phone booths, forked path leading up through autumn woods, sea visible far below through the trees, cracked pale tiles in front of the toilet block, weeds through the joints, wet fallen leaves, faded painted signage, low overcast afternoon light, no direct sun, flat and grey, cold damp air, smell of wet earth and rot, distant water, a rusted map board, scattered maple leaves, a single dark brown pump left on the tiles, from behind at standing height, the toilet block a few steps ahead, autumn chapter palette, medium contrast, pale tiles catching what little light there is
```

**ネガティブ:** `people, person, human, figure, worst quality, low quality, text, watermark, signature, jpeg artifacts, blurry`

> [!note] 人物は含めない
> 場所プロンプトに人物を入れないこと。シーン画像は**場所スロット＋キャラスロット**を生成時に合成して作る。

