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
    async def searchquote(self, ctx, search: Optional[str], count: Optional[int]
                          ):

        if search is None:
            await ctx.send('no inputs submitted')

        elif count is None:

            await ctx.send('Here is your singular quote containing the phrase/wo'
                           'rd: ' +
                           search + '\n')
            await ctx.send('-----------------------------------------')


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
                if j + 1 <= len(indxs) - 1:
                    out.append(op[indxs[j] + 1:indxs[j + 1]])
                else:
                    out.append(op[indxs[j] + 1:])

            # print(out)
            out2 = []
            for k in out:
                out2.append(''.join(k))

            # print(out2)
            for item in out2:
                if search in item:
                    lst.append(item)

            if len(lst) == 0:
                await ctx.send('no quotes found for the entry: ' + search)
            else:
                await ctx.send(random.choice(lst))

        elif count >= 10:
            await ctx.send('calm down there buddy less than 10 quotes at a '
                           'time')

        else:
            await ctx.send('These are the quotes containing the phrase/word: ' +
                           search + ', over ' + str(count) + ' times.' + '\n')
            await ctx.send('-----------------------------------------')


            out = []
            for i in range(count):
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
                    if j + 1 <= len(indxs) - 1:
                        out.append(op[indxs[j] + 1:indxs[j + 1]])
                    else:
                        out.append(op[indxs[j] + 1:])

                # print(out)
                out2 = []
                for k in out:
                    out2.append(''.join(k))

                # print(out2)
                for item in out2:
                    if search in item:
                        lst.append(item)
                
                out.append(random.choice(lst))
                await ctx.send(random.choice(lst))
            if len(out) == 0:
                await ctx.send('no quotes found for the entry: ' + search)

    @commands.command()
    async def randquote(self, ctx, count: Optional[int]):
        
        if count is None:
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
        else:
            if count > 10:
                await ctx.send('cant spam the chat that much, give me a lower '
                               'number')

            elif count < 1:
                await ctx.send('okay buddy give me a bigger integer than that.')
            else:
                for num in range(count):
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
                    out = str(num+1) + '. ' + random.choice(out2)
                    await ctx.send(out)
        #
        # with open('quote_data.txt', 'r') as f:
        #     for count, line in enumerate(f, start=1):
        #         if count % 2 == 0:
        #             lst.append(line)
        # await ctx.send(random.choice(lst))
    @commands.command()
    async def totalquote(self, ctx):
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

        await ctx.send('total quotes:' + str(len(out2)))


def setup(client):
    client.add_cog(quoteclass(client))
