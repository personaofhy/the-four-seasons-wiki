---
title: 🧪 Klein と SDXL の役割分担 — 「意味」と「質感」を分けて描く
type: rule
status: draft
tags: [comfyui, workflow, flux2, sdxl]
---

# 🧪 Klein と SDXL の役割分担 — 「意味」と「質感」を分けて描く

[[rules/comfyui-image-generation-reflection|キャラクター同一性の反省ノート]] が「**誰を**描くか」の話だとすれば、
本ノートは「**何が起きている状態を**描くか」の話である。

対象は、**関係性や状態を含む指定**——「開いた状態で」「その中心に」「周囲は乾いているので対比で読める」——を
画像に落とす工程。ここでモデルの選択を間違えると、何度回しても出ない。

---

## 1. 発端 — 同じ指示が3回とも無視された

「クロッチを広げた状態の下着に、シミが乗っている」画像を RealVisXL_V5.0（SDXL）で生成しようとした。

| 回 | 変更点 | 結果 |
| :--- | :--- | :--- |
| 1 | ハンガー吊り・タグ列プロンプト | 下着が2枚に増殖。**シミなし** |
| 2 | フラットレイ化、白いガセットを明示、増殖をネガティブで抑制 | 増殖は解消。**開かず、シミなし** |
| 3 | 裏返し（inside out）指定 | ガセットは見えた。**シミは完全にゼロ** |

3回目がもっとも「綺麗な商品写真」になった。これが症状の本質を示している。

> [!warning] SDXLは汚れを正常化する
> RealVisXL の「ランジェリー平置き」の事前分布は**ECの商品撮影に強く支配されている**。
> シミ・汚れの語は無視されるだけでなく、**打ち消される方向に働く**。
> プロンプトの書き方の問題ではないので、語を盛っても解決しない。

---

## 2. 原因は描画力ではなく読解力

SDXL の CLIP は、入れ子の関係を持つ指示を**トークンの袋に平坦化する**。
「Aを開いた状態にして、その中心にBがあり、Bの周囲のCは乾いているのでBが読める」——
この構文は保持されない。

FLUX.2 Klein は Qwen3 系のテキストエンコーダを積んでおり、ここが構造的に強い。

**同じ内容を自然文1回で投げたところ、初回で通った。**

| 工程 | 担当 | 根拠 |
| :--- | :--- | :--- |
| 意味・構図・関係性の解釈 | **Klein** | SDXL 3回失敗 → Klein 初回成功 |
| 内容そのものの修正 | **Kleinに戻って言い直す** | 後処理・img2img いずれも失敗（§3） |
| 布や肌の質感の仕上げ | SDXL | ただし**曖昧な領域には触らせない** |
| 局所修正 | CLIPSeg → inpaint | §5 |

---

## 3. 失敗した2つの修正ルート（やらないこと）

Klein の初回出力は構図こそ正しかったが、シミが**錆色で、中心に暗い芯**があった。
これを直そうとして2つ試し、どちらも失敗した。

### ❌ SDXL img2img で色と質感を移す

| denoise | 結果 |
| :--- | :--- |
| 0.45 | **シミが「花の飾り」に化けた** |
| 0.28 | 花にはならないが、**光沢を持った「こぼれた液体」**になり暗い芯も残存 |

§1と同じ事象の別の出方である。画面中央の曖昧な塊を、SDXLは「汚れ」ではなく
「もっともらしい綺麗なもの」として説明しにいく。

このとき、ネガティブに `circular blot, spilled liquid` と**シミ性を否定する語を入れたのが逆効果**だった。
ネガティブ設計を誤ると、モデルを「花」の側へ後押ししてしまう。

### ❌ 後処理での色補正

HSVでシミ画素を抽出して色相をずらす方法を試した。14,911画素を選択できたが、**見た目はほぼ変わらなかった。**

シミの芯が暗い灰色で**彩度が低く、色相補正の網に掛からない**ため。
つまりこれは色相の問題ではなく「暗い芯がある」という**構造の問題**で、後処理で殴る筋ではない。

