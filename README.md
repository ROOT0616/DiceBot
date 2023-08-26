
# Dicebot

Dicebotは、Discord上で様々なサイコロを振ることができるシンプルなボットです。

## 機能

- 6面のサイコロを1から3回振ることができます（`/d1`, `/d2`, `/d3`）。
- 100面のサイコロを1回振ることができます（`/d00`）。
- 3面のサイコロを1回振ることができます（`/1d3`）。
- 任意の回数と面数でサイコロを振ることができます（`/roll 回数d面数`）。

## 使用方法

1. ボットをサーバーに追加します。
2. テキストチャンネルで上記のコマンドを使用します。
3. ボットがサイコロの結果を返します。

## インストール

1. Python 3.8以上が必要です。
2. 必要な依存関係をインストールします：`pip install discord.py`
3. 設定ファイルにDiscordボットトークンを追加します。
4. `Dicebot.py`を実行します。

## ライセンス

このプロジェクトはMITライセンスのもとで公開されています。