import discord
from discord.ext import commands
from asyncio import sleep
import random

from config import settings
from systemFiles.helpCommands import Help
from systemFiles.moderation import Moder
from systemFiles.info import Info
from systemFiles.fun import Fun
from discord import utils
from discord import Status, Game

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
bot.remove_command('help')
prefix = settings['prefix']

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(1008101806624215121)
    embed = discord.Embed(title=f'У нас новенькие!', description=f'Пользователь {member.mention} Присоеденился к серверу!\n\nПривет {member.mention}, Добро пожаловать на сервер Сообщесто Программистов\nВ етом сервере ти можеж общаться с программистами\nТакже выбери роль на канале Роли\nТакже мы есть в телеграме\nКанал https://t.me/official_programmerchannel\nЧат https://t.me/official_programmerchat\nПожалуста прочитай правила сервера !rules\nПомощь по боту: !help', color=0xFAA200)
    await channel.send(embed=embed)

POST_ID = 1008429787284516935

ROLES = {
    '🐍': 1008007178793263185, # python
    '🟦': 1008007612865978408, # vb.net  
    '🌐': 1008007918613958696, # .net
    '🟠': 1008007981276856320, # html/css
    '🔷': 1008007988172308611, # c/c++
    '📑': 1008008160063262890, # sql
    '🐳': 1008008267936579644, # docker
    '🟧': 1008008319627169903, # java
    '💎': 1008008371116458164, # ruby
    '📒': 1008008432302968865, # json
    '🐘': 1008142636558848081, # php
    '🟣': 1008142723926216744, # charp
    '🟡': 1008142825071837305, # js
    '*️⃣': 1008142886178668605, # assembler
    '🍏': 1008142942361370765, # swift
    '🔵': 1008142980332409003, # kotlin
    '🏃': 1008143050712825927, # go
    '🦎': 1008143090915217419, # pascal
    '🔴': 1008143219508396103, # 1c
}

EXCROLES = ()

MAX_ROLES_PER_USER = 100000

PRO_ID = 1008493251411579021

PROGRAMMIST = {
    '🌚': 1008358985373601832, # full-stack
    '🎮': 1008438455153463308, # Game-dev
    '📺': 1008437481600987146, # front-end
    '🧠': 1008437534432432239, # back-end
    '📱': 1008438497297842329, # ПО-Developer
    '💻': 1008467921263140914, # Web Разработчик
    '🖼': 1008862515041677432, # Future Developer
    '🤖': 1008862000056643694, # Bots Developer
    '👶': 1008493418009350164, # Начинающий
    '❌': 1014941080841621545 # Не программист
}

TESTER_MESSAGE = 1014974589933211718

TROL = {
    '🧪': 1014973303380775032, # tester
}

VERIFY_ID = 1014683433441693696

VROL = {
    '✅': 1014671234333687948, # Verifed
}

SUBSCRIBE_MESSAGE = 1015381998187073577

SROL = {
    '📝': 1015230903074697308, # Подписка: Голосования
    '🦾': 1015400565255180421 # Подписка: Статус бота
}

