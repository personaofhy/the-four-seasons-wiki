---
title: "第2章：夏 プロットトポロジー分析"
chapter_id: "02-summer"
season: "夏"
protagonist: "金城向日葵"
document_type: "plot_topology"
---

# ☀️ 第2章：夏 プロットトポロジー（DAG依存関係分析）

本ドキュメントは、第2章「夏」（金城 向日葵）の物語展開、選択、環境トラップ、心理的拘束条件（心理的ロック）を有向非巡回グラフ（DAG / トポロジカル構造）として体系化したプロット設計書です。

---

## 1. 物語トポロジー依存関係図 (Mermaid)

```mermaid
flowchart TD
    classDef situation fill:#2a9d8f,stroke:#264653,stroke-width:2px,color:#fff;
    classDef choice fill:#d4a373,stroke:#bc6c25,stroke-width:2px,color:#000;
    classDef trap fill:#e76f51,stroke:#f4a261,stroke-width:2px,color:#fff;
    classDef psychLock fill:#457b9d,stroke:#1d3557,stroke-width:2px,color:#fff;
    classDef climax fill:#e63946,stroke:#9b2226,stroke-width:2px,color:#fff;
    classDef endBeat fill:#6a0dad,stroke:#3c096c,stroke-width:2px,color:#fff;

    Start(["導入：夏休みの屋上プール<br/>(うたた寝 / 陽光と無防備)"]):::situation

    %% ==========================================
    %% Phase 1: 屋上の拘束と最初の決断
    %% ==========================================
    subgraph Phase1_Rooftop ["【Phase 1：発端と最初の不可逆選択】"]
        Start --> LockPrank["悪意ある悪戯：水着とフェンスが南京錠で固定<br/>(犯人不明)"]:::trap
        LockPrank --> UrinationPressure1["生理的限界（尿意）の切迫"]
        
        UrinationPressure1 & LockPrank --> ChoiceNude["★ 選択：漏らす屈辱を避けるため水着を脱ぎ捨てる<br/>【不可逆フラグ：全裸化】"]:::choice
        ChoiceNude --> MoveToClassroom["衣服回収のため校舎・教室へ向かう"]
    end

    %% ==========================================
    %% Phase 2: 想定外の連鎖と空間アイロニー
    %% ==========================================
    subgraph Phase2_Classroom ["【Phase 2：空間の罠（遮蔽の反転）】"]
        MoveToClassroom --> TrapSuppClass["想定外①：無人のはずの教室で補習授業開始<br/>(逃げ場の喪失)"]:::trap
        TrapSuppClass --> ChoiceCurtain["★ 選択：教室から隠れるためカーテン裏へ潜入"]:::choice
        
        ChoiceCurtain --> TrapGlassReflect["想定外②：窓ガラスに身体前面を密着<br/>【構造的アイロニー：校庭の野次馬から前面が完全露出】"]:::trap
        TrapGlassReflect --> CrowdGaze["群衆の視線とざわめき（直接見えず気配のみ知覚）"]
    end

    %% ==========================================
    %% Phase 3: 情報の越境と心理的完全拘束
    %% ==========================================
    subgraph Phase3_Lockdown ["【Phase 3：内外からの完全包囲（心理的ロック）】"]
        CrowdGaze --> OutsideNoise["外の騒ぎが教室側へ伝播"]
        OutsideNoise --> ClassroomAware["教室側にも『カーテン裏に全裸の女がいる』と露見"]:::trap
        
        ClassroomAware --> SeeYuika["野次馬の中に親友・唯香の顔を発見<br/>(疑念と自己嫌悪の【内面露出】)"]:::psychLock
        
        %% 心理的ロックの3要因
        ChoiceCurtain --> PsychLock1["心理的ロック①：動けば教室全体へ全身露出"]:::psychLock
        ClassroomAware --> PsychLock2["心理的ロック②：教室に片想いの男子生徒がいる<br/>(彼にだけは見られたくない)"]:::psychLock
        
        PsychLock1 & PsychLock2 & SeeYuika --> CompleteFreeze["【選択肢ゼロ：完全フリーズ・身動き不能】"]
    end

    %% ==========================================
    %% Phase 4: 限界突破と受容
    %% ==========================================
    subgraph Phase4_Catastrophe ["【Phase 4：決壊と最終受容】"]
        CompleteFreeze --> ClimaxBreakdown["★ クライマックス：全員の前で限界崩壊（尿決壊）<br/>【身体的・社会的破綻のピーク】"]:::climax
        
        ClimaxBreakdown --> FinalBeat["★ 最終ビート：極限の抗いの果ての諦念と受容<br/>『もう全部見られちゃえばいいんだ』<br/>(一種の精神的解放)"]:::endBeat
    end
```

---

## 2. 物語のトポロジカル進行フェーズ表

| フェーズ | 舞台 | 主人公のアクション / 事象 | ロック＆キー・トポロジー機能 |
| :--- | :--- | :--- | :--- |
| **Phase 1** | 屋上のプール | ・悪戯でフェンスに南京錠で水着を拘束される<br/>・尿意の限界から、**水着を脱ぎ捨てて脱出**する | **不可逆フラグ（全裸化）の起動**<br/>（恥を回避するための合理的選択が次の罠の前提に） |
| **Phase 2** | 教室・窓際 | ・無人のはずが無数の生徒が集まる補習授業が開始<br/>・隠れるため**カーテン裏に潜入し窓ガラスに密着**<br/>・**校庭側の野次馬から前面が完全露出** | **空間トポロジーの表裏反転**<br/>（隠れるための遮蔽物が、外部への最大露出装置へと機能反転） |
| **Phase 3** | カーテン裏 | ・外の騒ぎが教室側へ伝わり内外から包囲される<br/>・野次馬の中に親友・唯香の顔を発見<br/>・**「動けば教室へ露出」「片想いの男子がいる」** | **心理的ロック（脱出パスの消滅）**<br/>身体の露出と同時に親友を疑う「内面の醜さ」が露出 |
| **Phase 4** | 決壊〜結末 | ・逃げ場のない極限状態での尿崩壊<br/>・極限の抗いの果てに訪れる「諦念と受容」 | **破綻のピークと精神的解放** |

---

## 3. 物語脚本としての構造的強度

1. **主人公の能動的選択が破滅を加速する（古典悲劇的DAG）**
   - 受動的に被害に遭うだけでなく、「漏らしたくないから脱ぐ」「隠れたいからカーテンに入る」という**その瞬間における最善の選択が、不可逆な罠を次々と連鎖させていく**無駄のない一本道構造です。

2. **多重レイヤーの「露出」（身体・社会・内面）**
   - 身体の露出（校庭側への前面露出）
   - 社会的立場の露出（満席の教室・片想いの相手・学校全体への公然化）
   - 内面の露出（天真爛漫な人気者が抱える親友への後ろ暗い猜疑心）
   これら3つの露出が「カーテン裏のフリーズ」という1点に収束し、クライマックスへ直結しています。
