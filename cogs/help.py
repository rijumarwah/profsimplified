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
from discord.ext.commands import Bot, guild_only
from disputils import BotEmbedPaginator


class Help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def help(self, ctx):

        embed = discord.Embed(
            color=0xb3d4ff, description=f"My prefix is `+`\n\nUse +cmd (command) to get help with a specific command\nReact to this message to view the other help pages"
        )
        embed.set_author(name="Professor Simplified Help", icon_url='https://i.imgur.com/djv68d4.png')
        embed.set_thumbnail(url="https://i.imgur.com/aTZOb2O.gif")
        embed.set_footer(text="Page 1/8 — React to view other pages")

        embeda = discord.Embed(
            color=0xb3d4ff

        )

        embeda.set_author(name="Utility Commands — 1", icon_url='https://i.imgur.com/djv68d4.png')
        embeda.set_thumbnail(url="https://i.imgur.com/aTZOb2O.gif")
        embeda.add_field(name='<a:motion1:759765518369947658> +ping', value='Bot latency')
        embeda.add_field(name='<a:motion1:759765518369947658> +wiki', value='Wiki Search')
        embeda.add_field(name='<a:motion1:759765518369947658> +expand', value='Expand Emote')
        embeda.add_field(name='<a:motion1:759765518369947658> +google', value='Google Search')
        embeda.add_field(name='<a:motion1:759765518369947658> +ms', value='Multi Search')
        embeda.add_field(name='<a:motion1:759765518369947658> +bbc', value='BBC News')
        embeda.add_field(name='<a:motion1:759765518369947658> +covid', value='Covid Stats')
        embeda.add_field(name='<a:motion1:759765518369947658> +urban', value='Urban Dict')
        embeda.add_field(name='<a:motion1:759765518369947658> +yt', value='YouTube Search')
        embeda.set_footer(text="Page 2/8 — React to view other pages")

        embedb = discord.Embed(
            color=0xb3d4ff

        )

        embedb.set_author(name="Utility Commands — 2", icon_url='https://i.imgur.com/djv68d4.png')
        embedb.set_thumbnail(url="https://i.imgur.com/aTZOb2O.gif")
        embedb.add_field(name='<a:motion1:759765518369947658> +say', value='Bot messages')
        embedb.add_field(name='<a:motion1:759765518369947658> +clear', value='Purge Chat')
        embedb.add_field(name='<a:motion1:759765518369947658> +slowmode', value='Slowmode')
        embedb.add_field(name='<a:motion1:759765518369947658> +avatar', value='User avatar')
        embedb.add_field(name='<a:motion1:759765518369947658> +userinfo', value='User info')
        embedb.add_field(name='<a:motion1:759765518369947658> +timer', value='Set Timer')
        embedb.add_field(name='<a:motion1:759765518369947658> +choose', value='Bot chooses')
        embedb.add_field(name='<a:motion1:759765518369947658> +remind', value='Se Reminder')
        embedb.add_field(name='<a:motion1:759765518369947658> +flip', value='Flip Coin')
        embedb.set_footer(text="Page 3/8 — React to view other pages")

        embedc = discord.Embed(
            color=0xb3d4ff

        )

        embedc.set_author(name="Fun Commands — 3", icon_url='https://i.imgur.com/djv68d4.png')
        embedc.set_thumbnail(url="https://i.imgur.com/aTZOb2O.gif")
        embedc.add_field(name='<a:motion1:759765518369947658> +dice', value='Roll dice')
        embedc.add_field(name='<a:motion1:759765518369947658> +weather', value='Weather')
        embedc.add_field(name='<a:motion1:759765518369947658> +reddit', value='Reddit Posts')
        embedc.add_field(name='<a:motion1:759765518369947658> +translate', value='Translate')
        embedc.add_field(name='<a:motion1:759765518369947658> +movie', value='Movie Search')

        embedc.set_footer(text="Page 4/8 — React to view other pages")

        embedd = discord.Embed(
            color=0xb3d4ff

        )

        embedd.set_author(name="History Commands — 1", icon_url='https://i.imgur.com/djv68d4.png')
        embedd.set_thumbnail(url="https://i.imgur.com/aTZOb2O.gif")
        embedd.add_field(name='<a:motion1:759765518369947658> +today', value='Specific Event')
        embedd.add_field(name='<a:motion1:759765518369947658> +ht', value='Events today')
        embedd.add_field(name='<a:motion1:759765518369947658> +wiki', value='Wiki Search')

        embedd.set_footer(text="Page 5/8 — React to view other pages")

        embede = discord.Embed(
            color=0xb3d4ff

        )

        embede.set_author(name="Fun Commands — 1", icon_url='https://i.imgur.com/djv68d4.png')
        embede.set_thumbnail(url="https://i.imgur.com/aTZOb2O.gif")
        embede.add_field(name='<a:motion1:759765518369947658> +urban', value='Urban Dict')
        embede.add_field(name='<a:motion1:759765518369947658> +8ball', value='Ask questions')
        embede.add_field(name='<a:motion1:759765518369947658> +dadjoke', value='Lame jokes')
        embede.add_field(name='<a:motion1:759765518369947658> +motivate', value='Motivation')
        embede.add_field(name='<a:motion1:759765518369947658> +memes', value='Dank memes')
        embede.add_field(name='<a:motion1:759765518369947658> +aww', value='Cute pictures')
        embede.add_field(name='<a:motion1:759765518369947658> +reddit', value='Reddit Search')
        embede.add_field(name='<a:motion1:759765518369947658> +simprate', value='Simp rate')
        embede.add_field(name='<a:motion1:759765518369947658> +uselessfact', value='Useless facts')

        embede.set_footer(text="Page 6/8 — React to view other pages")

        embedf = discord.Embed(
            color=0xb3d4ff

        )

        embedf.set_author(name="Fun Commands — 2", icon_url='https://i.imgur.com/djv68d4.png')
        embedf.set_thumbnail(url="https://i.imgur.com/aTZOb2O.gif")
        embedf.add_field(name='<a:motion1:759765518369947658> +cat', value='Cat pictures')
        embedf.add_field(name='<a:motion1:759765518369947658> +dog', value='Dog pictures')
        embedf.add_field(name='<a:motion1:759765518369947658> +fox', value='Fox pictures')
        embedf.add_field(name='<a:motion1:759765518369947658> +trump', value='Trump opinions')
        embedf.add_field(name='<a:motion1:759765518369947658> +rps', value='RockPaperScissors')
        embedf.add_field(name='<a:motion1:759765518369947658> +fml', value='FML')

        embedf.set_footer(text="Page 7/8 — React to view other pages")

        embedg = discord.Embed(
            color=0xb3d4ff

        )

        embedg.set_author(name="Anime Commands — 1", icon_url='https://i.imgur.com/djv68d4.png')
        embedg.set_thumbnail(url="https://i.imgur.com/aTZOb2O.gif")
        embedg.add_field(name='<a:motion1:759765518369947658> +anime', value='Anime Search')
        embedg.add_field(name='<a:motion1:759765518369947658> +manga', value='manga Search')
        embedg.add_field(name='<a:motion1:759765518369947658> +character', value='Char Search')

        embedg.set_footer(text="Page 8/8 — React to view other pages")

        embeds = [
            embed,
            embeda,
            embedb,
            embedc,
            embedd,
            embede,
            embedf,
            embedg
        ]

        paginator = BotEmbedPaginator(ctx, embeds)
        await paginator.run()




def setup(client):
    client.add_cog(Help(client))
