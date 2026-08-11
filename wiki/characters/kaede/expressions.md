---
title: "遠山 楓 表情設定：6段階"
type: expressions
character_id: toyama-kaede
decision_default: draft
decision_states:
  prompts: draft  # spec から生成した初版・未検証
  images: open    # 全6枚未生成
tags: [expressions, character/toyama-kaede, season/秋]
---

# 🍁 遠山 楓 表情設定：6段階

> [!abstract] この人物の表情設計
> **コントラスト:** 中程度（上から2番目）
> **崩れないことが顔の芸である。**離れ目・やや垂れ目という本来ゆるい造作を、緊張で引き締めて「女神」を成立させている。段階4では**造作そのものは動かさず、汗と喉の緊張だけで**耐えていることを示す。
> **段階の進み方:** 段階1〜4を長く保ち、段階5が**極端に短い**。落差の大きさが楓の設計であり、5を一瞬で通過して6に落ちる。

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
| ![未生成](../../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。ペルソナを維持した日常の顔を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
26yo japanese woman, corporate career-track employee, slim long-legged model figure, 165cm, long deep warm brown-black straight hair worn in a low chignon updo, round dark wide-set eyes, slightly drooping, light brown irises, serene poised expression, wide-set drooping eyes calm, brows softly arched, faint composed smile of authority, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm autumn palette, medium contrast, fair skin
```

## 2. 笑顔・安堵（Smile）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 魅せる笑顔、または一過性の安堵 |
| **発生タイミング** | 良好な他者対応・危機を脱した錯覚 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。魅せる笑顔、または一過性の安堵を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
26yo japanese woman, corporate career-track employee, slim long-legged model figure, 165cm, long deep warm brown-black straight hair worn in a low chignon updo, round dark wide-set eyes, slightly drooping, light brown irises, elegant measured smile, eyes curving warmly, chin slightly lowered, gracious and untouchable, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm autumn palette, medium contrast, fair skin
```

## 3. 警戒・違和感（Suspicion）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 異変や周囲の視線を察知 |
| **発生タイミング** | 罠の気配・逃げ場の喪失の予感 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。異変や周囲の視線を察知を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
26yo japanese woman, corporate career-track employee, slim long-legged model figure, 165cm, long deep warm brown-black straight hair worn in a low chignon updo, round dark wide-set eyes, slightly drooping, light brown irises, drooping eyes sharpening, brows lowering a fraction, jaw setting, gaze held very still, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm autumn palette, medium contrast, fair skin
```

## 4. 抑圧・冷や汗（Anxiety）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 生理的緊張・破綻の隠蔽 |
| **発生タイミング** | 耐えている最中 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。生理的緊張・破綻の隠蔽を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
26yo japanese woman, corporate career-track employee, slim long-legged model figure, 165cm, long deep warm brown-black straight hair worn in a low chignon updo, round dark wide-set eyes, slightly drooping, light brown irises, brows drawn hard together, cold sweat running from temple to jaw, lips pressed white, eyes glassy with effort, throat tight, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm autumn palette, medium contrast, fair skin
```

## 5. 狼狽・大赤面（Panic）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 破綻の瞬間・激しい羞恥 |
| **発生タイミング** | 露出・失禁の直前〜直後 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。破綻の瞬間・激しい羞恥を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
26yo japanese woman, corporate career-track employee, slim long-legged model figure, 165cm, long deep warm brown-black straight hair worn in a low chignon updo, round dark wide-set eyes, slightly drooping, light brown irises, crimson flush flooding the face and neck, wide-set eyes blown open and wet, mouth twisted open, composure shattered, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm autumn palette, medium contrast, fair skin
```

## 6. 虚脱・完全適応（Acceptance）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | 尊厳の死滅と被支配への安堵 |
| **発生タイミング** | 屈服・完全適応の結末 |
| **状態** | `open` — 画像未生成 |

| 参照画像 | 意図 |
| :---: | :--- |
| ![未生成](../../assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。尊厳の死滅と被支配への安堵を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
26yo japanese woman, corporate career-track employee, slim long-legged model figure, 165cm, long deep warm brown-black straight hair worn in a low chignon updo, round dark wide-set eyes, slightly drooping, light brown irises, eyes dulled and unseeing, head tilted down, mouth softened into a small broken smile, all tension gone from the face, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, warm autumn palette, medium contrast, fair skin
```

---

## 🔁 再生成

```bash
python3 -c "import json;s=json.load(open('workflows/character_prompt_spec.json'));c=s['characters']['toyama-kaede'];[print(k,':',', '.join([c['slots']['subject'],c['slots']['hair'],c['slots']['eyes'],v,s['expression_framing'],c['slots']['tone']]),'\n') for k,v in c['expression_slots'].items()]"
```

**ネガティブプロンプト（共通）:** `worst quality, low quality, bad anatomy, bad hands, missing limbs, extra limbs, cropped, text, watermark, signature, jpeg artifacts, blurry`
