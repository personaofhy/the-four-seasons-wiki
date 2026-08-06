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
| `~/.gemini/antigravity-cli/mcp/comfyui-mcp-server/workflows/` | MCPサーバーが読む実行用ディレクトリ |

```bash
bash scripts/sync_workflows.sh
```

> **シンボリックリンクは不可。** `WorkflowManager._safe_workflow_path()` がパスを `resolve()` してからワークフローディレクトリ配下かを検証するため、リンクは弾かれます。必ず実体コピー（＝上記スクリプト）を使ってください。
>
> 同期後は **MCPサーバーの再起動不要**です。`run_workflow` は mtime ベースでキャッシュを無効化し、ディスクから読み直します（専用ツールとして自動生成される `generate_image` 系のみ再起動が必要）。

---

## 🧩 ワークフロー①：`char_ipadapter`（同一性ロックのみ）

原画1枚から顔立ち・画風を固定する最小構成。素体設定画、表情差分、バストアップ等の**ポーズ指定が不要な用途**向け。

```
[base-ai 原画] ──> IPAdapterAdvanced ──> KSampler ──> SaveImage
```

## 🧩 ワークフロー②：`char_ipadapter_controlnet`（同一性＋ポーズロック）

黄金ルールの完全再現。ポーズ参照画像から Canny で輪郭を抽出し、構図・姿勢を固定します。ピクセルアートLoRA（`pixel-000020`）を内蔵し、**`lora_strength: 0.0` で無効化**できます。

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
| `lora_strength` | float | ✅（②のみ） | 0.0–1.5。ピクセルアート以外は **0.0** |
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
python3 scripts/upload_ref.py content/assets/base-ai/kaede_face_front_base.jpg
```

---

## 📞 呼び出し例（MCP `run_workflow`）

```json
{
  "workflow_id": "char_ipadapter_controlnet",
  "overrides": {
    "prompt": "pixel art, 16-bit retro game sprite, 1girl, Kaede Toyama, elegant long straight black hair, soft drooping eyebrows, cold sweat on forehead, furrowed brows, PC-98 retro pixel game style",
    "negative_prompt": "short hair, brown hair, western face, 3d render, blurry, bad anatomy, text, watermark",
    "character_ref": "kaede_face_front_base.jpg",
    "pose_ref": "himawari_emotion_blush_base.jpg",
    "ip_weight": 0.85,
    "cn_strength": 0.7,
    "lora_strength": 1.0,
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

## 👗 衣装リファレンスを使う

服装はプロンプトだけでは安定しません（後述）。衣装単体の参照画像を作って IP-Adapter に通すのが確実です。楓の紺碧ワンピースは作成済み：

| ファイル | 用途 |
| :--- | :--- |
| `content/assets/references/kaede_dress_navy_ref.png` | 衣装単体（顔なし）。**推奨** |
| `content/assets/references/kaede_dress_navy_worn_ref.png` | 着用イメージボードからの原典クロップ |

作り方：着用写真から衣装部分を切り出す → それを `character_ref` にして `ip_weight: 0.55` 前後で商品写真プロンプトを流す → 出力から頭部を切り落とす。

> `ip_weight` を 0.9 まで上げると人物・背景・照明ごと参照画像に引っ張られ、プロンプトの「白背景・衣装のみ」が効かなくなります。**0.5〜0.6 が衣装抽出の適正値**でした。

---

## ⚠️ 運用上の注意（初回検証で判明）

* **IP-Adapterは画風も引き継ぐ。** 楓の `base-ai` 原画はリアル寄りのため、プロンプトで `pixel art` を指定しても**ピクセルアートにはならない**。ドット絵スプライトを作るには、桃香の `momoka_expr1_base.jpg` に相当する**ドット絵版の楓原画**を先に用意する必要がある（16色化は生成後の減色工程 `strict-16colors/` が担当）。
* **ControlNetは参照画像の構図をそのまま強制する。** クローズアップ顔の参照（`himawari_emotion_blush_base.jpg`）を `cn_strength: 0.7` で使うと、出力も極端なクローズアップになり構図が破綻した。バストアップが欲しい場合はバストアップの参照を使うか、`cn_strength` を 0.3–0.4 まで下げる。
* **チェックポイントが画風を決める。** `Counterfeit-V3.0` はアニメモデルのため、リアル系の確定素体（`kaede_body_tpose_base.jpg` のようなセミリアル3Dレンダ調）に寄せたい場合は必ず `dreamshaper_8.safetensors` を指定する。プロンプトに `photorealistic` と書いてもモデルの画風は覆せない。
* **服装の細部はプロンプトでは制御しきれない。** 楓の紺ワンピースでは、スカートのスリット・ストッキングの色・ベルトの色が繰り返し破綻した。否定プロンプトを盛るほど衣装全体が崩壊する（袖だけ別色になる等）ので、**衣装参照画像を使うこと**。
* 中間生成物は黄金ルール③に従い `content/assets/intermediates/` に保存する。

---

### 📂 関連ファイル
* ワークフロー正本: `workflows/char_ipadapter.json` / `workflows/char_ipadapter_controlnet.json`
* 同期スクリプト: `scripts/sync_workflows.sh`
* アップロードスクリプト: `scripts/upload_ref.py`
* [[rules/comfyui-image-generation-reflection|画像生成 黄金ルール（反省ノート）]]
