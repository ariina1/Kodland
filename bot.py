import discord
from gen_pass import gen_pas
from random import choice
from discord.ext import commands
import asyncio
import os
import requests
# Переменная intents - хранит привилегии бота
intents = discord.Intents.default()
# Включаем привелегию на чтение сообщений
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

mems = os.listdir('mems')

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.startswith('pass'):
        await message.channel.sent(gen_pas(10))
    if message.content.startswith('$hello'):
        await message.channel.send("Hi!")
    elif message.content.startswith('$bye'):
        await message.channel.send("\\U0001f642")
    else:
        await message.channel.send(message.content)
    if message.content.startrswith('WOW'):
        embedVar = discord.Embed(title="Title", description='Desc', color = 0x00ff00)
        embedVar.add_field (name="Field1", value="hi", inline=False) 
        embedVar.add_field(name="Field2", value="hi2", inline=False)
        await message.channel.send(embed=embedVar)
    await bot.process_commands(message)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']


@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def mem(ctx):
    mem = choice(mems)
    with open(f"m1u3/mems/{mem}", 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)
@bot.command()
async def passwotd(ctx, lenght = 10):
    await asyncio.sleep(5)
    await ctx.send(gen_pas(lenght))


bot.run('MTE1NDUyMDMyMjA0NTkxMTE2MA.G9ls62.B4Jx45_zF8RgtEkD78TW0yc6FtqzuxQnXMR-xU')
