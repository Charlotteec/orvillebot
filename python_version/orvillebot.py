import discord
from discord.ext import commands
import random

def read_file(file):
    with open(file) as f:
        text = f.read()
    return text

description = '''He's literally just a little guy idk what to tell you'''

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', description=description, intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user} (ID: {bot.user.id})')
    print('------')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

def singsong():
    r = random.randrange(1, 12)
    text = read_file('assets/'+str(r)+'.txt')
    return text

@bot.command()
async def sing(ctx):
    song = singsong()
    await ctx.send(song)


token = read_file('config.txt')
#print(token)
bot.run(token)
