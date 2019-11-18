import random

import discord
from discord.ext import commands

from action import validations

class Grouping:

    def __init__(self, party_num):
        self.party_num = party_num

    def default_make(self, ctx):
        team = []
        remainder = []

        state = ctx.author.voice #VCのステータスを取得
        channel_mem = [i.name for i in state.channel.members] #VCメンバリスト取得
        mem_len = len(channel_mem)

        # バリデーション(チーム作成可能チェック)
        val = validations.Validations()
        result = val.grouping_check(state, self.party_num, mem_len)

        if not result == 1:
            return result

        random.shuffle(channel_mem)

        #VCの人数が割り切れない場合
        remainder_num = mem_len % self.party_num
        if remainder_num != 0: 
            for r in range(remainder_num):
                remainder.append(channel_mem.pop())
            team.append("=====余り=====")
            team.extend(remainder)

        #チーム分け
        for i in range(self.party_num): 
            team.append("=====チーム"+str(i+1)+"=====")
            team.extend(channel_mem[i:mem_len:self.party_num])

        return ('\n'.join(team))