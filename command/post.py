from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import client
import asyncio 
import discord
import datetime
now = datetime.datetime.now()
time = now.strftime('%Y-%m-%d %H:%M:%S')

class post(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="공지",description="공지용 명령어")  
    async def post(self, interaction: Interaction,공지명:str,내용:str) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick 
        user_role = str(interaction.user.roles)

        if "1094245109199028280" in user_role or "1094969120350548008" in user_role:
                time = now.strftime('%Y-%m-%d %H:%M:%S')
                embed=discord.Embed(title=""+공지명, color=0xb1daf5)
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
                embed.set_author(name="")
                embed.add_field(name="**"+내용+"**",value="", inline=False)
                await interaction.response.send_message("<@!"+user_id+">",embed=embed)
                print(user_name + '공지 사용')

        else:
            pass



async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        post(bot)
    )