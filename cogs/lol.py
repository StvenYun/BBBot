import discord
from discord.ext import commands
import random
from bs4 import BeautifulSoup
import aiohttp
from Dictionary import dict




class LeagueOfLegends(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('lol.py injected')

    #Commands
    @commands.command(name ='op', help='Returns op.gg link')
    async def op(self, ctx, username, username1=''):

        await ctx.send(
            f'Summoner(s): {username} {username1}\nOP.GG:https://na.op.gg/summoner/userName={username}+{username1}')

    @commands.command(name ='poro', help='Returns porofessor live game link')
    async def poro(self, ctx, username, username1=''):

        await ctx.send(
            f'Summoner: {username} {username1}\nPorofessor: https://porofessor.gg/live/na/{username}%20{username1}')

    @commands.command(name = 'ugg', help='Returns u.gg build')
    async def ugg(self, ctx, champion, rank='overall'):

        await ctx.send(f'Champion: {champion}\nU.GG: https://u.gg/lol/champions/{champion}/build?rank={rank}')

    @commands.command(name='rand', help='Returns a random champion')
    async def rand(self, ctx):
        champs = ['Aatrox',
                  'Ahri',
                  'Akali',
                  'Alistar',
                  'Amumu',
                  'Anivia',
                  'Annie',
                  'Aphelios',
                  'Ashe',
                  'Aurelion Sol',
                  'Azir',
                  'Bard',
                  'Blitzcrank',
                  'Brand',
                  'Braum',
                  'Caitlyn',
                  'Camille',
                  'Cassiopeia',
                  'Cho\'Gath'
                  'Corki',
                  'Darius',
                  'Draven',
                  'Dr.Mundo',
                  'Diana',
                  'Ekko',
                  'Elise',
                  'Evelynn',
                  'Ezreal',
                  'Fiddlesticks',
                  'Fiora',
                  'Fizz',
                  'Galio',
                  'Gangplank',
                  'Garen',
                  'Gnar',
                  'Gragas',
                  'Graves',
                  'Hecarim',
                  'Heimerdinger',
                  'Illaoi',
                  'Irelia',
                  'Ivern',
                  'Janna',
                  'Jarven IV',
                  'Jax',
                  'Jayce',
                  'Jhin',
                  'Jinx',
                  'Kai\'Sa',
                  'Kalista',
                  'Karma',
                  'Karthus',
                  'Kassadin',
                  'Katarina',
                  'Kayle',
                  'Kayn',
                  'Kennen',
                  'Kha\'Zix',
                  'Kindred',
                  'Kled',
                  'Kog\'Maw',
                  'LeBlanc',
                  'Lee Sin',
                  'Leona',
                  'Lillia',
                  'Lissandra',
                  'Lucian',
                  'Lulu',
                  'Lux',
                  'Malphite',
                  'Lux',
                  'Malphite',
                  'Malzahar',
                  'Maokai',
                  'Master Yi',
                  'Miss Fortune',
                  'Mordekaiser',
                  'Morgana',
                  'Nami',
                  'Nasus',
                  'Nautilus',
                  'Neeko',
                  'Nidalee',
                  'Nocturne',
                  'Nunu & Willump',
                  'Olaf',
                  'Orianna',
                  'Ornn',
                  'Pantheon',
                  'Poppy',
                  'Pyke',
                  'Qiyana',
                  'Quinn',
                  'Rakan',
                  'Rammus',
                  'Rek\'Sai',
                  'Rell',
                  'Renekton',
                  'Rengar',
                  'Riven',
                  'Rumble',
                  'Ryze',
                  'Samira',
                  'Sejuani',
                  'Senna',
                  'Seraphine',
                  'Sett',
                  'Shaco',
                  'Shen',
                  'Shyvana',
                  'Singed',
                  'Sion',
                  'Sivir',
                  'Skarner',
                  'Sona',
                  'Soraka',
                  'Swain',
                  'Sylas',
                  'Syndra',
                  'Tahm Kench',
                  'Taliyah',
                  'Talon',
                  'Taric',
                  'Teemo',
                  'Thresh',
                  'Tristana',
                  'Trundle',
                  'Tryndamere',
                  'Twisted Fate',
                  'Twitch',
                  'Udyr',
                  'Urgot',
                  'Varus',
                  'Vayne',
                  'Veigar',
                  'Vel\'Koz',
                  'Vi',
                  'Viktor',
                  'Vladimir',
                  'Volibear',
                  'Warwick',
                  'Wukong',
                  'Xayah',
                  'Xerath',
                  'Xin Zhao',
                  'Yasuo',
                  'Yone',
                  'Yorick',
                  'Yuumi',
                  'Zac',
                  'Zed',
                  'Ziggs',
                  'Zilean',
                  'Zoe',
                  'Zyra']

        randchamp = random.choice(champs)

        embed = discord.Embed(

            description=f'uwu   \nhttps://u.gg/lol/champions/{randchamp}/build?rank=overall',
            color=discord.Colour.blue()
        )

        embed.set_author(name=f'{randchamp}',
                         icon_url=f'https://static.u.gg/assets/lol/riot_static/10.25.1/img/champion/{randchamp}.png')

        embed.set_thumbnail(url=f'https://static.u.gg/assets/lol/riot_static/10.25.1/img/champion/{randchamp}.png')

        # await ctx.send(f'uwu: {randchamp}\nGuide: https://u.gg/lol/champions/{randchamp}/build?rank=overall')
        await ctx.send(embed=embed)


    @commands.command(name='opgg', help='Returns opgg for one summoner')
    async def opgg(self, ctx, username, username1='', username2='', username3='', username4=''):
        url = f'https://na.op.gg/summoner/userName={username}+{username1}+{username2}+{username3}+{username4}'
        print(url)
        async with aiohttp.ClientSession(loop=self.bot.loop) as session:
            async with session.get(url) as response:
                soups = await response.read()
        response = soups

        soup = BeautifulSoup(response, 'html.parser')
        name = soup.find('div', class_='Information').span.text

        # Profile Pic
        profilePic = soup.find('div', class_='ProfileIcon')
        profPic = profilePic.find('img', class_='ProfileImage').get('src')

        # Rank
        rankPic = soup.find('div', class_='SummonerRatingMedium')

        raPic = rankPic.find('img', class_='Image').get('src')

        if raPic != '//opgg-static.akamaized.net/images/medals/default.png?image=q_auto:best&v=1':

            rank = soup.find('div', class_='TierRank').text
            lp = soup.find('div', class_='TierInfo').span.text.strip()

            wins = soup.find('span', class_='wins').text
            losses = soup.find('span', class_='losses').text
            winRatio = soup.find('span', class_='winratio').text

        else:
            raPic = '//opgg-static.akamaized.net/images/medals/default.png?image=q_auto:best&v=1'
            rank = 'Unranked'
            lp = 'N/a'
            wins = '0W'
            losses = '0L'
            winRatio = '0%'

        ladder = soup.find('div', class_='LadderRank')  # .text.strip()
        # *************************************************************
        if ladder is not None:
            ladder = soup.find('div', class_='LadderRank').text.strip()
        # *************************************************************
        else:
            ladder = 'N/a'

        # Recent Stats
        # *************************************************************
        recentGames = soup.find('span', class_='total')

        if recentGames is not None:
            # *************************************************************
            recentGames = soup.find('span', class_='total').text
            recentWin = soup.find('span', class_='win').text
            recentLoss = soup.find('span', class_='lose').text
            # recentPercent = soup.find('div', class_='WinRatioGraph-summary')
            # recPercent = recentPercent.find('div', class_='Text').text
            #
            # print(recPercent)
            kills = soup.find('span', class_='Kill').text
            death = soup.find('span', class_='Death').text
            assist = soup.find('span', class_='Assist').text
            kdaRatio = soup.find('span', class_='KDARatio').text
            kPA = soup.find('span', class_='CKRate tip').span.text

        else:
            recentGames = '0'
            recentWin = '0'
            recentLoss = '0'
            kills = '0'
            death = '0'
            assist = '0'
            kdaRatio = '0'
            kPA = '0'

        # Recently Played with
        # if soup.find_all('div', class_='Recently Played With (Recent 10 Games)'):

        ###############################################################################################################

        # recPlay=[]
        #
        # recentlyPlayed = soup.find_all('td', class_='SummonerName Cell left_select_played_with_summoner')
        # gameCell = soup.find_all('td', class_='GameCount Cell')
        # winCell = soup.find_all('td', class_='Win Cell')
        # loseCell = soup.find_all('td', class_='Lose Cell')
        # wrCell = soup.find_all('td', class_='WinRatio Cell')
        #
        # for x in recentlyPlayed, gameCell, winCell, loseCell, wrCell:
        #     recent = x.text.strip()
        #     recPlay.append(recent)
        #
        # print(recPlay)

        ###################################################################################################
        playedWith = soup.find('div', class_='SummonersMostGame Box')

        if playedWith is not None:

            recentlyPlayed = soup.find_all('td', class_='SummonerName Cell left_select_played_with_summoner')

            players = []

            for j in recentlyPlayed:
                player = j.text.strip()
                players.append(player)
            #####################################################
            gameCell = soup.find_all('td', class_='GameCount Cell', limit=3)

            gameCount = []

            for k in gameCell:
                games = k.text.strip()
                gameCount.append(games)
            #####################################################
            winCell = soup.find_all('td', class_='Win Cell', limit=3)

            winCount = []

            for l in winCell:
                win = l.text.strip()
                winCount.append(win)
            #####################################################
            loseCell = soup.find_all('td', class_='Lose Cell', limit=3)

            loseCount = []

            for m in loseCell:
                loss = m.text.strip()
                loseCount.append(loss)
            #####################################################
            wrCell = soup.find_all('td', class_='WinRatio Cell', limit=3)

            wrCount = []

            for n in wrCell:
                wr = n.text.strip()
                wrCount.append(wr)

        else:
            players = []
        #     players = ['N/a', 'N/a', 'N/a']
        #     gameCount = ['0', '0', '0']
        #     winCount = ['0', '0', '0']
        #     loseCount = ['0', '0', '0']
        #     wrCount = ['0', '0', '0']

        ####### IF STATEMENT FOR RECENTLY PLAYED AND FOR LOOP FOR FORMATTING THE EMBED STATEMENT

        ####### FIX FOR IF RECENT PLAYERS IS LESS THAN 1 (maybe check limits) Maybe check list size and then recently played

        recent = soup.find('div', class_='GameItemWrap')

        if recent is not None:

            result = recent.find('div', class_='GameResult').text.strip()

            length = recent.find('div', class_='GameLength').text

            champion = recent.find('div', class_='ChampionName').a.text.strip()

            #######################EMOJI DICTIONARY################################################

            champEmoji = dict[f'{champion}']

            timestamp = recent.find('div', class_='TimeStamp')
            recentTimestamp = timestamp.find('span', class_='_timeago _timeCount').text

            recentKDA = recent.find('div', class_='KDA')

            recentKill = recentKDA.find('span', class_='Kill').text
            recentDeath = recentKDA.find('span', class_='Death').text
            recentAssist = recentKDA.find('span', class_='Assist').text

            recentStats = recent.find('div', class_='Stats')

            recentLevel = recentStats.find('div', class_='Level').text.strip()
            recentCS = recentStats.find('div', class_='CS').text.strip()

            if recentStats.find('div', class_='MMR') is not None:
                recentMMR = recentStats.find('div', class_='MMR').b.text.strip()

                mmrEmoji = dict[f'{recentMMR}']

            else:
                recentMMR = 'N/a'

                mmrEmoji = '791349848561025094'

            #####################################################################################################
            trinket = recent.find('div', class_='Items')
            ward = trinket.find('div', class_='Trinket')
            if ward is not None:
                wards = trinket.find('div', class_='Trinket').span.text
            else:
                wards = '0'

        # opScorecell = recent.find('div', class_='GameDetail')
        # recentOPScore = opScorecell.find('div', class_='OPScore Text').text
        # recentOPBadge = opScorecell.find('div', class_='OPScore Badge Score').text

        # else:
        #
        #     result = 'N/a'
        #     champion =''
        #     recentTimestamp =''
        #     recentKDA =''
        #     recentKill =''
        #     recentDeath =''
        #     recentAssist =''
        #     recentLevel =''
        #     recentCS =''
        #     recentMMR =''

        #         EMBED

        embed = discord.Embed(
            title=f'',
            description=f'{ladder}',
            color=discord.Colour.gold()
        )
        if raPic != '//opgg-static.akamaized.net/images/medals/default.png?image=q_auto:best&v=1':
            embed.set_author(name=f'{rank}   |   {lp}   |   {wins}/{losses}   |   {winRatio}',
                             icon_url=f'https:{raPic}')
        else:
            embed.set_author(name=f'{rank}   |   0   |   {wins}/{losses}   |   {winRatio}', icon_url=f'https:{raPic}')

        embed.set_thumbnail(url=f'https:{profPic}')
        embed.add_field(name="__Recent Stats__",
                        value=f'''{recentGames}G  {recentWin}W  {recentLoss}L
                        **KDA:** {kdaRatio}           
                        **KPA:**  {kPA}'''
                        , inline=True)
        #######################################RECENTLY PLAYED WITH#########################################################
        if len(players) < 1:
            embed.add_field(name="__Recently Played With__",
                            value=f'''
                            :sob: This Summoner has 0 Friends  :sob:
                            '''
                            , inline=True)

        if len(players) == 1:
            embed.add_field(name="__Recently Played With__",
                            value=f'''
                            • **{players[0]}** ({gameCount[0]} Games  |  {winCount[0]}W  {loseCount[0]}L  |  {wrCount[0]})
                            '''
                            , inline=True)
        elif len(players) == 2:
            embed.add_field(name="__Recently Played With__",
                            value=f'''
                            • **{players[0]}** ({gameCount[0]} Games  |  {winCount[0]}W  {loseCount[0]}L  |  {wrCount[0]})
                            • **{players[1]}** ({gameCount[1]} Games  |  {winCount[1]}W  {loseCount[1]}L  |  {wrCount[1]})
                            '''
                            , inline=True)
        elif len(players) > 2:
            embed.add_field(name="__Recently Played With__",
                            value=f'''
                            • **{players[0]}** ({gameCount[0]} Games  |  {winCount[0]}W  {loseCount[0]}L  |  {wrCount[0]})
                            • **{players[1]}** ({gameCount[1]} Games  |  {winCount[1]}W  {loseCount[1]}L  |  {wrCount[1]})
                            • **{players[2]}** ({gameCount[2]} Games  |  {winCount[2]}W  {loseCount[2]}L  |  {wrCount[2]})

                            '''
                            , inline=True)

        ############################################LAST GAME###############################################################
        if recent is not None:
            embed.add_field(name='__Last Game__',
                            value=f'''
                            {recentTimestamp} | Length: {length}
                            **{result}** as <:champ:{champEmoji}> {champion}  | {recentLevel} | {recentKill}/{recentDeath}/{recentAssist} | {recentCS} 
                            • ** MMR:** <:mmr:{mmrEmoji}> {recentMMR}   • ** Pinks:** <:controlward:791046593008369737> {wards}               

                            '''
                            , inline=False)

        else:
            embed.add_field(name='__Last Game__',
                            value=f'''No recent games''', inline=False)
        # {kills} / {death} / {assist}

        await ctx.send(embed=embed)


    @commands.command(name = 'uggbeta', help='Returns outline for new ugg champion builds command with custom embeds')
    async def uggbeta(self, ctx):

        embed = discord.Embed(
            title='<:Passive:791094099645300736> <:Q:791094099921862656> <:W:791094099800227890> <:E:791094099825917972> <:R:791094099864059965> | Summoner Spells: <:Flash:791088374835445812> <:Tele:791088374748282880>',
            description='__**Rune Path**__',
            color=discord.Colour.blue()
        )
        embed.set_author(name=f'Aatrox | Build for Top, Platinum+', icon_url='https://opgg-static.akamaized.net/images/medals/platinum_1.png?image=q_auto:best&v=1')
        embed.set_thumbnail(url='https://static.u.gg/assets/lol/riot_static/10.25.1/img/champion/Aatrox.png')

        embed.add_field(name='<:Precision:791086128006430750> __Precision__',
                        value='''
                        <:Conqueror:791086127977201674> Conqueror
                        <:Triumph:791086127938797568> Triumph
                        <:Tenacity:791086127801040897> Tenacity
                        <:LastStand:791086127989129236> Last Stand
                        ''', inline=True)
        embed.add_field(name='<:Domination:791087942827376670> __Domination__',
                        value='''
                            <:TasteofBlood:791086127985590272> Taste of Blood
        
                            <:RavenousHunter:791086128035135528> Ravenous Hunter
                            <:AdaptiveForce:791086127913107476> <:AdaptiveForce:791086127913107476> <:MagicResist:791086128220078110>
                            ''', inline=True)
        embed.add_field(name='__**Skill Order**__',
                        value='''
                            Q > <:Q:791094099921862656> E > <:E:791094099825917972> W > <:W:791094099800227890>
        
                            ''', inline=False)

        # Q - -E - -W - -Q - -Q - -R - -Q - -E - -Q - -E - -R - -E - -E - -W - -W - -R - -W - -W
        # <:Q: 791094099921862656 > - <:E: 791094099825917972 > - <:W: 791094099800227890 > - <:Q: 791094099921862656 > - <:Q: 791094099921862656 > - <:R: 791094099864059965 > - <:Q: 791094099921862656 > - <:E: 791094099825917972 > - <:R: 791094099864059965 > - <:E: 791094099825917972 > - <:E: 791094099825917972 > - <:W: 791094099800227890 > - <:W: 791094099800227890 > - <:R: 791094099864059965 > - <:W: 791094099800227890 > - <:W: 791094099800227890 >

        await ctx.send(embed=embed)
def setup(bot):
    bot.add_cog(LeagueOfLegends(bot))

