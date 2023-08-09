from discord import app_commands
from discord.ext import commands
import discord 


class report(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    @app_commands.command(name="신고",description="화재 신고는 돌핀소방청")
    async def reports(self,interaction: discord.Interaction) -> None:
        user_id = str (interaction.user.id)
        user_name = interaction.user.name
        user_nick = interaction.user.nick
        
        if user_id == ("1008381110314598510") or user_id == ("820156183998496830"):
            print("블랙리스트 접근")
        
        else:  
            embed=discord.Embed(title=":satellite_orbital: **"+ user_nick +"** 님의 신고가 접수되었습니다!:satellite_orbital:", description="<돌핀 소방청 소속 소방관을 부르는 중...>", color=0xFF0000)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/1133079804250431540/1135882626201288755/-_-009.png")
            embed.set_author(name="")
            embed.add_field(name=":fire_engine:돌핀의 소방은:fire_engine:", value="돌핀소방청이 책임집니다", inline=False)
            embed.add_field(name="사진과 좌표는 따로 올려주십시오",value="이 명령어는 소방관이 잠수 혹은 \n부재중 일 경우 사용해주십시오 \n 과다 사용시 |**이용금지**| 처리 될수도 있습니다!", inline=False)
            embed.set_footer(text="소방청 관련 문의는 chilsung5#0")
            await interaction.response.send_message(('<@&1132891083148374067>'),embed=embed)
            print(user_name+"님이 신고를 하였습니다")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        report(bot)
    )