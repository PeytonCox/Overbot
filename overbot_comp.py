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

    #generate profile links and compose them into a string for output
    bName,bNum = bTag.split('#')
    moLink = "https://masteroverwatch.com/profile/pc/global/" + bName + '-' + bNum
    #And generate overbuff link
    obLink = "https://www.overbuff.com/players/pc/" + bName + '-' + bNum ##Currently unused in this version, but may bring back later
    owLink = "https://playoverwatch.com/en-us/career/pc/" + bName + '-' + bNum
    profLinks = "[Official Profile](" + owLink + ") | [Master Overwatch](" + moLink + ") | [Overbuff](" + obLink + ")"

    #initiate the embed and also provide link to Master Overwatch profile
    #embed=discord.Embed(title="Master Overwatch Link", url=moLink, color=0xE69138)

    #List who the stats are for
    embed=discord.Embed(title="", value="Region: US     Platform: PC", color=0xE69138) #temporary hardcode region and platform

    #uses compRank to determine rank icon link
    icon=icon_select(compRank)

    embed.set_author(name= bTag + " Competitive Stats", url=owLink, icon_url=icon)

    #Adds player base level to message
    if int(level) < 10 and prestige > 0:
        level = '0' + level

    #Adds player prestige(stars) level to message
    if prestige == 0:
        embed.add_field(name='Level: ', value=level, inline=True)
    else:
        embed.add_field(name='Level:', value=str(prestige)+level, inline=True)

    #Add Season Rating/Rank
    embed.add_field(name="Season Rating:", value=compRank, inline=True)

    #Add Medals to Embed
    embed.add_field(name="Medals(Gold/Silver/Bronze): ", value=gold + "/" + silver + "/" + bronze, inline=False)

    embed.add_field(name="Profile Links:", value=profLinks, inline=False)


    return embed

def icon_select(compRank):
    #default web prefix
    icon="http://pcox.club/resources/"

    #convert back to int
    compRank=int(compRank)
    
    if compRank > 0 and compRank < 1500:
        icon += "Competitive_Bronze_Icon.png"
    elif compRank >= 1500 and compRank < 2000:
        icon += "Competitive_Silver_Icon.png"
    elif compRank >= 2000 and compRank < 2500:
        icon += "Competitive_Gold_Icon.png"
    elif compRank >= 2500 and compRank < 3000:
        icon += "Competitive_Platinum_Icon.png"
    elif compRank >= 3000 and compRank < 3500:
        icon += "Competitive_Diamond_Icon.png"
    elif compRank >= 3500 and compRank < 4000:
        icon += "Competitive_Master_Icon.png"
    elif compRank >= 4000 and compRank < 5000:
        icon += "Competitive_Grandmaster_Icon.png"
    else:
        icon += "Competitive_Grandmaster_Icon.png" #filler
    

    return icon
