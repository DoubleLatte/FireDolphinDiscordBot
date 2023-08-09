from discord import app_commands
from discord.ext import commands
from discord.ext import tasks
from discord import Interaction
from discord import channel
import discord 
import time
import json

class info(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="정보",description="돌핀 서버의 119봇의 정보를 보여줍니다!")
    async def infos(self,interaction: discord.Interaction) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick
        embed=discord.Embed(title="NAME: 소방청 봇", color=0x9ADFB0)
        embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
        embed.set_author(name="")
        embed.add_field(name="봇 버전", value="2.8.9", inline=True)
        embed.add_field(name="개발자", value="DDLATTE", inline=False)
        embed.set_footer(text="봇 관련 문의는 doublelatte#0 \n 소방청봇은 DDLATTE의 소유이며 \n 개발자의 상황에 따라 정지 또는 삭제 될 수 있습니다.")
        await interaction.response.send_message(embed=embed)
        print(user_name+"님이 조회 하였습니다")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        info(bot)
    )
