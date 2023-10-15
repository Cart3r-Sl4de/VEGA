import discord, os, asyncio
from discord import app_commands
from discord.ext import commands

class Polls(commands.Cog):

    def __init__(self, bot: commands.Cog) -> None:
        self.bot = bot

    @app_commands.command(name="poll")
    @app_commands.describe()
    async def yesNoPoll(self, interaction: discord.Interaction, title: str,
                        option1: str, option2: str, option3: str = None, option4: str = None,
                        option5: str = None, option6: str = None, option7: str = None,
                        option8: str = None, option9: str = None):
        
        emoji = {1: "1️⃣", 2: "2️⃣", 3: "3️⃣", 4: "4️⃣", 5: "5️⃣", 6: "6️⃣", 7: "7️⃣", 8: "8️⃣", 9: "9️⃣"}
        variables = [option1, option2, option3, option4, option5, option6, option7, option8, option9]
        result = "React with: "
        total_values = 0

        for counter, value in enumerate(variables, start = 1):
            if value != None:
                result += f"{emoji.get(counter)} for {value}, or "
            else:
                result = result[:-5]
                total_values = counter
                break
        
        embed = discord.Embed(title=title, description=result, colour=discord.Colour.red())
        await interaction.response.send_message(embed=embed)
        message = await interaction.original_response()
        await message.add_reaction("✅")

    '''@app_commands.command(name="yes-no-poll")
    async def yesNoPoll(self, interaction: discord.Interaction, question: str):
        txt = "React with ✅ for yes or ❌ for no"
        embed = discord.Embed(title = question, description=txt, colour = discord.Colour.blurple())
        message = await interaction.response.send_message(embed=embed)
        await message.add_reaction("✅")
        await message.add_reaction("❌")'''
    


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(Polls(bot))

#### buttons stop working on View edit