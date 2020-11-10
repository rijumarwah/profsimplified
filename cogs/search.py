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


def check(author):
    def inner_check(message):
        return message.author == author
    return inner_check


my_api_key = ""
my_cse_id = ""


def google_search(search_term, api_key, cse_id, **kwargs):
    service = build("customsearch", "v1", developerKey=api_key)
    res = service.cse().list(q=search_term, cx=cse_id, **kwargs).execute()
    return res


class Search(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command(aliases=['wikipedia'])
    async def wiki(self, ctx, *, arg):
        result = wikipedia.search(arg)

        em = discord.Embed()

        em.add_field(name="Choose one of the following", value=f"```[1] {result[0]}\n[2] {result[1]}\n[3] {result[2]}\n[4] {result[3]}\n[5] {result[4]}\n\n```")

        await ctx.send(embed=em)

        ida = await client.wait_for('message', check=check(ctx.author), timeout=40)

        ids = ida.content

        if ids == "1":
            choice = 0
        elif ids == "2":
            choice = 1
        elif ids == "3":
            choice = 2
        elif ids == "4":
            choice = 3
        elif ids == "5":
            choice = 4
        else:
            await ctx.send(f"Invalid choice, try again")

        page = wikipedia.page(result[choice])

        summary = page.summary

        if len(summary) > 1500:
            sum = summary[:1500] + "..."

        emb = discord.Embed(
            title=f"{page.title}", description=f"{sum}"
            )

        await ctx.send(embed=emb)


    @commands.command()
    async def google(self, ctx, *args):
        try:
            query = " ".join(args)

            result = google_search(query, my_api_key, my_cse_id)

            res_final = result['items'][0]

            title = res_final['title']
            link = res_final['link']

            await ctx.send(f"**{title} - Requested by {ctx.author}**\n<{link}>")

        except:
            em = discord.Embed(description=f"An error occured", color=0xb3d4ff)
            await ctx.send(embed=em)


    @commands.command(aliases=['ms'])
    async def multisearch(self, ctx, *args):
        ch = await access_check(ctx, "ms")

        if ch:
            try:
                query = " ".join(args)

                result = google_search(query, my_api_key, my_cse_id)

                await ctx.send(
                    f"Search Results for **'{query}'**:\n<{result['items'][0]['link']}>\n<{result['items'][1]['link']}>\n<{result['items'][2]['link']}>")

            except:
                em = discord.Embed(description=f"An error occured", color=0xb3d4ff)
                await ctx.send(embed=em)
        else:
            await ctx.send(f"**{ctx.author}** This command is disabled")


    @commands.command(aliases=['news'])
    async def bbc(self, ctx):
        main_url = ""

        open_bbc_page = requests.get(main_url).json()

        article = open_bbc_page["articles"]

        results = []
        desc = []

        for ar in article:
            results.append(ar["title"])

        for de in article:
            desc.append(de["url"])

        em = discord.Embed(title="BBC News Daily", description=f"{now_date}", color=0xe0c5ff)
        em.set_footer(text=f"Source: BBC News")
        for i in range(len(results)):
            em.add_field(name=f"{results[i]}", value=f"{desc[i]}‎", inline=False)

        await ctx.send(embed=em)


    @commands.command(aliases=['covid19', 'corona', 'coronavirus'])
    async def covid(self, ctx, *query):
        query = " ".join(query)

        try:
            url = ""

            querystring = {"format": "json", "name": query}

            headers = {
                'x-host': "",
                'x-key': ""
            }

            response = requests.request("GET", url, headers=headers, params=querystring)

            data = response.json()

            country = data[0]['code'].lower()

            em = discord.Embed(
                title=f"{data[0]['country']} ({data[0]['code']})", color=0xff0059
            )

            em.set_image(url="https://i.imgur.com/cusC1A7.png")
            em.add_field(name=f"Confirmed", value=f"{data[0]['confirmed']}")
            em.add_field(name=f"Recovered", value=f"{data[0]['recovered']}")
            em.add_field(name=f"Critical", value=f"{data[0]['critical']}")
            em.add_field(name=f"Deaths", value=f"{data[0]['deaths']}")
            em.add_field(name=f"Last Update", value=f"{data[0]['lastUpdate']}")
            em.set_thumbnail(url=f"https://flagcdn.com/w320/{country}.png")

            await ctx.send(embed=em)

        except:
            embed = discord.Embed(
                description=f"**{ctx.author}** Something went wrong, try again with a different name",
                color=0xff0000)
            await ctx.send(embed=embed)


    @commands.command()
    async def urban(self, ctx, *word: str):
        ch = await access_check(ctx, "urban")
        if ch:
            if ctx.channel.is_nsfw():

                try:
                    word_a = str(word)

                    word_r = word_a.replace(" ", "+")

                    url = 'http://api.urbandictionary.com/v0/define?term=' + word_r

                    x = requests.get(url)

                    resp = x.json()

                    defin = resp['list'][0]['definition']

                    a = defin.translate({ord('['): None})
                    final_def = a.translate({ord(']'): None})

                    em = discord.Embed(title=f"Urban Dictionary - {resp['list'][0]['word']}",
                                    url=f"{resp['list'][0]['permalink']}",

                                    description=f"{final_def}", color=0xb3d4ff

                                    )

                    em.set_footer(text=f"Requested by {ctx.author}")
                    await ctx.send(embed=em)

                except:
                    em = discord.Embed(
                        description=f"Unable to find definition for the word", color=0xb3d4ff
                    )

                    await ctx.send(embed=em)

            else:
                em = discord.Embed(
                    description=f"Command restricted to NSFW channels", color=0xb3d4ff
                )

                await ctx.send(embed=em)

        else:
            await ctx.send(f"**{ctx.author}** This command is disabled")



def setup(client):
    client.add_cog(Search(client))
