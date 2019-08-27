import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    """起動時に通知してくれる処理"""
    print('-----Logged in info-----')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------------------------')

@client.event
async def on_message(message):
    """メッセージを処理"""
    # 「おはよう」で始まるか調べる
    if message.content.startswith("おはよう"):
        # 送り主がBotだった場合反応したくないので
        if client.user != message.author:
            # メッセージを書きます
            m = "おはようございます" + message.author.name + "さん！"
            # メッセージが送られてきたチャンネルへメッセージを送ります
            await message.channel.send(m)
            
# botの接続と起動
client.run(token)