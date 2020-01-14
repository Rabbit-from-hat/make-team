import random

import discord
from discord.ext import commands
from cerberus import Validator

class MakeTeam:

    def __init__(self, party_num):
        self.party_num = party_num
        self.chanel_mem = []
        schema = {
            'num':{
                    'type': 'integer',
                    'min': 0
            }
        }
        self.vdate = Validator(schema)

    def int_check(func):
        def wrapper(self, *args, **kwargs):
            num = {'num': args[1]}
            if not self.vdate.validate(num):
                return '実行できません。整数で記載してください。'
            msg = func(self, *args, **kwargs)
            return msg
        return wrapper

    def set_mem(func):
        def wrapper(self, *args, **kwargs):
            ctx = args[0]
            state = ctx.author.voice # VCのステータスを取得
            if state is None: 
                return '実行できません。ボイスチャンネルに入ってコマンドを実行してください。'
            self.chanel_mem = [i.name for i in state.channel.members] # VCメンバリスト取得
            msg = func(self, *args, **kwargs)
            return msg
        return wrapper

    @set_mem
    @int_check
    def default_make(self, ctx, party_num):
        team = []
        remainder = []

        mem_len = len(self.channel_mem) # 人数取得
        random.shuffle(self.channel_mem) # メンバーリスト内をシャッフル

        # VCの人数が割り切れない場合
        remainder_num = mem_len % self.party_num
        if remainder_num != 0: 
            for r in range(remainder_num):
                remainder.append(self.channel_mem.pop())
            team.append("=====余り=====")
            team.extend(remainder)

        # チーム分け
        for i in range(self.party_num): 
            team.append("=====チーム"+str(i+1)+"=====")
            team.extend(self.channel_mem[i:mem_len:self.party_num])

        return ('\n'.join(team))

if __name__ == '__main__':
    token = "token"
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
        make_team = MakeTeam(party_num)
        msg = make_team.default_make(ctx,party_num)
        await ctx.channel.send(msg)

    """botの接続と起動"""
    bot.run(token)
