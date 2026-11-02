---
title: 短編集としての章構成マップ
document_type: collection_structure
---

# 📚 短編集としての章構成マップ

各章のmdファイルが、短編集全体として**どういう順序・関係にあるか**を1枚で見渡すための
整理ノート。個別の章の中身は各章の `index.md` を、経糸（桃香インサート）の詳細は
[[rules/momoka-warp-engine]] を、トライアド理論そのものは [[rules/triad-structure]] を参照。

---

## 1. エピソードの一覧と現在のファイル構成

**全五章・六エピソード。** 第5章「再び春」は前編／第六章に分かれ、この分割によって
5章が6エピソードになる（[[rules/triad-structure]] セクション2）。

| # | エピソード | 季節 | 主人公 | マクロ・トライアド機能 | このリポジトリにあるファイル |
| :-: | :--- | :--- | :--- | :--- | :--- |
| 1 | 春 | 🌸 | 田邊桃香 | 誘因（不安） | `01-spring/index.md`, `plot-topology.md`, `relationship-diagram.md` |
| 2 | 夏 | ☀️ | 金城向日葵 | 提示（暴発） | `02-summer/index.md`, `insert.md`（①）, `plot-topology.md`, `relationship-diagram.md` |
| 3 | 秋 | 🍂 | 遠山楓（高木圭視点） | 充足（萌芽） | `03-autumn/index.md`, `insert.md`（②）, `plot-topology.md`, `relationship-diagram.md` |
| 4 | 冬 | ❄️ | 橘柊 | 充足（爛熟） | `04-winter/index.md`, `insert.md`（③）, `plot-topology.md`, `relationship-diagram.md` |
| 5 | 再び春・前編 | ✨ | 田邊桃香 | 再誘因（恥辱。真相開示のツイスト） | `05-re-spring/5a-front.md`, `5a-insert.md`（④）, `5a-front-plot-topology.md`, `5a-front-relationship-diagram.md` |
| 6 | 第六章（再び春・後編） | 🌸 | 田邊桃香 | 再提示（倒錯。完全適応） | `05-re-spring/5b-back.md`, `5b-back-plot-topology.md`, `5b-back-relationship-diagram.md` |

> [!tip] 全6エピソード、トポロジー図が揃った（2026-08-17）
> 全エピソードに `plot-topology.md` / `relationship-diagram.md` が揃った。第1章は
> 「政治家の意図的な罠ではなく、不幸な偶然の積み重ね」という前提の訂正（[[cpt-4f1a]]）
> を反映。第六章は新しい舞台（[[locations/storage-room]]）と、命名した二人の生徒
> （谷口・宮下、[[cpt-f2b8]]）を反映している。

> [!tip] ディレクトリ構成を時系列順に整理（2026-08-17、[[cpt-3a91]]）
> 4つのインサートをそれぞれ独立ファイル `insert.md`（②③は同名、④のみ
> `5a-insert.md`）として、対応する章のディレクトリ内に配置した。`index.md`（本編）→
> `insert.md`（インサート）の順にアルファベットソートされるため、`ls` で見た
> ファイル一覧がそのまま物語の時系列になる。第5章の前編／第六章も `5a-*` / `5b-*`
> というプレフィックスに揃え、`06-back-half.md` という紛らわしい命名
> （章番号「5」のディレクトリに「6」始まりのファイル）を解消した。
> [[chapters/05-re-spring/index]] は各ファイルへのポータルに専念する。

> [!note] 充足だけ2章分の長さ
> トライアド理論上、充足フェーズは誘因・提示それぞれの2倍の重みを持つため、
> 秋・冬の2章にまたがる。第5〜6エピソードは前半の縮約再演（誘因→提示 の
> 再演＝再誘因→再提示）であり、独立した新サイクルではない（[[rules/triad-structure]]
> セクション2・5）。

> [!note] 第六章はファイルとして独立、章番号は「第五章」のまま表示
> `05-re-spring/5b-back.md` として内部的にはファイルを分けたが、読者への
> 見せ方は一貫して「第五章」——前編と後編で展開が連続しているため
> （[[cpt-5e7c]]）。`chapter_id` フロントマターも `05-re-spring` のまま揃えてある。

---

## 2. 全体の流れ：本編と経糸（桃香インサート）の二重構造 ＋ 各章の内部構造

