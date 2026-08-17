---
title: "第5章前編：再び春 プロットトポロジー分析"
chapter_id: "05-re-spring"
season: "再び春"
protagonist: "田邊桃香"
document_type: "plot_topology"
---

# ✨ 第5章前編：再び春 プロットトポロジー（DAG依存関係分析）

本ドキュメントは、第5章前編（主人公：田邊 桃香）における仮面の獲得、体質の露呈、
5段階エスカレーション、末尾のツイストを有向非巡回グラフ（DAG）として体系化した
プロット設計書です。**外面的には「第五章」の前半として提示しますが、後半＝
[[chapters/05-re-spring/5b-back|第六章]] はファイルを分けています。**

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

    Start(["導入：密室の秘密が露見することを恐れ<br/>教頭の計らいで別の学校へ転任"]):::situation

    subgraph Phase1_Mask ["【Phase 1：仮面の獲得】"]
        Start --> NewMask["以前とは別人の『強権的な教師』を演じ始める"]:::choice
        NewMask --> BodyChange["恐怖から反射的に漏らしてしまう体質への変化"]:::trap
    end

    subgraph Phase2_Trigger ["【Phase 2：浅田事件（トリガー）】"]
        BodyChange --> AsadaWitness["生徒・浅田の前でお漏らし<br/>【不可逆フラグ：体質の露呈】"]:::trap
        AsadaWitness --> PadStart["★ 選択：自己防衛を名目にパッド着用を開始"]:::choice
    end

    subgraph Phase3_Escalation ["【Phase 3：5段階エスカレーション】"]
        PadStart --> Stage1["①自宅での着用"]
        Stage1 --> Stage2["②学校のトイレでの着用"]
        Stage2 --> Stage3["③トイレの外＝生徒のいる廊下・教室で指導"]
        Stage3 --> MiniArc["【小さな誘因→提示→充足】<br/>誘因型の内部構造として要求される起伏<br/>（具体的な出来事は open）"]:::openNode
        MiniArc --> Stage4["④授業中の着用"]
        Stage4 --> Stage5["⑤丸一日つけたまま過ごす"]
    end

    subgraph Phase4_Twist ["【Phase 4：末尾のインサート④】"]
        Stage5 --> Insert4["★ インサート④：真相開示のツイスト<br/>『実は会議室で敗北していた』<br/>（第1章のミスリードへの答え）"]:::climax
        Insert4 --> ToChapter6["第六章へ"]:::endBeat
    end
```

---

## 2. 物語のトポロジカル進行フェーズ表

| フェーズ | 舞台 | 桃香のアクション／心理 | トポロジー機能 |
| :--- | :--- | :--- | :--- |
| **Phase 1** | 転任先の学校 | 教頭の計らいで転任し、強権的な教師の仮面を被る | 仮面の獲得。第1章の潔癖さとの対比構造 |
| **Phase 2** | 教室 | 浅田の前で恐怖性の失禁を目撃される | 不可逆フラグ（体質の露呈）の起動 |
| **Phase 3** | 学校内各所 | パッドからおむつへ、5段階のエスカレーション | 段階的な自壊。誘因型の内部構造として、途中に小さな起伏が要求される（`open`） |
| **Phase 4** | （末尾） | インサート④で「実は敗北していた」と開示される | 再誘因の終着点＝新誘因。第1章のミスリードを回収するツイスト |

> [!warning] `open` — Phase 3の内部にある「小さな起伏」の具体
> [[rules/triad-structure]] セクション5の規則により、誘因型（第1章・第5章前編）の
> 内部には完結した小さな誘因→提示→充足が一つ埋め込まれるべきとされている
> （[[cpt-2c91]]）。5段階のどこかに置く想定だが、具体的な出来事は未定。
