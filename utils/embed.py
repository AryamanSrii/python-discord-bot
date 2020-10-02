import discord


def newembed(c=0x428DFF):
    em = discord.Embed(colour=c)
    em.set_footer(text="Mitsuki",
                  icon_url="https://cdn.discordapp.com/avatars/740045367956996236/a4dec1ba1a4826f74ab3dc61e672dd8b.webp?size=1024")

    return em
