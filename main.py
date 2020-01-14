import os
import traceback

import discord
from discord.ext import commands

from models.grouping import MakeTeam

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')

"""起動処理"""
@bot.event
async def on_ready():
    print('-----Logged in info-----')
    print(bot.user.name)
    print(bot.user.id)
    print(discord.__version__)
    print('------------------------')

"""コマンド実行"""
@bot.command()
async def team(ctx, party_num=2): #チーム作成
    make_team = MakeTeam()
    msg = make_team.default_make(ctx,party_num)
    await ctx.channel.send(msg)

"""botの接続と起動"""
bot.run(token)