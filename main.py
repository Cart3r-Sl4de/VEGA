import discord, os
from discord import app_commands
from discord.ext import commands

file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chuckie_cheese.token')

with open(file_path, 'r') as file:
    chuckie_cheese = file.readline().strip()

intents = discord.Intents.all()
intents.message_content = True

bot = commands.Bot(command_prefix=">", intents=intents)

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    try:
        synced = await bot.tree.sync()
        print(f'The commands {len(synced)} are synced')
    except Exception as e:
        print(f'Ran into error: {e}')
    print('This is Gold Leader, standing by!')

@bot.event
async def on_message(message):
    if message.content == "F" or message.content == "f":
        await message.add_reaction("🇫")

@bot.tree.command(name="test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention} has summoned the angry one')



bot.run(chuckie_cheese)