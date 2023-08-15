from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
import datetime
now = datetime.datetime.now()

class sell(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="판매장부",description="판매 장부 적기 사잔은 따로 추가")  
    async def sell(self, interaction: Interaction,구매자:str,수량:str,금액:str,직업:str) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick
        user_role = str(interaction.user.roles)
        
        if "1094245109199028280" in user_role or "1132891083148374067" in user_role:        
            time = now.strftime('%Y-%m-%d %H:%M:%S')
            embed=discord.Embed(title="**"+user_nick +"** 님의 판매 내역", color=0x1b67e0)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
            embed.set_author(name="")
            embed.add_field(name="**구매자: **"+ 구매자 ,value="", inline=False)
            embed.add_field(name="**판매 수량: **"+ 수량,value="", inline=False)
            embed.add_field(name="**판매 이익: **"+ 금액,value="", inline=False)
            embed.add_field(name="**구매자 직업: **"+ 직업,value="", inline=False) 
            await interaction.response.send_message(embed=embed)

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        sell(bot)
    )