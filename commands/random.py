import random, nextcord

def coinflip():
    coin = ["Heads", "Tails"]
    choice = random.choice(coin)


    if (choice == "Heads"):
        embed=nextcord.Embed(title="Coinflip", description="Heads", color=0x958e8e)
        embed.set_thumbnail(url="https://washington-quarters.com/coins/300x300/1968-quarter-obverse.png")
        embed.set_footer(text="PandaBotv3")
        return embed

    else:
        embed=nextcord.Embed(title="Coinflip", description="Tails", color=0x958e8e)
        embed.set_thumbnail(url="https://washington-quarters.com/coins/300x300/1968-quarter-reverse.png")
        embed.set_footer(text="PandaBotv3")
        return embed

def randomnum(mssg):
    varlist = mssg.split(" ")
    try:
        magicnum= int(varlist[1])
    except:
        return "Thats not a number dumb dumb"
    if (len(varlist) == 1 or magicnum/magicnum != 1):
        ten = [1,2,3,4,5,6,7,8,9,10]
        tennum = random.choice(ten)
        return f"A random number out of 10 is: {tennum}"
    else:
        youngervalue = [i for i in range(magicnum)]
        x = random.choice(youngervalue)
        return f"A random number from 1 to {magicnum} is: ***{x+1}***"