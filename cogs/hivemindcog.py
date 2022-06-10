import discord
from discord.ext import commands
import random


class hivemind(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['nc'])
    async def nicecall(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/'
                       '377614224970743824/390700326862192640/nice_call.png')

    @commands.command(aliases=['hrony'])
    async def horny(self, ctx):
        await ctx.send('https://media.discordapp.net/attachments/'
                       '689310173655072795/729114794749198427/hrony.gif')

    @commands.command(aliases=['smex'])
    async def lotad(self, ctx):
        await ctx.send(
            'https://images-ext-2.discordapp.net/external/eVSgOt4lylaYZcvrGUaKy'
            'LjyPymIt4nfPXqGIGk9yb8/https/media.discordapp.net/attachments/732'
            '657620455784510/737428017940267008/yes.gif')

    #@commands.command(aliases=['prices'])
    #async def turnip(self, ctx):
    #    await ctx.send(
    #        '|| https://cdn.discordapp.com/attachments/732657620455784510/73918'
    #        '7730889703514/Screenshot_20200513-103846_Instagram.jpg')

    #@commands.command()
    #async def valorant(self, ctx):
    #    await ctx.send(
    #        '|| https://media.discordapp.net/attachments/732657620455784510/'
    #        '737879339634524220/walter.gif ||')

    #@commands.command()
    #async def league(self, ctx):
    #    await ctx.send(
    #        '|| https://media.discordapp.net/attachments/590697656230346798'
    #        '/740279677847076874/geton.gif ||')

    #@commands.command()
    #async def geton(self, ctx):
    #    lst = [
    #        '|| https://media.discordapp.net/attachments/732657620455784510'
    #        '/737879339634524220/walter.gif ||',
    #        '|| https://media.discordapp.net/attachments/590697656230346798'
    #        '/740279677847076874/geton.gif ||']

    #    await ctx.send(random.choice(lst))


def setup(client):
    client.add_cog(hivemind(client))
