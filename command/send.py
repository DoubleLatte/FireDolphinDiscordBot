from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
import datetime
now = datetime.datetime.now()
time = now.strftime('%Y-%m-%d %H:%M:%S')

class send(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="보고서",description="신나는보고서 쓰기")  
    async def sends(self, interaction: Interaction,상황:str,좌표:str,참가인원:str,누적리포트:str) -> None:
        global u
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick
        user_role = str(interaction.user.roles)
        
        if "1094245109199028280" in user_role or "1132891083148374067" in user_role:
            embed=discord.Embed(title=":fire_engine: **"+user_nick +"** 님의 보고서",  color=0x627ce6)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
            embed.set_author(name="")
            embed.add_field(name="**보고자**: "+ user_nick,value="", inline=False)
            embed.add_field(name="**상황**: "+ 상황,value="", inline=False)
            embed.add_field(name="**좌표**: "+ 좌표,value="", inline=False)
            embed.add_field(name="**참가인원**: ",value=참가인원, inline=False)
            embed.add_field(name="**누적리포트**: "+ 누적리포트,value="", inline=False)
            embed.set_footer(text=" 위 문서에 따라 사건을 보고함")
            await interaction.response.send_message(embed=embed)
            print(user_name + ' 보고서 사용')

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        send(bot)
    )