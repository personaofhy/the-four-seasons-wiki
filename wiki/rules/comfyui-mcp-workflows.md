---
title: 🔌 ComfyUI MCP用 キャラクター生成ワークフロー規定
---

# 🔌 ComfyUI MCP用 キャラクター生成ワークフロー規定

[[rules/comfyui-image-generation-reflection|画像生成 黄金ルール]]（IP-Adapter必須・ControlNet併用）を、**MCP経由でそのまま呼び出せる**ようにしたワークフローテンプレートの仕様です。

標準の `generate_image` ワークフローは txt2img のみで、黄金ルール①「既存キャラの生成には必ず `base-ai` 原画を IP-Adapter に通すこと」を満たせません。そのため専用のテンプレート2種をリポジトリ内に持ち、MCPサーバーのワークフローディレクトリへ同期して使用します。

---

## 📁 ファイル配置と同期

| 場所 | 役割 |
| :--- | :--- |
| `workflows/*.json` | **正本**（リポジトリ管理・編集はここ） |
| `workflows/character_prompt_spec.json` | **プロンプトの正本**（下記・実行用ワークフローではない） |
| `~/.gemini/antigravity-cli/mcp/comfyui-mcp-server/workflows/` | MCPサーバーが読む実行用ディレクトリ |

```bash
bash scripts/sync_workflows.sh
```

> **シンボリックリンクは不可。** `WorkflowManager._safe_workflow_path()` がパスを `resolve()` してからワークフローディレクトリ配下かを検証するため、リンクは弾かれます。必ず実体コピー（＝上記スクリプト）を使ってください。
>
> 同期後は **MCPサーバーの再起動不要**です。`run_workflow` は mtime ベースでキャッシュを無効化し、ディスクから読み直します（専用ツールとして自動生成される `generate_image` 系のみ再起動が必要）。

---

## 🔤 プロンプトのスロット順（固定）

`PARAM_PROMPT` に渡す文字列は、**必ず `workflows/character_prompt_spec.json` から組み立てる**。手書き禁止。

| # | スロット | 内容 |
| :-: | :--- | :--- |
| 1 | `subject` | 年齢・国籍・社会的役割・身長・体型 |
| 2 | `hair` | 長さ・色・質感・スタイリング |
| 3 | `eyes` | 形・二重・虹彩色・眉 |
| 4 | `top` | 上衣：素材・色・着方 |
| 5 | `bottom` | 下衣：丈・シルエット（ワンピースはスカート部をここに） |
| 6 | `legwear_shoes` | 脚衣＋靴。**留め具（紐／マジックテープ）は必ず明示**（キャラ造形の核） |
| 7 | `tone` | 季節パレット・コントラスト・肌・光 |

```bash
python3 -c "import json;s=json.load(open('workflows/character_prompt_spec.json'));print(', '.join(s['characters']['toyama-kaede']['slots'][k] for k in s['slot_order']))"
```

> [!warning] 禁止トークン
> * **実在人物名** — frontmatter の `face_model`（例：俳優名）は**内部の配役メモであって、プロンプトに入れてはならない**。実在人物の肖像に寄せた画像生成になる。
> * **`pixel art` / `16-bit` / `retro game` 系** — レトロゲーム路線は撤回済み。
> * **章ごとの破綻状態** — ベースプロンプトには入れず、シーン別のオーバーライドとして扱う。

> [!note] 衣装ノートとの関係
> 各 `characters/*/outfits/*.md` の「画像生成タグ」欄は、このspecから生成した**写し**。食い違った場合はspec側が正。ノートを手で直さず、spec を直して再生成すること。

---

## 🧩 ワークフロー①：`char_ipadapter`（同一性ロックのみ）

原画1枚から顔立ち・画風を固定する最小構成。素体設定画、表情差分、バストアップ等の**ポーズ指定が不要な用途**向け。

```
[base-ai 原画] ──> IPAdapterAdvanced ──> KSampler ──> SaveImage
```

