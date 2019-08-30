import discord
from discord.ext import commands
import random

def default_make(ctx, party_num):

    state = ctx.author.voice #VCのステータスを取得

    if state is None: #依頼主自身がVoiceChannelにいないとき
        return '実行できません。ボイスチャンネルに入ってコマンドを実行してください。'

    print(party_num)
    channel_mem = [i.name for i in state.channel.members] #VCメンバリスト取得
    random.shuffle(channel_mem)
    return '\n'.join(channel_mem)