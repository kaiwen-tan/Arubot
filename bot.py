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


@client.command(aliases=['nc'])
async def nicecall(ctx):
    await ctx.send(
        'https://cdn.discordapp.com/attachments/377614224970743824/390700326862192640/nice_call.png')


@client.command()
@commands.has_permissions(manage_messages=True)
async def purge(ctx, i=2):
    if i < 50:
        await ctx.channel.purge(limit=i)
    else:
        await ctx.send("enter a valid number(0<x<50)")

#this is where the token goes for the bot, i have hosted the bot already but if you'd like to run this yourself, please refer to the discord developer portal and discord.py documentations.
client.run('')