## 🧩 ワークフロー②：`char_ipadapter_controlnet`（同一性＋ポーズロック）

黄金ルールの完全再現。ポーズ参照画像から Canny で輪郭を抽出し、構図・姿勢を固定します。旧路線のピクセルアートLoRA（`pixel-000020`）がグラフに残っているが、**路線封印につき `lora_strength` は常に `0.0`** とすること。

```
[base-ai 原画] ──> IPAdapterAdvanced ──┐
                                       ├──> KSampler ──> SaveImage
[ポーズ参照] ──> Canny ──> ControlNet ──┘
```

---

## ⚙️ 固定値（変更するにはJSONを編集）

| 項目 | 値 | 理由 |
| :--- | :--- | :--- |
| Checkpoint | `Counterfeit-V3.0_fix_fp16.safetensors` | IP-Adapter / ControlNet が SD1.5 系のため固定。グローバル既定値（`dreamshaper_8`）に上書きされるのを防ぐ目的もある |
| IP-Adapter | `ip-adapter_sd15.safetensors` ＋ `clip_vision_h.safetensors` | |
| ControlNet | `control_v11p_sd15_canny_fp16.safetensors`（Canny閾値 100/200、`end_percent` 0.85） | |
| Sampler / Scheduler | `euler_ancestral` / `karras`、`denoise` 1.0 | 桃香の成功例と同一 |

## 🎛 パラメーター一覧

| パラメーター | 型 | 必須 | 備考 |
| :--- | :--- | :--- | :--- |
| `prompt` | str | ✅ | ポジティブプロンプト |
| `character_ref` | str | ✅ | **ComfyUI input内のファイル名**（例 `kaede_face_front_base.jpg`） |
| `pose_ref` | str | ✅（②のみ） | 同上。Cannyで輪郭抽出される |
| `ip_weight` | float | ✅ | 0.0–2.0。推奨 0.8–0.85 |
| `cn_strength` | float | ✅（②のみ） | 0.0–2.0。推奨 0.5–0.7 |
| `lora_strength` | float | ✅（②のみ） | **常に 0.0。**旧ピクセルアートLoRA用の枠で、路線封印により使用しない |
| `filename_prefix` | str | ✅ | 出力ファイル名の接頭辞 |
| `negative_prompt` | str | ⚠️ | 省略するとグローバル既定値 `"text, watermark"` に落ちるため**毎回明示**すること |
| `seed` | int | – | 省略時はランダム生成 |
| `width` / `height` | int | – | 省略時 512×512。全身は 512×768 推奨 |
| `steps` / `cfg` | int / float | – | 省略時 20 / 8.0。推奨 25 / 7.0 |

> **必須パラメーターを省略すると、プレースホルダ文字列（`PARAM_...`）がそのままComfyUIへ渡ります。** MCPサーバーの既定値機構は標準名（`seed` `width` `height` `steps` `cfg` `negative_prompt`）にしか働かないため、それ以外は必ず指定してください。

---

## 📤 参照画像のアップロード

`LoadImage` は ComfyUI 側の input ディレクトリしか見ません。MCPにアップロード機能はないため、新規の原画・ポーズ参照は先に転送します。

```bash
python3 scripts/upload_ref.py content/assets/characters/kaede/face/kaede_face_front_base.jpg
```

---

## 📞 呼び出し例（MCP `run_workflow`）

```json
{
  "workflow_id": "char_ipadapter_controlnet",
  "overrides": {
    "prompt": "26yo japanese woman, corporate career-track employee, long deep warm brown-black straight hair in a low chignon updo, round dark wide-set eyes slightly drooping light brown irises, brows drawn hard together, cold sweat running from temple to jaw, lips pressed white, bust-up portrait, plain neutral background, warm autumn palette",
    "negative_prompt": "short hair, brown hair, western face, 3d render, blurry, bad anatomy, text, watermark",
    "character_ref": "kaede_face_front_base.jpg",
    "pose_ref": "himawari_emotion_blush_base.jpg",
    "ip_weight": 0.85,
    "cn_strength": 0.7,
    "lora_strength": 0.0,
    "width": 512,
    "height": 768,
    "steps": 25,
    "cfg": 7.0,
    "seed": 555123,
    "filename_prefix": "kaede_expr_anxiety"
  }
}
```