短編集としての各章は、季節ごとに**独立した主人公と物語**を持つ（本編）。それとは別に、
**桃香だけが全編を貫く経糸**として存在し、他の3人の破綻に同期する断片（インサート）を
末尾に挿入されていく。本編とインサートは**別の書き手の目線が必要**——本編はその章の
主人公の物語として完結させ、インサートは桃香の適応プロセスの1コマとして書く。

**インサートは4箇所。** 第2・3・4章の末尾、そして第5章前編の末尾。前者3つは
「他の主人公の破綻と桃香の適応プロセスを同期させる」機能。**4つ目だけ機能が違う**
——第1章が仕込んだ「勇敢に戦った美談」というミスリードへの答え（「実は敗北していた」
という真相開示）であり、同期ではなく**ツイスト**として働く。このツイストを経て、
インサートを挟まない桃香単独の本編＝**第六章**が語られ、経糸が閉じる。

**インサートが無いのは第1章と第六章の2つだけ。** 他の4ブロック（第2〜4章、第5章前編）
はいずれも本編＋インサートの2ピース構成。**分量の実際の出典は
[[rules/triad-structure]]の元になった外部資料**（`the-four-seasons-blog/
03_Drafting_Hub/_小説/01_資料/とりあえず放り込む箱/全6章トライアド構造設計図.md`
の22ステップ・マトリックス）——空白セルは「直前のラベルが継続する」の意味と読み、
各局面が何ステップ分続くかを数え、さらに `大充足`/`小導入`/`新誘因`/`再提示` は
それぞれ `充足`/`誘因`/`誘因`/`提示` の系列として集計すると:

| 章 | 誘因 | 提示 | 充足 | 合計 |
| :--- | :-: | :-: | :-: | :-: |
| 春（第1章） | 7＋α | 2 | 13 | 22＋α |
| 夏（第2章） | 7 | 7 | 8 | 22 |
| 秋（第3章） | 2 | 7 | 13 | 22 |
| 冬（第4章） | 2 | 7 | 13 | 22 |
| 春前（第5章前編） | 7 | 2 | 13 | 22 |
| 春後（第六章） | 7 | 7＋α | 8 | 22＋α |

**本編は、外部資料の配分単位で見ると4章（夏・秋・冬・春前編）が22ユニットで共通。**
違うのは局面ごとの配分だけ——**誘因型（春・春前）は誘因の章と言いつつ、実際は
「大充足」から始まり充足が最大配分（13）を占める**——章の冒頭は前サイクルの充足を
引きずり、終盤で新しい誘因（★終着点）へ持ち上げる構造。提示型（夏・春後）は提示と
充足がほぼ均等（7:8）。充足型（秋・冬）は充足が最大配分（13）で、誘因は最小（2）。
しかも**春＝春前、夏＝春後、秋＝冬は配分パターンまで完全一致**——同じ型の2エピソード
が骨格を共有するという規則の、数値レベルでの裏付け（[[cpt-9d41]]）。

> [!important] 訂正（2026-09-13）：第1章・第六章の合計は22ユニットにならない
> 旧記述「インサートが無い分、他の4話より短い」は誤り。正しくは**22＋α**（α＝他章の
> インサートと同じ長さ）。**最初の4段階（誘因型なら大充足→誘因→提示→充足、提示型
> なら小導入→提示→充足→誘因）は現行の配分のまま変えず、加算分はすべて末尾の
> 終着点フェーズ（第1章＝新誘因、第六章＝再提示）に乗る。** 終着点フェーズはこの
> 加算によって、単体の一拍ではなく、それ自体の内部に誘因・提示・充足を持つ、
> より詳細なフラクタル構造へと育つ（[[rules/triad-structure]] セクション6）。

> [!note] `draft` — α ＝ 8ユニット ＝ 16ページ（2026-09-13 仮設定）
> 本作は漫画で、**1ユニット ＝ 2ページ**。インサート標準長も α も 8ユニット。よって
> **全6話が 30ユニット ＝ 60ページで揃う**——本編22＋インサート8の4話も、
> 本編22＋α8の第1章・第六章も同じ総量。全体で180ユニット＝360ページ。
> 算出根拠は [[rules/triad-structure]] セクション6。

