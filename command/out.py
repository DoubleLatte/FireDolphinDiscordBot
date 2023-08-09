from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
import datetime
now = datetime.datetime.now()
time = now.strftime('%Y-%m-%d %H:%M:%S')

class out(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="퇴근",description="퇴근 도장 찍기")  
    async def outs(self, interaction: Interaction) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick 
        user_role = str(interaction.user.roles)
        
        if "1094245109199028280" in user_role or "1132891083148374067" in user_role:
            time = now.strftime('%Y-%m-%d %H:%M:%S')
            embed=discord.Embed(title=":fire_engine: **"+user_nick +"** 님의 퇴근시간", color=0xb1daf5)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
            embed.set_author(name="")
            embed.add_field(name="**"+time+"**",value="", inline=False)
            await interaction.response.send_message("<@!"+user_id+">",embed=embed)
            print(user_name + ' 퇴근 도장 사용')

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        out(bot)
    )