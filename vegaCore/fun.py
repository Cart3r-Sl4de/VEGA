import discord, os, asyncio, random, requests, json, pytz
from datetime import datetime
from discord import app_commands
from discord.ext import commands
from typing import Literal

file_location = os.path.dirname(os.path.abspath(__file__))
eightball = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
ALLOWED_TIMEZONES = [
    'US/Eastern',
    'US/Mountain',
    'US/Pacific',
    'Europe/Paris',
    'Europe/Kiev',
    'Europe/Berlin',
    'Canada/Atlantic',
    'Canada/Central',
    'Canada/Eastern',
    'Canada/Pacific'
]
# apparently 'type hinting' is mandatory for lists in function declarations
Timezones = Literal[tuple(ALLOWED_TIMEZONES)]

class Fun(commands.Cog):

  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    
  ## eight ball, ask it a question and it will try to not be sarcastic
  @app_commands.command(name="8ball", description="Enter a question, and the 8ball will respond")
  async def eightBall(self, interaction: discord.Interaction, question: str):
    await interaction.response.send_message(f'Question: {question}\nAnswer: {random.choice(eightball)}', ephemeral=True)

  ## wise quote command, gets wise quotes from a API call to a website
  @app_commands.command(name="wise-quote", description="This finds a insightful/wise quote for you.")
  async def wiseQuote(self, interaction: discord.Interaction):
    response = requests.get('https://zenquotes.io/api/random')
    json_stuff = json.loads(response.text)
    quote = json_stuff[0]['q'] + ' -' + json_stuff[0]['a']
    await interaction.response.send_message(quote)

  ## random number generator
  @app_commands.command(name="random-number-generator", description="Takes two numbers and then finds a random number between (and including) them.")
  @app_commands.describe(minimum = "lowest number in the range for random selection.", maximum = "largest number in range for random selection.")
  async def randNum(self, interaction: discord.Interaction, minimum: int, maximum: int):
    if minimum > maximum:
      await interaction.response.send_message(f'Error: your minimum ({minimum}) is larger than your maximum ({maximum}).')
    else:
      await interaction.response.send_message(f'Random number: {random.randint(minimum, maximum)}')

  ## Time past since secret docs are leaked to War Thunder
  @app_commands.command(name="war-thunder-counter", description="Calculates how long it has been since secret documents are leaked on War Thunder")
  async def warThunderCounter(self, interaction: discord.Interaction):
    with open(os.path.join(file_location, 'picsAndFiles', 'war_thunder_date.txt'), "r") as file:
      stored_date_str = file.read().strip()

    stored_date = datetime.strptime(stored_date_str, "%Y-%m-%d %H:%M:%S")
    current_time = datetime.now()
    time_difference = current_time - stored_date

    await interaction.response.send_message(f"Day(s) since classified documents have been leaked in War Thunder Forums: {time_difference.days} days.")

  ## Reset the War Thunder Day Counter
  @app_commands.command(name="war-thunder-reset", description="Reset the War Thunder data leak counter")
  async def warThunderReset(self, interaction: discord.Interaction):
    current_time_formatted = (datetime.now()).strftime("%Y-%m-%d %H:%M:%S")

    with open(os.path.join(file_location, 'picsAndFiles', 'war_thunder_date.txt'), "w") as file:
      file.write(current_time_formatted)

    await interaction.response.send_message(file=discord.File(os.path.join(file_location, 'picsAndFiles', 'dayCounter.png')))

  # timezone calculator. https://mljar.com/blog/list-pytz-timezones/
  @app_commands.command(name="timezone-calc", description="Calculate what time it would be from one timezone to another")
  @app_commands.describe(initial_timezone = "The timezone you are converting from", target_timezone = "Timezone you're converting to", time = "The time being converted from initial to target (24 hour time). Ex: 12/31/2024 14:25")
  async def timeStone(self, interaction: discord.Interaction, initial_timezone: Timezones, target_timezone: Timezones, time: str):
            time_format = '%m/%d/%Y %H:%M'
            try:
                time_result = datetime.strptime(time, time_format)
                firstTZ = pytz.timezone(initial_timezone).localize(time_result)
                result = firstTZ.astimezone(pytz.timezone(target_timezone))
                await interaction.response.send_message(f"**{initial_timezone} > {target_timezone}:**\n{time} > {result}")
            except:
                await interaction.response.send_message("Error: Most likely you entered the date in the wrong format. Remember that it's 24 hour time, and to use slashes for the date and a colon (:) for the time!\nFormat example: 12/31/2003 14:25")
  
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Fun(bot))
