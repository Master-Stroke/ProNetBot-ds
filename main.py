import discord
import psutil
import datetime
import requests

import config

from discord.ext import commands
from discord import utils
from config import mat
from bs4 import BeautifulSoup as BS

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

Year = int(datetime.datetime.now().strftime("%Y"))
Mounth = datetime.datetime.now().strftime("%B")
Dey = int(datetime.datetime.now().strftime("%d"))
Hour = int(datetime.datetime.now().strftime("%H"))
Minute = datetime.datetime.now().strftime("%M")
Dates = [Dey, Hour, Minute, Mounth, Year]
date = f"{Dates[4]}y {Dates[3]} {Dates[0]} {Dates[1]}:{Dates[2]}"

def cpu ():
  cpu_per = int (psutil.cpu_percent (1))
  return cpu_per

@bot.event
async def on_ready():
    print("<<<START>>>")
    print("{0.user} is now online!".format(bot))

@bot.event
async def on_member_join(member: discord.Member):
    channel = bot.get_channel(1008101806624215121)
    embed = discord.Embed(title=f'У нас новенькие!', description=f'Пользователь {member.mention} Присоеденился к серверу!\n\nПривет {member.mention}, Добро пожаловать на сервер Сообщесто Программистов\nВ етом сервере ти можеж общаться с программистами\nТакже вибери роль на канале Роли\nТкже ми есть в телеграме\nКанал https://t.me/official_programmerchannel\nЧат https://t.me/official_programmerchat\nПожалуста прочитай правила сервера !rules\nКоманди бота !commands', color=0xFAA200)
    await channel.send(embed=embed)

@bot.event
async def on_raw_reaction_add(payload):
    if payload.message_id == config.POST_ID:
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = payload.member
        print(member)

        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=config.ROLES[emoji])

            if len([i for i in member.roles if i and i.id not in config.EXCROLES]) <= config.MAX_ROLES_PER_USER:
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
    if payload.message_id == config.POST_ID:
        try:
            emoji = str(payload.emoji)
            role = utils.get(message.guild.roles, id=config.ROLES[emoji])

            await member.remove_roles(role)
            print('[SUCCESS] Role {1.name} has been remove for user {0.display_name}'.format(member, role))

        except KeyError as e:
            print('[ERROR] KeyError, no role found for ' + emoji)

        except Exception as e:
            print(repr(e))

@bot.event
async def on_command_error(ctx, error):
    print(error)

    if isinstance(error, commands.MissingPermissions):
        await ctx.send(f"{ctx.author}, у вас недостаточно прав для выполнения данной команды!")
    elif isinstance(error, commands.UserInputError):
        await ctx.send(embed=discord.Embed(
            description=f"Правильное использование команды: `{ctx.prefix}{ctx.command.name}` ({ctx.command.brief})\nExample: {ctx.prefix}{ctx.command.usage}"
        ))

@bot.command(name="!clear", brief="Очистить чат от сообщений, по умолчанию 10 сообщений", usage="clear <amount=10>")
async def clear(ctx, amount: int=10):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"Was deleted {amount} messages...")

@bot.command(name="!kick", brief="Выгнать пользователя с сервера", usage="kick <@user> <reason=None>")
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.message.delete(delay=1) # Если желаете удалять сообщение после отправки с задержкой

    await member.send(f"Вас кикунали с сервера!") # Отправить личное сообщение пользователю
    await ctx.send(f"Пользователь {member.mention} бил кикнут с сервера!")
    await member.kick(reason=reason)

@bot.command(name="!ban", brief="Забанить пользователя на сервере", usage="ban <@user> <reason=None>")
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await member.send(f"Тебя забанили на сервере!") # Отправить личное сообщение пользователю
    await ctx.send(f"Пользователь {member.mention} бил забанен на сервере!")
    await member.ban(reason=reason)

