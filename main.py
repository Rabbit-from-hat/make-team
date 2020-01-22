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
# メンバー数が均等になるチーム分け
@bot.command()
<<<<<<< HEAD
async def team(ctx, specified_num=2):
    make_team = MakeTeam()
    remainder_flag = 'true'
    msg = make_team.make_party_num(ctx,specified_num,remainder_flag)
=======
async def team(ctx, party_num=2): #チーム作成
    msg = grouping.default_make(ctx, party_num)
>>>>>>> 581e43e298a8192dc3f8dd801852d35da592c6dc
    await ctx.channel.send(msg)

# メンバー数が均等にはならないチーム分け
@bot.command()
async def team_norem(ctx, specified_num=2):
    make_team = MakeTeam()
    msg = make_team.make_party_num(ctx,specified_num)
    await ctx.channel.send(msg)

"""botの接続と起動"""
bot.run(token)