---

## 4. 効いた方法 — 否定形を文として書く

Klein に戻り、色を言葉で直接指定し直した。

```
The stain is a VERY PALE, FAINT YELLOW — a soft washed-out straw colour, only slightly
deeper than the white cotton around it. It is NOT brown, NOT rust coloured, NOT orange,
and there is NO dark or grey patch at its centre; the middle of the stain is the same
pale yellow as the rest of it.
```

これで一発で通った。

> [!important] Kleinは肯定文中の否定を「文」として読む
> SDXLのネガティブプロンプト（別枠の語リスト）とは別物である。
> **「〜ではない」を本文に書くと効く。** これが今回もっとも実用的な発見。

---

## 5. テンプレートが使い切っていなかった2つのレバー（実測済み）

現行の `studio/references/workflows/flux2_txt2img.json` は `BasicGuider` を使っており、**ネガティブ条件の枠自体が無い**。
差し替えて実測した結果は以下。

### ✅ `CFGGuider` — 採用

```
CLIPTextEncode(positive) → FluxGuidance ─┐
CLIPTextEncode(negative) ────────────────┴→ CFGGuider(cfg 3.5) → SamplerCustomAdvanced
```

`BasicGuider` を `CFGGuider` に差し替えるだけで `positive / negative / cfg` が揃う。
**これが現時点の最良構成。** シミの色が安定し、タグの文字化けも消えた。

> [!tip] 否定の置き場所が2つになる
> §4の「否定形を本文に書くと効く」は、**ネガティブ枠が無かったから本文に書くしかなかった**とも言える。
> 両方使えるなら、本文は肯定的な描写に専念させ、除外はネガティブ枠へ逃がすとプロンプトが読みやすい。

### ⚠️ `ReferenceLatent` — 動くが、用途を選ぶ

```
CLIPTextEncode → FluxGuidance → ReferenceLatent(latent=VAEEncode(画像)) → CFGGuider
```

Klein内でのimg2img／編集として**機能することは確認できた**。参照画像の構図・背景・皺を保持して再生成する。

ただし**参照への束縛が強く、「消す」指示が通らない。**
本文とネガティブの両方で「ラベルもタグも無い」と指定したにもかかわらず、
参照画像にあった衣類タグがそのまま残った。

| 用途 | 可否 |
| :--- | :--- |
| 構図を保ったまま質感やディテールを詰める | ✅ |
| 画面内の要素を**除去する** | ❌ inpaintの仕事 |

### ❌ `FluxGuidance` — `CFGGuider` と併用すると死ぬ

同一シード・同一プロンプトで guidance のみ 3.0 / 6.0 と振った結果、**出力は完全に一致した。**

```
mean abs diff = 0.0000 / 255,  max = 0,  差のある画素 0.0000%
```

> [!warning] `CFGGuider` を使うなら `FluxGuidance` の値は無意味
> 効くノブは `CFGGuider` の `cfg` のほう。`FluxGuidance` を調整しても何も起きない。
> `BasicGuider` 構成では逆に `FluxGuidance` が唯一のノブになる。**両者は排他的**と考えてよい。

### ✅ プロンプト語順 — 効くが、トレードオフ

主語を入れ替えると、前に出した対象が強くなり、後ろに下げた対象が弱くなる。

| 語順 | 結果 |
| :--- | :--- |
| 「ミントグリーンのショーツがあり…その中心にシミ」 | 下着の色は設定通り。シミは控えめ |
| 「白いコットンにシミがあり…それはショーツのガセットの中心」 | **シミが拡大**。ただし**ミント色が後退**し、ほぼ白い下着になる |

単純な改善ではなく**何を主役にするかの選択**。コマの意図で使い分ける。

