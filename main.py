from discord import Intents
from discord.ext import commands
from discord import Game
from discord import Status
from discord import client
from discord import Interaction
import asyncio
import discord
import json

class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix='!',
            intents=discord.Intents.all(),
            sync_command=True,
            application_id=""
        )
        self.initial_extension = [
            "command.report",
            "command.go",
            "command.out",
            "command.huga",
            "command.info",
            "command.send",
            "command.post",
            "command.suport",
            "command.warn",
            "command.sell",
            "command.make",
            "command.check"
        ]

    async def setup_hook(self):
        for ext in self.initial_extension:
            await self.load_extension(ext)
        await bot.tree.sync()
        #await bot.tree.sync(guild=Object(id=))


    async def on_ready(self):
        print("login")
        print("BOT_Name",self.user.name)
        print("BOT_id",self.user.id)
        print("===============")
        game = Game("돌핀섭 소방청 보조")
        await self.change_presence(status=Status.online, activity=game)
    
bot = MyBot()
bot.run("")
