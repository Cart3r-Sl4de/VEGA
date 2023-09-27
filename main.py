import discord, os, random
from discord import app_commands
from discord.ext import commands

## lists for emoji reaction compositions
fricc = ["🇫", "🇷", "🇮", "🇨", "🇰"]
dang = ["🇩", "🇦", "🇳", "🇬"]
## lists of words to detect
superior_words = ["frick", "fricc", "dang"]
karEnTuk = ["rip and tear", "kar en tuk"]
cipher = ["dorito", "bill", "cipher"]
## lists of responses
affirming_emojis = ["👌", "👍", "<:ThanosFingerguns:749486523669413908>"]
rockin_stone = [
    "Rock on!", "Rock and Stone... Yeeaaahhh!", "Rock and Stone forever!",
    "ROCK... AND... STONE!", "Rock and Stone!", "For Rock and Stone!",
    "We are unbreakable!", "Rock and roll!", "Rock and roll and stone!",
    "That's it lads! Rock and Stone!", "Like that! Rock and Stone!",
    "Yeaahhh! Rock and Stone!", "None can stand before us!", "Rock solid!",
    "Stone and Rock! ...Oh, wait...", "Come on guys! Rock and Stone!",
    "If you don't Rock and Stone, you ain't comin' home!",
    "We fight for Rock and Stone!", "We rock!", "Rock and Stone everyone!",
    "Yeah, yeah, Rock and Stone.", "Rock and Stone in the Heart!",
    "For Teamwork!", "Did I hear a Rock and Stone!", "Rock and Stone!",
    "Rock and Stone, Brother!", "Rock and Stone to the Bone!", "For Karl!",
    "Leave no Dwarf behind!", "By the Beard!"
]

## add the cogs to the program automagically
async def setup_hook(self):
    for filename in os.listdir('./vegaCore'):
        if filename.endswith('.py'):
            await client.load_extension(f'vegaCore.{filename[:-3]}')

## It's a healthy habit not to have one's API keys visible on github
file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'chuckie_cheese.token')
with open(file_path, 'r') as file:
    chuckie_cheese = file.readline().strip()

## my intentions are pure
## declare the bot/client here as well as the intentions
intents = discord.Intents.all()
intents.message_content = True
#activity = discord.Game('with Fate'),
client = commands.Bot(command_prefix=">", intents=intents, activity=discord.Game('with Destiny'), status=discord.Status.do_not_disturb)

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
    message_lowered = (message.content).lower()
    ## if someone writes f in chat, react with f in chat
    if message_lowered == 'f':
        await message.add_reaction("🇫")

    ## in the event someone says a naughty word
    if "fuck" in message_lowered:
        for emoji in fricc:
            await message.add_reaction(emoji)

    if "damn" in message_lowered:
        for emoji in dang:
            await message.add_reaction(emoji)

    ## in the event someone says a superior word
    if any(word in message_lowered for word in superior_words):
        await message.channel.send(random.choice(affirming_emojis))

    if "rock and stone" in message_lowered:
        await message.channel.send(random.choice(rockin_stone))
        await message.channel.send("⛏️")
        


## --> commands

## test command
@client.tree.command(name = "test")
async def test(interaction: discord.Interaction):
    await interaction.response.send_message(f'{interaction.user.mention} has summoned the angry one')

@client.tree.command(name = "ping")
async def ping(interaction: discord.Interaction):
    await interaction.response.send_message(f'Latency is: {round(client.latency * 1000)}ms')


## actually run the bot
client.run(chuckie_cheese)