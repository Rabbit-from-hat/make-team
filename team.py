import discord
import random

def team_shuffle(message):
        channel_mem = [i.name for i in message.author.voice.channel.members] #VCメンバリスト取得
        random.shuffle(channel_mem)
        await message.channel.send("\n".join(channel_mem[::2]))
        await message.channel.send("\n".join(channel_mem[1::2]))