import discord, os, requests
from discord.ext import commands
from discord.ext.commands import bot
from config import TOKEN
from eco_list import eco_list

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')
    
@bot.command()
async def ping(ctx: commands.Context):
    await ctx.send('Pong!')
    
@bot.command() 
async def hello(ctx): 
    author = ctx.message.author 
    await ctx.send(f'Привет, {author.mention}!  ⸜(｡˃ ᵕ ˂ )⸝♡') 

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command()
async def duck(ctx):
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def eco(ctx: commands.Context):
    random_advice = random.choice(eco_list)
    await ctx.send(random_advice)   
    
bot.run(TOKEN)
