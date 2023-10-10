import discord, os, asyncio, random
from discord.ext import commands
from discord import app_commands
from PIL import Image, ImageFont
from io import BytesIO

#font = ImageFont.truetype("Minecraft.ttf", 10)
file_location = os.path.dirname(os.path.abspath(__file__))

class Pic(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    ## wanted poster maker, can be random choice or specific user
    @app_commands.command(name="wanted")
    async def wanted(self, interaction: discord.Interaction, user: discord.Member = None):
        await imageGrabber(interaction, user)
        wanted  = Image.open("wanted.png")
        pfp = Image.open("pfp.png")
        pfp = pfp.resize((282, 282))

        wanted.paste(pfp, (94, 234))
        wanted.save("target.png")

        await interaction.response.send_message(file=discord.File("target.png"))



async def imageGrabber(interaction, user):
    user = user or random.choice(interaction.guild.members)
    asset = user.avatar
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.save("pfp.png")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Pic(bot))