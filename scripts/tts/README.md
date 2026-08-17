# キャラクターボイス生成（Irodori-TTS）

キャラクターページの音声サンプルを作るためのワークフロー。[Irodori-TTS](https://github.com/Aratako/Irodori-TTS)（VoiceDesign機能）をローカルのDocker上で動かし、テキストとキャラごとの声質指定（caption）から音声を生成する。

**テキストの出所は問わない。** AIに書かせたセリフでも、自分で書いた原稿でも、同じコマンド一つで声にできる。

参照音声（声のクローン元）は使っていない。あくまでテキストによる声質デザイン（VoiceDesign）。

## なぜDockerか

Irodori-TTSはtorch>=2.10を要求するが、これはIntel Mac（macOS x86_64）向けのビルドを配布していない（Apple SiliconとLinuxのみ）。そのため`linux/amd64`のDockerコンテナ内でCPU推論している。Apple Silicon Macや、torchが直接動く環境ではDockerなしでも動くはず（未検証）。

## セットアップ（初回のみ）

```bash
open -a Docker          # Docker Desktopが起動していなければ
scripts/tts/setup.sh    # イメージ four-seasons-tts:latest をビルド
```

## 使い方

```bash
scripts/tts/generate.sh <character_id> <出力名> "<セリフ>"
```

例:

```bash
# AIが書いたセリフでも
scripts/tts/generate.sh kaede greeting-01 "遠山楓です。よろしくお願いします。"

# 自分で書いた原稿でも（ファイルから読み込む場合）
scripts/tts/generate.sh hiiragi my-draft-01 "$(cat draft.txt)"

# その場だけ声質を変えたい場合
scripts/tts/generate.sh kaede angry-01 "……ふざけないで。" --caption "怒りを抑えきれず声が震える、低く冷たいトーン"
```

初回実行時はモデル（約1.1GB）をHugging Faceからダウンロードする。2回目以降はDockerの名前付きボリューム（`four-seasons-tts-hf-cache`）にキャッシュされるため速い。CPU推論のため、短いセリフ1本で1〜2分程度かかる。

生成物は `wiki/assets/characters/<character_id>/voice/<出力名>.mp3` に保存される。コマンドの最後に、キャラクターページへ貼るための`![[<出力名>.mp3]]`スニペットが表示されるので、それをコピーしてページに貼るだけで再生ボタン付きプレイヤーになる（Quartzのオブジディアン形式埋め込みが`<audio controls>`に自動変換される）。

## キャラの声質を管理する — `voices.yaml`

キャラクターごとの声質指定（caption）は [`voices.yaml`](voices.yaml) にまとめてある。ここを編集すれば、以後そのキャラで生成する全ての音声に反映される。

新しいキャラを追加する場合は、同じ形式でエントリを足すだけでよい：

```yaml
character_id:
  name_ja: 表示名
  caption: >-
    年齢感・話し方の特徴・声のトーン・距離感などを日本語の自然文で記述。
```

captionは実際の人物設定（`wiki/characters/<id>/index.md`のfrontmatter・性格描写）から一貫させること。

## キャラクターページへの組み込み例

`遠山楓`のページ（[`wiki/characters/kaede/index.md`](../../wiki/characters/kaede/index.md)）に実装済み。「🖼️ 確定素材 > 顔」の直後、顔画像のすぐ下に音声プレイヤーを置いている——「顔とセリフを一緒に確認できる」ことを優先した配置。新しいキャラに追加するときもこのパターン（顔画像の直後）を踏襲するとよい。

```markdown
> [!example]- 🔊 声を聞く（Irodori-TTS / VoiceDesign, サンプル）
> ![[ファイル名.mp3]]
>
> 「セリフのテキストをここに書く」
>
> 一言メモ（声質指定の要約など）
```

## 制約・注意点

- 生成音声には自動的に電子透かし（SilentCipher）が入る（Irodori-TTS側の仕様）。
- CPU推論のみ検証済み。GPUがある環境なら`Dockerfile`のtorchインストール行を`cu128`用に差し替えれば速くなるはず（未検証）。
- モデルの利用条件は [Irodori-TTS-v4.1-Small のモデルカード](https://huggingface.co/Aratako/Irodori-TTS-v4.1-Small) を参照。
