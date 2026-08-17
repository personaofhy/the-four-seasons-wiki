---
title: "第六章：再び春・後編 プロットトポロジー分析"
chapter_id: "05-re-spring"
season: "再び春"
protagonist: "田邊桃香"
document_type: "plot_topology"
---

# 🌸 第六章：再び春・後編 プロットトポロジー（DAG依存関係分析）

本ドキュメントは、第六章（主人公：田邊 桃香）における発見・呼び出し・対峙・完全適応を
有向非巡回グラフ（DAG）として体系化したプロット設計書です。インサートを持たない、
経糸の終着点にあたるエピソードです。

---

## 1. 物語トポロジー依存関係図 (Mermaid)

```mermaid
flowchart TD
    classDef situation fill:#72713E,stroke:#3f3e20,stroke-width:2px,color:#fff;
    classDef choice fill:#d4a373,stroke:#bc6c25,stroke-width:2px,color:#000;
    classDef trap fill:#e76f51,stroke:#f4a261,stroke-width:2px,color:#fff;
    classDef climax fill:#e63946,stroke:#9b2226,stroke-width:2px,color:#fff;
    classDef endBeat fill:#343a40,stroke:#212529,stroke-width:2px,color:#fff;
    classDef openNode fill:#ffffff,stroke:#8a6d3b,stroke-width:2px,stroke-dasharray:4 3,color:#000;

    Start(["承前：強権的な教師の仮面を保ったまま<br/>おむつ常用がエスカレートした日常"]):::situation

    subgraph Phase1_Discovery ["【Phase 1：発見（優先案・未確定）】"]
        Start --> ScoldScene["谷口が別の生徒を説教している場面"]
        ScoldScene --> SkirtFlip["★ 桃香のスカートがめくれ、おむつが露呈<br/>【不可逆フラグ：秘密の発覚】"]:::trap
    end

    subgraph Phase2_Summon ["【Phase 2：呼び出し】"]
        SkirtFlip --> Summon["谷口が桃香を閉じたスペースへ呼び出す<br/>（体育倉庫、仮）"]:::trap
        Summon --> KnowsTrap["★ 桃香は内心『罠だ、秘密を暴こうとしている』<br/>と分かった上で応じる"]:::choice
    end

    subgraph Phase3_Confrontation ["【Phase 3：対峙と半ば協力の露呈】"]
        KnowsTrap --> HandFrozen["おむつを隠す手が、羞恥と恐怖で動かせなくなる<br/>——内心では露呈を望んでいる"]
        HandFrozen --> HandPried["★ 谷口が手をこじ開ける<br/>桃香の意志は拒んでいないため『半ば協力』が成立"]:::climax
        HandPried --> FullExposure["動物柄の児童用おむつが完全に露呈"]:::climax
    end

    subgraph Phase4_Adaptation ["【Phase 4：完全適応】"]
        FullExposure --> DignityDeath["尊厳の完全な死滅"]
        DignityDeath --> FinalRelief["★ 被支配の安堵の中で、倒錯的な適応を完了"]:::endBeat
    end
```

---

## 2. 物語のトポロジカル進行フェーズ表

| フェーズ | 舞台 | 桃香のアクション／心理 | トポロジー機能 |
| :--- | :--- | :--- | :--- |
| **Phase 1** | 教室など | スカートがめくれ、おむつが露呈する（優先案） | 秘密発覚の不可逆フラグ（`open`・留保） |
| **Phase 2** | 校内 | 谷口に呼び出される。罠と分かった上で応じる | 抵抗の放棄。「自ら罠に踏み込む」という第4章（柊）との共鳴 |
| **Phase 3** | 閉じたスペース | 手が動かせなくなる→こじ開けられる→完全露呈 | 「半ば協力」——強制でも自発でもない第三の機構（[[cpt-3a76]]） |
| **Phase 4** | 同 | 尊厳死滅、被支配の安堵 | 経糸の終着点。第1章と対をなす完全適応 |

> [!warning] `open` — Phase 1の発見経緯は留保
> スカートめくれ説を優先案としているが、前の学校からの噂・浅田による漏洩という
> 代替案も残っている（[[cpt-6d5c]]）。
