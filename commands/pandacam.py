import nextcord
def pandacam():
    embed=nextcord.Embed(title="Panda Cam", url="https://nationalzoo.si.edu/webcams/panda-cam")
    embed.set_author(name="Smithsonian's Live Panda Cam")
    embed.set_thumbnail(url="https://images-ext-1.discordapp.net/external/ahTsby-7mof7vYb-jRm1SNzncwxo96xRn7A9rRbfLrw/https/nationalzoo.si.edu/sites/default/files/animals/giantpanda-008.jpg?width=1097&height=662")
    embed.set_footer(text="Pandabotv3")
    return embed