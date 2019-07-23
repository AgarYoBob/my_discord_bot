import discord
from discord.ext import commands
from asyncio import sleep
import os
import datetime



client = commands.Bot(command_prefix='.', self_bot=True)


@client.event
async def on_ready():
    print("----------")
    print("Logged in as:")
    print("    "+str(client.user.name))
    print("    "+str(client.user.id))
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


async def command_log(message):
    now = datetime.datetime.now()
    embed = discord.Embed(title="명령어 사용이 감지되었습니다.", description=message.author.name + " (<@" + message.author.id + ">)\n#" + message.channel.name + " (<#" + message.channel.id + ">)\n**" + message.content + "**", color=0x0000ff)
    embed.set_footer(text=str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
    await client.send_message(client.get_channel('542335831675764736'), embed=embed)


@client.event 
async def on_message(message):
    
    now = datetime.datetime.now()

    if message.author.id != client.user.id:
        return
    if len(message.embeds) > 0:
        return
        
    if message.content == "/소통1":
        embed = discord.Embed(title="#소통해요_1", description="첫 번째 질문입니다!\n새로 생긴 <#590852771125788699> 시스템에 대해 본인의 생각을 아무렇게나 적어주세요!", color=0x738adb)
        embed.set_footer(text="2019_06_19")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통2":
        embed = discord.Embed(title="#소통해요_2", description="본인이 할 일 없을 때 평소에 하는 것을 적어주세요!\n예를 들어서 숨쉬기라던가 숨쉬기라던가...?", color=0x738adb)
        embed.set_footer(text="2019_06_20")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통3":
        embed = discord.Embed(title="#소통해요_3", description="더운 여름을 날려버릴 가장 좋은 것을 말해봐요!", color=0x738adb)
        embed.set_footer(text="2019_06_21")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통4":
        embed = discord.Embed(title="#소통해요_4", description="인생에 꼭 담고싶은 가장 좋아하는 명언같은 것이 있나요?\n있다면 그것은 무엇인가요?", color=0x738adb)
        embed.set_footer(text="2019_06_22")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통5":
        embed = discord.Embed(title="#소통해요_5", description="이 서버의 이름인 [들어오면 후회함]을 보면 어떤 생각이 드는 지 말해보아요!", color=0x738adb)
        embed.set_footer(text="2019_06_23")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통6":
        embed = discord.Embed(title="#소통해요_6", description="망할 월요일이 돌아왔습니다!\n돌아온 월요일을 위해(?) 한 마디씩 남겨주세요!", color=0x738adb)
        embed.set_footer(text="2019_06_24")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통7":
        embed = discord.Embed(title="#소통해요_7", description="**강아지 vs 고양이** | 본인이 가장 좋아하는 것은?", color=0x738adb)
        embed.set_footer(text="2019_06_25")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통8":
        embed = discord.Embed(title="#소통해요_8", description="비가 오는 날씨에 가장 하고 싶은 일은 무엇일까요?", color=0x738adb)
        embed.set_footer(text="2019_06_26")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통9":
        embed = discord.Embed(title="#소통해요_9", description="여러분의 평균 타자 속도는 얼마나 되나요?", color=0x738adb)
        embed.set_footer(text="2019_06_27")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통10":
        embed = discord.Embed(title="#소통해요_10", description="<@311791989681291264> vs <@150577293981515776>\n둘 중 더 귀여운 사람을 선택한다면? ||~~난죽택~~||", color=0x738adb)
        embed.set_footer(text="2019_06_28")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통11":
        embed = discord.Embed(title="#소통해요_11", description="과옌 마춤뻡을 않지킈면 불ㅡ편하까???", color=0x738adb)
        embed.set_footer(text="2019_06_29")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통12":
        embed = discord.Embed(title="#소통해요_12", description="6월의 마지막 날입니다!\n올해 하반기의 목표는 무엇인가요?", color=0x738adb)
        embed.set_footer(text="2019_06_30")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통13":
        embed = discord.Embed(title="#소통해요_13", description="기말고사에 대한 응원의 메시지를 남겨보아요!\n~~물론 난 시험 안보니까 탈주~~", color=0x738adb)
        embed.set_footer(text="2019_07_01")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통14":
        embed = discord.Embed(title="#소통해요_14", description="[들어오면 후회함] 서버에 건의를 해본다면?", color=0x738adb)
        embed.set_footer(text="2019_07_02")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통15":
        embed = discord.Embed(title="#소통해요_15", description="<#548571647947309076>에 있는 직업 중 자신이 가장 좋아하는 직업은 무엇인가요?", color=0x738adb)
        embed.set_footer(text="2019_07_03")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통16":
        embed = discord.Embed(title="#소통해요_16", description="다음 소통해요 주제를 예측해봅시다!\n||~~절대 할만한 주제 아이디어가 안떠오르는게 아니라구요!!~~||", color=0x738adb)
        embed.set_footer(text="2019_07_04")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통17":
        embed = discord.Embed(title="#소통해요_17", description="자신의 인생에서 절대 잊지 못할 순간은?", color=0x738adb)
        embed.set_footer(text="2019_07_05")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통19":
        embed = discord.Embed(title="#소통해요_19", description="첫번째로 변경 된 밸런스 패치에 대한 생각을 적어주세요!\n의견은 나중에 참고하도록 하겠습니다.", color=0x738adb)
        embed.set_footer(text="2019_07_07")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통20":
        embed = discord.Embed(title="#소통해요_20", description="망할 월요일 컴 백 Again.\n월요일에 대한 저주를 한다면?", color=0x738adb)
        embed.set_footer(text="2019_07_08")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통21":
        embed = discord.Embed(title="#소통해요_21", description="이 서버에서 제일 미X놈은 누구인가요?", color=0x738adb)
        embed.set_footer(text="2019_07_09")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통22":
        embed = discord.Embed(title="#소통해요_22", description="샌즈가 ppap 추면서 액체괴물을 1000도칼로 자르는게 개꿀잼 몰카였다는게 학계의 정설이라는 얘기를 듣다니 상상도 못한 정체입니까 human?\n||~~대체 뭔 개소리인지 나도 모르게따~~||", color=0x738adb)
        embed.set_footer(text="2019_07_10")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통23":
        embed = discord.Embed(title="#소통해요_23", description="만약 내가 [들어오면 후회함] 서버를 뜯어고친다면 가장 먼저 할 것 같은 일은?", color=0x738adb)
        embed.set_footer(text="2019_07_11")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통24":
        embed = discord.Embed(title="#소통해요_24", description="[들어오면 후회함] 서버에서 추가하고 싶거나 퇴출하고 싶은 봇은?\n(의견 많으면 반영할게요!)", color=0x738adb)
        embed.set_footer(text="2019_07_12")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통25":
        embed = discord.Embed(title="#소통해요_25", description="<@311791989681291264>와(과) <@150577293981515776>(이)가 싸우면 누가 이길거가틈?\n||~~나~~||", color=0x738adb)
        embed.set_footer(text="2019_07_13")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통26":
        embed = discord.Embed(title="#소통해요_26", description="누군가 나에게 패드립이라는 스킬을 선사했을 때 당신이 할 반응으로 가장 적절한 것은 무엇일까요?", color=0x738adb)
        embed.set_footer(text="2019_07_14")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통27":
        embed = discord.Embed(title="#소통해요_27", description="벌써 7월이 반이나 지나갔어요!\nwa! 곧 방학이댜아ㅏㅏ!!", color=0x738adb)
        embed.set_footer(text="2019_07_15")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통28":
        embed = discord.Embed(title="#소통해요_28", description="가장 좋아하는 음악을 말해주세요!\n~~심심할때 들어봄~~", color=0x738adb)
        embed.set_footer(text="2019_07_16")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통29":
        embed = discord.Embed(title="#소통해요_29", description="시공의 폭풍은 정말 최고일까요? 아니라면 그 이유는 무엇일까요?\n||~~삐빅- 이미 죽은 게임입니다.~~||", color=0x738adb)
        embed.set_footer(text="2019_07_17")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통30":
        embed = discord.Embed(title="#소통해요_30", description="본인이 좋아하는 게임은?\n~~당연히 늑인 아닙니까아ㅏ~~", color=0x738adb)
        embed.set_footer(text="2019_07_18")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통32":
        embed = discord.Embed(title="#소통해요_32", description="오늘 늑인게임을 하기 가장 좋은 타이밍(시간대)는?", color=0x738adb)
        embed.set_footer(text="2019_07_20")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통33":
        embed = discord.Embed(title="#소통해요_33", description="지금 여러분이 사용하고 있는 키보드는 무엇인가요?", color=0x738adb)
        embed.set_footer(text="2019_07_21")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통34":
        embed = discord.Embed(title="#소통해요_34", description="늑대인간 vs 연쇄살인마\n당신의 선택은?", color=0x738adb)
        embed.set_footer(text="2019_07_22")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통35":
        embed = discord.Embed(title="#소통해요_35", description="건의 채널을 새로 생성하는 것에 대해서 어떻게 생각하시나요?", color=0x738adb)
        embed.set_footer(text="2019_07_23")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통36":
        embed = discord.Embed(title="#소통해요_36", description="당신이 생각하는 가장 똥망겜을 고르자면?", color=0x738adb)
        embed.set_footer(text="2019_07_24")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통37":
        embed = discord.Embed(title="#소통해요_37", description="모든것이 귀찮아서 아무것도 하기 싫을 때 당신의 대처법은?", color=0x738adb)
        embed.set_footer(text="2019_07_25")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통38":
        embed = discord.Embed(title="#소통해요_38", description="본인이 가장 많이 하는 헛소리는 무엇인가요?", color=0x738adb)
        embed.set_footer(text="2019_07_26")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/소통39":
        embed = discord.Embed(title="#소통해요_39", description="<@311791989681291264>는 지금 무엇을 하고 있을 지 예측해봅시다!", color=0x738adb)
        embed.set_footer(text="2019_07_27")
        await client.send_message(message.channel, embed=embed)

    if message.content == "/time":
        await command_log(message)
        embed = discord.Embed(title="요밥 봇 알림", description="", color=0x00ff00)
        embed.set_footer(text="현재 시각(태평양 표준시 기준):\n" + str(now.year) + "년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        await client.send_message(message.channel, embed=embed)

    if not message.content.startswith('/e '):
        return

    actualDict = {}
    name = message.clean_content[3:]
    print(message.clean_content)

    actualObj = makeEmbed(name=name, icon=client.user.avatar_url, values=actualDict)
    await client.edit_message(message, '  ', embed=actualObj)



#token = os.environ["USER_TOKEN"]
#client.run(token, bot=False)

token = "MTUwNTc3MjkzOTgxNTE1Nzc2.XP0JzQ.5Vlf3gH_PlNR7aLS0_NFFTrsVl4"
client.run(token, bot=False)
