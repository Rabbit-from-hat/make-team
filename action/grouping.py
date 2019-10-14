import random

import discord
from discord.ext import commands

import validations

class Grouping:

    def __init__(self, ctx, party_num):
        self.state = ctx.author.voice #VCのステータスを取得
        self.channel_mem = [i.name for i in self.state.channel.members] #VCメンバリスト取得
        self.mem_len = len(self.channel_mem)
        self.party_num = party_num

    def default_make(self):
        team = []
        remainder = []

        val = validations.Validations()
        result = val.grouping_check(self.state, self.party_num, self.mem_len)

        if not result[0]:
            return result[1]

        random.shuffle(self.channel_mem)

        #VCの人数が割り切れない場合
        remainder_num = self.mem_len % self.party_num
        if remainder_num != 0: 
            for r in range(remainder_num):
                remainder.append(self.channel_mem.pop())
            team.append("=====余り=====")
            team.extend(remainder)

        #チーム分け
        for i in range(self.party_num): 
            team.append("=====チーム"+str(i+1)+"=====")
            team.extend(self.channel_mem[i:self.mem_len:self.party_num])

        return ('\n'.join(team))