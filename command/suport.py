from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
import datetime


class suport(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="지원",description="돌핀 최강 소방청 지원하기")  
    async def suport(self, interaction: Interaction,닉네임:str,나이:str,지원동기:str) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick 
        user_role = str(interaction.user.roles)
        now = datetime.datetime.now()
        time = now.strftime('%Y-%m-%d %H:%M:%S')


        if "1094245109199028280" in user_role or "1094973339514179666" in user_role:
            now = datetime.datetime.now()
            time = now.strftime('%Y-%m-%d %H:%M:%S')
            embed=discord.Embed(title=user_nick +"** 님의 소방청 지원서", color=0xb1daf5)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
            embed.set_author(name="")
            embed.add_field(name="닉네임: "+ 닉네임,value="", inline=False)
            embed.add_field(name="나이: "+ 나이,value="", inline=False)
            embed.add_field(name="지원동기: "+ 지원동기,value="", inline=False)
            embed.set_footer(text=time)
            await interaction.response.send_message("<@!"+user_id+">",embed=embed)
            print(user_name + ' 퇴근 도장 사용')

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        suport(bot)
    )
