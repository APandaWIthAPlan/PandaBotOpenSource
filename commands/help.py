import nextcord
def help(message):

    if(message == "!help help"):
        return "wtf are you on?"

    elif("ping" in message):
        return "Just something to check if I'm awake"

    elif("merch" in message):
        return "rep the merch"
    
    elif("coinflip" in message):
        return "Heads or Tails?"

    elif("random" in message or "roll" in message):
        return "Legit just a random number generator"    

    elif("pandacam" in message):
        return "If you get bored during class"

    elif("panda" in message):
        return "I scan a really stupid API and find a random panda image"

    elif("lore" in message):
        return "Brought to you by Sam L."

    elif("rps" in message):
        return "A completly randomated Rock Paper Scissors game"

    else:
        return "Idk what to do with that cause thats not a command"


def helpembed():
        embed1=nextcord.Embed(title="Command List:", description="!help [command] for more info", color=0xc7c7c7)
        embed1.set_thumbnail(url="https://media.discordapp.net/attachments/647983568542367764/892425948350283876/image0.png?width=663&height=663")
        embed1.add_field(name="--------------", value="⠀", inline=False)
        embed1.add_field(name="!help", value="this page", inline=True)
        embed1.add_field(name="!merch", value="merch store", inline=False)
        embed1.add_field(name="!lore", value="learn the history", inline=False)
        embed1.add_field(name="!panda", value="random panda image", inline=False)
        embed1.add_field(name="!pandacam", value="live camera of a panda", inline=False)
        embed1.add_field(name="!ping", value="pong", inline=False)
        embed1.add_field(name="!coinflip", value="returns a coinflip", inline=False)
        embed1.add_field(name="!random [number] / !roll [number]", value="random number generator", inline=False)
        embed1.add_field(name="!rps [rock, paper, scissors]", value="Rock, Paper, Scissors baybee", inline=False)
        embed1.set_footer(text="PandaBotOS")
        return embed1