さらに、[[rules/triad-structure]] セクション5の規則により、各章の内部構造（4〜5段階の
変化）はマクロ機能に応じて**3つの型**に集約される——同じ型の2エピソードは、内部の
骨格まで完全に一致する。**分量（マクロ）とミクロ・トライアド構造は別の軸だが、
1枚の図に統合できる**（[[cpt-9a17]]、[[cpt-9d41]]、[[cpt-4b62]]）——各行を2段にし、**上段＝分量
（主人公カラー、文字あり、本編は全章22ユニットで共通）／下段＝トライアドの局面
（誘因・提示・充足の3色のみ、文字なし、幅は実際のユニット数に比例）**とすることで、
段階ラベルを詰め込まずに済む。

<svg viewBox="0 0 720 650" xmlns="http://www.w3.org/2000/svg" font-family="'Hiragino Sans','Yu Gothic',sans-serif">
  <rect x="0" y="0" width="720" height="650" fill="#fdfaf5"/>
  <defs>
    <pattern id="alphaAdd" width="6" height="6" patternTransform="rotate(45)" patternUnits="userSpaceOnUse">
      <line x1="0" y1="0" x2="0" y2="6" stroke="#fdfaf5" stroke-width="2" opacity=".55"/>
    </pattern>
  </defs>
  <!-- ガイド線：開始位置／外部資料の22ユニット終端／全6話共通の右端 -->
  <line x1="160" y1="26" x2="160" y2="514" stroke="#999" stroke-width="1" stroke-dasharray="2 3"/>
  <line x1="336" y1="26" x2="336" y2="514" stroke="#999" stroke-width="1" stroke-dasharray="2 3"/>
  <line x1="400" y1="26" x2="400" y2="514" stroke="#8a6d3b" stroke-width="1.2" stroke-dasharray="2 3"/>
  <text x="160" y="18" font-size="11" fill="#726a5e">開始</text>
  <text x="332" y="18" font-size="11" fill="#726a5e" text-anchor="end">本編22ユニット＝44ページ</text>
  <text x="406" y="18" font-size="11" fill="#8a6d3b" font-weight="700">全6話とも30ユニット＝60ページで揃う</text>
  <text x="10" y="52" font-size="13" font-weight="700" fill="#2a2622">🌸 第1章</text>
  <text x="10" y="68" font-size="11" fill="#726a5e">春・桃香</text>
  <rect x="160" y="34" width="240" height="44" rx="6" fill="#72713E" stroke="#3f3e20" stroke-width="2"/>
  <rect x="336" y="37" width="61" height="38" fill="url(#alphaAdd)"/>
  <text x="368.0" y="60" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">＋α</text>
  <text x="248.0" y="60" font-size="11.5" fill="#fff" text-anchor="middle" font-weight="700">桃香・本編</text>
  <rect x="160.00" y="82" width="72.00" height="15" fill="#2F6F76" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="232.00" y="82" width="32.00" height="15" fill="#6B5B95" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="264.00" y="82" width="16.00" height="15" fill="#E07A5F" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="280.00" y="82" width="32.00" height="15" fill="#2F6F76" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="312.00" y="82" width="88.00" height="15" fill="#6B5B95"/>
  <rect x="336.00" y="82" width="64.00" height="15" fill="url(#alphaAdd)"/>
  <rect x="312.00" y="82" width="88.00" height="15" fill="none" stroke="#8a6d3b" stroke-width="2.5"/>
  <text x="10" y="132" font-size="13" font-weight="700" fill="#2a2622">☀️ 第2章</text>
  <text x="10" y="148" font-size="11" fill="#726a5e">夏・向日葵</text>
  <rect x="160" y="114" width="176" height="44" rx="6" fill="#FCD57E" stroke="#b5942a" stroke-width="2"/>
  <text x="248.0" y="140" font-size="11.5" fill="#000" text-anchor="middle" font-weight="700">向日葵・本編</text>
  <rect x="336" y="114" width="64" height="44" rx="6" fill="#72713E" stroke="#3f3e20" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="368.0" y="140" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">桃香</text>
  <rect x="160.00" y="162" width="24.00" height="15" fill="#6B5B95" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="184.00" y="162" width="32.00" height="15" fill="#E07A5F" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="216.00" y="162" width="64.00" height="15" fill="#2F6F76" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="280.00" y="162" width="32.00" height="15" fill="#6B5B95" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="312.00" y="162" width="24.00" height="15" fill="#E07A5F" stroke="#8a6d3b" stroke-width="2.5"/>
  <text x="10" y="212" font-size="13" font-weight="700" fill="#2a2622">🍂 第3章</text>
  <text x="10" y="228" font-size="11" fill="#726a5e">秋・楓</text>
  <rect x="160" y="194" width="176" height="44" rx="6" fill="#812E2A" stroke="#4a1512" stroke-width="2"/>
  <text x="248.0" y="220" font-size="11.5" fill="#fff" text-anchor="middle" font-weight="700">楓・本編</text>
  <rect x="336" y="194" width="64" height="44" rx="6" fill="#72713E" stroke="#3f3e20" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="368.0" y="220" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">桃香</text>
  <rect x="160.00" y="242" width="24.00" height="15" fill="#E07A5F" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="184.00" y="242" width="32.00" height="15" fill="#2F6F76" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="216.00" y="242" width="16.00" height="15" fill="#6B5B95" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="232.00" y="242" width="32.00" height="15" fill="#E07A5F" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="264.00" y="242" width="72.00" height="15" fill="#2F6F76" stroke="#8a6d3b" stroke-width="2.5"/>
  <text x="10" y="292" font-size="13" font-weight="700" fill="#2a2622">❄️ 第4章</text>
  <text x="10" y="308" font-size="11" fill="#726a5e">冬・柊</text>
  <rect x="160" y="274" width="176" height="44" rx="6" fill="#8E99A4" stroke="#3d4750" stroke-width="2"/>
  <text x="248.0" y="300" font-size="11.5" fill="#212529" text-anchor="middle" font-weight="700">柊・本編</text>
  <rect x="336" y="274" width="64" height="44" rx="6" fill="#72713E" stroke="#3f3e20" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="368.0" y="300" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">桃香</text>
  <rect x="160.00" y="322" width="24.00" height="15" fill="#E07A5F" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="184.00" y="322" width="32.00" height="15" fill="#2F6F76" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="216.00" y="322" width="16.00" height="15" fill="#6B5B95" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="232.00" y="322" width="32.00" height="15" fill="#E07A5F" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="264.00" y="322" width="72.00" height="15" fill="#2F6F76" stroke="#8a6d3b" stroke-width="2.5"/>
  <text x="10" y="372" font-size="13" font-weight="700" fill="#2a2622">✨ 第5章前編</text>
  <text x="10" y="388" font-size="11" fill="#726a5e">再び春・桃香</text>
  <rect x="160" y="354" width="176" height="44" rx="6" fill="#72713E" stroke="#3f3e20" stroke-width="2"/>
  <text x="248.0" y="380" font-size="11.5" fill="#fff" text-anchor="middle" font-weight="700">桃香・本編</text>
  <rect x="336" y="354" width="64" height="44" rx="6" fill="#72713E" stroke="#3f3e20" stroke-width="2" stroke-dasharray="4 3"/>
  <text x="368.0" y="380" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">桃香</text>
  <rect x="160.00" y="402" width="72.00" height="15" fill="#2F6F76" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="232.00" y="402" width="32.00" height="15" fill="#6B5B95" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="264.00" y="402" width="16.00" height="15" fill="#E07A5F" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="280.00" y="402" width="32.00" height="15" fill="#2F6F76" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="312.00" y="402" width="24.00" height="15" fill="#6B5B95" stroke="#8a6d3b" stroke-width="2.5"/>
  <text x="10" y="452" font-size="13" font-weight="700" fill="#2a2622">🌸 第六章</text>
  <text x="10" y="468" font-size="11" fill="#726a5e">再び春・桃香</text>
  <rect x="160" y="434" width="240" height="44" rx="6" fill="#72713E" stroke="#3f3e20" stroke-width="2"/>
  <rect x="336" y="437" width="61" height="38" fill="url(#alphaAdd)"/>
  <text x="368.0" y="460" font-size="10" fill="#fff" text-anchor="middle" font-weight="700">＋α</text>
  <text x="248.0" y="460" font-size="11.5" fill="#fff" text-anchor="middle" font-weight="700">桃香・本編</text>
  <rect x="160.00" y="482" width="24.00" height="15" fill="#6B5B95" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="184.00" y="482" width="32.00" height="15" fill="#E07A5F" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="216.00" y="482" width="64.00" height="15" fill="#2F6F76" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="280.00" y="482" width="32.00" height="15" fill="#6B5B95" stroke="#fdfaf5" stroke-width="1.2"/>
  <rect x="312.00" y="482" width="88.00" height="15" fill="#E07A5F"/>
  <rect x="336.00" y="482" width="64.00" height="15" fill="url(#alphaAdd)"/>
  <rect x="312.00" y="482" width="88.00" height="15" fill="none" stroke="#8a6d3b" stroke-width="2.5"/>  <!-- 凡例：上段（主人公・分量） -->
  <text x="160" y="536" font-size="10.5" font-weight="700" fill="#2a2622">上段＝分量（主人公カラー。本編22ユニット＋第1・6章のみ終着点に＋α）</text>
  <g transform="translate(160,544)">
    <rect x="0" y="0" width="14" height="14" rx="3" fill="#72713E"/>
    <text x="20" y="11" font-size="10" fill="#2a2622">本編（桃香の場合、全話共通の色）</text>
    <rect x="200" y="0" width="14" height="14" rx="3" fill="#72713E" stroke="#3f3e20" stroke-width="1.5" stroke-dasharray="3 2"/>
    <text x="220" y="11" font-size="10" fill="#2a2622">桃香インサート</text>
    <rect x="320" y="0" width="14" height="14" rx="3" fill="#72713E"/>
    <rect x="320" y="0" width="14" height="14" rx="3" fill="url(#alphaAdd)"/>
    <text x="340" y="11" font-size="10" fill="#2a2622">＋α（インサート相当）</text>
  </g>
  <!-- 凡例：下段（トライアド局面、3色のみ） -->
  <text x="160" y="576" font-size="10.5" font-weight="700" fill="#2a2622">下段＝トライアドの局面（3色のみ、文字なし、幅＝実際のユニット数比例）</text>
  <g transform="translate(160,584)">
    <rect x="0" y="0" width="14" height="14" fill="#6B5B95"/>
    <text x="19" y="11" font-size="9.5" fill="#2a2622">誘因（誘因・新誘因・小誘因）</text>
    <rect x="180" y="0" width="14" height="14" fill="#E07A5F"/>
    <text x="199" y="11" font-size="9.5" fill="#2a2622">提示（提示・再提示）</text>
    <rect x="320" y="0" width="14" height="14" fill="#2F6F76"/>
    <text x="339" y="11" font-size="9.5" fill="#2a2622">充足（充足・大充足）</text>
    <rect x="460" y="0" width="14" height="14" fill="#8E99A4" stroke="#8a6d3b" stroke-width="2.5"/>
    <text x="479" y="11" font-size="9.5" fill="#2a2622">★終着点</text>
  </g>
  <text x="160" y="608" font-size="9.2" fill="#999">※ 各章は「導入」を最初の実質局面に統合して表示（誘因型=大充足に、充足型=提示に統合／誘因〜充足の3色に必ず属す）</text>
  <text x="160" y="624" font-size="9.2" fill="#999">※ 網掛け＝第1章・第六章の＋α。独立した断片ではなく、末尾の終着点フェーズの内部に加算される（下段も同じ幅だけ伸びる）</text>
  <text x="160" y="638" font-size="9.2" fill="#999">　 帯は1ユニット＝8pxの実スケール。1ユニット＝2ページ（漫画）、インサートもαも8ユニット＝16ページ（仮設定）</text>
