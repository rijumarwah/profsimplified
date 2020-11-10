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
    @commands.has_permissions(administrator=True)
    async def say(self, ctx, *args):
        await ctx.send(' '.join(args), tts=True)


    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clear(self, ctx, arg: int):
        await ctx.channel.purge(limit=arg + 1)
        msg = await ctx.send(f"Deleted the last `{arg} messages` <a:ok_hand:730116758433693746>")
        await asyncio.sleep(2)
        await msg.delete()


    @commands.command(aliases=['sm', 'slowmo', 'slow'])
    @commands.has_permissions(manage_messages=True)
    async def slowmode(self, ctx, seconds):
        try:
            if seconds == "off":
                await ctx.channel.edit(slowmode_delay=0)
                em = discord.Embed(
                    description=f"**Slowmode has been removed**",
                    color=0xe0c5ff
                )

                await ctx.send(embed=em)
            else:
                seconds_i = int(seconds)
                await ctx.channel.edit(slowmode_delay=seconds_i)
                em = discord.Embed(
                    description=f"This channel is now on slowmode, **members can type once in every {seconds} seconds**",
                    color=0xe0c5ff
                )

                await ctx.send(embed=em)

        except:
            em = discord.Embed(
                description=f"**Usage Example - <slowmode 30  |  <slowmode off**", color=0xe0c5ff
            )

            await ctx.send(embed=em)


    @commands.command(aliases=['av'])
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def avatar(self, ctx, member: discord.Member):
        embed = discord.Embed(description=f"{member.mention} — [URL]({member.avatar_url})", color=0xe0c5ff)
        embed.set_image(url=member.avatar_url)
        await ctx.send(embed=embed)


    @commands.command()
    async def userinfo(self, ctx, member: discord.Member):
        roles = [role for role in member.roles]

        embed = discord.Embed(colour=member.color, timestamp=ctx.message.created_at)

        embed.set_author(name=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

        embed.add_field(name="ID: ", value=member.id)
        embed.add_field(name="Guild name: ", value=member.display_name)

        embed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]))
        embed.add_field(name="Top role: ", value=member.top_role.mention)

        embed.add_field(name="Bot", value=member.bot)

        await ctx.send(embed=embed)


    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question):
        responses = ['Absolutely.',
                    'Definitely not.',
                    'It is certain.',
                    'Not at all.',
                    'My sources say no',
                    'Not sure',
                    'Yeah',
                    'Very doubtful',
                    "Don't count on it",
                    'Outlook not so good',
                    "That's a no",
                    'Most likely',
                    'Without a doubt',
                    'As I see it, yes',
                    'Yup',
                    'Yeah lol',
                    "Lmao yeah",
                    'Why not',
                    "Yes, but actually no.",
                    "Yes and no.",
                    "No",
                    "Nah",
                    "Sure",
                    ]
        await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


    @commands.command(aliases=['youtube', 'video'])
    async def yt(self, ctx, *args):
        ch = await access_check(ctx, "yt")
        if ch:
            query = " ".join(args)

            search = SearchVideos(f"{query}", offset=1, mode="dict", max_results=1)

            search = search.result()

            await ctx.send(search['search_result'][0]['link'])
        else:
            await ctx.send(f"**{ctx.author}** This command is disabled")


    @commands.command()
    async def choose(self, ctx, *choices):
        string = " ".join(choices)

        string = string.split(';')

        await ctx.send(f"{ctx.author.mention} I would choose: {random.choice(string)}")


    @commands.command()
    async def remind(self, ctx, arg: int, *args):
        await ctx.message.delete()
        await ctx.send(f"Ok, I will remind you in {arg} minutes.")
        await asyncio.sleep(arg * 60)
        await ctx.author.send(' '.join(args), tts=True)


    @commands.command(pass_context=True)
    async def flip(self, ctx):
        flip = ['https://i.imgur.com/OqFNJO7.png',
                'https://i.imgur.com/DarGk5i.png', ]
        embed = discord.Embed(
            title='Heads and tails',
            colour=discord.Colour.from_rgb(233, 30, 99)

        )

        embed.set_image(url=f'{random.choice(flip)}')

        await ctx.send(embed=embed)


    @commands.command(aliases=['roll'])
    async def dice(self, ctx):
        roll = [
            "You rolled `1`!",
            "You rolled `2`!",
            "You rolled `3`!",
            "You rolled `4`!",
            "You rolled `5`!",
            "You rolled `6`!",
        ]
        await ctx.send(f"{random.choice(roll)}")


    @commands.command()
    async def weather(self, ctx, *args):
        try:
            query = " ".join(args)

            querya = query.replace(" ", "+")

            api_address = ''

            url = api_address + querya

            json_data = requests.get(url).json()

            weather_t = json_data['weather'][0]['main']

            temp = json_data['main']['temp']

            temp_c = (int(temp) - 273.15)

            temp_f = (temp_c * 9 / 5) + 32

            windspeed = json_data['wind']['speed']

            feels_like = json_data['main']['feels_like']

            temp_min = json_data['main']['temp_min']
            temp_min_c = (int(temp_min) - 273.15)

            temp_max = json_data['main']['temp_max']
            temp_max_c = (int(temp_max) - 273.15)

            pressure = json_data['main']['pressure']

            humidity = json_data['main']['humidity']

            loc_c = json_data['sys']['country']

            loc_p = json_data['name']

            visibility = json_data['visibility']

            lat = json_data['coord']['lat']

            lon = json_data['coord']['lon']

            embed = discord.Embed(
                colour=discord.Colour.from_rgb(233, 30, 99)

            )

            embed.add_field(name=":earth_africa: Location", value=f"{loc_p}, {loc_c}",
                            inline=True)
            embed.add_field(name=':cloud: Weather', value=f"{weather_t}",
                            inline=True)
            embed.add_field(name=':sweat: Humidity',
                            value=f"{humidity}%",
                            inline=True)
            embed.add_field(name=":thermometer: Temperature", value=f"{round(temp_f, 2)}°F/{round(temp_c, 2)}°C",
                            inline=True)
            embed.add_field(name=':dash: Wind Speed',
                            value=f"{windspeed}mph",
                            inline=True)
            embed.add_field(name=":eyes: Visibility",
                            value=f"{visibility}m",
                            inline=True)
            embed.add_field(name=":straight_ruler: Lat/Long",
                            value=f"{lat}/{lon}",
                            inline=True)
            embed.add_field(name=":high_brightness: Min/Max",
                            value=f"{round(temp_min_c, 1)}°C/{round(temp_max_c, 1)}°C",
                            inline=True)
            embed.add_field(name=":anger: Pressure",
                            value=f"{pressure}hPa",
                            inline=True)

            embed.set_footer(text="Powered by openweathermap.org")

            await ctx.send(embed=embed)

        except:
            em = discord.Embed(
                description="Location not found", color=0xff0000
            )

            await ctx.send(embed=em)


    @commands.command(alisases=['dadjokes', 'dad'])
    async def dadjoke(self, ctx]):
        url = ''

        x = requests.get(url)

        resp = x.json()

        embed = discord.Embed(color=0xffee00)
        embed.add_field(name=f"{resp['setup']}", value=f"{resp['punchline']}")

        await ctx.send(embed=embed)





def setup(client):
    client.add_cog(History(client))
