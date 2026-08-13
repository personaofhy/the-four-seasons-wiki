---
title: "金城 向日葵 表情設定：6段階"
type: expressions
character_id: kaneshiro-himawari
decision_default: done
decision_states:
  prompts: done
  images: done    # 全6枚生成・埋め込み完了
tags: [expressions, character/kaneshiro-himawari, season/夏]
---

# 🌻 金城 向日葵 表情設定：6段階

> [!abstract] この人物の表情設計
> **コントラスト:** 弱め（上から3番目）
> **4人中もっとも表情の可動域が広い。**大きく丸い瞳と太めの眉が、段階1と段階5の落差を最大化する。青みの白い肌の上では**頬の円形の赤面だけが突出する**ので、赤面は輪郭をぼかさず円形に。
> **段階の進み方:** 段階2（笑顔）から段階5（狼狽）へ**3をほぼ飛ばして落ちる**のが向日葵だけの経路。破綻が偶然の事故であるため、警戒する時間が与えられない。

共通の6段階定義は [[characters/index#😐 表情：全キャラ共通の6段階定義|キャラクター一覧]] を参照。

---

## 1. 通常（Neutral）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | ペルソナを維持した日常の顔 |
| **発生タイミング** | 章の序盤・日常会話・社会的対応 |
| **状態** | `done` — 生成完了 |

|                                 参照画像                                  | 意図                           |
| :-------------------------------------------------------------------: | :--------------------------- |
| ![通常](wiki/assets/characters/himawari/face/himawari_face_neutral.jpg) | 涼しげで素直な日常の顔。ペルソナを維持した無防備な状態。 |

```text
18yo japanese high school girl, cheerful and popular, tall curvy athletic build, 170cm, long soft dark brown to black wavy hair with a bluish cast, bangs down, unstyled, large round eyes, wide double eyelids, big dark irises, thick soft grey-brown eyebrows, vivid sunny yellow long sleeve button-up cotton shirt, top buttons undone, white undershirt underneath, bright open expression, large round eyes fully visible, thick brows level, mouth in an easy line, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool summer palette, pale fair skin, healthy clear complexion
```

## 2. 笑顔・安堵（Smile）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 魅せる笑顔、または一過性の安堵 |
| **発生タイミング** | 良好な他者対応・危機を脱した錯覚 |
| **状態** | `done` — 生成完了 |

|                                参照画像                                 | 意図                        |
| :-----------------------------------------------------------------: | :------------------------ |
| ![笑顔](wiki/assets/characters/himawari/face/himawari_face_smile.jpg) | 太陽のように輝く無防備な笑顔。瞳が弾け頬が上がる。 |

```text
18yo japanese high school girl, cheerful and popular, tall curvy athletic build, 170cm, long soft dark brown to black wavy hair with a bluish cast, bangs down, unstyled, large round eyes, wide double eyelids, big dark irises, thick soft grey-brown eyebrows, vivid sunny yellow long sleeve button-up cotton shirt, top buttons undone, white undershirt underneath, wide unguarded grin, eyes crinkling almost shut, cheeks lifted, radiant and careless, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool summer palette, pale fair skin, healthy clear complexion
```

## 3. 警戒・違和感（Suspicion）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 異変や周囲の視線を察知 |
| **発生タイミング** | 罠の気配・逃げ場の喪失の予感 |
| **状態** | `done` — 生成完了 |

|                                  参照画像                                   | 意図                       |
| :---------------------------------------------------------------------: | :----------------------- |
| ![警戒](wiki/assets/characters/himawari/face/himawari_face_suspicion.jpg) | 笑顔がすっと引く。太い眉が寄り、異変への戸惑い。 |

```text
18yo japanese high school girl, cheerful and popular, tall curvy athletic build, 170cm, long soft dark brown to black wavy hair with a bluish cast, bangs down, unstyled, large round eyes, wide double eyelids, big dark irises, thick soft grey-brown eyebrows, vivid sunny yellow long sleeve button-up cotton shirt, top buttons undone, white undershirt underneath, round eyes going still and staring, thick brows knitting in concern, smile draining away mid-expression, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool summer palette, pale fair skin, healthy clear complexion
```

## 4. 抑圧・冷や汗（Anxiety）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 生理的緊張・破綻の隠蔽 |
| **発生タイミング** | 耐えている最中 |
| **状態** | `done` — 生成完了 |

|                                   参照画像                                    | 意図                           |
| :-----------------------------------------------------------------------: | :--------------------------- |
| ![抑圧・冷や汗](wiki/assets/characters/himawari/face/himawari_face_anxiety.jpg) | 眉が角度を増し、額に冷や汗が浮かぶ。必死に噛み締める唇。 |

```text
18yo japanese high school girl, cheerful and popular, tall curvy athletic build, 170cm, long soft dark brown to black wavy hair with a bluish cast, bangs down, unstyled, large round eyes, wide double eyelids, big dark irises, thick soft grey-brown eyebrows, vivid sunny yellow long sleeve button-up cotton shirt, top buttons undone, white undershirt underneath, brows steeply angled, cold sweat at the hairline and forehead, teeth clamped on lower lip, big eyes darting, breath held, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool summer palette, pale fair skin, healthy clear complexion
```

## 5. 狼狽・大赤面（Panic）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 破綻の瞬間・激しい羞恥 |
| **発生タイミング** | 露出・失禁の直前〜直後 |
| **状態** | `done` — 生成完了 |

|                                  参照画像                                   | 意図                      |
| :---------------------------------------------------------------------: | :---------------------- |
| ![狼狽・大赤面](wiki/assets/characters/himawari/face/himawari_face_panic.jpg) | 頬中央に鮮烈な円形の赤面。涙目の瞳、崩れた眉。 |

```text
18yo japanese high school girl, cheerful and popular, tall curvy athletic build, 170cm, long soft dark brown to black wavy hair with a bluish cast, bangs down, unstyled, large round eyes, wide double eyelids, big dark irises, thick soft grey-brown eyebrows, vivid sunny yellow long sleeve button-up cotton shirt, top buttons undone, white undershirt underneath, violent circular blush on both cheeks spreading to neck and ears, eyes enormous and streaming with tears, mouth wide open in despair, brows collapsed, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool summer palette, pale fair skin, healthy clear complexion
```

## 6. 虚脱・完全適応（Acceptance）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 尊厳の死滅と被支配への安堵 |
| **発生タイミング** | 屈服・完全適応の結末 |
| **状態** | `done` — 生成完了 |

|                                     参照画像                                      | 意図                  |
| :---------------------------------------------------------------------------: | :------------------ |
| ![虚脱・完全適応](wiki/assets/characters/himawari/face/himawari_face_acceptance.jpg) | 光の消えた大きな瞳。微かな諦念の笑み。 |

```text
18yo japanese high school girl, cheerful and popular, tall curvy athletic build, 170cm, long soft dark brown to black wavy hair with a bluish cast, bangs down, unstyled, large round eyes, wide double eyelids, big dark irises, thick soft grey-brown eyebrows, vivid sunny yellow long sleeve button-up cotton shirt, top buttons undone, white undershirt underneath, large eyes emptied of light, dull hollow stare past viewer, mouth slack with faint bewildered smile, dried tear tracks on pale cheeks, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool summer palette, pale fair skin, healthy clear complexion
```