</svg>

> [!question] `open` — この図は第1章・第六章の追加分をまだ反映していない
> 上段の第1章・第六章の帯（桃香・本編）は、終着点フェーズに+αを加えた後の実際の
> 長さではなく、外部資料の22ユニットのままの表示（加算の位置と考え方は
> [[rules/triad-structure]] セクション6で決定済み）。αの実際の大きさが決まり次第、
> 帯の末尾に伸長分を区別できる形で継ぎ足す。

### 読み方の要点

- **本編4つ（春・夏・秋・冬）は季節ごとに独立した主人公の物語。** 相互に世界観が
  混ざらず連関しない（桃香を除く）。ただし「尿失禁のもたらすホラー・エロス」という
  主題を多角的に描くという意味で、互いに意識し合う関係にある——1章だけ突出して
  完成させることは避ける（プロジェクトの横展開方針）
- **桃香だけが全編を貫く。** 第1章で予兆を、第2〜4章末尾のインサートで段階的な
  適応を、第5章前編末尾のインサート④でツイストを、第六章で収束・完結を担う
- **第1章と第六章は「インサートが挿入される側」ではなく、桃香自身の本編のみで
  完結する。** 失禁直前で閉じる第1章と対をなす、経糸の終着点が第六章
- **インサート①〜③は同期、④はツイスト。** 夏の「放出」に桃香の「放出」を、秋の
  「客観支配」に桃香の「客観処理」を、冬の「主観的退行」に桃香の「主観的退行」を
  重ねるのが①〜③。④だけは他の主人公と同期せず、第1章のミスリードを回収する
