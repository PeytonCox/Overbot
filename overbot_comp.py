#Author: Peyton (Petie/Zooplug)
#Program: Overbot (Message compile)
#Description: This file specifically takes stats
##>>          and puts them into one friendly string
##>>          that can then be sent via a message in discord

import discord

def message_create(data, bTag):

    gametype = 'competitive'
    
    ##DATA COLLECTION##
    #Medals
    gold = str("{:.0f}".format(data['pc']['us'][gametype]['game_stats']['medals_gold']))
    silver = str("{:.0f}".format(data['pc']['us'][gametype]['game_stats']['medals_silver']))
    bronze = str("{:.0f}".format(data['pc']['us'][gametype]['game_stats']['medals_bronze']))
    #Current Season Competitive Rank:
    compRank = str(data['pc']['us'][gametype]['overall_stats']['comprank'])
    #Current Prestige (Stars)
    prestige = data['pc']['us'][gametype]['overall_stats']['prestige']
    #Current Level
    level = str(data['pc']['us'][gametype]['overall_stats']['level'])

    #generate Master Overwatch link for profile
    bName,bNum = bTag.split('#')
    moLink = "https://masteroverwatch.com/profile/pc/global/" + bName + '-' + bNum
    #And generate overbuff link
    #obLink = "https://www.overbuff.com/players/pc/" + bName + '-' + bNum ##Currently unused in this version, but may bring back later

    #initiate the embed and also provide link to Master Overwatch profile
    embed=discord.Embed(title="Master Overwatch Link", url=moLink, color=0xE69138)

    #List who the stats are for
    embed.add_field(name='-=Comp Stats for ' + bTag + '=-', value="Region: US     Platform: PC", inline=False) #temporary hardcode region and platform

    #Adds player base level to message
    if int(level) < 10 and prestige > 0:
        level = '0' + level

    #Adds player prestige(stars) level to message
    if prestige == 0:
        embed.add_field(name='Level: ', value=level, inline=False)
    else:
        embed.add_field(name='Level:', value=str(prestige)+level, inline=False)

    #Add Season Rating/Rank
    embed.add_field(name="Season Rating:", value=compRank, inline=False)

    #Add Medals to Embed
    embed.add_field(name="Medals(Gold/Silver/Bronze): ", value=gold + "/" + silver + "/" + bronze, inline=False)


    return embed
