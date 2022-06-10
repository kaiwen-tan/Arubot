import discord
from typing import Optional
from discord.ext import commands


class Pollclass(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, aliases=['poll'])
    async def quickpoll(self, ctx, question, *options: str):
        if len(options) <= 1:
            await ctx.send('You need more than one option to make a poll!')
            return
        if len(options) > 10:
            await ctx.send('You cannot make a poll for more than 10 things!')
            return

        if len(options) == 2 and options[0] == 'yes' and options[1] == 'no':
            reactions = ['<:checkmark:726120592612261920>', '❌']
        else:
            reactions = ['1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣',
                         '8️⃣', '9️⃣',
                         '🔟']

        description = []
        for x, option in enumerate(options):
            description += '\n {} {}'.format(reactions[x], option)
        embed = discord.Embed(title=question, description=''.join(description))
        react_message = await ctx.send(embed=embed)
        for reaction in reactions[:len(options)]:
            await react_message.add_reaction(reaction)
        embed.set_footer(text='Poll ID: {}'.format(react_message.id))
        await react_message.edit(embed=embed)

    @commands.command(pass_context=True)
    async def tally(self, ctx, id):
        poll_message = await ctx.fetch_message(id)
        if not poll_message.embeds:
            return
        embed = poll_message.embeds[0]
        if poll_message.author != ctx.message.guild.me:
            return
        # if not embed['footer']['text'].startswith('Poll ID:'):
        #     return
        unformatted_options = [x.strip() for x in
                               embed.description.split('\n')]
        opt_dict = {x[:2]: x[3:] for x in unformatted_options} if \
            unformatted_options[0][0] == '1' \
            else {x[:1]: x[2:] for x in unformatted_options}

        voters = [
            ctx.message.guild.me.id]

        tally = {x: 0 for x in opt_dict.keys()}
        for reaction in poll_message.reactions:
            if reaction.emoji in opt_dict.keys():
                reactors = await reaction.users().flatten()
                for reactor in reactors:
                    if reactor.id not in voters:
                        tally[reaction.emoji] += 1
                        voters.append(reactor.id)

        output = 'Results of the poll for "{}":\n'.format(embed.title) + \
                 '\n'.join(
                     ['{}: {}'.format(opt_dict[key], tally[key]) for key in
                      tally.keys()])
        await ctx.send(output)


def setup(client):
    client.add_cog(Pollclass(client))