@bot.command(name="!unban", brief="Разбанить пользователя на сервере", usage="unban <user_id>")
@commands.has_permissions(ban_members=True)
async def unban(ctx, member: discord.Member, *, user_id: int):
    user = await bot.fetch_user(user_id)
    await ctx.guild.unban(user)
    await ctx.send(f"Пользователь {member.mention} бил разбанен на сервере!")

@bot.event
async def on_message(message):
    for word in mat: 
        if word in message.content.lower():
            await message.delete()
            await message.channel.send(f"{message.author.mention}, ай-ай-ай... Плохо, плохо, так нельзя!\nПользователь {message.author.mention} написав мат!")

    if message.content.startswith('!report'):
        channel = bot.get_channel(1008390975460220968)
        await message.channel.send('РЕПОРТ отправлен!')
        await channel.send('Бил отправлен репорт!')        

    if message.content.startswith('!start'):
        await message.channel.send('Привет! Я модератор этого сервера\n'
                                   'В етом сервере ти можеж общаться с программистами\n'
                                   'Ти можеж вибрать чат и там разговаривать\n'
                                   'Также вибери роль на канали Роли\n'
                                   'Пожалуста следуй правилам сервера!\n'
                                   'Правила сервера !rules\n'
                                   'Все команди бота !commands')

    if message.content.startswith('!help'):
        await message.channel.send('В етом сервере ти можеж общаться с программистами\n'
                                   'Ти можеж вибрать чат и там разговаривать\n'
                                   'Также вибери роль на канале Роли\n'
                                   'Пожалуста следуй правилам сервера!\n'
                                   'Правила сервера !rules\n'
                                   'Все команди бота !commands')
    if message.content.startswith('!commands'):
        await message.channel.send('Команди бота:\n'
                                   '!start - Старт бота\n'
                                   '!help - Помощь по боту\n'
                                   '!rules - Правила сервера\n'
                                   '!commands - Визвать этое собщенния\n'
                                   '!report - Жалоба на пользователя\n'
                                   '!bot - Проверка на работоспособность бота\n'
                                   '!usd - Курс Доллара\n'
                                   '!eur - Курс Евро\n'
                                   '!uah - Курс Гривни\n'
                                   '!rub - Курс Рубля\n'
                                   '!pln - Курс Злотих\n'
                                   '!gbp - Курс Фунта')

    if message.content.startswith('!rules'):
        await message.channel.send('Правила сервера:\n'
                                   '🚫 Ненормативная лексика запрещена\n'
                                   '🚫Спам запрещен\n'
                                   'Не следуванния правил чата караеться баном или мутом!\n'
                                   'Незнание правил не освобождает вас от ответственности!\n')     
    if message.content.startswith('!bot'):
        await message.channel.send(f'Бот запущен!\nПоследнее обновленния било: {date} (GMT+3).\nНагрузка на процессор хостинга: {cpu()}%')                                                                   

    if message.content.startswith('!usd'):
        url = 'https://www.currency.me.uk/convert/usd/uah'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        uah = soup.find("span", { "class" : "mini ccyrate" }).text

        url = 'https://www.currency.me.uk/convert/usd/rub'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        rub = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/usd/eur'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        eur = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/usd/gbp'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        gbp = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/usd/pln'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        pln = soup.find("span", { "class" : "mini ccyrate" }).text    

        res = f"USD💵\n🇺🇦{uah}\n🇷🇺{rub}\n🇪🇺{eur}\n🇬🇧{gbp}\n🇵🇱{pln}"
        await message.channel.send(f"{res}")

    if message.content.startswith('!eur'):  
            url = 'https://www.currency.me.uk/convert/eur/uah'
            r = requests.get(url)
            soup = BS(r.text, 'lxml')
            uah = soup.find("span", { "class" : "mini ccyrate" }).text

            url = 'https://www.currency.me.uk/convert/eur/rub'
            r = requests.get(url)
            soup = BS(r.text, 'lxml')
            rub = soup.find("span", { "class" : "mini ccyrate" }).text 

            url = 'https://www.currency.me.uk/convert/eur/usd'
            r = requests.get(url)
            soup = BS(r.text, 'lxml')
            usd = soup.find("span", { "class" : "mini ccyrate" }).text 

            url = 'https://www.currency.me.uk/convert/eur/gbp'
            r = requests.get(url)
            soup = BS(r.text, 'lxml')
            gbp = soup.find("span", { "class" : "mini ccyrate" }).text 

            url = 'https://www.currency.me.uk/convert/eur/pln'
            r = requests.get(url)
            soup = BS(r.text, 'lxml')
            pln = soup.find("span", { "class" : "mini ccyrate" }).text 

            res = f"EUR💶\n🇺🇦{uah}\n🇷🇺{rub}\n🇺🇸{usd}\n🇬🇧{gbp}\n🇵🇱{pln}"
            await message.channel.send(f"{res}")
    
    if message.content.startswith('!pln'): 
        url = 'https://www.currency.me.uk/convert/pln/usd'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        usd = soup.find("span", { "class" : "mini ccyrate" }).text

        url = 'https://www.currency.me.uk/convert/pln/rub'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        rub = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/pln/eur'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        eur = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/pln/uah'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        uah = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/pln/gbp'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        gbp = soup.find("span", { "class" : "mini ccyrate" }).text    

        res = f"PLN🇵🇱\n🇺🇸{usd}\n🇷🇺{rub}\n🇪🇺{eur}\n🇺🇦{uah}\n🇬🇧{gbp}"  

        await message.channel.send(f"{res}")


    if message.content.startswith('!gbp'): 
        url = 'https://www.currency.me.uk/convert/gbp/usd'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        usd = soup.find("span", { "class" : "mini ccyrate" }).text

        url = 'https://www.currency.me.uk/convert/gbp/rub'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        rub = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/gbp/eur'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        eur = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/gbp/uah'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        uah = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/gbp/pln'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        pln = soup.find("span", { "class" : "mini ccyrate" }).text    

        res = f"GBP💷\n🇺🇸{usd}\n🇷🇺{rub}\n🇪🇺{eur}\n🇺🇦{uah}\n🇵🇱{pln}"

        await message.channel.send(f"{res}")

    if message.content.startswith('!rub'): 
        url = 'https://www.currency.me.uk/convert/rub/usd'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        usd = soup.find("span", { "class" : "mini ccyrate" }).text

        url = 'https://www.currency.me.uk/convert/rub/uah'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        uah = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/rub/eur'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        eur = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/rub/gbp'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        gbp = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/rub/pln'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        pln = soup.find("span", { "class" : "mini ccyrate" }).text    

        res = f"RUB🇷🇺\n🇺🇸{usd}\n🇺🇦{uah}\n🇪🇺{eur}\n🇬🇧{gbp}\n🇵🇱{pln}"

        await message.channel.send(f"{res}")

    if message.content.startswith('!uah'): 
        url = 'https://www.currency.me.uk/convert/uah/usd'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        usd = soup.find("span", { "class" : "mini ccyrate" }).text

        url = 'https://www.currency.me.uk/convert/uah/rub'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        rub = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/uah/eur'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        eur = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/uah/gbp'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        gbp = soup.find("span", { "class" : "mini ccyrate" }).text 

        url = 'https://www.currency.me.uk/convert/uah/pln'
        r = requests.get(url)
        soup = BS(r.text, 'lxml')
        pln = soup.find("span", { "class" : "mini ccyrate" }).text    

        res = f"UAH🇺🇦\n🇺🇸{usd}\n🇷🇺{rub}\n🇪🇺{eur}\n🇬🇧{gbp}\n🇵🇱{pln}"

        await message.channel.send(f"{res}")

bot.run(config.TOKEN)