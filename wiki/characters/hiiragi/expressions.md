---
title: "橘 柊 表情設定：6段階"
type: expressions
character_id: tachibana-hiiragi
decision_default: draft
decision_states:
  prompts: draft  # spec から生成した初版・未検証
  images: open    # 全6枚未生成
tags: [expressions, character/tachibana-hiiragi, season/冬]
---

# ❄️ 橘 柊 表情設定：6段階

> [!abstract] この人物の表情設計
> **コントラスト:** 4人中もっとも強い
> **高コントラストゆえ、赤面が最も劇的に出る。**真っ黒な髪と青白い肌の中で、赤は他3人より強く見える。一方で**人形的な静止**が基調なので、段階1〜3では顔をほとんど動かさないこと。
> **段階の進み方:** **唯一、段階6が「安堵」ではなく「充足」として描かれる。**他3人の6が虚脱なのに対し、柊の6は自ら選んだ結果なので、微笑が壊れていない。

共通の6段階定義は [[characters/index#😐 表情：全キャラ共通の6段階定義|キャラクター一覧]] を参照。
プロンプトは `workflows/character_prompt_spec.json` から生成した**写し**。食い違った場合はspecが正。

---

## 1. 通常（Neutral）

| 項目 | 内容 |
| :--- | :--- |
| **定義** | ペルソナを維持した日常の顔 |
| **発生タイミング** | 章の序盤・日常会話・社会的対応 |
| **状態** | `open` — 画像未生成 |

|                        参照画像                        | 意図                                                                                                        |
| :------------------------------------------------: | :-------------------------------------------------------------------------------------------------------- |
| ![未生成](wiki/assets/templates/placeholder_full.jpg) | **`open`／未生成。**バストアップ・正面・無地背景。ペルソナを維持した日常の顔を、上記「この人物の表情設計」の方針で描き分けたもの。6枚は**同一の構図・光・距離**で揃えること（並べて比較するため）。 |

```text
19yo japanese university student, aspiring idol, petite soft rounded build, 155cm, medium bob, pure black with a blue cast, delicate, large round moist eyes, palest grey irises of the four, doll-like, doll-like blank calm, huge round pale grey eyes, small mouth closed, face very still, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool winter palette, highest contrast of the four, pale skin against black hair
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
19yo japanese university student, aspiring idol, petite soft rounded build, 155cm, medium bob, pure black with a blue cast, delicate, large round moist eyes, palest grey irises of the four, doll-like, tiny careful smile, pale grey eyes curving, cheeks barely lifting, fragile and rehearsed, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool winter palette, highest contrast of the four, pale skin against black hair
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
19yo japanese university student, aspiring idol, petite soft rounded build, 155cm, medium bob, pure black with a blue cast, delicate, large round moist eyes, palest grey irises of the four, doll-like, huge eyes widening further, pupils shrinking, small mouth compressing, chin pulling back into the scarf, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool winter palette, highest contrast of the four, pale skin against black hair
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
19yo japanese university student, aspiring idol, petite soft rounded build, 155cm, medium bob, pure black with a blue cast, delicate, large round moist eyes, palest grey irises of the four, doll-like, brows tented upward, cold sweat on the pale forehead, lower lip bitten hard, enormous eyes glassy and fixed, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool winter palette, highest contrast of the four, pale skin against black hair
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
19yo japanese university student, aspiring idol, petite soft rounded build, 155cm, medium bob, pure black with a blue cast, delicate, large round moist eyes, palest grey irises of the four, doll-like, stark red flush blazing across the white face and ears, pale grey eyes flooded with tears, mouth open in a small round gasp, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool winter palette, highest contrast of the four, pale skin against black hair
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
19yo japanese university student, aspiring idol, petite soft rounded build, 155cm, medium bob, pure black with a blue cast, delicate, large round moist eyes, palest grey irises of the four, doll-like, pale grey eyes gone flat and dull, thousand-yard stare, mouth curved into a small contented childlike smile, face utterly relaxed, bust-up portrait, head and shoulders, facing viewer, plain neutral background, even soft lighting, cool winter palette, highest contrast of the four, pale skin against black hair
```

---

## 🔁 再生成

```bash
python3 -c "import json;s=json.load(open('workflows/character_prompt_spec.json'));c=s['characters']['tachibana-hiiragi'];[print(k,':',', '.join([c['slots']['subject'],c['slots']['hair'],c['slots']['eyes'],v,s['expression_framing'],c['slots']['tone']]),'\n') for k,v in c['expression_slots'].items()]"
```

**ネガティブプロンプト（共通）:** `worst quality, low quality, bad anatomy, bad hands, missing limbs, extra limbs, cropped, text, watermark, signature, jpeg artifacts, blurry`
