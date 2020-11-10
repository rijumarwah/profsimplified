import discord
from discord.ext import commands
from discord.utils import get
import datetime
import time
import random
import json
import asyncio
import os
import aiohttp
from requests import get
from json import loads
import urllib.parse, urllib.request, re
import requests


class History(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def today(self, ctx, choice=None):
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

    
    @commands.command(aliases=['ht'])
    async def historytoday(self, ctx, choice=None):
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

        em.add_field(name=f"•  Events: {rand_event['year']} — {rand_event['text']}",
                    value=f"{rand_event['links'][0]['link']}", inline=False)
        em.add_field(name=f"•  Births: {rand_birth['year']} — {rand_birth['text']}",
                    value=f"{rand_birth['links'][0]['link']}", inline=False)
        em.add_field(name=f"•  Deaths: {rand_deaths['year']} — {rand_deaths['text']}",
                    value=f"{rand_deaths['links'][0]['link']}", inline=False)

        await ctx.send(embed=em)



def setup(client):
    client.add_cog(History(client))
