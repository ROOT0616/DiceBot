# README.md

## English

### Dicebot for Discord

#### Introduction
This Python script serves as a dice-rolling bot for Discord servers. Users can roll dice with various faces and times based on the command provided.

#### Features
- Roll a 6-sided dice with commands like `/d1`, `/d2`, `/d3`.
- Roll a 100-sided dice with the command `/d00`.
- Custom roll with the command `/r` followed by the format `XdY` where `X` is the number of rolls and `Y` is the number of faces.
- Error handling to guide users on proper usage.

#### Requirements
- Python 3.x
- Discord.py library
- JSON for configuration

#### Installation
1. Clone the repository.
2. Install the required packages.
3. Update the `config.json` with your Discord bot token and other settings.
4. Run the script.

#### Configuration
The `config.json` file contains settings like:
- Discord bot token
- Help message
- Max and Min faces for dice
- Max and Min rolls for dice

---

## 日本語

### Discord用ダイスボット

#### 紹介
このPythonスクリプトは、Discordサーバー用のダイスを振るボットです。ユーザーは提供されたコマンドに基づいて、さまざまな面と回数でダイスを振ることができます。

#### 機能
- `/d1`、`/d2`、`/d3`などのコマンドで6面のサイコロを振る。
- `/d00`のコマンドで100面のサイコロを振る。
- `/r`コマンドに続いて `XdY` の形式でカスタムロールができる。ここで `X` は回数、`Y` は面数。
- 適切な使用方法についてユーザーをガイドするエラーハンドリング。

#### 必要条件
- Python 3.x
- Discord.pyライブラリ
- 設定用のJSON

#### インストール方法
1. リポジトリをクローンする。
2. 必要なパッケージをインストールする。
3. `config.json`にDiscordボットのトークンと他の設定を更新する。
4. スクリプトを実行する。

#### 設定
`config.json` ファイルには以下のような設定が含まれます：
- Discordボットトークン
- ヘルプメッセージ
- サイコロの最大・最小面数
- サイコロの最大・最小振り数
