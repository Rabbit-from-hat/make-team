import os
import traceback

import discord
from discord.ext import commands

from action import grouping
from action import validations

token = os.environ['DISCORD_BOT_TOKEN']
bot = commands.Bot(command_prefix='/')
validation = validations.Validations()

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
@validation.int_check
async def team(ctx, party_num): #チーム作成
    g = grouping.Grouping(ctx, party_num)
    await g.default_make()

"""botの接続と起動"""
bot.run(token)