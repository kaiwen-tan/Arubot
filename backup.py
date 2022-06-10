import discord
import random
import math
import time
from datetime import date
from discord.ext import commands

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Is online")

# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined')
#
# @client.event
# async def on_member_remove(member):
#     print(f'member has left')

# @client.command()
# async def ping(ctx):
#     await ctx.send(f'your ping is {round(client.latency * 1000)}ms')

@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    lst = ['yes', 'no']
    await ctx.send(random.choice(lst))

@client.command()
async def quote(ctx, *, message):
    channel = discord.utils.get(client.get_all_channels(), \
    guild__name = str(ctx.guild), name = 'quotes')
    out = '> ' + message + '\n' +  '\n quoted by:' + ctx.author.mention
    out2 = '> ' + message + ' on: '+ date.today().strftime("%B %d, %Y") + ' ' + time.strftime("%H:%M", time.localtime())
    await channel.send(out)
    with open('quote_data.txt', 'a') as output:
        output.write('\n' + out2 + '\n')
    print('quote saved')

@client.command()
async def randquote(ctx):
    lst = []
    with open('quote_data.txt', 'r') as f:
        for count, line in enumerate(f, start=1):
            if count % 2 == 0:
                lst.append(line)
    await ctx.send(random.choice(lst))


client.run('NzE0MTI3ODE2NDM3OTIzOTMw.XsrIUA.VC1icK0ICyAgglfDFZP5QPQ8NBQ')
