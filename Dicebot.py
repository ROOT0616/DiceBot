import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


print(list(range(1,6,1)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
@client.event
async def on_message(message):
    # 「/d1」で始まるか調べる
    if message.content.startswith("/d1"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            n = random.randrange(1,6,1)
            m =  message.author.name + ' : 1d6 : ' + str(n)
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    # 「/d2」で始まるか調べる
    if message.content.startswith("/d2"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            n1 = random.randrange(1,6,1)
            n2 = random.randrange(1,6,1)
            n3 = n1 + n2
            m =  message.author.name + ' : 2d6 : ' + str(n1)+ ' + ' + str(n2) + ' = ' + str(n3)
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    # 「/d3」で始まるか調べる
    if message.content.startswith("/d3"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            n1 = random.randrange(1,6,1)
            n2 = random.randrange(1,6,1)
            n3 = random.randrange(1,6,1)
            n4 = n1 + n2 + n3
            m =  message.author.name + ' : 3d6 : ' + str(n1)+ ' + ' + str(n2) + ' + ' + str(n3) + ' = ' + str(n4)
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    if message.content.startswith("/d00"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m =  message.author.name + ' : 1d100 : ' + str(random.randrange(1,100,1))
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
    if message.content.startswith("/1d3"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m =  message.author.name + ' : 1d3 : ' + str(random.randrange(1,3,1))
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)

client.run("NzMyMDg4NTQyNjU3NzczNjY4.Xwvglg.bHJLzlgRSrO9dh74mJkxiZNu5B4")