#Author: Peyton (Petie/Zooplug)
#Program: Overbot (Message compile)
#Description: This file specifically takes stats
##>>          and puts them into one friendly string
##>>          that can then be sent via a message in discord

import asyncio
import aiohttp
import discord
from overwatch_api.core import AsyncOWAPI
from overwatch_api.constants import *

async def top_heroes(bTag):
    # Instantiating the api
    client = AsyncOWAPI()

    data = {}
    heroes = {}
    count = 1
    blizzID=bTag

    file = open('heroes.txt','r').read()
    heroes = eval(file)

    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        data[PC] = await client.get_hero_stats(blizzID, session=session, platform=PC)

    mostTimeHero=0
    mostTimeAtt=0
    mostTimeDef=0
    mostTimeTank=0
    mostTimeSupp=0
    
    mostPlayedAtt='None'
    mostPlayedDef='None'
    mostPlayedTank='None'
    mostPlayedSupp='None'
    mostPlayedHero='None'
    heroType='attack'
    topHeroType='None'
    
    while count <= 23:

        if (data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]] > mostTimeHero):
            mostPlayedHero=str(count)
            mostTimeHero = data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]]
            topHeroType=heroType

        if (data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]] > mostTimeAtt and heroType=='attack'):
            mostPlayedAtt=str(count)
            mostTimeAtt = data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]]

        elif (data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]] > mostTimeDef and heroType=='defence'):
            mostPlayedDef=str(count)
            mostTimeDef = data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]]

        elif (data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]] > mostTimeTank and heroType=='tank'):
            mostPlayedTank=str(count)
            mostTimeTank = data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]]

        elif (data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]] > mostTimeSupp and heroType=='support'):
            mostPlayedSupp=str(count)
            mostTimeSupp = data['pc']['us']['playtime']['quickplay'][heroes[heroType][str(count)]]
        
        count+=1
        if count==8:
            heroType='defence'
        elif count==14:
            heroType='tank'
        elif count==20:
            heroType='support'
        
        
    topHeroes={'mostPlayedHero':heroes[topHeroType][str(mostPlayedHero)],
    'mostPlayedAtt':heroes['attack'][str(mostPlayedAtt)],
    'mostPlayedDef':heroes['defence'][str(mostPlayedDef)],
    'mostPlayedTank':heroes['tank'][str(mostPlayedTank)],
    'mostPlayedSupp':heroes['support'][str(mostPlayedSupp)]}

    return topHeroes

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(testing(loop))