- **マクロ・トライアドは既存資料がある。** 誘因＝第1章、提示＝第2章、
  充足（2章分の長さ）＝第3・4章、再誘因＝第5章前編、再提示＝第六章
  （[[rules/triad-structure]] セクション2・4）
- **本編は外部資料上、4章（夏・秋・冬・春前編）が22ユニットで同じ長さ。** 差があるのは
  局面の配分だけ（[[cpt-9d41]]）——秋・冬（充足型）が個別に短いわけではなく、充足に
  力点が寄っているだけ。**第1章・第六章はこれとは別枠で、終着点フェーズに他章の
  インサートと同じ長さ（α）が加算され、合計は22＋αになる**
  （[[rules/triad-structure]] セクション6。αの実際の大きさは `open`）
- **下段の★終着点セルが、その章のマクロ機能そのもの。** 誘因型（第1章・第5章前編）
  は「新誘因」、提示型（第2章・第六章）は「再提示」、充足型（第3・4章）は「大充足」
  で終わる、という[[rules/triad-structure]] セクション5の規則がそのまま図の右端に
  現れる。第六章の帯は桃香色（上段）なのに下段の局面配列は第2章と同じ「提示型」
  ——楓や柊の担当章と骨格が同じという、直感に反する一致もこの図なら一目で分かる。

