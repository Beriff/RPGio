import discord
import game
from discord.utils import get
from discord.ext import commands

client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('-help'))
    print('[RPGIO] Bot ready to use')

print('[RPGIO] Starting discord client...')
client.run('TOKEN')

if input() == 'leave':
    client.close()
