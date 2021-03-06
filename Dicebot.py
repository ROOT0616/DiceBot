import discord
import random

client = discord.Client()

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


print(list(range(1,7,1)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
@client.event
async def on_message(message):
    # 「/d help」で始まるか調べる
    if message.content.startswith("/d help"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m1 =  message.author.name + '\n　　　　　 HELP'
            m2 = '\n/d1で六面ダイスを一個降ります。'
            m3 = '\n/d2で六面ダイスを二個降ります。'
            m4 = '\n/d3で六面ダイスを三個降ります。'
            m5 = '\n/d00で百面ダイスを一個降ります。'
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m1)
            await message.channel.send(m2)
            await message.channel.send(m3)
            await message.channel.send(m4)
            await message.channel.send(m5)
    # 「/d1」で始まるか調べる
    if message.content.startswith("/d1"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m2 = str(message.content)
            m3 = m2.replace('/d1', '')
            # メッセージが送られてきたチャンネルへメッセージを送ります
            # await message.channel.send(m)
            # await message.channel.send(m2)
            # await message.channel.send(m3)
            m4 = str('')
            m5 = 0
            if m3 == m4:
                # メッセージを書きます
                n1 = random.randrange(1,7,1)
                m =  message.author.name + ' : 1d6 : ' + str(n1)
                await message.channel.send(m)
            elif type(int(m3)) == type(m5):
                if int(m3) < 11:
                    await message.channel.send('1d6を' + str(m3) + '回ふります')
                    while int(m3) > m5:
                        # メッセージを書きます
                        n1 = random.randrange(1,7,1)
                        m =  message.author.name + ' : 1d6 : ' + str(n1)
                        await message.channel.send(m)
                        m5 += 1
                else:
                        await message.channel.send('10以下でお願いします')
    # 「/d2」で始まるか調べる
    if message.content.startswith("/d2"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m2 = str(message.content)
            m3 = m2.replace('/d2', '')
            # メッセージが送られてきたチャンネルへメッセージを送ります
            # await message.channel.send(m)
            # await message.channel.send(m2)
            # await message.channel.send(m3)
            m4 = str('')
            m5 = 0
            if m3 == m4:
                # メッセージを書きます
                n1 = random.randrange(1,7,1)
                n2 = random.randrange(1,7,1)
                n3 = n1 + n2
                m =  message.author.name + ' : 2d6 : ' + str(n1)+ ' + ' + str(n2) + ' = ' + str(n3)
                await message.channel.send(m)
            elif type(int(m3)) == type(m5):
                if int(m3) < 11:
                    await message.channel.send('2d6を' + str(m3) + '回ふります')
                    while int(m3) > m5:
                        # メッセージを書きます
                        n1 = random.randrange(1,7,1)
                        n2 = random.randrange(1,7,1)
                        n3 = n1 + n2
                        m =  message.author.name + ' : 2d6 : ' + str(n1)+ ' + ' + str(n2) + ' = ' + str(n3)
                        await message.channel.send(m)
                        m5 += 1
                else:
                        await message.channel.send('10以下でお願いします')
    # 「/d3」で始まるか調べる
    if message.content.startswith("/d3"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m2 = str(message.content)
            m3 = m2.replace('/d3', '')
            # メッセージが送られてきたチャンネルへメッセージを送ります
            # await message.channel.send(m)
            # await message.channel.send(m2)
            # await message.channel.send(m3)
            m4 = str('')
            m5 = 0
            if m3 == m4:
                # メッセージを書きます
                n1 = random.randrange(1,7,1)
                n2 = random.randrange(1,7,1)
                n2 = random.randrange(1,7,1)
                n3 = random.randrange(1,7,1)
                n4 = n1 + n2 + n3
                m =  message.author.name + ' : 2d6 : ' + str(n1)+ ' + ' + str(n2) + ' + ' + str(n3) + ' = ' + str(n4)
                await message.channel.send(m)
            elif type(int(m3)) == type(m5):
                if int(m3) < 11:
                    await message.channel.send('3d6を' + str(m3) + '回ふります')
                    while int(m3) > m5:
                        # メッセージを書きます
                        n1 = random.randrange(1,7,1)
                        n2 = random.randrange(1,7,1)
                        n2 = random.randrange(1,7,1)
                        n3 = random.randrange(1,7,1)
                        n4 = n1 + n2 + n3
                        m =  message.author.name + ' : 2d6 : ' + str(n1)+ ' + ' + str(n2) + ' + ' + str(n3) + ' = ' + str(n4)
                        await message.channel.send(m)
                        m5 += 1
                else:
                        await message.channel.send('10以下でお願いします')
    if message.content.startswith("/d00"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m2 = str(message.content)
            m3 = m2.replace('/d00', '')
            # メッセージが送られてきたチャンネルへメッセージを送ります
            # await message.channel.send(m)
            # await message.channel.send(m2)
            # await message.channel.send(m3)
            m4 = str('')
            m5 = 0
            if m3 == m4:
                # メッセージを書きます
                n1 = random.randrange(1,101,1)
                m =  message.author.name + ' : 1d100 : ' + str(n1)
                await message.channel.send(m)
            elif type(int(m3)) == type(m5):
                if int(m3) < 11:
                    await message.channel.send('1d100を' + str(m3) + '回ふります')
                    while int(m3) > m5:
                        # メッセージを書きます
                        n1 = random.randrange(1,101,1)
                        m =  message.author.name + ' : 1d100 : ' + str(n1)
                        await message.channel.send(m)
                        m5 += 1
                else:
                        await message.channel.send('10以下でお願いします')
    if message.content.startswith("/1d3"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            m2 = str(message.content)
            m3 = m2.replace('/1d3', '')
            # メッセージが送られてきたチャンネルへメッセージを送ります
            # await message.channel.send(m)
            # await message.channel.send(m2)
            # await message.channel.send(m3)
            m4 = str('')
            m5 = 0
            if m3 == m4:
                # メッセージを書きます
                n1 = random.randrange(1,4,1)
                m =  message.author.name + ' : 1d3 : ' + str(n1)
                await message.channel.send(m)
            elif type(int(m3)) == type(m5):
                if int(m3) < 11:
                    await message.channel.send('1d3を' + str(m3) + '回ふります')
                    while int(m3) > m5:
                        # メッセージを書きます
                        n1 = random.randrange(1,4,1)
                        m =  message.author.name + ' : 1d3 : ' + str(n1)
                        await message.channel.send(m)
                        m5 += 1
                else:
                        await message.channel.send('10以下でお願いします')

client.run("")