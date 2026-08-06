# 🍁 遠山楓（Kaede）`image-79` 構図再現・超リアル生成プロンプト集

元画像 `image-79.png`（四つん両手つき・突き出された丸いお尻・股間/ヴァギナの繊細な素肌スリット・振り返り美貌）を、ComfyUI や Stable Diffusion、Midjourney 等で完璧に直接生成させるための専用プロンプトセットです。

---

## 🎨 1. ComfyUI / SD1.5 / SDXL 用（最高画質・リアル肉体・デリケートゾーン再現）

### 🌟 ポジティブプロンプト (Positive Prompt)

```text
masterpiece, best quality, ultra detailed, photorealistic, 8k photo, raw photo, (1girl:1.5), (crouching on all fours:1.6), (arching back:1.5), (protruding large round nude buttocks:1.7), (view from behind:1.5), looking back over shoulder at camera, (completely bare nude skin buttocks:1.8), (naked smooth bottom:1.8), (detailed pussy slit between buttocks:1.6), (realistic vulva detail:1.5), (soft pink skin tone:1.4), (subtle shadow in crotch area:1.4), (mature 24yo adult Japanese woman:1.5), (healthy natural female body:1.5), (soft supple waist and hips:1.5), (beautiful 24yo Japanese face like Manami Konishi:1.6), (innocent doe-like dewy dark eyes looking back at viewer:1.6), (soft drooping dark chocolate brown eyebrows:1.6), (blushing embarrassed flustered gentle expression:1.6), (flowing glossy long black wavy hair:1.5), dewy porcelain skin, soft warm autumn studio lighting, plain neutral grey studio background
```

### 🚫 ネガティブプロンプト (Negative Prompt)

```text
(panties covering buttocks:2.0), (underwear covering buttocks:2.0), (stockings covering buttocks:2.0), (fabric on buttocks:1.8), (skinny:1.8), (emaciated:1.8), (bony:1.8), (flat buttocks:1.8), (young:1.8), (underage:1.8), (childish:1.8), (loli:1.8), (jet black thick eyebrows:1.8), (arched fierce eyebrows:1.8), (harsh expression:1.8), (multiple faces:1.8), (multiple people:1.8), (caucasian:1.8), (western features:1.8), (deformed body:1.8), (extra limbs:1.8), (bad hands:1.8), (bad feet:1.8), text, watermark, frame, border
```

---

## ⚙️ 2. おすすめ生成パラメータ (Recommended Generation Parameters)

> * **Model (Checkpoint):** `DreamShaper 8` (実写・グラビア向け) / `Counterfeit-V3.0` (アニメ調の場合)
> * **Sampler:** `dpmpp_2m` / `karras`
> * **Steps:** 32 ~ 40
> * **CFG Scale:** 6.5 ~ 7.5
> * **ControlNet (任意):** `control_v11f1p_sd15_depth.pth` (強度: `0.70`, ポーズ完全固定用)
> * **IP-Adapter (任意):** `kaede_face_front_base.jpg` (重み: `0.45`, 確定顔移植用)
