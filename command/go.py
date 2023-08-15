from discord import app_commands
from discord.ext import commands
from discord import Interaction
from discord import Object
import discord
import datetime
now = datetime.datetime.now()

class go(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="출근",description="출근 도장 찍기")  
    async def go(self, interaction: Interaction) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick
        user_role = str(interaction.user.roles)
        
        if "1094245109199028280" in user_role or "1132891083148374067" in user_role:        
            time = now.strftime('%Y-%m-%d %H:%M:%S')
            embed=discord.Embed(title=":fire_engine: **"+user_nick +"** 님의 출근시간", color=0x1b67e0)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
            embed.set_author(name="")
            embed.add_field(name="**"+time+"**",value="", inline=False)
            await interaction.response.send_message("<@!"+user_id+"><출근>",embed=embed)
            print(user_name + ' 출근 도장 사용')

        else:
            pass


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        go(bot)
    )