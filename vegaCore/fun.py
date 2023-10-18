import discord, os, asyncio, random, requests, json
from discord import app_commands
from discord.ext import commands

np = [
  "Glad I could be of service",
  "Got your back",
  "👌"
  ]

#remember to implement "thanks VEGA"

eightball = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]


class Fun(commands.Cog):

  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    
  #eight ball
  @app_commands.command(name="8ball", description="Enter a question, and the 8ball will respond")
  async def eightball(self, interaction: discord.Interaction, question: str):
    await interaction.response.send_message(f'Question: {question}\nAnswer: {random.choice(eightball)}', ephemeral=True)

  @app_commands.command(name="wise-quote", description="This finds a insightful/wise quote for you")
  async def wisequote(self, interaction: discord.Interaction):
    response = requests.get('https://zenquotes.io/api/random')
    json_stuff = json.loads(response.text)
    quote = json_stuff[0]['q'] + ' -' + json_stuff[0]['a']
    await interaction.response.send_message(quote)

  @app_commands.command(name="random-number-generator", description="Takes two numbers and then finds a random number between (and including) them")
  @app_commands.describe(minimum = "lowest number in the range for random selection", maximum = "largest number in range for random selection")
  async def randnum(self, interaction: discord.Interaction, minimum: int, maximum: int):
    if minimum > maximum:
      await interaction.response.send_message(f'Error: your minimum ({minimum}) is larger than your maximum ({maximum}).')
    else:
      try:
        min = int(minimum)
        max = int(maximum)
        await interaction.response.send_message(f'Random number: {random.randint(min, max)}')
      except:
        await interaction.response.send_message('Error: problem with converting to integer. You most likely were a comedian and tried to send a word instead of a number.')


  
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Fun(bot))