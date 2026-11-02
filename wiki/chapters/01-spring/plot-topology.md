---
title: "第1章：春 プロットトポロジー分析"
chapter_id: "01-spring"
season: "春"
protagonist: "田邊桃香"
document_type: "plot_topology"
---

# 🌸 第1章：春 プロットトポロジー（DAG依存関係分析）

本ドキュメントは、第1章（主人公：田邊 桃香）における、**政治家の意図的な罠ではない
アクシデントの積み重ね**が、いかにして失禁寸前まで追い詰めるかを有向非巡回グラフ
（DAG）として体系化したプロット設計書です。

---

## 1. 物語トポロジー依存関係図 (Mermaid)

```mermaid
flowchart TD
    classDef situation fill:#E5A1C8,stroke:#a3527a,stroke-width:2px,color:#000;
    classDef choice fill:#d4a373,stroke:#bc6c25,stroke-width:2px,color:#000;
    classDef trap fill:#e76f51,stroke:#f4a261,stroke-width:2px,color:#fff;
    classDef psychLock fill:#457b9d,stroke:#1d3557,stroke-width:2px,color:#fff;
    classDef endBeat fill:#343a40,stroke:#212529,stroke-width:2px,color:#fff;

    Start(["導入：生徒を守るため、政治家一人と<br/>女性秘書が待つ密室の会議室へ向かう"]):::situation

    subgraph Phase1_Accident ["【Phase 1：アクシデントの積み重ね（罠ではない）】"]
        Start --> LongTalk["政治家の田舎者特有の長話<br/>（家に関する蘊蓄自慢）で時間が経過"]:::trap
        LongTalk --> ToiletHurdle["着いてすぐトイレを借りることへの<br/>心理的ハードル"]:::psychLock
    end

    subgraph Phase2_Argument ["【Phase 2：言い争いという第二の罠】"]
        ToiletHurdle --> HarshWord["★ 選択：正義感から政治家に強い言葉をかける"]:::choice
        HarshWord --> Enraged["政治家が激昂し、言葉の応酬になる<br/>【この言葉が後のインサート③④の伏線】"]:::trap
        Enraged --> CantAsk["強く出た手前『トイレに行きたい』と言えない<br/>『結局男にビビって逃げ込むのか』への恐れ"]:::psychLock
    end

    subgraph Phase3_Limit ["【Phase 3：限界への接近】"]
        CantAsk --> UrineLimit["尿意が限界に近づいていく"]
        UrineLimit --> ChapterEnd["★ 章はここで閉じる（失禁直前）"]:::endBeat
    end

    ChapterEnd --> ToInsert1["第2章末尾のインサート①へ<br/>（実際の失禁が初めて描かれる）"]:::endBeat
```

---

## 2. 物語のトポロジカル進行フェーズ表

| フェーズ | 舞台 | 桃香のアクション／心理 | トポロジー機能 |
| :--- | :--- | :--- | :--- |
| **Phase 1** | 密室の会議室 | 政治家の長話、トイレを借りる心理的ハードル | アクシデントの積み重ね。**意図的な罠ではない**（[[cpt-4f1a]]） |
| **Phase 2** | 同 | 強い言葉→言い争い→トイレに行けなくなる | 「強がりを裏切れない」という心理的自縄自縛（[[cpt-8b3d]]） |
| **Phase 3** | 同 | 尿意が限界に近づく | 章はここで閉じる。破綻本体はインサート①へ持ち越し |

> [!important] この章の言葉が後で効いてくる
> Phase 2でかけた「ある言葉」（**作者指定（2026-10-12）：政治家に向けた「まるで赤ん坊ですね」**）は、第4章末尾のインサート③・第5章前編末尾の④で描かれる
> 政治家・秘書による意趣返し（オムツを履かされる経緯）の引き金になる
> （[[cpt-c7e2]]、[[rules/momoka-warp-engine]]）。
