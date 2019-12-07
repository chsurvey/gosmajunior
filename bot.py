import asyncio
import discord
import discord.utils
import datetime
from parser import*
from discord.ext import commands

client = discord.Client()
token = "NTQzNTMwMTg1NDQ2NjUzOTcz.Xet3Cg.vKaZRd8m8Hy3owA5kGpbjG9umr0"



@client.event
async def on_ready():
    print(client.user.name)
    print(client.user.id)
    print("===========")
    await client.change_presence(game=discord.Game(name="반갑습니다 :D", type=1))
    
@client.event
async def on_message(message):
    now = datetime.datetime.now() 
    if message.author.bot: 
        return None
    if message.content.startswith('!채널'):
        await client.send_message(message.channel,message.channel.id)
    if message.content.startswith('!role'):
        role=""
        rolename=message.content.split(" ")
        member=discord.utils.get(client.get_all_members(), id=rolename[1])
        for i in message.server.roles:
            if i.name == rolename[2]:
                role = i
                break
        await client.add_roles(member, role)
        
    if message.channel.is_private
        await client.send_message(getchannel("650619509303934977"),message.content)
'''
    if message.content.startswith('!나'):
        embed = discord.Embed(title="Profile", description="Nickname : 웨하스 \n ID : warehas \n main : Ike \n second : ike", color=0x00ff00)
        embed.set_footer(text = str(now.year) +" 년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        embed.set_image(url="https://cdn.discordapp.com/attachments/544553467474346007/544811657399107585/EB94B8EAB8B0-600x600.png")
        await client.send_message(message.channel, embed=embed)
    if message.content.startswith('!허윤범'):
        embed2 = discord.Embed(title="허윤범", description="롤을 시작했다. 30렙됬다.", color=0x0054ff)
        embed2.set_footer(text = str(now.year) +" 년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        embed2.set_image(url="https://cdn.discordapp.com/attachments/544553467474346007/545512792216567819/B0EDB9ABB8C1C4A1R.png")        
        await client.send_message(message.channel, embed=embed2)
    if message.content.startswith('!yeoul'):
        embed3 = discord.Embed(title="여울", description="동물의 숲 시리즈 중 2012년에 닌텐도 3DS로 발매된 튀어나와요 동물의 숲에 첫 등장한 캐릭터.\n\n본판 이름은 개의 품종 중 하나인 시추(シーズー)에서 유래한 시즈에(しずえ)이며, 대한민국 정식 발매판에는 여울이란 이름으로 로컬라이징되었다. \n영어권 이름은 이사벨(Isabelle)이며,이 이름의 유래는 이 Npc의 머리를 묶은 방울(bell) 에서 착안한 것이라고 한다", color=0x0054ff)
        embed3.set_footer(text ="fot nigh sky||"+ str(now.year) +" 년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        embed3.set_image(url="https://cdn.discordapp.com/attachments/544553467474346007/545514220545114112/045.png")        
        await client.send_message(message.channel, embed=embed3)
    if message.content.startswith('!ganon'):
        embed3 = discord.Embed(title="가논돌프", description="대마왕 가논돌프, 또다른 이름은 마수(魔獸) 가논. 서구권에서는 흔히 개넌(Ganon)이라고 발음한다.\n\n젤다의 전설 신들의 트라이포스의 슈퍼패미컴 버전 영문판 설명서에서는 가논돌프 드래그마이어(Ganondorf Dragmire)라고 풀네임을 소개했다. 다만 이후에 나온 GBA 이식작 설명서 등이나 여타 다른 작품에는 저 성(姓) 부분이 등장하지 않아 삭제된 설정이라 생각되었으나 결국 북미 공식 웹사이트 가이드에서 가논돌프 드래그마이어란 명칭을 표기하여 이것이 공식이었음을 확인해주고 있었다. \n\n젤다의 전설 시리즈의 최종 보스로 유명한 캐릭터이다. 링크와 젤다의 숙적. 마리오와 쿠파 같은 관계라 보면 이해가 편하다.[5] 용사 링크, 젤다 공주와는 달리 모든 작품에서 등장하지는 않지만 젤다의 전설 시리즈 최고의 인기 악역. 그러나 최강인지는 알 수 없다.[6]", color=0x8041d9)
        embed3.set_footer(text ="fot nigh sky||"+ str(now.year) +" 년 " + str(now.month) + "월 " + str(now.day) + "일 | " + str(now.hour) + ":" + str(now.minute) + ":" + str(now.second))
        embed3.set_image(url="https://cdn.discordapp.com/attachments/544553467474346007/545552960399081472/screen-6.png")        
        await client.send_message(message.channel, embed=embed3)
'''
client.run(token)
