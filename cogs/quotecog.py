import discord
import random
import time
import os
from datetime import date
from discord.ext import commands
import json
from typing import Optional


class quoteclass(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def quote(self, ctx, *, message: Optional[str]):
        channel = discord.utils.get(self.client.get_all_channels(),
                                    guild__name=str(ctx.guild), name='quotes')
        if len(ctx.message.attachments) == 1:
            out = '> ' + ctx.message.attachments[0].url + '\n' + \
                  '\n quoted by:' + ctx.author.mention
            message = ctx.message.attachments[0].url
        else:
            out = '> ' + message + '\n' + '\n quoted by:' + ctx.author.mention

        await channel.send(out)

        out_stored = '> ' + message + ' on: ' + date.today().strftime(
            "%B %d, %Y") + ' ' + time.strftime("%H:%M", time.localtime())
        with open(f'quote_data_{ctx.guild.id}.txt', 'a') as output:
            output.write('\n' + out_stored + '\n')

        print('quote saved')

    @commands.command()
    async def randquote(self, ctx):
        lst = []
        file1 = open(f"quote_data_{ctx.guild.id}.txt", "r")
        op = file1.readlines()
        # print(op)
        out = []
        indxs = []
        for i in range(len(op)):
            if op[i] == '\n':
                indxs.append(i)

        for j in range(len(indxs)):
            if j+1 <= len(indxs)-1:
                out.append(op[indxs[j]+1:indxs[j+1]])
            else:
                out.append(op[indxs[j]+1:])

        # print(out)
        out2 = []
        for k in out:
            out2.append(''.join(k))

        # print(out2)
        await ctx.send(random.choice(out2))

        #
        # with open('quote_data.txt', 'r') as f:
        #     for count, line in enumerate(f, start=1):
        #         if count % 2 == 0:
        #             lst.append(line)
        # await ctx.send(random.choice(lst))


def setup(client):
    client.add_cog(quoteclass(client))
