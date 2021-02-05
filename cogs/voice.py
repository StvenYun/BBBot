import discord
from discord.ext import commands
import speech_recognition as sr
import os
from gtts import gTTS
import warnings
import datetime
import calendar
from discord.utils import get


warnings.filterwarnings('ignore')


async def getDate():
    now = datetime.datetime.now()
    my_date = datetime.datetime.today()
    weekday = calendar.day_name[my_date.weekday()]
    monthNum = now.month
    dayNum = now.day

    month_names = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    ordinalNumbers = ['1st', '2nd', '3rd', '4th', '5th', '6th', '7th', '8th', '9th', '10th', '11th', '12th', '13th', '14th', '15th', '16th',
                      '17th', '18th', '19th', '20th', '21st', '22nd', '23rd', '24th', '25th', '26th', '27th', '28th', '29th', '30th', '31st']

    return f'Today is {weekday}, {month_names[monthNum-1]} the {ordinalNumbers[dayNum-1]}.'

class voice(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('voice.py injected')

    @commands.command()
    async def join(self, ctx):
        connected = ctx.author.voice
        if connected:
            await connected.channel.connect()  #   Use the channel instance you put into a variable

    @commands.command()
    async def leave(self, ctx):

        await ctx.voice_client.disconnect()

    @commands.command()
    async def date(self, ctx):
        date = await getDate()
        print(date)
        tts = gTTS(text='edm77 youre the best midlaner i know', lang='en')
        tts.save('text.mp3')

        print(ctx)
        vc = ctx.voice_client
        print(vc)

        vc.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f'Finished playing'))



    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        bot_client = get(self.bot.voice_clients)
    #     channel = before.channel

        # print(channel)
        person = str(member)
        # print(self)
        # print(member)
        #
        # print(f'{person[:5]}')

        # print(before)
        # print(after)

        # vc = await channel.connect()
        # print(vc)
        # tts = gTTS(text='hi hows it goin', lang='en')
        # tts.save('text.mp3')
        # vc.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f'Finished playing'))
        if after.channel != before.channel:
            if after.channel == None:
                text = f'{person[:-5]} has been ejected from {before.channel.name}.'
                # print(text)
                tts = gTTS(text=text, lang='en-gb')
                tts.save('text.mp3')

                bot_client.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f'Finished playing'))

            else:
                text = f'{person[:-5]} has entered {after.channel.name}.'
                # print(text)
                tts = gTTS(text=text, lang='en-gb')
                tts.save('text.mp3')

                bot_client.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f'Finished playing'))

        if after.self_stream != before.self_stream:
            if after.self_stream == True:
                text = f'{person[:-5]} started streaming.'
                tts = gTTS(text=text, lang='en-gb')
                tts.save('text.mp3')
                bot_client.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f'Finished playing'))
            else:
                text = f'{person[:-5]} stopped streaming.'
                tts = gTTS(text=text, lang='en-gb')
                tts.save('text.mp3')
                bot_client.play(discord.FFmpegPCMAudio('text.mp3'), after=lambda e: print(f'Finished playing'))


def setup(bot):
    bot.add_cog(voice(bot))

