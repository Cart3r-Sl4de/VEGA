import discord, os
from discord import app_commands
from discord.ext import commands

## It's a healthy habit not to have one's API keys visible on github
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chuckie_cheese.token')

with open(file_path, 'r') as file:
    chuckie_cheese = file.readline().strip()

## my intentions are pure
intents = discord.Intents.all()
intents.message_content = True

## The bot/client itself
client = commands.Bot(command_prefix=">", intents=intents)

## --> events
@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))
    try:
        synced = await client.tree.sync()
        print(f'Commands synced: {len(synced)}')
    except Exception as e:
        print(f'Ran into error: {e}')
    print('This is Gold Leader, standing by!')

## when someone sends a message, see which of these applies
@client.event
async def on_message(message):
    ## if someone writes f in chat, react with f in chat
    if (message.content).lower() == "f":
        await message.add_reaction("🇫")


## --> commands

## test command
@client.tree.command(name="test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention} has summoned the angry one')


## actually run the bot
client.run(chuckie_cheese)