import discord
from discord.ext import commands
import os
import traceback
import grouping

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')

@bot.event
async def on_ready():
    """起動処理"""
    print('-----Logged in info-----')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------------------------')

@bot.command()
async def team(ctx, *party_num:int): #チーム作成
    if not party_num:
        await ctx.channel.send("チーム数を指定してください。")
    else:
        msg = grouping.default_make(ctx, party_num)
        await ctx.channel.send(msg)
            
# botの接続と起動
bot.run(token)