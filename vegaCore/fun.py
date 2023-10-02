import discord, os, asyncio, random, requests, json
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import has_permissions

np = [
  "Glad I could be of service",
  "Got your back",
  "👌"
  ]

thanks = ["Thanks, VEGA", "thanks vega", "thanks, vega", "thanks VEGA"]

eightball = ["It is certain.", "It is decidedly so.", "Without a doubt.", "Yes - definitely.", "You may rely on it.", "As I see it, yes.", "Most likely.", "Outlook good.", "Yes.", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]


class Fun(commands.Cog):

  def __init__(self, bot: commands.Bot) -> None:
    self.bot = bot
    
  #eight ball
  @app_commands.command(name="8ball")
  async def eightball(self, interaction: discord.Interaction, question: str):
    await interaction.response.send_message(f'Question: {question}\nAnswer: {random.choice(eightball)}', ephemeral=True)
  
async def setup(bot: commands.Bot) -> None:
  await bot.add_cog(Fun(bot))