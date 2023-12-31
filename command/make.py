from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
import datetime
now = datetime.datetime.now()

class make(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="제조장부",description="제조 장부 적기 사진은 패더클 업로드 기능 이용")  
    async def make(self, interaction: Interaction,이미지:str,수량:str,반입반출:str) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick
        user_role = str(interaction.user.roles)
        
        if "1094245109199028280" in user_role or "1132891083148374067" in user_role:        
            time = now.strftime('%Y-%m-%d %H:%M:%S')
            embed=discord.Embed(title="**"+user_nick +"** 님의 재료 내역", color=0x7f83ff)
            embed.set_thumbnail(url=이미지)
            embed.set_author(name="")
            embed.add_field(name="**제조자: **"+ user_nick ,value="", inline=False)
            embed.add_field(name="**제조 수량: **",value=수량, inline=True)
            embed.add_field(name="**[반입 / 반출]**",value=반입반출, inline=True)
            await interaction.response.send_message(embed=embed)

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        make(bot)
    )