> [!danger] `Flux2ImageNode` / `Flux2ProImageNode` / `Flux2MaxImageNode` は使わない
> これらは Black Forest Labs の**有料APIノード**であり、ローカルGPUでは動かない。
> ローカルのKleinは `UNETLoader` + `CLIPLoader(type: flux2)` + `VAELoader` の経路。

---

## 6. 実測値（RTX 4070 Laptop / VRAM 8GB）

| 構成 | 解像度 | steps | 所要 | 1枚あたり |
| :--- | :--- | :--- | ---: | ---: |
| Klein 4B fp8・**コールド** | 1216x832 | 26 | 91秒 | 91秒 |
| Klein 4B fp8・**ウォーム** | 1216x832 | 26 | **53秒** | **53秒** |
| Klein 4B fp8・**batch 4** | 1216x832 | 26 | 304秒 | **76秒** |
| RealVisXL V5.0 txt2img | 1216x832 | 30 | 124〜127秒 | — |
| RealVisXL V5.0 txt2img | 832x1216 | 30 | 29秒（ウォーム） | — |
| RealVisXL V5.0 img2img | 1216x832 | 30 / denoise 0.45 | 103秒 | — |

**Kleinのほうが速い。** 4Bなので当然だが、「重いから最後に回す」という発想は誤り。

> [!danger] `batch_size` を上げてはいけない（VRAM 8GB環境）
> batch 4 は 1枚あたり **76秒** で、ウォームの単発 **53秒** より**遅い**。
> 1216x832×4 はVRAMに対して重すぎ、オフロードの分だけ悪化する。
>
> **効くのはバッチ化ではなくモデルの常駐。** ComfyUIはキュー間でモデルを保持するので、
> 単に連続で積むだけで 91秒 → 53秒（1.7倍）が得られる。バッチ化する必要はない。

導入済みモデル:

```
diffusion_models/flux2/flux-2-klein-4b-fp8.safetensors   ← 9Bではなく 4B
text_encoders/flux2/qwen_3_4b_fp4_flux2.safetensors
vae/flux2/flux2-vae.safetensors
```

> [!note] CivitAIでLoRAを探すときは基盤モデル "Flux.2 Klein 4B" で絞る
> `Flux.2 Klein 9B` とは別ラベルで、互換性がない。

---

## 7. 手順（現時点の推奨）

1. **Kleinで意味と構図を確定させる。** 自然文で、関係性と否定形を明示して書く
2. 内容がズレたら **Kleinに戻って言い直す。** SDXLや後処理に渡して直そうとしない
3. 質感の仕上げにSDXLを使う場合、**意味を担っている領域はマスクで保護**する。
   全面img2imgは禁止（必ず再解釈される）
4. 局所の修正は CLIPSeg → inpaint（§8）

---

## 8. マスク自動化の経路（確保済み・未実施）

テキストで領域を指定してマスクを作れる。tritonは不要。

```
LoadCLIPSegModels+  →  ApplyCLIPSeg+  →  VAEEncodeForInpaint  →  KSampler
                        (prompt / threshold / smooth / dilate / blur)
```

> [!warning] `DownloadAndLoadCLIPSeg` とは繋がらない
> あちらの出力型は `CLIPSEGMODEL`、`ApplyCLIPSeg+` の要求は `CLIP_SEG`。**別物。**
> `LoadCLIPSegModels+`（入力なし → `CLIP_SEG`）を使うこと。

`ComfyUI-RMBG` の `SAM3Segment` は `No module named 'triton'` で**ロードに失敗している**。
使いたい場合は `pip install triton-windows`（KJNodesの `PatchTritonVAE` も同時に直る）。
ただし CLIPSeg で足りるなら不要。

---

## 🔗 関連

* [[rules/comfyui-image-generation-reflection|キャラクター同一性と画風再現の反省ノート]] — 誰を描くか
* [[rules/comfyui-mcp-workflows|ComfyUI MCP用 キャラクター生成ワークフロー規定]]
* `studio/references/workflows/flux2_txt2img.json` — Klein用テンプレート（`PARAM_*` 差し替え式）