@commands.Cog.listener()
async def on_member_join(self, member):
     channel = bot.get_channel(1008101806624215121)
     embed = discord.Embed(title=f'У нас новенькие!', description=f'Пользователь {member.mention} Присоеденился к серверу!\n\nПривет {member.mention}, Добро пожаловать на сервер Сообщесто Программистов\nВ етом сервере ти можеж общаться с программистами\nТакже выбери роль на канале Роли\nТакже мы есть в телеграме\nКанал https://t.me/official_programmerchannel\nЧат https://t.me/official_programmerchat\nПожалуста прочитай правила сервера !rules\nКоманди бота !commands', color=0xFAA200)
     await channel.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
      if payload.message_id == POST_ID:
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = payload.member
        print(member)

        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=ROLES[emoji])

            if len([i for i in member.roles if i and i.id not in EXCROLES]) <= MAX_ROLES_PER_USER:
                await member.add_roles(role)
                print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
            else:
                await message.remove_reaction(payload.emoji, member)
                print('[ERROR] Too many roles for user {0.display_name}'.format(member))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))
      if payload.message_id == PRO_ID:
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = payload.member
        print(member)

        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=PROGRAMMIST[emoji])

            if len([i for i in member.roles if i and i.id not in EXCROLES]) <= MAX_ROLES_PER_USER:
                await member.add_roles(role)
                print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
            else:
                await message.remove_reaction(payload.emoji, member)
                print('[ERROR] Too many roles for user {0.display_name}'.format(member))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))
      if payload.message_id == TESTER_MESSAGE:
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = payload.member
        print(member)

        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=TROL[emoji])

            if len([i for i in member.roles if i and i.id not in EXCROLES]) <= MAX_ROLES_PER_USER:
                await member.add_roles(role)
                print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
            else:
                await message.remove_reaction(payload.emoji, member)
                print('[ERROR] Too many roles for user {0.display_name}'.format(member))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e)) 
      if payload.message_id == VERIFY_ID:
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = payload.member
        print(member)

        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=VROL[emoji])

            if len([i for i in member.roles if i and i.id not in EXCROLES]) <= MAX_ROLES_PER_USER:
                await member.add_roles(role)
                print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
            else:
                await message.remove_reaction(payload.emoji, member)
                print('[ERROR] Too many roles for user {0.display_name}'.format(member))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))                       
      if payload.message_id == SUBSCRIBE_MESSAGE:
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = payload.member
        print(member)

        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=SROL[emoji])

            if len([i for i in member.roles if i and i.id not in EXCROLES]) <= MAX_ROLES_PER_USER:
                await member.add_roles(role)
                print('[SUCCESS] User {0.display_name} has been granted with role {1.name}'.format(member, role))
            else:
                await message.remove_reaction(payload.emoji, member)
                print('[ERROR] Too many roles for user {0.display_name}'.format(member))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)
        except Exception as e:
            print(repr(e))

@bot.event
async def on_raw_reaction_remove(payload):
    channel = bot.get_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    user_id = payload.user_id
    member = await (await bot.fetch_guild(payload.guild_id)).fetch_member(payload.user_id)
    print(member, user_id)
    if payload.message_id == POST_ID:
        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=ROLES[emoji])

            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)

        except Exception as e:
            print(repr(e))
    if payload.message_id == PRO_ID:
        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=PROGRAMMIST[emoji])

            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)

        except Exception as e:
            print(repr(e))
    if payload.message_id == TESTER_MESSAGE:
        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=TROL[emoji])

            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)

        except Exception as e:
            print(repr(e))     
    if payload.message_id == SUBSCRIBE_MESSAGE: 
        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=SROL[emoji])

            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)

        except Exception as e:
            print(repr(e))                                

# запуск бота
@bot.event
async def on_ready():
    print("Готов к труду и обороне")
    
    await bot.change_presence(status=Status.idle, activity=Game(name=f" {prefix}help"))

    #await bot.change_presence(status=Status.idle, activity=Game(name=f" {prefix}help"))

   # watch = ['Хауди Хо', 'Гошу Дударя', 'Фсоки', 'UnderMind', 'мемы', '!help']
  #  listen = ['музыку', 'радио', '!help']
  #  games = ['Terraria', 'Minecraft', 'ROBLOX', 'Geometry Dash', 'Мафия', 'World of Tanks', '!help']
  #  stream = ['кодинг', 'Minecraft', 'хакинг', 'на twich', '!help']
  #  while True:
  #      await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=random.choice(watch)))
  #      await sleep(5)
  #      await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=random.choice(listen)))
  #      await sleep(5)
  #      await bot.change_presence(activity=discord.Game(name=random.choice(games)))
  #      await sleep(5)
   #     await bot.change_presence(activity=discord.Streaming(name=random.choice(stream), url='https://www.twitch.tv/rf'))
   #     await sleep(5)

async def setup(bot):
  await bot.add_cog(Moder(bot))
  await bot.add_cog(Help(bot))
  await bot.add_cog(Info(bot))
  await bot.add_cog(Fun(bot))

asyncio.run(setup(bot))

bot.run(settings['token'])
