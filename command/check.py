from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
import datetime
now = datetime.datetime.now()

class check(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="재고정리",description="재고 장부 적기 사진은 패더클 업로드로 추가")  
    async def check(self, interaction: Interaction,이미지:str,재고:str,특이사항:str) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick
        user_role = str(interaction.user.roles)
        
        if "1094245109199028280" in user_role or "1132891083148374067" in user_role:        
            time = now.strftime('%Y-%m-%d %H:%M:%S')
            embed=discord.Embed(title="**"+user_nick +"** 님의 재고 정리", color=0xd6ff7f)
            embed.set_thumbnail(url=이미지)
            embed.set_author(name="")
            embed.add_field(name="**재고 수량: **"+ 재고,value="", inline=False)
            embed.add_field(name="**특이사항: **"+ 특이사항,value="", inline=False)
            await interaction.response.send_message(embed=embed)

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        check(bot)
    )
