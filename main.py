import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()

@client.event
async def on_ready():
    """起動処理"""
    print('-----Logged in info-----')
    print(client.user.name)
    print(client.user.id)
    print(discord.__version__)
    print('------------------------')

@client.event
async def on_message(message):
    """メッセージ処理"""
    # チーム作成依頼
    if message.content.startswith("/team"):
        state = message.author.voice

        if state is None: #依頼主自身がVoiceChannelにいないとき
            await message.channel.send("実行できません" + message.author.name + "さん、該当のVCへ入ってください")
        else:
            tmp = [i.name for i in state.channel.members] #VCメンバリスト取得
            await message.channel.send("\n".join(tmp))
            
# botの接続と起動
client.run(token)