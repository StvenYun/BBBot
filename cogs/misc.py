import discord
from discord.ext import commands
import random
import aiohttp

class Misc(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('misc.py injected')

    #Commands


    #watch2gether link
    @commands.command(name = 'watch', help='watch2gether link')
    async def watch(self, ctx):
        await ctx.send(f'https://w2g.tv/rooms/bangbus-p86zqt6c5vgldqervi?lang=en')


    #coinflip
    @commands.command(name = 'coin', help='flips a coin')
    async def coin(self, ctx):
        choices = ['Heads', 'Tails']
        coinflip = random.choice(choices)
        embed = discord.Embed(
        )

        if coinflip == 'Heads':
            embed.set_author(name='Heads',
                             icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/2/2e/US_One_Cent_Obv.png/1200px-US_One_Cent_Obv.png')
        else:
            embed.set_author(name='Tails',
                             icon_url='https://upload.wikimedia.org/wikipedia/commons/thumb/d/da/US_One_Cent_Rev.png/220px-US_One_Cent_Rev.png')
        await ctx.send(embed=embed)


    #magic8ball
    @commands.command(name='8ball', help='Magic 8 ball')
    async def _8ball(self, ctx, *, question):
        responses = ['It is certain.',
                     'It is decidedly so.',
                     'Without a doubt.',
                     'Yes – definitely.',
                     'You may rely on it.',
                     'As I see it, yes.',
                     'Most likely.',
                     'Outlook good.',
                     'Yes.',
                     'Signs point to yes.',
                     'Reply hazy, try again.',
                     'Ask again later.',
                     'Better not tell you now.',
                     'Cannot predict now.',
                     'Concentrate and ask again.',
                     'Don\'t count on it.',
                     'My reply is no.',
                     'My sources say no.',
                     'Outlook not so good.',
                     'Very doubtful.',
                     'Fuck You']
        response = random.choice(responses)
        embed = discord.Embed(

            description=f'Question: {question}\nAnswer: {response}',
            color=discord.Colour.blue()
        )
        embed.set_author(name='Magic 8-Ball',
                         icon_url=f'https://avatars.slack-edge.com/2020-03-01/976199605440_9012024fe987401150d7_512.png')
        await ctx.send(embed=embed)

    @commands.command()
    async def cat(self, ctx: commands.Context):
        """Gives you a random picture of a cat"""

        async with aiohttp.ClientSession(loop=ctx.bot.loop) as session:
            async with session.get("https://aws.random.cat/meow") as r:
                data = await r.json()

        embed = discord.Embed()
        embed.set_image(url=data['file'])
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Misc(bot))