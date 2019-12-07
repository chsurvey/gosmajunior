import asyncio
import discord
import os

client = discord.Client()



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
access_token=os.environ["BOT_TOKEN"]
client.run(access_token)
