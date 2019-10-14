import discord
from discord.ext import commands
import random 

def default_make(ctx, party_num):
    team = []
    remainder = []
    state = ctx.author.voice #VCのステータスを取得

    #依頼主自身がVoiceChannelにいないとき
    if state is None: 
        return '実行できません。ボイスチャンネルに入ってコマンドを実行してください。'

    channel_mem = [i.name for i in state.channel.members] #VCメンバリスト取得

    random.shuffle(channel_mem)
    mem_len = len(channel_mem)

    #ボイスチャンネルに一人しかいない場合
    if mem_len == 1:
        return '実行できません。２人以上参加してください。'

    #VCの人数が割り切れない場合
    remainder_num = mem_len % party_num
    if remainder_num != 0: 
        for r in range(remainder_num):
            remainder.append(channel_mem.pop())
        team.append("余剰")
        team.extend(remainder)

    #チーム分け
    for i in range(party_num): 
        team.append("チーム"+str(i+1))
        team.extend(channel_mem[i:mem_len:party_num])

    return '\n'.join(team)