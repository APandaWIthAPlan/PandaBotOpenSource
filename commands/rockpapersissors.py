import random, nextcord
def botchoice():
    choices = ["rock", "paper", "scissors"]
    x = random.choice(choices)
    return x

def whowon(player, bot):
    rock = "rock"
    paper = "paper"
    scissors = "scissors"

    if (player == bot):
        return 2

    if (player == rock):
        if (bot == paper):
            return 0
        else:
            return 1
    
    if (player == paper):
        if (bot == scissors):
            return 0
        else:
            return 1

    if (player == scissors):
        if (bot == rock):
            return 0
        else:
            return 1

def embedbuild(player, bot, result):
    if (result == 0):
        temp1 = "You Lose!"
    elif (result == 1):
        temp1 = "You Win!"
    else:
        temp1 = "We Tied!"

    if (player == "rock"):
        playeremoji = "🪨"
    elif(player == "paper"):
        playeremoji = "📜"
    else:
        playeremoji = "✂️"

    if (bot == "rock"):
        botemoji = "🪨"
    elif(bot == "paper"):
        botemoji = "📜"
    else:
        botemoji = "✂️"

    embed=nextcord.Embed(title="Rock, Paper, Scissors", description=temp1, color=0x958e8e)
    embed.set_thumbnail(url="https://media.discordapp.net/attachments/647983568542367764/892425948350283876/image0.png?width=663&height=663")
    embed.add_field(name="You Picked:", value=playeremoji, inline=True)
    embed.add_field(name="I Picked:", value=botemoji, inline=True)
    embed.set_footer(text="PandaBotv3")
    return embed

def rps(mssg):
    varlist = mssg.split(" ")
    if len(varlist) == 1:
        return "bad"
    player = varlist[1]
    if (player == "rock" or player == "paper" or player == "scissors"):
        bot = botchoice()
        result = whowon(player, bot)
        final = embedbuild(player,bot,result)
        return final
        
    else:
        return "bad"



# Rock > Scissors > Paper