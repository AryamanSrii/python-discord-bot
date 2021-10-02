import discord
from discord.ext import commands
from discord.ext import tasks
import asyncio
import functools
import math
import os
import jishaku
import keep_alive

client = commands.Bot(description='Mitsuki', command_prefix='>')
@client.event
async def on_ready():
    print('Logged in as:\n{0.user.name}\n{0.user.id}'.format(client))

client.remove_command("help")   



@tasks.loop(seconds=80)
async def status_change():
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=">help"))
  await asyncio.sleep(80)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="ur mom" ))
  await asyncio.sleep(80)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name="Jai shree ram"))
  await asyncio.sleep(80)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name=f"{len(client.users)} users."))
  await asyncio.sleep(80)
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name=f"{len(client.guilds)} servers."))
  await asyncio.sleep(80)
status_change.before_loop(client.wait_until_ready)    
status_change.start()



for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')
 
client.load_extension("jishaku")


@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.CommandOnCooldown):
     msg = 'This command is on cooldown, please try again in {:.2f}s'.format(error.retry_after)
     em = discord.Embed(title = "Cooldown", description = msg ,colour= discord.Colour.red())
     await ctx.send (embed = em)
  elif isinstance(error, commands.NSFWChannelRequired):
    embed = discord.Embed(title = "Not NSFW", description ="This is not a nsfw channel\nGo into settings and change change it to use the command", colour = discord.Colour.red())
    await ctx.send (embed = embed)    
  elif isinstance(error, commands.MissingRequiredArgument):
    embed = discord.Embed(title = "Missing Arguments", description ="Missing an argument\nNext time use a prooper arguments", colour = discord.Colour.red())
    await ctx.send (embed = embed)  


client.run(os.getenv("TOKEN"))

