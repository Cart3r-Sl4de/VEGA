import discord, os, asyncio
from discord import app_commands
from discord.ext import commands

class Polls(commands.Cog):

    def __init__(self, bot: commands.Cog) -> None:
        self.bot = bot

    ## the yes or no poll, pretty simple
    @app_commands.command(name="yes-no-poll", description="Create a simple yes/no poll based on a specific question.")
    async def yesNoPoll(self, interaction: discord.Interaction, question: str):

        txt = "React with ✅ for yes or ❌ for no"
        embed = discord.Embed(title = question, description=txt, colour = discord.Colour.blurple())

        await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()
        await message.add_reaction("✅")
        await message.add_reaction("❌")

    ## the ULTIMATE polling command
    @app_commands.command(name="poll", description="Create a poll with a question and up to 9 answer options for users to choose from.")
    @app_commands.describe(title = "The title of your desired poll.", option1 = "The first option of your poll (mandatory).",
                           option2 = "The second option of your poll (mandatory). Other options are optional.", color = "Write the hex code for your desired color. Example: \"aa1bab\"")
    async def pollInator(self, interaction: discord.Interaction, title: str,
                        option1: str, option2: str, option3: str = None, option4: str = None,
                        option5: str = None, option6: str = None, option7: str = None,
                        option8: str = None, option9: str = None, color: str = "ffffff"):
        
        emoji_suffix = f"\N{variation selector-16}\N{combining enclosing keycap}"
        variables = [option1, option2, option3, option4, option5, option6, option7, option8, option9]
        result = "React with: "
        total_values = 1

        for counter, value in enumerate(variables, start = 1):
            if value != None:
                emoji = f"{counter}{emoji_suffix}"
                result += f"\n{emoji} for {value}"
                total_values += 1
        ### originally reduced the size of the output, apparently isn't needed anymore    
        #result = result[:-1]

        color_result = f"0x{color}"
        embed = discord.Embed(title=title, description=result, colour=discord.Color.from_str(color_result))
        await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()

        for index in range(1, total_values):
            emoji =  f"{index}{emoji_suffix}"
            await message.add_reaction(emoji)


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Polls(bot))

#### buttons stop working on View edit
