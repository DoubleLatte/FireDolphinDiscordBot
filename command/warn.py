from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
import datetime


class warn(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="경고",description="소방청 내부 경고")  
    async def warn(self, interaction: Interaction,대상자:str,사유:str) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick 
        user_role = str(interaction.user.roles)
        now = datetime.datetime.now()
        time = now.strftime('%Y-%m-%d %H:%M:%S')
        
        if "1094245109199028280" in user_role or "1094969112016453662" in user_role:
            embed=discord.Embed(title="[ 소방청 내부 경고 ]", color=0xFF0000)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
            embed.set_author(name="")
            embed.add_field(name="처리자 : "+user_nick ,value="", inline=False)
            embed.add_field(name="대상자 : " ,value= 대상자, inline=False)
            embed.add_field(name="사유 : " ,value=사유, inline=False)
            await interaction.response.send_message(embed=embed)
            print(user_name + ' 퇴근 도장 사용')

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        warn(bot)
    )
