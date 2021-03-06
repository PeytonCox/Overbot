#Author: Peyton (Petie/Zooplug)
#Program: Overbot
#Description: This is a discord bot specifically created
##>>          for various utilities regarding Overwatch by
##>>          Blizzard Ent.

import discord
import asyncio
import aiohttp
from overbot_comp import message_create
from overbot_heroes import top_heroes
from overwatch_api.core import AsyncOWAPI
from overwatch_api.constants import *

#bot setup
client = discord.Client()

#Token Grab
TF = open('token.txt','r')
token = TF.read()
TF.close()

#Display bot info on launch
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

@client.event
async def on_message(message):
    ###!comp chat command###
    if message.content.startswith('!comp'):
        botmsg = await client.send_message(message.channel, 'Grabbing stats...')

        bTag = message.content[len('!comp'):].strip() #grabs !comp command and strips "!comp" from the message

        #if the user entered !comp without an argument
        if not bTag:
            await botmsg_delete(botmsg)
            await client.send_message(message.channel, 'You must provide a battletag! (ex. !comp Petie#2812)')
            return
        #a help option for !comp to explain how to us it
        elif bTag == 'help' or bTag == 'Help' or bTag == 'h' or bTag == 'H':
            await botmsg_delete(botmsg)
            await client.send_message(message.channel, '```This command is used by typing your battletag after !comp (ex. !comp Petie#2812)```')
            return
        else:
            pass

        try:
            #Runs stat_grab with provided bTag (More details in stat_grab)
            data,topHeroes = await stat_grab(bTag)
            #Does this user have competitive stats? (I may have it redirect to the quickplay command later if false)
            if data['pc']['us']['competitive']['overall_stats']['comprank']:
                #Runs message_create function from overbot_comp
                embed = message_create(data, bTag, topHeroes)
            else:
                await client.send_message(message.channel, 'No competitive stats for ' + bTag + '!')
                print("[!!!]No comp stats for " + bTag)
                await botmsg_delete(botmsg)
                return
            await botmsg_delete(botmsg) #delete old grabbing stats message
            await client.send_message(message.channel, embed=embed) #send message with stats
        except:
            await botmsg_delete(botmsg) #delete old grabbing stats message
            #Create console report for failed stat grab
            print("[!!!]Error grabbing comp stats for " + bTag)
            await client.send_message(message.channel, "Error grabbing stats... :cry: \nMaybe retry?")



        
async def stat_grab(bTag):
    # Instantiating the api
    client = AsyncOWAPI()
    #initiate some variables
    data = {}
    topHeroes={}
    stat_success = 0
    tries = 0
    blizzID=bTag
    
    async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(verify_ssl=False)) as session:
        #attempt 3 times to grab stats (sometimes it times out)
        while stat_success == 0 & tries < 3:
            #try to grab stats and store them in dict 'data'
            try:
                data[PC] = await client.get_stats(blizzID, session=session, platform=PC)
                topHeroes = await top_heroes(bTag)
                stat_success = 1
            #after 5 timeouts, report error and exit
            except:
                print("Failed...retrying.")
                tries += 1
                if tries == 5:
                    return "Error grabbing stats.."
        return data,topHeroes

#just to make the code a little easier to read
async def botmsg_delete(botmsg):
    await client.delete_message(botmsg)
    return
        
#client ID for discord, to be removed during git upload
client.run(token)