---

## 🧩 ワークフロー③：`char_ipadapter_dual`（顔＋素体の2枚同時参照）

`ImageBatch` で確定済みリファレンス2枚を1つのIP-Adapterに流し込む構成。全身設定画向け。

* **顔だけを参照すると構図がバストアップに寄る**（IP-Adapterは参照画像の画角も引き継ぐ）
* **Tポーズ素体は首から上が切れているため ControlNet に使えない**（輪郭を固定すると頭部のない人物が出る）

この2つを同時に回避するための構成です。パラメーターは `character_ref` の代わりに `face_ref` / `body_ref` を取ります。

---

## 🗺️ ワークフロー④：`depth_map`（深度マップ生成）

指定した画像から ControlNet Depth 用の深度マップを作り、**任意のサブフォルダへ保存**します。チェックポイントもサンプラーも通らない純粋な前処理グラフなので、seed・prompt・サイズ指定はありません（出力は元画像のアスペクトを保持）。

```bash
# 1. 元画像を ComfyUI input へ送る
python3 scripts/upload_ref.py content/assets/characters/kaede/body/kaede_body_tpose_base.jpg

# 2. run_workflow で depth_map を実行（filename_prefix にサブフォルダを含められる）
#    例: "depth-maps/kaede_body_tpose" → <ComfyUI output>/depth-maps/ に保存

# 3. 結果を Vault へ取り込む
python3 scripts/fetch_output.py kaede_body_tpose_00001_.png \
  --subfolder depth-maps --dest content/assets/depth-maps \
  --as kaede_body_tpose_depth.png
```

| パラメーター | 推奨値 | 備考 |
| :--- | :--- | :--- |
| `source_image` | – | ComfyUI input 内のファイル名 |
| `midas_a` | 6.28 | 画角に相当する項 |
| `bg_threshold` | 0.1 | 上げると背景がより黒く落ち、被写体が分離される |
| `resolution` | 1024 | 出力の長辺基準 |
| `filename_prefix` | `depth-maps/xxx` | **スラッシュでサブフォルダ指定可** |

> [!warning] Depth Anything V2 は使えない
> 精度では DepthAnything V2 が上ですが、**ComfyUIマシンのディスクが満杯**で初回のモデル自動ダウンロードが `[Errno 28] No space left on device` で失敗します。
> ディスクを空ければ `DepthAnythingV2Preprocessor` に差し替えられます（`ckpt_name` は `depth_anything_v2_vitl.pth`）。
>
> **MiDaS と Zoe は既にモデルがキャッシュ済み**で動作します。両者を比較した結果、Zoe は腕の背後に黒い塊が出て身体も白飛び気味だったため、シルエットが締まり背景が滑らかな **MiDaS を採用**しました。

---

## 🎭 ワークフロー⑤：`face_swap_masked`（顔だけ差し替え）

既存画像の**マスクした領域だけ**を、指定キャラの同一性で描き直します。「顔だけ変える」ために3段構えになっています。

| 仕組み | 役割 |
| :--- | :--- |
| IPAdapterの `attn_mask` | 同一性の効果をマスク内に限定（マスクなしだと画風・照明・背景まで参照元に寄る） |
| `SetLatentNoiseMask` | マスク内だけをノイズ除去 |
| `ImageCompositeMasked` | 元画像に合成し、**マスク外のピクセルを完全保証** |

### 検証で確定した設定値

