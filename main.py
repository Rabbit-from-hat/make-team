import os
import traceback

import discord
from discord.ext import commands

from action import grouping
from action import validations
from action import send_message

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

    sendact = send_message.SendMessage(ctx)

    # バリデーション(整数チェック)
    val = validations.Validations()
    result = val.int_check(party_num)

    if result == 1:
        makeact = grouping.Grouping(ctx, party_num)
        msg = makeact.default_make()
        await sendact.default_send(msg)
    else:
        await sendact.error_send(result)

"""botの接続と起動"""
bot.run(token)