import discord
from discord import Member
from discord.ext import commands
import random
import os
import aiohttp
import json
from utils import lists, permissions, http, default, argparser,helpers
from bs4 import BeautifulSoup
import requests
import async_timeout
import asyncio
import xkcd
import time
import qrcode
from io import BytesIO
import aiohttp
import config
from io import BytesIO
import random
import datetime
import lxml


class fun(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.session = aiohttp.ClientSession()
    
    def __embed_json(self, data, key="message"):
        em = discord.Embed(color=0xDEADBF)
        em.set_image(url=data[key])
        return em


    async def __get_image(self, ctx, user=None):
        if user:
            if user.is_avatar_animated():
                return str(user.avatar_url_as(format="gif"))
            else:
                return str(user.avatar_url_as(format="png"))

        await ctx.trigger_typing()

        message = ctx.message

        if len(message.attachments) > 0:
            return message.attachments[0].url

        def check(m):
            return m.channel == message.channel and m.author == message.author

        try:
            await ctx.send("Send me an image!")
            x = await self.bot.wait_for('message', check=check, timeout=10000)
        except:
            return await ctx.send("Timed out...")

        if not len(x.attachments) >= 1:
            return await ctx.send("No images found.")

        return x.attachments[0].url

            

    @commands.command(aliases=['flip', 'coin'])
    async def toss(self, ctx):
        """ Coinflip! """
        coinsides = ['Heads', 'Tails']
        await ctx.send(f"**{ctx.author.name}** flipped a coin and got **{random.choice(coinsides)}**!")

    @commands.command(aliases=['8ball'])
    async def eightball(self, ctx, *, question: commands.clean_content):
        """ Consult 8ball to receive an answer """
        answer = random.choice(lists.ballresponse)
        await ctx.send(f"🎱 **Question:** {question}\n**Answer:** {answer}")

    @commands.command(aliases=['ppsize', 'measurepp'])
    async def pp(self, ctx ,member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author
        """ Coinflip! """
        PP = ['YOU DONT EVEN HAVE A PP', 'IT IS SO SMALL I CANT MEASURE IT','8D','8==D','8===D','8====D','8======D','8=======D','8========D','8============D','8=================D','MEGA PP']
        
        embed = discord.Embed(title = 'PP', description = f"**{member.name.mention}'s pp is this big\n** {random.choice(PP)}!",colour = discord.Colour.red())

  
        await ctx.send(embed = embed)


    @commands.command()
    @commands.cooldown(rate=1, per=2.0, type=commands.BucketType.user)
    async def urban(self, ctx, *, search: commands.clean_content):
        """ Find the 'best' definition to your words """
        async with ctx.channel.typing():
            try:
                url = await http.get(f'https://api.urbandictionary.com/v0/define?term={search}', res_method="json")
            except Exception:
                return await ctx.send("Urban API returned invalid data... might be down atm.")

            if not url:
                return await ctx.send("I think the API broke...")

            if not len(url['list']):
                return await ctx.send("Couldn't find your search in the dictionary...")

            result = sorted(url['list'], reverse=True, key=lambda g: int(g["thumbs_up"]))[0]

            definition = result['definition']
            if len(definition) >= 1000:
                definition = definition[:1000]
                definition = definition.rsplit(' ', 1)[0]
                definition += '...'

            await ctx.send(f"📚 Definitions for **{result['word']}**```fix\n{definition}```")



    @commands.command(aliases=['slots', 'bet'])
    @commands.cooldown(rate=1, per=3.0, type=commands.BucketType.user)
    async def slot(self, ctx):
        """ Roll the slot machine """
        emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
        a = random.choice(emojis)
        b = random.choice(emojis)
        c = random.choice(emojis)

        slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"

        if (a == b == c):
            await ctx.send(f"{slotmachine} All matching, you won! 🎉")
        elif (a == b) or (a == c) or (b == c):
            await ctx.send(f"{slotmachine} 2 in a row, you won! 🎉")
        else:
            await ctx.send(f"{slotmachine} No match, you lost 😢")


    @commands.command(aliases = ["simpr8","howsimp"])
    async def simp(self, ctx,member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author      
        s = random.randint(1,100)
        embed = discord.Embed(title = "simp r8", description = f"{member.name} is {s}% simp", colour = discord.Colour.red())
        await ctx.send (embed = embed)



    @commands.command(aliases = ["howgay","gayr8"])
    async def gay(self, ctx,member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author      
        s = random.randint(1,100)
        embed = discord.Embed(title = "Gayr8", description = f"{member.name} is {s}% gay", colour = discord.Colour.red())
        await ctx.send (embed = embed)



    @commands.command()
    async def aww(self, ctx):

        embed = discord.Embed(title="aww", description="cuteie", colour = discord.Colour.red())
        
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://www.reddit.com/r/aww/new.json?sort=hot') as r:
                res = await r.json()
                embed.set_image(url=res['data']['children'] [random.randint(0, 25)]['data']['url'])
                await ctx.send(embed=embed)
    


    @commands.command(aliases=['howhot', 'hot'])
    async def hotcalc(self, ctx, *, user: discord.Member = None):
        """ Returns a random percent for how hot is a discord user """
        user = user or ctx.author

        random.seed(user.id)
        r = random.randint(1, 100)
        hot = r / 1.17

        emoji = "💔"
        if hot > 25:
            emoji = "❤"
        if hot > 50:
            emoji = "💖"
        if hot > 75:
            emoji = "💞"

        await ctx.send(f"**{user.name}** is **{hot:.2f}%** hot {emoji}")
        
    @commands.command()
    async def roast(self, ctx,member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author       
        roast = [" You have your entire life to be a jerk. Why not take today off?","Your ass must be pretty jealous of all the shit that comes out of your mouth.","Remember when I asked for your opinion? Me neither.","If you’re waiting for me to care, I hope you brought something to eat, ‘cause it’s gonna be a really long time.","Some day you’ll go far—and I really hope you stay there.","I’m trying my absolute hardest to see things from your perspective, but I just can’t get my head that far up my ass.",
        "Sometimes it’s better to keep your mouth shut and give the impression that you’re stupid than open it and remove all doubt.","I’m not a proctologist, but I know an asshole when I see one.",
        "You only annoy me when you’re breathing, really.","Do yourself a   favor and ignore anyone who tells you to be yourself. Bad idea in your case.","I don’t know what your problem is, but I’m guessing it’s hard to pronounce.","Do your parents even realize they’re living proof that two wrongs don’t make a right"," Remember that time I said I thought you were cool? I lied.","Everyone’s entitled to act stupid once in awhile, but you really abuse the privilege."]
 
        embed = discord.Embed(title = f'{member.name}', description =f"{random.choice(roast)}")
        await ctx.send(embed = embed)

    @commands.command()
    async def cat(self, ctx):
        response = requests.get('https://aws.random.cat/meow')
        data = response.json()
        await ctx.send(data['file'])



    @commands.command(name='waifu', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def waifu(self, ctx):
        """Queries reddit for a random waifu."""
        waifu_api = 'https://meme-api.herokuapp.com/gimme/awwnime'
        parameter = dict()
        resp = requests.get(url=waifu_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Waifu', url=data['postLink'], color=0xe19fa9,
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)

    
    @commands.command(name='baka', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def baka(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Call someone an idiot"""
        baka_api = 'https://nekos.life/api/v2/img/baka'
        parameter = dict()
        resp = requests.get(url=baka_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='baka', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** called **{member.name}** an Idiot ',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)


  
  
    @commands.command(name='cuddle', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def cuddle(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/cuddle'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Awww', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** cuddled with **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)    

    @commands.command(name='lick', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def lick(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://waifu.pics/api/sfw/lick'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Lick', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** licked at **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  



    @commands.command(name='blush', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def blush(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://waifu.pics/api/sfw/blush'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Lick', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** blushes at **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  


    @commands.command(name='tickle', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tickle(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/tickle'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='hehehe', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** tickled  **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)    

    @commands.command(name='slap', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author 
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/slap'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='It hurts', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author} slapped {member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed) 


    @commands.command(name='dog', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def dog(self, ctx, member: discord.Member = None):
        """Cute doggo"""
        lick_api = 'https://dog.ceo/api/breeds/image/random'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Doggo', url=data['message'], color=0xe19fa9, description = "",
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['message'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  

 
    @commands.command(name='kiss', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def kiss(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/kiss'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Kissi', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** kissed  **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)    


    @commands.command(name='goose', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def goose(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/goose'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Honki', url=data['url'], color=0xe19fa9, description ="honk" ,
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)    

    

    @commands.command(aliases = ["pressf"])
    async def F(self,ctx):
        embed = discord.Embed(title = "Presss F to pay respect", description = f'<a:pressF:752476619033018418>{ctx.author.name} paid their respect', colour = discord.Colour.green())
        await ctx.send(embed = embed)            
             	


    @commands.command(aliases=['rjoke'])
    async def joke(self, ctx):
        """"I got a funny joke for ya!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://official-joke-api.appspot.com/random_joke') as r:
                res = await r.json()
                await ctx.send(res['setup'])
                time.sleep(5)
                await ctx.send(res['punchline'])

    @commands.command()
    @commands.cooldown(1, 4, commands.BucketType.user)
    async def coffee(self, ctx):
        """Coffee owo"""
        await ctx.channel.trigger_typing()
        async with aiohttp.ClientSession() as cs:
            async with cs.get("https://nekobot.xyz/api/image?type=coffee") as res:
                imgdata = await res.json()
            em = discord.Embed()
            msg = await ctx.send("*drinks coffee*", embed=em.set_image(url=imgdata["message"]))
            color = await helpers.get_dominant_color(self.bot, imgdata["message"])
            em = discord.Embed(color=color)
            await msg.edit(embed=em.set_image(url=imgdata["message"]))


    @commands.command()
    @commands.cooldown(1, 12, commands.BucketType.user)
    async def qr(self, ctx, *, message: str):
        """Generate a QR Code"""
        temp = BytesIO()
        qrcode.make(message).save(temp)
        temp.seek(0)
        await ctx.send(file=discord.File(temp, filename="qr.png"))
         

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def choose(self, ctx, *items):
        """Choose between multiple options"""
        if not items:
            return await ctx.send_help(ctx.command)
        await ctx.send("I chose: **{}**!".format(helpers.clean_text(random.choice(items))))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def lolice(self, ctx):
        """KNOCK KNOCK KNOCK"""
        await ctx.trigger_typing()
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=lolice&url=%s" % ctx.author.avatar_url_as(format="png")) as r:
            res = await r.json()
        em = discord.Embed(color=0xDEADBF)
        await ctx.send(embed=em.set_image(url=res["message"]))
  
 
    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def ship(self, ctx, user1: discord.Member, user2: discord.Member = None):
        """Ship OwO"""
        if user2 is None:
            user2 = ctx.author

        await ctx.trigger_typing()
        if user1.avatar:
            user1url = "https://cdn.discordapp.com/avatars/%s/%s.png" % (user1.id, user1.avatar,)
        else:
            user1url = "https://cdn.discordapp.com/embed/avatars/1.png"
        if user2.avatar:
            user2url = "https://cdn.discordapp.com/avatars/%s/%s.png" % (user2.id, user2.avatar,)
        else:
            user2url = "https://cdn.discordapp.com/embed/avatars/1.png"

        self_length = len(user1.name)
        first_length = round(self_length / 2)
        first_half = user1.name[0:first_length]
        usr_length = len(user2.name)
        second_length = round(usr_length / 2)
        second_half = user2.name[second_length:]
        finalName = first_half + second_half

        score = random.randint(0, 100)
        filled_progbar = round(score / 100 * 10)
        counter_ = '█' * filled_progbar + '‍ ‍' * (10 - filled_progbar)

        async with self.session.get("https://nekobot.xyz/api/imagegen?type=ship&user1=%s&user2=%s" % (user1url, user2url,)) as r:
            res = await r.json()

        em = discord.Embed(color=0xDEADBF)
        em.title = "%s ❤ %s" % (user1.name, user2.name,)
        em.description = f"**Love %**\n" \
                         f"`{counter_}` **{score}%**\n\n{finalName}"
        em.set_image(url=res["message"])

        await ctx.send(embed=em)

    @commands.command()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def fact(self, ctx, *, text: str):
        if len(text) > 165:
            return await ctx.send("Text too long...")
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=fact"
                          "&text=%s" % text) as r:
            res = await r.json()

        await ctx.trigger_typing()
        em = discord.Embed(color=0xDEADBF)
        em.set_footer(text = "Powered by nekobot.xyz")
        await ctx.send(embed=em.set_image(url=res["message"]))



    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def clyde(self, ctx, *, text: str):
        await ctx.trigger_typing()
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=clyde&text=%s" % text) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def tweet(self, ctx, username: str, *, text: str):
        """Tweet as someone."""
        await ctx.trigger_typing()
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=tweet"
                          "&username=%s"
                          "&text=%s" % (username, text,)) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 3, commands.BucketType.user)
    async def trash(self, ctx, user: discord.Member):
        """trash smh"""
        await ctx.trigger_typing()
        url = user.avatar_url_as(format="jpg")
        async with self.session.get("https://nekobot.xyz/api/imagegen?type=trash&url=%s" % (url,)) as r:
            res = await r.json()
        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def iphonex(self, ctx, user:discord.Member=None):
        """Generate an iPhone X Image"""
        img = await self.__get_image(ctx, user)
        if not isinstance(img, str):
            return img
        await ctx.trigger_typing()
        async with self.session.get(f"https://nekobot.xyz/api/imagegen?type=iphonex&url={img}") as r:
            res = await r.json()
        await ctx.send(embed=self.__embed_json(res))

    @commands.command()
    @commands.guild_only()
    @commands.cooldown(2, 5, commands.BucketType.user)
    async def anime(self, ctx, *, search: str):
        """Get Anime Stats"""
        await ctx.trigger_typing()
        async with aiohttp.ClientSession() as cs:
            async with cs.post("https://graphql.anilist.co", json={
                "query": helpers.anilist_query,
                "variables": {
                    "search": search
                }
            }) as res:
                data = await res.json()
        if data.get("errors", []):
            return await ctx.send("Error getting data from anilist: {}".format(data["errors"][0]["message"]))
        media = data["data"]["Page"]["media"]
        if not media:
            return await ctx.send("Nothing found.")
        media = media[0]
        if media["isAdult"] is True and not ctx.channel.is_nsfw():
            return await ctx.send("NSFW Anime can't be displayed in non NSFW channels.")
        color = int(media["coverImage"]["color"].replace("#", ""), 16) if media["coverImage"]["color"] else 0xdeadbf
        em = discord.Embed(colour=color)
        em.title = "{} ({})".format(media["title"]["romaji"], media["title"]["english"])
        if media["description"]:
            desc = BeautifulSoup(media["description"], "lxml")
            if desc:
                em.description = desc.text
        em.url = "https://anilist.co/anime/{}".format(media["id"])
        em.set_thumbnail(url=media["coverImage"]["extraLarge"])
        em.add_field(name="Status", value=media["status"].title(), inline=True)
        em.add_field(name="Episodes", value=media["episodes"], inline=True)
        em.add_field(name="Score", value=str(media["averageScore"]), inline=True)
        em.add_field(name="Genres", value=", ".join(media["genres"]))
        dates = "{}/{}/{}".format(media["startDate"]["day"], media["startDate"]["month"], media["startDate"]["year"])
        if media["endDate"]["year"] is not None:
            dates += " - {}/{}/{}".format(media["endDate"]["day"], media["endDate"]["month"], media["endDate"]["year"])
        em.add_field(name="Date", value=dates)
        await ctx.send(embed=em)

    @commands.command(name="attack", hidden=True)

    async def attack(self, ctx, member: Member):
        """Throw Insults at Members"""

        # Set up array of insults to throw at people
        responses = [
            f"{member.mention} is stinky",
            f"{member.mention} is ugly",
            f"{member.mention} has a gigantic nose",
            f"{member.mention} gets no views on their tiktok",
            f"{member.mention} is obviously compensating for something :eyes:",
            f"{member.mention} DIE DIE DIE :knife: :skull:",
            f"{member.mention} is so annoying smh :rolling_eyes:",
            f"I'd say {member.mention} was dropped as a child but they would have to be held to be dropped in the first place",
            f"I hate {member.mention}",
            f"{member.mention} close your legs, it smells like clam chowder :face_vomiting: :face_vomiting: :nauseated_face: :nauseated_face:",
            f"I bet {member.mention} can't reach the wall cabinets without a booster chair",
            f"{member.mention} Browses 4Chan and Reddit all day looking for love",
            f"{member.mention} Your forehead could be used as a landing pad",
            f"I bet {member.mention} likes eating watermelon with the rind.",
            f"{member.mention} You were the first creation to make god say oops",
            f"{member.mention} You have delusions of adequacy",
            f"{member.mention} I treasure the time I don't spend with you",
            f"Don't be ashamed of yourself {member.mention}, that's your parent's job",
            f"I don't have the energy to pretend I like {member.mention} today",
            f"I know this was made for me to insult but it’s kinda hard to be a hateful cunt like {member.mention} :star_struck::star_struck:",
            f"#{member.mention}IsOverParty",
            f"I hope {member.mention} drops dead with a curable disease that doctors simply didn’t feel like curing :)",
            f"{member.mention} You know there's no vaccine for stupidity right?",
            f"{member.mention} You are not very epic at all",
            f"You make Kpop Fancams 24/7 for validation on the internet {member.mention}",
            f"Your mother wanted to drop you on the head when you were little {member.mention}",
            f"{member.mention} You're the CEO of Racism",
            f"{member.mention} has no common sense"
        ]

        # Sending out a random insult from the array "responses"
        await ctx.send(random.choice(responses))

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def phcomment(self, ctx, *, comment: str):
        """PronHub Comment Image"""
        await ctx.trigger_typing()
        async with self.session.get(f"https://nekobot.xyz/api/imagegen?type=phcomment"
                          f"&image={ctx.author.avatar_url_as(format='png')}"
                          f"&text={comment}&username={ctx.author.name}") as r:
            res = await r.json()
        if not res["success"]:
            return await ctx.send("**Failed to successfully get image.**")
        await ctx.send(embed=self.__embed_json(res))


    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def awooify(self, ctx, user: discord.Member = None):
        """AwWOOOOO"""
        img = await self.__get_image(ctx, user)
        if not isinstance(img, str):
            return img

        async with self.session.get("https://nekobot.xyz/api/imagegen?type=awooify&url=%s" % img) as r:
            res = await r.json()

        await ctx.send(embed=self.__embed_json(res))


    @commands.command(aliases=['momma'])
    async def yomomma(self, ctx):
        """"I got a funny joke for ya!"""
        async with aiohttp.ClientSession() as cs:
            async with cs.get('https://api.yomomma.info') as r:
                res = await r.json()
                momma = res['joke']
                embed = discord.Embed(title = "Yomomma", description = momma, colour = discord.Colour.red())
                await ctx.send(embed = embed)

                
    @commands.command()
    async def OwO(self,ctx):
        await ctx.send("OwO\nUwU")

  
  
    @commands.command(name='pat', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def pat(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/pat'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Pat', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** Patted **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)   


              
  
    @commands.command(name='hug', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def hug(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/hug'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Awww', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** hugged **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)    
            
  
    @commands.command(name='feed', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def feed(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/feed'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='Feed', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** feeded **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)

    @commands.command(name='poke', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def poke(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://nekos.life/api/v2/img/poke'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='poke', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** poked **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)                

    @commands.command(name='slap', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def slap(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://waifu.pics/api/sfw/slap'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='slap', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** slapped **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  

    @commands.command(name='bully', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bully(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://waifu.pics/api/sfw/bully'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='bully', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** bullied **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='This does not promote any kind of bullying \n Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  

    @commands.command(name='bite', ignore_extra=False)
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def bite(self, ctx, member: discord.Member = None):
        if not member:  # if member is no mentioned
            member = ctx.message.author   
        """Lick someone"""
        lick_api = 'https://waifu.pics/api/sfw/bite'
        parameter = dict()
        resp = requests.get(url=lick_api, params=parameter)
        data = resp.json()
        waifu_embed = discord.Embed(title='bite', url=data['url'], color=0xe19fa9, description = f'**{ctx.message.author}** bit **{member.name}**',
                                    timestamp=ctx.message.created_at)
        waifu_embed.set_image(url=data['url'])
        waifu_embed.set_footer(text='Requested by %s' % ctx.author, icon_url=ctx.author.avatar_url)
        await ctx.channel.send(embed=waifu_embed)  


    @commands.command()
    async def reddit(self,ctx, subreddit=None):
      if subreddit == None:
        await ctx.send("You need to specify subreddit")
      else:
        r = requests.get(url=f"https://meme-api.herokuapp.com/gimme/{subreddit}")
        rd = r.json()
        postlink = rd['postLink']
        sub = rd['subreddit']
        title = rd['title']
        url= rd['url']
        nsfw = rd['nsfw']
        spoiler = rd['spoiler']
        
        if nsfw == True:
            await ctx.send("This is a NSFW post")
        else:
            if spoiler == True:
                await ctx.send("This post is marked as spoiler, are you sure you still want to view this? Respond with `y` or `n`")
                try:
                    response = await self.bot.wait_for('message', check=lambda m: m.author.id == ctx.author.id and m.channel.id == ctx.channel.id, timeout=10)
                    
                    if response.content.lower().startswith("y"):
                        embed = discord.Embed(color=ctx.author.color, description=f"[{title}]({postlink})")
                        embed.set_image(url=url)
                        embed.set_footer(text=f"r/{sub}")
                        await ctx.send(embed=embed)
                    elif response.content.lower().startswith("n"):
                        await ctx.send("cancelled")
                    else:
                        await ctx.send("cancelled")
                except asyncio.TimeoutError:
                    await ctx.send("timeout")
            else:
                embed = discord.Embed(color=ctx.author.color, description=f"[{title}]({postlink})")
                embed.set_image(url=url)
                embed.set_footer(text=f"r/{sub}")
                await ctx.send(embed=embed)
    
    @commands.command()
    async def meme (self, ctx):
        api =      "https://api.ksoft.si/images/random-meme?Authorization=0de1ef1b67fb9ebd70a6dbea0aa8c69a2131e3d1"
        parameter = dict()
        r = requests.get(url=api, params = parameter)
        data = r.json()
        embed = discord.Embed(title = data["title"], url = data["image_url"], colour = discord.Colour.Red())
        embed.set_image(url = data["image_url"]),
        embed.set_footer("test")
        await ctx.send(embed = embed)




def setup(client):
    client.add_cog(fun(client))
    