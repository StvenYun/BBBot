import discord
from discord.ext import commands
from bs4 import BeautifulSoup
import aiohttp
import mysql.connector
from decouple import config
from dateutil import parser

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password=config('mydbpassword'),
    database="userlevels",
    auth_plugin="mysql_native_password"

)

async def iterate(ctx, list):
    for i in range(len(list)):
        return list[i]

async def getBalance(ctx):
    client_id = ctx.author.id
    cursor = mydb.cursor()
    cursor.execute(f'''SELECT user_xp FROM users WHERE client_id = {client_id}''' )
    result = cursor.fetchall()
    mydb.commit()
    return(result[0][0])

async def updateAVG(ctx, stock, amount, price):
    client_id = ctx.author.id
    cursor = mydb.cursor()
    cursor.execute(f'''SELECT avg_price, number_of_stock FROM portfolio WHERE client_id = {client_id}''')
    result = cursor.fetchall()
    mydb.commit()

class test(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('test.py injected')

    @commands.command(name='port', help='Returns your stock portfolio')
    async def port(self, ctx):
        client_id = ctx.author.id
        author = ctx.message.author
        pfp = author.avatar_url
        cursor = mydb.cursor(buffered=True)
        cursor.execute(f'''SELECT stock, number_of_stock FROM portfolio WHERE client_id = '{client_id}'
                           ''')
        stock = cursor.fetchall()
        mydb.commit()


        #############Retrieves stock and amount from tuple############

        first_tuple_elements = []
        for a_tuple in stock:
            first_tuple_elements.append(a_tuple[0])

        print(first_tuple_elements)

        second_tuple_elements = []
        for a_tuple in stock:
            second_tuple_elements.append(a_tuple[1])
        print(second_tuple_elements)

        print(len(first_tuple_elements))

        stock_string = ''
        for i in first_tuple_elements:
            stock_string += ('\n' + i)

        #######list of int to list of string#######
        second_tuple = [str(x) for x in second_tuple_elements]
        amount_string = ''
        for i in second_tuple:
            amount_string += ('\n' + i)













        balance = await getBalance(ctx)



        embed = discord.Embed(
            title=f'''Balance = ${balance}''',
            color=discord.Colour.gold()
        )

        if len(stock)<1:
            embed.add_field(name='__Stock__',
                            value=f'''
                            None
                            ''',
                            inline=True)
            embed.add_field(name='__Amount__',
                            value=f'''
                            0
                            ''',
                            inline=True)

            embed.add_field(name='__$__',
                            value=f'''
                            0
                            ''',
                            inline=True)
        else:
            embed.add_field(name='__Stocks__',
                            value=f'''{stock_string}''',
                            inline=True)

            embed.add_field(name='__Amount__',
                            value=f'''{amount_string}''',
                            inline=True)
        # if len(stock)<1:
        #     embed.add_field(name='__Stock__',
        #                     value=f'''
        #                     None
        #                     ''',
        #                     inline=True)
        #     embed.add_field(name='__Amount__',
        #                     value=f'''
        #                     0
        #                     ''',
        #                     inline=True)
        #
        #     embed.add_field(name='__$__',
        #                     value=f'''
        #                     -
        #                     ''',
        #                     inline=True)
        # elif len(stock) == 1:
        #     embed.add_field(name='__Stock__',
        #                     value=f'''
        #                     {stock[0][0]}
        #                     ''',
        #                     inline=True)
        #     embed.add_field(name='__Amount__',
        #                     value=f'''
        #                     {number[0][0]}
        #                     ''',
        #                     inline=True)
        #
        #     embed.add_field(name='__$__',
        #                     value=f'''
        #                     -
        #                     ''',
        #                     inline=True)
        # elif len(stock) == 2:
        #     embed.add_field(name='__Stock__',
        #                     value=f'''
        #                     {stock[0][0]}\n{stock[1][0]}
        #                     ''',
        #                     inline=True)
        #     embed.add_field(name='__Amount__',
        #                     value=f'''
        #                     {number[0][0]}\n{number[1][0]}
        #                     ''',
        #                     inline=True)
        #
        #     embed.add_field(name='__$__',
        #                     value=f'''
        #                     -
        #                     ''',
        #                     inline=True)
        # elif len(stock) == 3:
        #     embed.add_field(name='__Stock__',
        #                     value=f'''
        #                     {stock[0][0]}\n{stock[1][0]}\n{stock[2][0]}
        #                     ''',
        #                     inline=True)
        #     embed.add_field(name='__Amount__',
        #                     value=f'''
        #                     {number[0][0]}\n{number[1][0]}\n{number[2][0]}
        #                     ''',
        #                     inline=True)
        #
        #     embed.add_field(name='__$__',
        #                     value=f'''
        #                     -
        #                     ''',
        #                     inline=True)
        # elif len(stock) == 4:
        #     embed.add_field(name='__Stock__',
        #                     value=f'''
        #                     {stock[0][0]}\n{stock[1][0]}\n{stock[2][0]}\n{stock[3][0]}
        #                     ''',
        #                     inline=True)
        #     embed.add_field(name='__Amount__',
        #                     value=f'''
        #                     {number[0][0]}\n{number[1][0]}\n{number[2][0]}\n{number[3][0]}
        #                     ''',
        #                     inline=True)
        #
        #     embed.add_field(name='__$__',
        #                     value=f'''
        #                     -
        #                     ''',
        #                     inline=True)

        embed.set_thumbnail(url=pfp)

        embed.set_author(name=f'''{ctx.author.name}'s Stonk Portfolio''',
                         icon_url='https://cdn.iconscout.com/icon/free/png-512/apple-stock-493158.png')

        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(test(bot))