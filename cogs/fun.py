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


class Fun(commands.Cog):

    def __init__(self, client):
        self.client = client


    @commands.command()
    async def motivate(self, ctx):
        response = get('')
        await ctx.send('{quoteText} - {quoteAuthor}'.format(**loads(response.text)))


    @commands.command(aliases=['meme', 'dankmemes'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def memes(self, ctx):
        url = f""

        headers = {
            'Authorization': '',
        }

        para = {
            'remove_nsfw': True,
            'span': 'week',
        }

        response = requests.request("GET", url, headers=headers, params=para).json()

        try:
            em = discord.Embed(title=f"{response['title']}", url=f"{response['source']}", color=discord.Colour.gold()

                            )

            em.set_image(url=f"{response['image_url']}")

            em.set_footer(text=f"{response['upvotes']} 👍 ・ {response['author']}")

            await ctx.send(embed=em)

        except:
            embed = discord.Embed(
                description=f"**{ctx.author}** an error occured",
                color=0xff0000)
            await ctx.send(embed=embed)


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def aww(self, ctx):
        url = ""

        headers = {
            'Authorization': '',
        }

        response = requests.request("GET", url, headers=headers)

        im = response.json()

        em = discord.Embed(title=f"{im['title']}", colour=discord.Colour.gold())
        em.set_image(url=f"{im['image_url']}")
        em.set_footer(text=f"{im['upvotes']} Upvotes ・ {im['author']}")

        await ctx.send(embed=em)


    @commands.command(aliases=['reddit', 'sr'])
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def sreddit(self, ctx, sub):
        url = f"/{sub}"

        headers = {
            'Authorization': '',
        }

        para = {
            'remove_nsfw': True,
            'span': 'week',
        }

        response = requests.request("GET", url, headers=headers, params=para).json()

        try:
            em = discord.Embed(title=f"{response['title']}", url=f"{response['source']}", color=discord.Colour.gold()

                            )

            em.set_image(url=f"{response['image_url']}")

            em.set_footer(text=f"{response['upvotes']} Upvotes ・ {response['author']}")

            await ctx.send(embed=em)

        except:
            embed = discord.Embed(
                description=f"**{ctx.author}** Unable to get posts, make sure the subreddit exists and it isn't NSFW",
                color=0xff0000)
            await ctx.send(embed=embed)


    @commands.command(aliases=['simp'])
    async def simprate(self, ctx, member: discord.Member = None):
        eighty = [
            'YOOOOOOOO',
            'Shit bro',
            'Calm down',
            'Lmao simp',
            'STOP RIGHT THERE',
            'UNACCEPTABLE',
            'Chill dude',
            'S I M P'
        ]

        fifty = [
            'Damn simp',
            'Stop',
            'Bruh, simp',
            'Understandable',
        ]

        twenty = [
            'Still less',
            'Lol simp',
            "You're still a simp",
            'Kid',
        ]

        zero = [
            'Pass',
            'Not simp looks like',
            'Cool',
            "You're cool",
        ]

        perc = random.randrange(0, 101)
        if member == None:
            if perc >= 80:
                embed = discord.Embed(description=f"{ctx.author.mention} is **{perc}%** simp ― {random.choice(eighty)}",
                                    color=0xe0c5ff)
                await ctx.send(embed=embed)

            elif perc >= 50:
                embed = discord.Embed(description=f"{ctx.author.mention} is **{perc}%** simp ― {random.choice(fifty)}",
                                    color=0xe0c5ff)
                await ctx.send(embed=embed)

            elif perc >= 20:
                embed = discord.Embed(description=f"{ctx.author.mention} is **{perc}%** simp ― {random.choice(twenty)}",
                                    color=0xe0c5ff)
                await ctx.send(embed=embed)

            elif perc >= 0:
                embed = discord.Embed(description=f"{ctx.author.mention} is **{perc}%** simp ― {random.choice(zero)}",
                                    color=0xe0c5ff)
                await ctx.send(embed=embed)

        else:
            if perc >= 80:
                embed = discord.Embed(description=f"{member.mention} is **{perc}%** simp ― {random.choice(eighty)}",
                                    color=0xe0c5ff)
                await ctx.send(embed=embed)

            elif perc >= 50:
                embed = discord.Embed(description=f"{member.mention} is **{perc}%** simp ― {random.choice(fifty)}",
                                    color=0xe0c5ff)
                await ctx.send(embed=embed)

            elif perc >= 20:
                embed = discord.Embed(description=f"{member.mention} is **{perc}%** simp ― {random.choice(twenty)}",
                                    color=0xe0c5ff)
                await ctx.send(embed=embed)

            elif perc >= 0:
                embed = discord.Embed(description=f"{member.mention} is **{perc}%** simp ― {random.choice(zero)}",
                                    color=0xe0c5ff)
                await ctx.send(embed=embed)


    @commands.command(aliases=['kitty', 'pussy', 'meow', 'kitten'])
    async def cat(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Here's a cat! :cat:", color=0xe0c5ff)
                    embed.set_image(url=data['file'])

                    await ctx.send(embed=embed)


    @commands.command(aliases=['puppy', 'doggo', 'bark'])
    async def dog(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Here's a dog! :dog:", color=0xe0c5ff)
                    embed.set_image(url=data['url'])

                    await ctx.send(embed=embed)


    @commands.command()
    async def fox(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("") as r:
                    data = await r.json()

                    embed = discord.Embed(title="Fox :fox:", color=0xe0c5ff)
                    embed.set_image(url=data['image'])

                    await ctx.send(embed=embed)


    @commands.command()
    async def trump(self, ctx, member: discord.Member = None):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("") as r:
                    data = await r.json()

                    trump_response_p = data['messages']['personalized']
                    trump_response_n = data['messages']["non_personalized"]

                    if member == None:
                        await ctx.send(f"Trump: {random.choice(trump_response_n)}")

                    else:
                        await ctx.send(f"Trump thinks {member.mention} {random.choice(trump_response_p)}")


    @commands.command()
    async def rps(self, ctx, arg):
        rpschoice = [
            "rock",
            "paper",
            "scissors",
        ]
        choicebot = random.choice(rpschoice)

        await ctx.send(f"I chose: {choicebot}")

        if arg == "r" or arg == "rock":
            if choicebot == "rock":
                await ctx.send("Tie!")
            elif choicebot == "paper":
                await ctx.send(f"I win!")
            else:
                await ctx.send(f"You win!")
        elif arg == "p" or arg == "paper":
            if choicebot == "rock":
                await ctx.send("You win!")
            elif choicebot == "paper":
                await ctx.send(f"Tie")
            else:
                await ctx.send(f"I win!")
        elif arg == "s" or arg == "scissors":
            if choicebot == "rock":
                await ctx.send("I win!")
            elif choicebot == "paper":
                await ctx.send(f"You win!")
            else:
                await ctx.send(f"Tie!")
        else:
            await ctx.send(f"Invalid choice!")



    @commands.command(aliases=['uf', 'useless'])
    async def uselessfact(self, ctx):
        url = ''

        x = requests.get(url)

        resp = x.json()

        embed = discord.Embed(description=f"{resp['text']}", color=0xffee00)

        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(Fun(client))
