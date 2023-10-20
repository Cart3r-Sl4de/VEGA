import discord, os, asyncio, random
from discord.ext import commands
from discord import app_commands
from PIL import Image, ImageFont
from io import BytesIO

#font = ImageFont.truetype("Minecraft.ttf", 10)
user_describe = "Mention a user to use their pfp, or leave blank for random choice."
file_location = os.path.dirname(os.path.abspath(__file__))
pfp_location = os.path.join(file_location, './pics/pfp.png')
target_location = os.path.join(file_location, './pics/target.png')
wanted_location = os.path.join(file_location, './pics/wanted.png')
class Pic(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    ## wanted poster maker, can be random choice or specific user
    @app_commands.command(name="wanted", description="Generate a wanted poster using a user's profile picture.")
    @app_commands.describe(user=user_describe)
    async def wanted(self, interaction: discord.Interaction, user: discord.Member = None):
        await imageGrabber(interaction, user)
        wanted  = Image.open(wanted_location)
        pfp = Image.open(pfp_location)
        pfp = pfp.resize((282, 282))

        wanted.paste(pfp, (94, 234))
        wanted.save(target_location)

        await interaction.response.send_message(file=discord.File(target_location))

    ## a dandy profile picture grabber
    @app_commands.command(name="pfp-grabber", description="Enter someones username or leave the field blank (random) to grab their profile picture.")
    @app_commands.describe(user=user_describe)
    async def pfpGrabber(self, interaction: discord.Interaction, user: discord.Member = None):
        await imageGrabber(interaction, user)
        await interaction.response.send_message(file=discord.File(pfp_location))



## to prevent redundancy, have the profile picture grabber be it's own callable function
async def imageGrabber(interaction, user):
    ## if the user is None, then do a random choice
    user = user or random.choice(interaction.guild.members)
    asset = user.avatar
    data = BytesIO(await asset.read())
    pfp = Image.open(data)
    pfp.save(pfp_location)

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Pic(bot))