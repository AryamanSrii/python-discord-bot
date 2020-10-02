import discord
from discord.ext import commands
import random
import os
import requests
import aiohttp




class NSFW(commands.Cog):
    def __init__(self, client):
        self.client = client
    

    @commands.command()
    @commands.is_nsfw()

    async def realgirls(self, ctx):
        """Sends gif from r/realgirls"""
        embed = discord.Embed(title="realgirls", description="test")
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/realgirls/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)

   
    @commands.is_nsfw()
    @commands.command(name='4k', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def fourK(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """4K"""
        lick_api = 'https://nekobot.xyz/api/image?type=4k'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='4K', url=data['message'], color=0xe19fa9, description = "Very bad ",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['message'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  

  
    @commands.is_nsfw()
    @commands.command(name='nsfw', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def nsfw(self, ctx):
        """Queries reddit for a random NSFW."""
        waifu_api = 'https://meme-api.herokuapp.com/gimme/nsfw'
        parameter = dict()
        resp = requests.get(url=waifu_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='NSFW', url=data['postLink'], color=0xe19fa9,
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)

    @commands.is_nsfw()
    @commands.command(name='spank', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def spank(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Spank"""
        lick_api = 'https://nekos.life/api/v2/img/spank'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Spank', url=data['url'], color=0xe19fa9, description = "oof",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  

    @commands.is_nsfw()
    @commands.command(name='hanal', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hanal(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """hentai anal"""
        lick_api = 'https://nekos.life/api/v2/img/anal'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='hentai anal', url=data['url'], color=0xe19fa9, description = "oof",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  

    @commands.is_nsfw()
    @commands.command(name='anal', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def anal(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """4K"""
        lick_api = 'https://nekobot.xyz/api/image?type=anal'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Anal', url=data['message'], color=0xe19fa9, description = "Very bad ",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['message'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  

    @commands.is_nsfw()
    @commands.command(name='gonewild', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def gonewild(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """gonewild"""
        lick_api = 'https://nekobot.xyz/api/image?type=gonewild'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='gonewild', url=data['message'], color=0xe19fa9, description = "",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['message'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  


    @commands.is_nsfw()
    @commands.command(name='pgif', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pgif(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """pgif"""
        lick_api = 'https://nekobot.xyz/api/image?type=pgif'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='pgif', url=data['message'], color=0xe19fa9, description = "",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['message'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  


    @commands.is_nsfw()
    @commands.command(name='ass', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ass(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Ass"""
        lick_api = 'https://nekobot.xyz/api/image?type=ass'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Ass', url=data['message'], color=0xe19fa9, description = "",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['message'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  

 
    @commands.is_nsfw()
    @commands.command(name='holo', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def holo(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """holo"""
        lick_api = 'https://nekobot.xyz/api/image?type=holo'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='holo', url=data['message'], color=0xe19fa9, description = "",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['message'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)          


    @commands.is_nsfw()
    @commands.command(name='hentai', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hentai(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """hentai"""
        lick_api = 'https://nekobot.xyz/api/image?type=hentai'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Hentai', url=data['message'], color=0xe19fa9, description = "",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['message'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)      

   
    @commands.is_nsfw()
    @commands.command(name='lewd', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lewd(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/lewd'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Lewds', url=data['url'], color=0xe19fa9, description ="Lewds" ,
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)    

    @commands.is_nsfw()
    @commands.command(name='boobs', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def boobs(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """hentai anal"""
        lick_api = 'https://nekos.life/api/v2/img/boobs'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='tits', url=data['url'], color=0xe19fa9, description = "oof",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)             
                              

    @commands.is_nsfw()
    @commands.command(name='h_avatar', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def h_avatar(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """hentai anal"""
        lick_api = 'https://nekos.life/api/v2/img/avatar'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Avatar', url=data['url'], color=0xe19fa9, description = "oof",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)    

    @commands.is_nsfw()
    @commands.command(name='keta', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def keta(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """hentai anal"""
        lick_api = 'https://nekos.life/api/v2/img/keta'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Keta', url=data['url'], color=0xe19fa9, description = "oof",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)
 
    @commands.is_nsfw()
    @commands.command(name='bj', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bj(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """hentai anal"""
        lick_api = 'https://nekos.life/api/v2/img/bj'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='BJ', url=data['url'], color=0xe19fa9, description = "oof",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)    

 
    @commands.is_nsfw()
    @commands.command(name='traps', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def traps(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """hentai anal"""
        lick_api = 'https://nekos.life/api/v2/img/trap'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Traps', url=data['url'], color=0xe19fa9, description = "oof",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)   

   

               
                              
def setup(client):
    client.add_cog(NSFW(client))
    