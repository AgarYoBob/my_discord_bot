import discord
from discord.ext import commands
from asyncio import sleep
import random



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

    if message.content == "/소통1":
        embed = discord.Embed(title="#소통해요_1", description="첫 번째 질문입니다!\n새로 생긴 <#590852771125788699> 시스템에 대해 본인의 생각을 아무렇게나 적어주세요!", color=0x738adb)
        embed.set_footer(text="2019_06_19")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통2":
        embed = discord.Embed(title="#소통해요_2", description="본인이 할 일 없을 때 평소에 하는 것을 적어주세요!\n예를 들어서 숨쉬기라던가 숨쉬기라던가...?", color=0x738adb)
        embed.set_footer(text="2019_06_20")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통3":
        embed = discord.Embed(title="#소통해요_3", description="더운 여름을 날려버릴 가장 좋은 것을 말해봐요!", color=0x738adb)
        embed.set_footer(text="2019_06_21")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통4":
        embed = discord.Embed(title="#소통해요_4", description="인생에 꼭 담고싶은 가장 좋아하는 명언같은 것이 있나요?\n있다면 그것은 무엇인가요?", color=0x738adb)
        embed.set_footer(text="2019_06_22")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통5":
        embed = discord.Embed(title="#소통해요_5", description="이 서버의 이름인 [들어오면 후회함]을 보면 어떤 생각이 드는 지 말해보아요!", color=0x738adb)
        embed.set_footer(text="2019_06_23")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통6":
        embed = discord.Embed(title="#소통해요_6", description="망할 월요일이 돌아왔습니다!\n돌아온 월요일을 위해(?) 한 마디씩 남겨주세요!", color=0x738adb)
        embed.set_footer(text="2019_06_24")

    if message.content == "/소통7":
        embed = discord.Embed(title="#소통해요_7", description="**강아지 vs 고양이** | 본인이 가장 좋아하는 것은?", color=0x738adb)
        embed.set_footer(text="2019_06_25")
        await me.send_message(message.channel, embed=embed)

    if not message.content.startswith('/e '):
        return

    actualDict = {}
    name = message.clean_content[3:]
    print(message.clean_content)

    actualObj = makeEmbed(name=name, icon=me.user.avatar_url, values=actualDict)
    await me.edit_message(message, '  ', embed=actualObj)




token = os.environ["BOT_TOKEN"]
me.run(token, bot=False)