---

## 3. 各章の内部構造への入り口

| 章 | 中心的な力学 | 参照 |
| :--- | :--- | :--- |
| 秋・冬 | 「命令なき支配」（環境と物理リソースの掌握による無言の強制） | 各章の `relationship-diagram.md` |
| 夏 | 選択の連鎖が不可逆な罠を呼び込む古典悲劇的DAG | `02-summer/plot-topology.md` |
| 全章共通 | トライアド（誘因・提示・充足）＋ 入れ子のフラクタル構造 | [[rules/triad-structure]] |
| 桃香の適応プロセス | 経糸システムそのもの（4つのインサート） | [[rules/momoka-warp-engine]] |

---

## 4. 章をまたぐ「反響する叫び」（提案段階・未確定）

経糸（桃香インサート）とは別系統の、もう一つの連結装置が提案されている。**各章・各
インサートの末尾で人物に叫ばせる台詞（あるいは心の叫び）を、次のエピソードの
対応する瞬間で反響させる**——バラバラな本編同士を繋ぐ「縫い糸」として機能させる狙い。

例（確定ではない）:
- 第1章末尾、失禁直前の桃香が心の中で叫ぶ「こんなこと、私の身には起こらない！」を、
  第2章・向日葵の失禁直前の場面で反響させる
- 第3章、高木が楓に向けて（心の中で）「見られる気分ってどうでしたか？」と問い、
  それが第4章（主観視点の深掘り）に繋がる

> [!warning] `open` — ゼロから共同設計する段階
> どのエピソード境界に適用するか、起点はインサートか本編か、経糸とどう共存させるか
> ——すべて未確定。次のインタビューで詰める（[[cpt-9d02]]）。

---

## 5. まだ無いもの（`open`）

- ~~第1章・第六章の `plot-topology.md` / `relationship-diagram.md`~~ — **全6エピソード
  完成**（2026-08-17）
- ~~各章 `index.md` から、対応する `plot-topology.md` / `relationship-diagram.md` /
  本ファイルへのリンク~~ — **完了**（2026-08-17）
- ~~インサートの独立ファイル化とディレクトリの時系列整理~~ — **完了**（2026-08-17）
- ~~フラクタル・トライアド構造（誘因の中の誘因・提示・充足）を視覚化した図~~ —
  **完了**（2026-08-17、セクション2に統合。ただし「誘因の中の誘因」まで潜る
  2階層目は未着手——今回の図は1階層目＝章タイプ別の4〜5段階のみ）
- 「反響する叫び」技法の具体設計（セクション4）
- 第六章の新しい舞台（[[locations/storage-room]]）の詳細仕様
