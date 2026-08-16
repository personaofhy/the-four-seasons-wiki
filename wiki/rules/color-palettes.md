---
title: 🎨 テーマカラー・パレット規定
---

# 🎨 テーマカラー・パレット規定

本作『THE FOUR SEASONS』の**テーマカラー**を定める規定。

キャラクターと章のイメージを固めるために色数を絞る。**ドット絵にするための減色ではない。**
画像生成の色指定、および執筆時の情景描写は、ここで定めた色を基準にする。

> [!info] 旧「16色限定・ドット絵」規定からの改訂
> 本ノートはもともと90年代ドット絵路線のための**減色パレット規定**だった。**その路線は封印済み。**
> 色を絞るという方針だけを、**テーマカラーの定義**として引き継いでいる。
> 「16色以外の使用を禁じる」という旧文言は撤回した。色数は下記の枠に従う。

---

## 📐 2層構造

| 層 | 対象 | 色数 | 正の所在 |
| :--- | :--- | :---: | :--- |
| **① 章パレット** | 背景・光・空気・情景描写 | **12〜16色** | **本ノート** |
| **② キャラパレット** | 肌・髪・瞳・衣装 | **6〜8色** | 各キャラノートの frontmatter |

①と②は**別々に持つ**。人物は背景から浮いてよい——というより、**浮かせるために分けている。**

---

## 🏷 章識別色（1色）

上の2層とは**別物**。章パレット（12〜16色）が情景描写のための色域であるのに対し、
こちらは**「この記述はどの章のものか」を一目で示すためのUI用の1色**。
ダッシュボード・図表・索引で使う。作品内の色設計には影響しない。

各章の `index.md` frontmatter に `theme_color` として持つ。

| 章 | 色 | 名前 | 導出元 |
| :--- | :--- | :--- | :--- |
| 🌸 第1章 春 | <span style="display:inline-block;width:12px;height:12px;background:#E5A1C8;border-radius:3px;vertical-align:middle;"></span> `#E5A1C8` | くすんだ桜 | 春の章パレット（定義済み16色）より |
| ☀️ 第2章 夏 | <span style="display:inline-block;width:12px;height:12px;background:#FCD57E;border-radius:3px;vertical-align:middle;"></span> `#FCD57E` | 陽に灼けた黄 | 向日葵 `color_sub[0]`（黄色シャツ） |
| 🍂 第3章 秋 | <span style="display:inline-block;width:12px;height:12px;background:#812E2A;border-radius:3px;vertical-align:middle;"></span> `#812E2A` | 錆びた赤 | 楓 `color_accent[0]` |
| ❄️ 第4章 冬 | <span style="display:inline-block;width:12px;height:12px;background:#8E99A4;border-radius:3px;vertical-align:middle;"></span> `#8E99A4` | 凍てついた青灰 | 柊 `color_main[1]` |
| ✨ 第5章 再び春 | <span style="display:inline-block;width:12px;height:12px;background:#72713E;border-radius:3px;vertical-align:middle;"></span> `#72713E` | 芽吹きの薄緑 | 桃香 `color_main[0]`（再登場章のため） |

> [!note] 導出案
> 5色とも既存のパレットから引いてある。新しく作った色は一つもない。
> 第5章だけ第1章と別の色にしたのは、同じ桃香の章でも「原点」と「再生」を
> 区別する必要があるため。第1章は章パレット由来の桜色、第5章は桃香本人の主色を当てた。
>
> **変えたい場合は各章 `index.md` の `theme_color` を書き換えるだけでよい。**
> ダッシュボードはそこを読んでいる。

---

## 🧍 キャラパレットのスロット（6枠＋任意2枠）

色数を絞るだけでは4人を比較できない。**同じ枠を同じ順で持つ**ことで初めて横並びが成立する。

| # | スロット | 内容 | 必須 |
| :-: | :--- | :--- | :-: |
| 1 | `skin` | 肌のベース | ✅ |
| 2 | `hair` | 髪のベース | ✅ |
| 3 | `eyes` | 虹彩 | ✅ |
| 4 | `garment_main` | 衣装の主色（面積最大） | ✅ |
| 5 | `garment_sub` | 衣装の副色 | ✅ |
| 6 | `symbol` | **象徴色** — 下着・小道具など、破綻に関わる一点 | ✅ |
| 7 | `shadow` | 影の寄せ先 | 任意 |
| 8 | `flush` | 紅潮・血色（段階5で使う） | 任意 |

