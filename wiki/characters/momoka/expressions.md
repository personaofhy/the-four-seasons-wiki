---
title: "田邊 桃香 表情設定：6段階"
type: expressions
character_id: tanabe-momoka
decision_default: draft
decision_states:
  prompts: draft  # spec から生成した初版・未検証
  images: open    # 全6枚未生成
tags: [expressions, character/tanabe-momoka, season/春]
---

# 🌸 田邊 桃香 表情設定：6段階

> [!abstract] この人物の表情設計
> **コントラスト:** 4人中もっとも弱い
> **低コントラストゆえ、変化が出にくい。**明るい髪・明るい瞳・淡い肌が近い明度で並ぶため、段階4〜5の冷や汗と赤面は**面積ではなく密度**で描く。額の汗粒を大きく、赤面は耳から首筋という細い帯に集中させる。
> **段階の進み方:** 段階3（警戒）が最も長い。罠と気づいてから落ちるまでに猶予があるのが桃香だけの特徴で、その間ずっと4を隠している。

共通の6段階定義は [[characters/index#😐 表情：全キャラ共通の6段階定義|キャラクター一覧]] を参照。
プロンプトは `workflows/character_prompt_spec.json` から生成した**写し**。食い違った場合はspecが正。

---

## 1. 通常（Neutral）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | ペルソナを維持した日常の顔 |
| **発生タイミング** | 章の序盤・日常会話・社会的対応 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。ペルソナを維持した日常の顔を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
23yo japanese woman, novice high school english teacher, slender petite build, 160cm, short light brown-beige hair, shortest of the four, wispy see-through bangs, flipped-out ends, forehead visible, inner double eyelids, bright light brown irises, straight thin eyebrows, composed dignified gaze, calm composed expression, straight thin eyebrows level, lips lightly closed, upright dignified gaze, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm spring palette, lowest contrast of the four, soft daylight
```

## 2. 笑顔・安堵（Smile）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 魅せる笑顔、または一過性の安堵 |
| **発生タイミング** | 良好な他者対応・危機を脱した錯覚 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。魅せる笑顔、または一過性の安堵を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
23yo japanese woman, novice high school english teacher, slender petite build, 160cm, short light brown-beige hair, shortest of the four, wispy see-through bangs, flipped-out ends, forehead visible, inner double eyelids, bright light brown irises, straight thin eyebrows, composed dignified gaze, gentle small smile, eyes softening into a slight crease, brows relaxed, warm and teacherly, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm spring palette, lowest contrast of the four, soft daylight
```

## 3. 警戒・違和感（Suspicion）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 異変や周囲の視線を察知 |
| **発生タイミング** | 罠の気配・逃げ場の喪失の予感 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。異変や周囲の視線を察知を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
23yo japanese woman, novice high school english teacher, slender petite build, 160cm, short light brown-beige hair, shortest of the four, wispy see-through bangs, flipped-out ends, forehead visible, inner double eyelids, bright light brown irises, straight thin eyebrows, composed dignified gaze, eyes narrowing slightly, brows drawing straighter and lower, lips pressed thin, gaze flicking sideways, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm spring palette, lowest contrast of the four, soft daylight
```

## 4. 抑圧・冷や汗（Anxiety）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 生理的緊張・破綻の隠蔽 |
| **発生タイミング** | 耐えている最中 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。生理的緊張・破綻の隠蔽を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
23yo japanese woman, novice high school english teacher, slender petite build, 160cm, short light brown-beige hair, shortest of the four, wispy see-through bangs, flipped-out ends, forehead visible, inner double eyelids, bright light brown irises, straight thin eyebrows, composed dignified gaze, brows pulled together, beads of cold sweat on the forehead and temple, lower lip caught between the teeth, eyes fixed forward too hard, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm spring palette, lowest contrast of the four, soft daylight
```

## 5. 狼狽・大赤面（Panic）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 破綻の瞬間・激しい羞恥 |
| **発生タイミング** | 露出・失禁の直前〜直後 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。破綻の瞬間・激しい羞恥を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
23yo japanese woman, novice high school english teacher, slender petite build, 160cm, short light brown-beige hair, shortest of the four, wispy see-through bangs, flipped-out ends, forehead visible, inner double eyelids, bright light brown irises, straight thin eyebrows, composed dignified gaze, deep flush spreading from the earlobes down the neck, eyes brimming and wide, mouth fallen open, brows lifted helplessly, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm spring palette, lowest contrast of the four, soft daylight
```

## 6. 虚脱・完全適応（Acceptance）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 尊厳の死滅と被支配への安堵 |
| **発生タイミング** | 屈服・完全適応の結末 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。尊厳の死滅と被支配への安堵を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
23yo japanese woman, novice high school english teacher, slender petite build, 160cm, short light brown-beige hair, shortest of the four, wispy see-through bangs, flipped-out ends, forehead visible, inner double eyelids, bright light brown irises, straight thin eyebrows, composed dignified gaze, light gone from the eyes, unfocused hollow stare, faint resigned smile, face slack, flush fading to pallor, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm spring palette, lowest contrast of the four, soft daylight
```

---

## 🔁 再生成

```bash
python3 -c "import json;s=json.load(open('workflows/character_prompt_spec.json'));c=s['characters']['tanabe-momoka'];[print(k,':',', '.join([c['slots']['subject'],c['slots']['hair'],c['slots']['eyes'],v,s['expression_framing'],c['slots']['tone']]),'\n') for k,v in c['expression_slots'].items()]"
```

**ネガティブプロンプト（共通）:** `worst quality, low quality, bad anatomy, bad hands, missing limbs, extra limbs, cropped, text, watermark, signature, jpeg artifacts, blurry`
