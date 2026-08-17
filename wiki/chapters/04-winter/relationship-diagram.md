---
title: "第4章：冬 人間関係・心理力学トポロジー"
chapter_id: "04-winter"
season: "冬"
protagonist: "橘柊"
document_type: "character_relationship"
---

# ❄️ 第4章：冬 人間関係・心理力学トポロジー

第4章「冬」（主人公：橘 柊）における**「過去の少女への執着・再演動機」「欺瞞（子供の演技）と制裁の力学」「視線の受動から自発への転換」**を有向グラフとして整理した相関図です。

---

## 1. 人間関係・心理力学相関図 (Mermaid)

```mermaid
flowchart TB
    classDef protagonist fill:#8E99A4,stroke:#495057,stroke-width:3px,color:#fff;
    classDef pastGirl fill:#d4a373,stroke:#bc6c25,stroke-width:2px,color:#000;
    classDef staff fill:#457b9d,stroke:#1d3557,stroke-width:2px,color:#fff;
    classDef crowd fill:#6c757d,stroke:#495057,stroke-width:2px,color:#fff;
    classDef mascot fill:#e63946,stroke:#9b2226,stroke-width:2px,color:#fff;

    subgraph MemoryOrigin ["【原体験の記憶：小学校時代】"]
        PastGirl["👧 小学校時代の幼馴染（少女）<br/>【憧憬と見下しの対象】<br/>人前で失禁し大人に処理された少女"]:::pastGirl
        AdultPast["👤 処理を見せつけた『ある大人』<br/>(柊に少女の屈辱を目撃させた存在)"]:::pastGirl
    end

    subgraph CurrentEvent ["【現代の舞台：遊園地】"]
        Hiiragi["❄️ 橘 柊 (19)<br/>【主人公 / アイドル志望大学生】<br/>自発的露出・子供のフリ・欺瞞の破綻"]:::protagonist
        Takanashi["👩 小鳥遊 (たかなし / お姉さん)<br/>【遊園地スタッフ】<br/>下着を脱がせる → 欺瞞看破・制裁執行"]:::staff
        RabbitMascot["🐰 ウサギの着ぐるみ<br/>(事務的な脱衣・足首の固定)"]:::mascot
        QueueCrowd["👥 観覧車待機列の群衆<br/>(自ら踏み込んだ視線の海)"]:::crowd
    end

    %% ==========================================
    %% 心理・行動ベクトルの結合
    %% ==========================================

    %% 柊 ⇄ 過去の少女
    Hiiragi ==>|"「見下されながらも深く憧れる」屈折<br/>目撃者から当事者への【再演願望】"| PastGirl
    AdultPast -.->|"屈辱の光景を柊へ刻印"| Hiiragi

    %% 柊 ⇄ 待機列群衆
    Hiiragi ==>|"自ら群衆の眼前で排尿<br/>(受動的被害ではなく自発的露出)"| QueueCrowd

    %% 柊 ⇄ 小鳥遊・着ぐるみ
    Hiiragi -->|"「未熟な子供」を演じて下着脱衣を懇願"| Takanashi
    Takanashi -->|"欺瞞（大人の女）看破により悪意に転換<br/>着ぐるみと共に事務的拘束・行為半強要"| Hiiragi
    RabbitMascot -->|"足首固定・逃走封鎖"| Hiiragi
```

---

## 2. 心理力学の構造分析

### ① 他者体験の「再演（Reenactment）」という特異なトポロジー
他の章（桃香・向日葵・楓）が「予期せぬ事故や他者の悪意によって受動的に破綻させられる」のに対し、柊だけは**「かつて他人が受けた屈辱の儀式を、自らの肉体で完全にトレース（再演）したい」**という歪んだ自発的動機から始まります。

### ② 欺瞞（子供のフリ）が呼び込む悪意の反作用
- **願望段階**: 「子供だから処理できない」という演技が通じている間は、単なるバケットリストの達成に過ぎない。
- **破綻段階**: 「大人の女が子供のフリをして脱がせてもらおうとしていた」という**欺瞞の発覚そのものが、スタッフ（小鳥遊・着ぐるみ）の冷酷な悪意と制裁を呼び込む**という因果応報のトポロジーになっています。