> [!tip] なぜ6〜8色か
> 5色では肌・髪・瞳で3枠が埋まり、衣装が2色しか持てず、象徴色の枠が消える。
> 9色を超えると「絞った」と言えるだけの制約が効かなくなり、いまの9〜11色と変わらない。
> **6が下限、8が上限**が妥当。`shadow` と `flush` を任意枠にしてあるのは、この2つは他の色から導出できることがあるため。

**現状はどのキャラもこのスロット構造になっていない**（9〜11色を `color_main`/`color_sub`/`color_accent` という面積基準で持っている）。移行は未着手。

---

## 🚦 定義状況

| 季節 | ① 章パレット | ② キャラパレット |
| :--- | :--- | :--- |
| 🌸 春（桃香） | ✅ 定義済み（下記16色） | ⚠️ 旧形式10色・スロット未移行 |
| 🌻 夏（向日葵） | ❌ **未定義** | ⚠️ 旧形式11色・スロット未移行 |
| 🍁 秋（楓） | ❌ **未定義** | ⚠️ 旧形式10色・スロット未移行 |
| ❄️ 冬（柊） | ❌ **未定義** | ⚠️ 旧形式9色・スロット未移行 |

> [!question] `open` — 夏・秋・冬
> 章パレット3つとキャラパレット4つが未確定。
> 衣装ノートの `⚠夏パレット未定義` `⚠秋パレット未定義` マーカーは、この欠落を指している。

---

## 🌸 第1章：春（田邊桃香）パレット【16色】

湿ったアスファルト、曇り空、褪せた桜、そして皮膚の下に隠された不穏な赤みと湿気。

<div style="display: grid; grid-template-columns: repeat(auto-fill, minmax(130px, 1fr)); gap: 12px; margin: 20px 0;">

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #E5A1C8; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">くすんだ桜</div>
      <strong>#E5A1C8</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #4F5862; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">湿った灰</div>
      <strong>#4F5862</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #F0D5C3; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">蒼白な肌</div>
      <strong>#F0D5C3</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #1A2B44; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">制服の濃紺</div>
      <strong>#1A2B44</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #8C2A3F; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">破綻・紅潮の赤</div>
      <strong>#8C2A3F</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #DBDFE3; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">霧がかった白</div>
      <strong>#DBDFE3</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #334B76; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">雨空のブルー</div>
      <strong>#334B76</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #667C4D; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">濡れた植栽</div>
      <strong>#667C4D</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #121922; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">静寂の漆黒</div>
      <strong>#121922</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #808D96; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">コンクリート</div>
      <strong>#808D96</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #2A636A; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">澱んだティール</div>
      <strong>#2A636A</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #9D634C; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">錆びた金属</div>
      <strong>#9D634C</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #3D5C40; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">深緑の葉</div>
      <strong>#3D5C40</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #6E7D88; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">黒板のくすみ</div>
      <strong>#6E7D88</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #EFE1C9; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">微かな日光</div>
      <strong>#EFE1C9</strong>
    </div>
  </div>

  <div style="border: 1px solid #333; border-radius: 8px; overflow: hidden; background: #1a1a1a;">
    <div style="background-color: #493322; height: 45px; width: 100%;"></div>
    <div style="padding: 6px; font-size: 11px; font-family: monospace; color: #eee;">
      <div style="font-size: 9px; color: #888; margin-bottom: 2px;">木目ブラウン</div>
      <strong>#493322</strong>
    </div>
</div>

> [!note] 旧・減色サンプル画像について
> ここには「AI生成原画（30,571色）→ 16色完全減色後」の比較サンプルが置かれていたが、
> **画像ファイルは既に失われており、ドット絵路線自体も封印済み**のため節ごと削除した。
> 上記16色は**テーマカラー（情景の色域）**として引き続き有効。
