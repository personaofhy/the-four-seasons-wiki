---
title: 場所・舞台一覧
decision_default: canon
---

# 📍 場所・舞台一覧

各章の舞台を、キャラクターから独立した単位で管理する。**複数のキャラ・複数のシーンから参照される唯一の要素**であり、ここが揃うとwikiに横のリンクが通る。

プロンプトの正は `workflows/location_prompt_spec.json`。各ノートの記述はそこからの写し。

| 場所 | 章 | 決定状態 |
| :--- | :--- | :--- |
| [[locations/meeting-room\|政治家たちの密室・会議室]] | [[chapters/01-spring/index\|01-spring]] | ✅ canon |
| [[locations/rooftop-pool\|屋上のプール]] | [[chapters/02-summer/index\|02-summer]] | ✅ canon |
| [[locations/summer-classroom\|補習授業中の教室・カーテン裏]] | [[chapters/02-summer/index\|02-summer]] | ✅ canon |
| [[locations/campsite-mud\|社内キャンプ場・紅葉の泥]] | [[chapters/03-autumn/index\|03-autumn]] | ✅ canon |
| [[locations/private-room\|静まり返った自室・炬燵]]（準備段階） | [[chapters/04-winter/index\|04-winter]] | ✅ canon |
| [[locations/ferris-wheel-queue\|遊園地・観覧車の待機列]]（破綻） | [[chapters/04-winter/index\|04-winter]] | 🔓 open |
| [[locations/school-corridor\|学校・トイレ前の廊下]] | [[chapters/05-re-spring/index\|05-re-spring]] | ✅ canon |

> [!note] 第2章と第4章は舞台が2つある
> 第2章は発端（屋上のプール）と破綻（補習授業中の教室）が別の場所であり、**その移動そのものが筋**であるため分割している。
> 第4章は準備（自室）と破綻（遊園地）が別の場所。破綻は群衆の前で、柊が自ら踏み出す形で起こる。

---

## 🧩 スロット順（固定）

| # | スロット | 内容 |
| :-: | :--- | :--- |
| 1 | `space` | What kind of room or place, its scale and enclosure. Enclosure is the horror lever - say whether it can be left. |
| 2 | `surfaces` | Floor, walls, and the material the body will touch. This is what stains, soaks, or reflects. |
| 3 | `light` | Source, direction, colour temperature, time of day. |
| 4 | `weather_air` | Temperature, humidity, smell, sound. Drives the physical sensation in prose even when invisible in an image. |
| 5 | `props` | Objects that carry meaning. Keep to three or fewer - a prop list longer than that stops reading as composition. |
| 6 | `camera` | Height, distance, lens feel. Fixed per location so repeat generations match. |
| 7 | `tone` | Seasonal palette and contrast, matching the chapter. |

> [!warning] 人物を含めない
> 場所プロンプトは背景単体。シーン画像は場所スロット＋キャラスロットの合成で作る。

