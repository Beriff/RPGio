import discord
import game
from discord.utils import get
from discord.ext import commands

instance_table = {}

client = commands.Bot(command_prefix='-')

def renderRoom(room):
    printable = room
    #for i in range(1, len(room)):
    #    printable.insert(i, '\n')
    return printable


@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.online, activity=discord.Game('-help'))
    print('[RPGIO] Bot ready to use')

@client.command()
async def init(ctx):
    newPlr = game.Player(ctx.author.name, ':flushed:')
    newGame = game.Game(newPlr)
    instance_table[ctx.author.name] = newGame

@client.command()
async def enter(ctx):
    dungeon_name = instance_table[ctx.author.name].enterDungeon()    
    print(renderRoom(instance_table[ctx.author.name].current_room))
    await ctx.send(f'you enter {dungeon_name[0]} dungeon!\n {renderRoom(instance_table[ctx.author.name].current_room)}')

@client.command()
async def right(ctx):
    await ctx.send(renderRoom(instance_table[ctx.author.name].listenRender('right')))
    

print('[RPGIO] Starting discord client...')
client.run('NzY5ODE3MDI5NTk0NzEwMDM3.X5Uh-g.SnH4Ws5C5h_GEqe31Lg1tixwiMA')
