import discord
import random
import time
import requests
from discord.ext import commands

client = commands.Bot(command_prefix = '+')

@client.event
async def on_ready() :
    print('Bot is ready')
    
@client.event
async def on_message(message) :
    sent = message.content
    id = client.get_guild(592426994109513758)
    if message.content.find('+card') != -1:
        card2 = sent[6:]
        card = ''
        for i in card2 :
            if i == ' ' :
                card+='_'
            else :
                card+=i
        print(card)
        em = discord.Embed()
        em.set_image(url='https://static-3.studiobebop.net/ygo_data/card_images/'+card+'.jpg')
        await message.channel.send(embed=em)

client.run('NTkyNDI2NTEwNTc3NTY1Njk4.XQ_LuA.HnrIHq_K2_A6YPoXXt9eIWV7_lQ')
