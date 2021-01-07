from discord.ext import commands


#######################KEY COMPONENT#########################
class Example(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

#######################KEY COMPONENT#########################

    #Events

    @commands.Cog.listener()
    async def on_ready(self):
        print('example.py injected')

    #Commands

    @commands.command(name='ping', help='Returns latency between bot,api, and database')
    async def ping(self, ctx):
        await ctx.send(f'Pong! { round(self.bot.latency*1000)} ms')







#######################KEY COMPONENT#########################

def setup(bot):
    bot.add_cog(Example(bot))

#######################KEY COMPONENT#########################
