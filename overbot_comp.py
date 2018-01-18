#Author: Peyton (Petie/Zooplug)
#Program: Overbot (Message compile)
#Description: This file specifically takes stats
##>>          and puts them into one friendly string
##>>          that can then be sent via a message in discord

def message_create(data, bTag, gametype):
    #Set gametype
    if gametype == 1:
        gametype = 'quickplay'
    elif gametype == 2:
        gametype = 'competitive'
    
    ##DATA COLLECTION##
    #Medals
    gold = str("{:.0f}".format(data['pc']['us'][gametype]['game_stats']['medals_gold']))
    silver = str("{:.0f}".format(data['pc']['us'][gametype]['game_stats']['medals_silver']))
    bronze = str("{:.0f}".format(data['pc']['us'][gametype]['game_stats']['medals_bronze']))
    #Current Season Competitive Rank:
    if gametype == 'competitive':
        compRank = str(data['pc']['us'][gametype]['overall_stats']['comprank'])
    #Current Prestige (Stars)
    prestige = data['pc']['us'][gametype]['overall_stats']['prestige']
    #Current Level
    level = str(data['pc']['us'][gametype]['overall_stats']['level'])

    #generate Master Overwatch link for profile
    bName,bNum = bTag.split('#')
    moLink = "https://masteroverwatch.com/profile/pc/global/" + bName + '-' + bNum
    #And generate overbuff link
    obLink = "https://www.overbuff.com/players/pc/" + bName + '-' + bNum 
    

    #initiates the message
    message = ''

    ##If competitive stats are called
    if gametype == 'competitive':
        #Adds the comp header to the message
        message += "**-=Competitive stats for " + bTag + "=-**\n"
        #Adds comp SR to message
        message += "Rank: " + compRank + '*SR*'
        
    ##If quickplay stats are called
    if gametype == 'quickplay':
        #Adds the qp header to the message
        message += "**-=Quickplay stats for " + bTag + "=-**\n"
        
    #Adds player prestige(stars) level to message
    if prestige == 0:
        message += '\nLevel: '
    else:
        message += '\nLevel: ' + str(prestige)

    #Adds player base level to message
    if int(level) < 10 and prestige > 0:
        level = '0' + level
    message += level + "\nMedals(Gold/Silver/Bronze): "
    #Adds Medals to message
    message += gold + "/" + silver + "/" + bronze

    #Adds Master Overwatch and Overbuff links to end of message:
    message += "\n\nMore at:\n● <" + moLink + '>'
    message += "\n● <" + obLink + '>'


    return message
