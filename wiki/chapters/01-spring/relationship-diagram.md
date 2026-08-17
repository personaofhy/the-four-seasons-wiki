---
title: "第1章：春 人間関係・心理力学トポロジー"
chapter_id: "01-spring"
season: "春"
protagonist: "田邊桃香"
document_type: "character_relationship"
---

# 🌸 第1章：春 人間関係・心理力学トポロジー

第1章（主人公：田邊 桃香）における**「正義感と言い争い」「秘書という鏡像」**を
有向グラフとして整理した相関図です。

---

## 1. 人間関係・心理力学相関図 (Mermaid)

```mermaid
flowchart TB
    classDef protagonist fill:#E5A1C8,stroke:#a3527a,stroke-width:3px,color:#000;
    classDef politician fill:#6c757d,stroke:#495057,stroke-width:2px,color:#fff;
    classDef mirror fill:#457b9d,stroke:#1d3557,stroke-width:2px,color:#fff;

    subgraph MeetingRoom ["【密室：政治家の会議室】"]
        Momoka["🌸 田邊桃香 (23)<br/>【主人公】<br/>潔癖で正義感溢れる女性教師"]:::protagonist
        Politician["👤 政治家（一人）<br/>田舎者特有の長話<br/>言い争いの相手"]:::politician
        Secretary["🪞 女性秘書<br/>【桃香の弱さの鏡像】<br/>男性・権力に媚びる存在"]:::mirror
    end

    Momoka -->|"正義感から強い言葉をかける"| Politician
    Politician -->|"激昂し、言葉の応酬になる<br/>この言葉が後の意趣返しの引き金"| Momoka

    Momoka -.->|"軽蔑・反感<br/>『あの女のようにはなりたくない』"| Secretary
    Secretary -.->|"表向きは媚びる弱い女性の象徴<br/>（実は男性への強さを持つ、という反転案は未確定）"| Momoka
```

---

## 2. 心理力学の構造分析

### ① 桃香 ⇄ 政治家（言い争いという第二の罠）

政治家は桃香を意図的に罠にかけようとしていない——長話で時間を浪費させただけの
無自覚な加害者。真の罠は**桃香自身が招いた言い争い**にある。強い言葉で相手を
激昂させたことで、自分から「トイレに行きたい」と言い出す退路を自分で塞いでしまう
（[[cpt-8b3d]]）。

### ② 桃香 ⇄ 女性秘書（弱さの鏡像）

秘書は単なる脇役ではなく、**桃香が最も嫌悪する弱さ（男性・権力への迎合）を体現する
鏡**として確立される（[[cpt-0a9f]]）。この対立の構図が、後の第3・4章末尾のインサート
（[[rules/momoka-warp-engine]]）で秘書が桃香を追い詰める側に回ったときの落差を
支える。「秘書の方が実は男性への強さを持っている」という反転案は未確定。
