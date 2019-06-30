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
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통7":
        embed = discord.Embed(title="#소통해요_7", description="**강아지 vs 고양이** | 본인이 가장 좋아하는 것은?", color=0x738adb)
        embed.set_footer(text="2019_06_25")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통8":
        embed = discord.Embed(title="#소통해요_8", description="비가 오는 날씨에 가장 하고 싶은 일은 무엇일까요?", color=0x738adb)
        embed.set_footer(text="2019_06_26")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통9":
        embed = discord.Embed(title="#소통해요_9", description="여러분의 평균 타자 속도는 얼마나 되나요?", color=0x738adb)
        embed.set_footer(text="2019_06_27")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통10":
        embed = discord.Embed(title="#소통해요_10", description="<@311791989681291264> vs <@150577293981515776>\n둘 중 더 귀여운 사람을 선택한다면? ||~~난죽택~~||", color=0x738adb)
        embed.set_footer(text="2019_06_28")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통11":
        embed = discord.Embed(title="#소통해요_11", description="과옌 마춤뻡을 않지킈면 불ㅡ편하까???", color=0x738adb)
        embed.set_footer(text="2019_06_29")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통12":
        embed = discord.Embed(title="#소통해요_12", description="6월의 마지막 날입니다!\n올해 하반기의 목표는 무엇인가요?", color=0x738adb)
        embed.set_footer(text="2019_06_30")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통13":
        embed = discord.Embed(title="#소통해요_13", description="기말고사에 대한 응원의 메시지를 남겨보아요!\n~~물론 난 시험 안보니까 탈주~~", color=0x738adb)
        embed.set_footer(text="2019_07_01")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통14":
        embed = discord.Embed(title="#소통해요_14", description="[들어오면 후회함] 서버에 건의를 해본다면?", color=0x738adb)
        embed.set_footer(text="2019_07_02")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통15":
        embed = discord.Embed(title="#소통해요_15", description="<#548571647947309076>에 있는 직업 중 자신이 가장 좋아하는 직업은 무엇인가요?", color=0x738adb)
        embed.set_footer(text="2019_07_03")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통16":
        embed = discord.Embed(title="#소통해요_16", description="다음 소통해요 주제를 예측해봅시다!\n||~~절대 할만한 주제 아이디어가 안떠오르는게 아니라구요!!~~||", color=0x738adb)
        embed.set_footer(text="2019_07_04")
        await me.send_message(message.channel, embed=embed)

    if message.content == "/소통17":
        embed = discord.Embed(title="#소통해요_17", description="자신의 인생에서 절대 잊지 못할 순간은?", color=0x738adb)
        embed.set_footer(text="2019_07_05")
        await me.send_message(message.channel, embed=embed)

    if not message.content.startswith('/e '):
        return

    actualDict = {}
    name = message.clean_content[3:]
    print(message.clean_content)

    actualObj = makeEmbed(name=name, icon=me.user.avatar_url, values=actualDict)
    await me.edit_message(message, '  ', embed=actualObj)



token = os.environ["USER_TOKEN"]
me.run(token, bot=False)
