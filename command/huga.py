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
    async def h(self,interaction: discord.Interaction,휴가기간:str,휴가사유:str) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick
        user_role = str(interaction.user.roles)
        
        if "1094245109199028280" in user_role or "1132891083148374067" in user_role:        
            embed=discord.Embed(title=""+user_nick+"님의 소방청 휴가 신청 하는중", color=0x00bbff)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
            embed.set_author(name="")
            embed.add_field(name="휴가일정:", value=휴가기간, inline=False)
            embed.add_field(name="휴가사유:", value=휴가사유, inline=False)
            embed.set_footer(text="위 사유에 의해 휴가를 신청 합니다.")
            await interaction.response.send_message("<@!"+user_id+">",embed=embed)
            print(user_name + ' 휴가 사용')

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        hello(bot)
    )
