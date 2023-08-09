from discord import app_commands
from discord.ext import commands
from discord.ext import tasks
from discord import Interaction
from discord import Object
import discord 
import time


class hello(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="휴가",description="신나는 휴가 신청하기")
    async def h(self,interaction: discord.Interaction) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick
        user_role = str(interaction.user.roles)
        
        if "1094245109199028280" in user_role or "1132891083148374067" in user_role:        
            embed=discord.Embed(title="소방청 휴가 신청 하는중", color=0xFF0000)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
            embed.set_author(name="")
            embed.add_field(name=":airplane_departure: **"+user_nick+"** 님 휴가 신청되었습니다! ", value="세부일정은 소방청장에게 문의하세요!", inline=False)
            await interaction.response.send_message("<@!"+user_id+">",embed=embed)
            print(user_name + ' 휴가 사용')

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        hello(bot)
    )