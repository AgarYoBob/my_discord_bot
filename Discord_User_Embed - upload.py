import discord
from discord.ext import commands
from asyncio import sleep
import os


me = commands.Bot(command_prefix='.', self_bot=True)


@me.event
async def on_ready():
    print("----------")
    print("Logged in as:")
    print("    "+str(me.user.name))
    print("    "+str(me.user.id))
    print("----------")


def makeEmbed(*, name=None, icon=None, colour=0xDEADBF, values={}):
    '''Creates an embed messasge with specified inputs'''

    embedObj = discord.Embed(colour=colour)

    embedObj.set_author(name=name, icon_url=icon)

    for i in values:
        if values[i] == '':
            values[i] = 'None'
        embedObj.add_field(name=i, value='{}'.format(values[i]))

    return embedObj


@me.event 
async def on_message(message):
    if message.author.id != me.user.id:
        return
    if len(message.embeds) > 0:
        return
    if not message.content.startswith('/e '):
        return

    actualDict = {}
    name = message.clean_content[3:]
    print(message.clean_content)

    actualObj = makeEmbed(name=name, icon=me.user.avatar_url, values=actualDict)
    await me.edit_message(message, '  ', embed=actualObj)



token = os.environ["USER_TOKEN"]
me.run(token, bot=False)