import discord
from discord.ext import commands
from discord.utils import get
import datetime
import time
import random
import json
import asyncio
import os
import webserver
from webserver import keep_alive
import aiohttp
from requests import get
from json import loads
import urllib.parse, urllib.request, re
import requests
import wikipedia
from youtubesearchpython import SearchVideos
from jikanpy import Jikan
from jikanpy.exceptions import APIException
from pokedex import pokedex


client = commands.Bot(command_prefix=commands.when_mentioned_or("<", '+'))
client.remove_command('help')


t = time.localtime()
now = datetime.datetime.now()
now_date = now.strftime("%c")
current_time = time.strftime("%H:%M:%S", t)


@client.event
async def on_ready():
  print('Logged in as {0} ({0.id})'.format(client.user))


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):  # fails silently
        pass
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
            description=f"Please pass in all requirements!",
            color=0xff0000)
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
            description=f"You don't have the required permissions",
            color=0xff0000)
        await ctx.send(embed=embed)
    if isinstance(error, commands.CommandOnCooldown):
        coold = str(time.strftime('%H:%M:%S', time.gmtime(error.retry_after)))
        embed = discord.Embed(
            description=f"**{ctx.author}** This command is on cooldown. Try again in {coold}",
            color=0xff0000)
        await ctx.send(embed=embed)


@client.command()
async def load(ctx, extension):
    client.load_extension(f"cogs.{extension}")
                                 
                                 
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
                                 
                            
@client.command()
async def reload(ctx, extension):
    client.unload_extension(f"cogs.{extension}")
    client.load_extension(f"cogs.{extension}")
                                 
  
for filename in os.listdir("./cogs"):
    if filename.endswith('.py'):
        client.load_extension(f"cogs.{filename[:-3]}")
        
        
@client.command()
async def help(ctx):
    await ctx.author.send(file=discord.File('categories.png'))
    await ctx.message.add_reaction('✔️')


@client.command()
async def utility(ctx):
    await ctx.author.send(file=discord.File('utility - 1.png'))
    await ctx.author.send(file=discord.File('utility - 2.png'))
    await ctx.message.add_reaction('✔️')


@client.command()
async def image(ctx):
    await ctx.author.send(file=discord.File('image.png'))
    await ctx.message.add_reaction('✔️')


@client.command()
async def search(ctx):
    await ctx.author.send(file=discord.File('search.png'))
    await ctx.message.add_reaction('✔️')


@client.command()
async def history(ctx):
    await ctx.author.send(file=discord.File('history.png'))
    await ctx.message.add_reaction('✔️')


@client.command()
async def animanga(ctx):
    await ctx.author.send(file=discord.File('animanga.png'))
    await ctx.message.add_reaction('✔️')


@client.command()
async def economy(ctx):
    await ctx.author.send(file=discord.File('eco - 1.png'))
    await ctx.author.send(file=discord.File('eco - 2.png'))
    await ctx.message.add_reaction('✔️')
    
    
@client.command()
async def fun(ctx):
    await ctx.author.send(file=discord.File('fun.png'))
    await ctx.message.add_reaction('✔️')



@client.command()
async def ping(ctx):
    await ctx.send(f"Ping is {round(client.latency * 1000)}ms!")
    
    

@client.command()
async def today(ctx, choice=None):

    URL = 'http://history.muffinlabs.com/date'

    response = requests.request('GET', URL).json()

    if choice == "events":
        events = response['data']['Events']

        rand_event = events[random.randrange(0, len(events))]

        em = discord.Embed(color=0xfffb7a)

        em.add_field(name=f"{rand_event['year']} — {rand_event['text']}", value=f"{rand_event['links'][0]['link']}")

        await ctx.send(embed=em)

    elif choice == "births":
        births = response['data']['Births']

        rand_event = births[random.randrange(0, len(births))]

        em = discord.Embed(color=0xfffb7a)

        em.add_field(name=f"{rand_event['year']} — {rand_event['text']}", value=f"{rand_event['links'][0]['link']}")

        await ctx.send(embed=em)

    elif choice == "deaths":
        deaths = response['data']['Deaths']

        rand_event = deaths[random.randrange(0, len(deaths))]

        em = discord.Embed(color=0xfffb7a)

        em.add_field(name=f"{rand_event['year']} — {rand_event['text']}", value=f"{rand_event['links'][0]['link']}")

        await ctx.send(embed=em)

    elif choice == None:
        await ctx.send(f"Options: Events, Births, Deaths")

    else:
        await ctx.send(f"Options: Events, Births, Deaths")


@client.command(aliases=['ht'])
async def historytoday(ctx, choice=None):

    URL = 'http://history.muffinlabs.com/date'

    response = requests.request('GET', URL).json()

    # Events

    events = response['data']['Events']

    rand_event = events[random.randrange(0, len(events))]

    # Births

    births = response['data']['Births']

    rand_birth = births[random.randrange(0, len(births))]

    # Deaths

    deaths = response['data']['Deaths']

    rand_deaths = deaths[random.randrange(0, len(deaths))]

    em = discord.Embed(color=0x8fff93)

    em.add_field(name=f"•  Events: {rand_event['year']} — {rand_event['text']}", value=f"{rand_event['links'][0]['link']}", inline=False)
    em.add_field(name=f"•  Births: {rand_birth['year']} — {rand_birth['text']}", value=f"{rand_birth['links'][0]['link']}", inline=False)
    em.add_field(name=f"•  Deaths: {rand_deaths['year']} — {rand_deaths['text']}", value=f"{rand_deaths['links'][0]['link']}", inline=False)

    await ctx.send(embed=em)
    
    
    
keep_alive()

client.run(TOKEN)

    
