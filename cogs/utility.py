import discord
from discord.ext import commands, tasks
from io import BytesIO
from utils import default
from itertools import cycle
import datetime
import psutil
import time
import discord
import psutil
import os
import qrcode
from datetime import datetime
from discord.ext import commands
from utils import default, helpers
import aiohttp
import random
import codecs
import aiohttp
import discord
from bs4 import BeautifulSoup
import wikipedia


class utility(commands.Cog):
    def __init__(self, client):
        self.client = client


    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(title = "ping", description  =f'**Pong!\n{round(self.client.latency * 1000)}ms**:ping_pong:', colour = discord.Colour.green() )
        await ctx.send(embed = embed )

    @commands.command()
    async def invite(self, ctx):
        """ Invite me to your server """
        await ctx.send(f"**{ctx.author.name}**, use this URL to invite me\n https://discord.com/api/oauth2/authorize?client_id=740045367956996236&permissions=8&scope=bot")


    @commands.command()
    async def whois(self,ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author  # set member as the author
        roles = [role for role in member.roles[1:]]
        embed = discord.Embed(colour=discord.Colour.purple(), timestamp=ctx.message.created_at,
                              title=f"User Info - {member}")
        embed.set_thumbnail(url=member.avatar_url)
        embed.set_footer(text=f"Requested by {ctx.author.name}")

        embed.add_field(name="ID:", value=member.id)
        embed.add_field(name="Display Name:", value=member.display_name)

        embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
        embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))

        embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
        embed.add_field(name="Highest Role:", value=member.top_role.mention)
        print(member.top_role.mention)
        await ctx.send(embed=embed)

    @commands.command()
    async def support(self, ctx):
        embed = discord.Embed(colour = discord.Colour.red(),title =f"**{ctx.author.name}**",timestamp=ctx.message.created_at)
        embed.add_field(name = "support server Invite link", value = "https://discord.gg/tbSGmhf")
        await ctx.send(embed = embed)


    
    @commands.command()
    @commands.guild_only()
    async def avatar(self, ctx, *, user: discord.Member = None):
        """ Get the avatar of you or someone else """
        user = user or ctx.author
        await ctx.send(f"Avatar of **{user.name}**\n{user.avatar_url_as(size=1024)}")



    @commands.command()
    @commands.guild_only()
    async def mods(self, ctx):
        """ Check which mods are online on current guild """
        message = ""
        online, idle, dnd, offline = [], [], [], []

        for user in ctx.guild.members:
            if ctx.channel.permissions_for(user).kick_members or \
               ctx.channel.permissions_for(user).ban_members:
                if not user.bot and user.status is discord.Status.online:
                    online.append(f"**{user}**")
                if not user.bot and user.status is discord.Status.idle:
                    idle.append(f"**{user}**")
                if not user.bot and user.status is discord.Status.dnd:
                    dnd.append(f"**{user}**")
                if not user.bot and user.status is discord.Status.offline:
                    offline.append(f"**{user}**")

        if online:
            message += f"🟢 {', '.join(online)}\n"
        if idle:
            message += f"🟡 {', '.join(idle)}\n"
        if dnd:
            message += f"🔴 {', '.join(dnd)}\n"
        if offline:
            message += f"⚫ {', '.join(offline)}\n"

        await ctx.send(f"Mods in **{ctx.guild.name}**\n{message}")

   


    @commands.command()
    @commands.guild_only()
    async def joinedat(self, ctx, *, user: discord.Member = None):
        """ Check when a user joined the current server """
        user = user or ctx.author

        embed = discord.Embed(colour=user.top_role.colour.value)
        embed.set_thumbnail(url=user.avatar_url)
        embed.description = f'**{user}** joined **{ctx.guild.name}**\n{default.date(user.joined_at)}'
        await ctx.send(embed=embed)

    @commands.command()
    @commands.guild_only()
    async def channels (self,ctx):
        guild = ctx.guild
        total_text_channels = len(guild.text_channels)
        total_voice_channels = len(guild.voice_channels)
        total_channels = total_text_channels  + total_voice_channels 
        embed = discord.Embed(title = "Channels", colour = discord.Colour.red())
        embed.add_field(name="Server Channels: ", value=total_channels , inline = False )
        embed.add_field(name="Server Text Channels: ", value=total_text_channels, inline = False )
        embed.add_field(name="Server Voice Channels: ", value=total_voice_channels, inline = False )
        await ctx.send(embed = embed)

    @commands.command(aliases = ["si","serverinfo"])
    @commands.guild_only()
    async def server(self, ctx):
        """ Check info about current server """
        if ctx.invoked_subcommand is None:
            findbots = sum(1 for member in ctx.guild.members if member.bot)

            embed = discord.Embed(colour = discord.Colour.red())

            if ctx.guild.icon:
                embed.set_thumbnail(url=ctx.guild.icon_url)
            if ctx.guild.banner:
                embed.set_image(url=ctx.guild.banner_url_as(format="png"))

            embed.add_field(name="Server Name", value=ctx.guild.name, inline=False)
            embed.add_field(name="Server ID", value=ctx.guild.id, inline=False)
            embed.add_field(name="Members", value=ctx.guild.member_count, inline=False)
            embed.add_field(name="Bots", value=findbots, inline=False)
            embed.add_field(name="Owner", value=ctx.guild.owner, inline=False)
            embed.add_field(name="Region", value=ctx.guild.region, inline=False)
            embed.add_field(name="Created", value=default.date(ctx.guild.created_at), inline = False)
            await ctx.send(content=f"ℹ information about **{ctx.guild.name}**", embed=embed)




    @commands.command(name="savatar", aliases=["icon","sa"])
    async def server_avatar(self, ctx):
        """ Get the current server icon """
        if not ctx.guild.icon:
            return await ctx.send("This server does not have a avatar...")
        await ctx.send(f"Avatar of **{ctx.guild.name}**\n{ctx.guild.icon_url_as(size=1024)}")

    @commands.command(name="banner")
    async def server_banner(self, ctx):
        """ Get the current banner image """
        if not ctx.guild.banner:
            return await ctx.send("This server does not have a banner...")
        await ctx.send(f"Banner of **{ctx.guild.name}**\n{ctx.guild.banner_url_as(format='png')}")

    @commands.command(aliases=['wikipedia'])
    async def wiki(self, ctx, *, query):
        '''Search up something on wikipedia'''
        em = discord.Embed(title=str(query))
        em.set_footer(text='Powered by wikipedia.org')
        try:
            result = wikipedia.summary(query)
            if len(result) > 2000:
                em.color = discord.Color.red()
                em.description = f"Result is too long. View the website [here](https://wikipedia.org/wiki/{query.replace(' ', '_')}), or just google the subject."
                return await ctx.send(embed=em)
            em.color = discord.Color.green()
            em.description = result
            await ctx.send(embed=em)
        except wikipedia.exceptions.DisambiguationError as e:
            em.color = discord.Color.red()
            options = '\n'.join(e.options)
            em.description = f"**Options:**\n\n{options}"
            await ctx.send(embed=em)
        except wikipedia.exceptions.PageError:
            em.color = discord.Color.red()
            em.description = 'Error: Page not found.'
            await ctx.send(embed=em)




           

def setup(client):
    client.add_cog(utility(client))
