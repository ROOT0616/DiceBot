import discord
from discord.ext import commands
from discord import app_commands
import random
import json
import logging

# ログの設定
logging.basicConfig(level=logging.INFO, filename='bot.log', format='%(asctime)s:%(levelname)s:%(message)s')

# config.jsonからトークンを読み込む (UTF-8エンコーディングを指定)
try:
    with open("config.json", encoding='utf-8') as config_file:
        config = json.load(config_file)
except FileNotFoundError:
    logging.error("config.jsonファイルが見つかりません。")
    raise SystemExit("config.jsonファイルが見つかりません。")
except json.JSONDecodeError:
    logging.error("config.jsonのフォーマットが不正です。")
    raise SystemExit("config.jsonのフォーマットが不正です。")

# インテントの設定
intents = discord.Intents.default()
intents.message_content = True

# ボットのインスタンス作成
bot = commands.Bot(command_prefix="!", intents=intents)

# ボットの初期化処理
@bot.event
async def on_ready():
    logging.info(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print(f"Logged in as {bot.user} (ID: {bot.user.id})")
    print("------")
    # スラッシュコマンドのシンク
    try:
        synced = await bot.tree.sync()
        logging.info(f"Synced {len(synced)} command(s)")
    except Exception as e:
        logging.error(f"Failed to sync commands: {e}")
        print(f"Failed to sync commands: {e}")

# /roll コマンドの定義（サイコロの詳細を表示）
@bot.tree.command(name="roll", description="指定した回数と面数でサイコロを振ります。")
@app_commands.describe(rolls="サイコロを振る回数", faces="サイコロの面数")
async def roll(interaction: discord.Interaction, rolls: int = 1, faces: int = 6):
    if not (1 <= rolls <= 10):
        await interaction.response.send_message("サイコロの回数は1~10の間で指定してください。", ephemeral=True)
        return
    if not (2 <= faces <= 100):
        await interaction.response.send_message("サイコロの面数は2~100の間で指定してください。", ephemeral=True)
        return
    
    # サイコロを振る処理
    results = [random.randint(1, faces) for _ in range(rolls)]
    results_str = ", ".join(map(str, results))
    
    # 結果をわかりやすく表示
    await interaction.response.send_message(f"{rolls}回の{faces}面のサイコロの結果: {results_str}")

# /multiroll コマンドの定義（サイコロの種類ごとの結果を表示）
@bot.tree.command(name="multiroll", description="複数の異なるサイコロを同時に振ります。")
@app_commands.describe(rolls_faces="複数のサイコロの形式（例: 3d6, 2d100）")
async def multiroll(interaction: discord.Interaction, rolls_faces: str):
    try:
        # "3d6, 2d100" の形式を解析
        roll_sets = rolls_faces.split(",")
        results_summary = []
        for roll_set in roll_sets:
            rolls, faces = map(int, roll_set.strip().split("d"))
            if not (1 <= rolls <= 10) or not (2 <= faces <= 100):
                raise ValueError("回数または面数が範囲外です")
            results = [random.randint(1, faces) for _ in range(rolls)]
            results_str = ", ".join(map(str, results))
            # 各セットの結果をわかりやすく表示
            results_summary.append(f"{rolls}回の{faces}面のサイコロの結果: {results_str}")
        
        # 全結果をまとめて送信
        await interaction.response.send_message("\n".join(results_summary))
    except ValueError:
        await interaction.response.send_message("入力形式が正しくありません。例: 3d6, 2d100", ephemeral=True)
    except Exception as e:
        logging.error(f"マルチロールの処理中にエラーが発生しました: {e}")
        await interaction.response.send_message("サイコロを振る処理中にエラーが発生しました。", ephemeral=True)

# /help コマンドの定義
@bot.tree.command(name="help", description="Botの使い方を説明します。")
async def help(interaction: discord.Interaction):
    help_message = (
        "/roll - 指定した回数と面数でサイコロを振ります。\n"
        "/multiroll - 複数のサイコロを同時に振ります。\n"
        "例: 3d6, 2d100\n"
        "/help - Botの使い方を表示します。"
    )
    await interaction.response.send_message(help_message)

# ボットの起動
try:
    bot.run(config["TOKEN"])
except discord.errors.LoginFailure:
    logging.error("無効なトークンです。トークンを確認してください。")
    raise SystemExit("無効なトークンです。トークンを確認してください。")
except Exception as e:
    logging.error(f"ボットの起動中にエラーが発生しました: {e}")
    raise SystemExit(f"ボットの起動中にエラーが発生しました: {e}")
