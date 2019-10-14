import discord
from discord.ext import commands

class SendMessage:

    def __init__(self, ctx):
        self.ctx = ctx
    
    def default_send(self, msg):
        send_msg = []

        send_msg.append("コマンドが実行されました。")
        send_msg.extend(msg)
        self.ctx.channel.send(msg)

    def error_send(self, msg):
        send_msg = []

        send_msg.append("実行できません。")
        send_msg.extend(msg)
        self.ctx.channel.send(msg)