| パラメーター | 値 | 理由 |
| :--- | :--- | :--- |
| `mask_blur` / `mask_sigma` | **31 / 8** | 継ぎ目を消すために必須 |
| `strength` | **0.5** | 0.75だと元の顔の角度を無視して正面を向く |
| `cn_strength` | **0.6** | depthで頭部の位置を保持 |
| `mask_expand` | 6 | |
| `ip_weight` | 0.9 | |

> [!warning] `FeatherMask` は使えない
> Core の `FeatherMask` は **マスク画像の外周（画像の縁）** をフェードさせるノードで、画面中央に描いた楕円などの**形状の輪郭はぼかしません**。これを使った初回テストでは、額に三角形の継ぎ目、頬に縦の切れ目がはっきり残りました。
> 正しくは `MaskToImage → ImageBlur → ImageToMask` で輪郭をぼかします。本ワークフローはこの構成です。

> [!note] マスクは手作りが必要
> このComfyUIには **顔の自動検出がありません**（Impact Pack・SAM ともに未導入）。マスクは元画像と同サイズのPNG（塗り替える部分が白、他が黒）を用意してアップロードします。**顔だけでなく生え際まで含めた広めの範囲**を取ると馴染みます。
> 自動化するなら Impact Pack か SAM のインストールが必要です。

---

## 👗 衣装リファレンスを使う

服装はプロンプトだけでは安定しません（後述）。衣装単体の参照画像を作って IP-Adapter に通すのが確実です。楓の紺碧ワンピースは作成済み：

| ファイル | 用途 |
| :--- | :--- |
| `content/assets/characters/kaede/outfit/kaede_outfit_dress_ref.png` | 衣装単体（顔なし）。**推奨** |
| `content/assets/characters/kaede/outfit/kaede_outfit_dress_worn_ref.png` | 着用イメージボードからの原典クロップ |

作り方：着用写真から衣装部分を切り出す → それを `character_ref` にして `ip_weight: 0.55` 前後で商品写真プロンプトを流す → 出力から頭部を切り落とす。

> `ip_weight` を 0.9 まで上げると人物・背景・照明ごと参照画像に引っ張られ、プロンプトの「白背景・衣装のみ」が効かなくなります。**0.5〜0.6 が衣装抽出の適正値**でした。

---

## ⚠️ 運用上の注意（初回検証で判明）

* **IP-Adapterは画風も引き継ぐ。** 参照画像の画風がそのまま出力に乗るため、**画風はプロンプトではなく参照画像で決まる**。狙った画風があるなら、その画風の原画を先に用意すること。
* **ControlNetは参照画像の構図をそのまま強制する。** クローズアップ顔の参照（`himawari_emotion_blush_base.jpg`）を `cn_strength: 0.7` で使うと、出力も極端なクローズアップになり構図が破綻した。バストアップが欲しい場合はバストアップの参照を使うか、`cn_strength` を 0.3–0.4 まで下げる。
* **チェックポイントが画風を決める。** `Counterfeit-V3.0` はアニメモデルのため、リアル系の確定素体（`kaede_body_tpose_base.jpg` のようなセミリアル3Dレンダ調）に寄せたい場合は必ず `dreamshaper_8.safetensors` を指定する。プロンプトに `photorealistic` と書いてもモデルの画風は覆せない。
* **服装の細部はプロンプトでは制御しきれない。** 楓の紺ワンピースでは、スカートのスリット・ストッキングの色・ベルトの色が繰り返し破綻した。否定プロンプトを盛るほど衣装全体が崩壊する（袖だけ別色になる等）ので、**衣装参照画像を使うこと**。
* 中間生成物は黄金ルール③に従い `content/assets/_scratch/` に保存する。

---

### 📂 関連ファイル
* ワークフロー正本: `workflows/char_ipadapter.json` / `workflows/char_ipadapter_controlnet.json`
* 同期スクリプト: `scripts/sync_workflows.sh`
* アップロードスクリプト: `scripts/upload_ref.py`
* [[rules/comfyui-image-generation-reflection|画像生成 黄金ルール（反省ノート）]]
