#Ignore the messy import statements, this is mostly used to debug and makes life easy with docker
import nextcord
from datetime import datetime, date
from nextcord.ext import commands
from nextcord.ext import *
from commands.merch import *
from commands.pandacam import pandacam
from commands.ping import *
from commands.random import coinflip, randomnum
from commands.rockpapersissors import rps
from commands.help import *
from commands.panda import *
from commands.ratelimit import *
from files.channelcheck import channelcheck


#################################################
#PUT YOUR BOT ID DOWN BELOW
botID = ""
#################################################

#################################################
#PUT YOUR PREFIX DOWN BELOW [default = !]
commandPrefix = ''
#################################################

#################################################
#This is just to handle DMs, it sets up the dm in a nice format
#and plops it in a channel of your choice
#If you want to use this, place the prefered channel ID below
pmChannel = 0
#################################################


#Ignore this unless you know what you are doing
intents = nextcord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True


#Sets the "Activity" of the bot, defaults to 'Playing' but can be changed
activityname = ''
activity = nextcord.Activity(type=nextcord.ActivityType.playing, name=activityname)
pandabot = commands.Bot(command_prefix='!', intents=intents, activity=activity)

#Console startup message
@pandabot.event
async def on_ready(): 
    print('We have logged in as {0.user}'.format(pandabot))
    print("testing bot active")


@pandabot.event
async def on_message(message):
    #Checks if the message was sent in a DM or public channel
    ifdm = channelcheck(message.channel)

    ###########################################################
    #If message was detected as a DM and pmChannel is not equal to 0
    if ifdm == True and message.author != pandabot.user and pmChannel != 0:
        today = date.today()
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        dm = message.channel
        await dm.send("Hey whats good? Idk what you are asking of me (yet) but ill pass it onto my owner")
        embed = nextcord.Embed(title = 'DM Received', description = f'{message.content}', color = 0x9fffff)
        channel = pandabot.get_channel(pmChannel)
        embed.set_footer(text=f'Sent by {message.author.display_name} | {today} {current_time}')
        await channel.send(embed=embed)
    ###########################################################


    #Make sure the bot doesnt run off its own commands, useful later for reactions
    usrname = str(message.author)
    if message.author == pandabot.user:
        return

############################################################################################
    #This is where the commands start, I made it easy by using elif statements,
    #all commands are their own file in the ./commands folder and return something here
    #if you were to add or take away any commands just mess with these elif statements
    
    #Descriptions for all the default commands can be found in at ./commands/help.py
   
   
    if message.content.startswith(commandPrefix): #Command Hub
        
        #makes all command messages lowercase, makes it easier to parse
        messg = (message.content)
        mssg = messg.lower()

        if (mssg == commandPrefix+"ping"): # PING command
            await message.channel.send(ping(mssg))

        elif (mssg == commandPrefix+"merch"): # I need to make money somehow
            await message.channel.send(embed=merch())

        elif (mssg == commandPrefix+"pandacam"): 
            await message.channel.send(embed=pandacam())
            
        elif (commandPrefix+"rps" in mssg):
            rpsresult = rps(mssg)
            if (rpsresult == "bad"):
                await message.channel.send("You have to pick either Rock, Paper, or Scissors.")
            else:
                await message.channel.send(embed=rpsresult)

        elif (mssg == commandPrefix+"panda"):
            await message.channel.send(get_panda()) 

        elif (mssg == commandPrefix+"lore"):
            lore = "./files/lore.mp4"
            await message.channel.send("Brought to you by Sam L:")
            await message.channel.send(file=nextcord.File(lore))

        elif (mssg == commandPrefix+"coinflip"):
            await message.channel.send(embed=coinflip())

        elif(commandPrefix+"random" in mssg or commandPrefix+"roll" in mssg):
            await message.channel.send(randomnum(mssg))  
  
        elif (commandPrefix+"help" in mssg or commandPrefix+"commands" in mssg):
            if (messg == commandPrefix+"help" or mssg == commandPrefix+"commands"):
                await message.channel.send(embed=helpembed())
            else: 
                await message.channel.send(help(mssg))

        else:
            print(f"idk what to do with {mssg}")
    

##########################################################################################
    #Reactions are also left for elif commands but are not currently included in any
    #message with the prefix above.
    #!bread or !panda should not produce any reactions b/c they are passed off as commands
    elif ("panda" in message.content or "Panda" in message.content):
        panda = "🐼"
        await message.add_reaction(panda)

    elif ("Damn" in message.content or "damn" in message.content):
        await message.channel.send("https://media.discordapp.net/attachments/884919548061548598/934905967513075742/Kendrick_Lamar_-_Damn.png")

#Dont mess with this
pandabot.run(botID)
