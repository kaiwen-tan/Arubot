import discord
import random
import os
import math
import time
import youtube_dl
from datetime import date
from discord.ext import commands

client = commands.Bot(command_prefix='?')


# load
@client.command()
@commands.has_permissions(administrator=True)
async def load(ctx, extension):
    await ctx.send('extension loaded')
    client.load_extension(f'cogs.{extension}')


# unload
@client.command()
@commands.has_permissions(administrator=True)
async def unload(ctx, extension):
    await ctx.send('extension unloaded')
    client.unload_extension(f'cogs.{extension}')


# list of cogs
@client.command()
@commands.has_permissions(administrator=True)
async def listcogs(ctx):
    await ctx.send('List of cogs:')
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await ctx.send(str(filename))


# checking py file and loading the cog
for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')


@client.event
async def on_member_join(member):
    print(f'{member} has joined')


@client.event
async def on_member_remove(member):
    print(f'{member} has left')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    lst = ["It is certain", "It is decidedly so", "Without a doubt",
           "Yes, definitely",
           "You may rely on it", "As I see it, yes", "Most Likely",
           "Outlook Good",
           "Yes", "Signs point to yes", "Reply hazy, try again",
           "Ask again later",
           "Better not tell you now", "Cannot predict now",
           "Concentrate and ask again",
           "Don't count on it", "My reply is no", "My sources say no",
           "Outlook not so good", "Very Doubtful"]
    await ctx.send(random.choice(lst))


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, i=2):
    if i < 50:
        await ctx.channel.purge(limit=i)
    else:
        await ctx.send("enter a valid number(0<x<50)")


client.run('NzE0MTI3ODE2NDM3OTIzOTMw.XsrIUA.VC1icK0ICyAgglfDFZP5QPQ8NBQ')

# graveyard
# @client.command()
# async def quote(ctx, *, message):
#     channel = discord.utils.get(client.get_all_channels(),
#                                 guild__name=str(ctx.guild), name='quotes')
#     out = '> ' + message + '\n' + '\n quoted by:' + ctx.author.mention
#     out2 = '> ' + message + ' on: ' + date.today().strftime(
#         "%B %d, %Y") + ' ' + time.strftime("%H:%M", time.localtime())
#     await channel.send(out)
#     with open('quote_data.txt', 'a') as output:
#         output.write('\n' + out2 + '\n')
#     print('quote saved')
#
#
# @client.command()
# async def randquote(ctx):
#     lst = []
#     with open('quote_data.txt', 'r') as f:
#         for count, line in enumerate(f, start=1):
#             if count % 2 == 0:
#                 lst.append(line)
#     await ctx.send(random.choice(lst))

# players = {}
#
#
# @client.command(pass_context=True)
# async def play(ctx, url):
#     server = ctx.message.guild
#     channel = ctx.message.author.voice_channel
#     voice_client = client.voice_client_in(server)
#     player = await voice_client.create_ytdl_player(url)
#     players[server.id] = player
#     player.start()
