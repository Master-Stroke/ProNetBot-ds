import discord
from discord.ext.commands import Context
from discord.ext import commands
import requests
from bs4 import BeautifulSoup as BS
import datetime
import psutil
from discord.ui import Button, View
from discord import utils
from config import settings

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=intents)
bot.remove_command('help')
prefix = settings['prefix']

 #: commands.clean_content

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

class MyView(View):
    def __init__(self, ctx):
        super().__init__(timeout=10)
        self.ctx = ctx

    @discord.ui.button(label="🗝", style=discord.ButtonStyle.grey, emoji = None)
    async def button_callback(payload, button, interaction):
      #  button.label = "Wow!"
        channel = bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        member = payload.member
        role = utils.get(message.guild.roles, id=1050550289394045028)
        await member.add_roles(role)
        await interaction.response.send_message("Вы успешно прошли верификацию! Вам открыт доступ к каналам сервера!", ephemeral=True)
        button.disabled = False

        await interaction.response.edit_message(view=self)

class Info(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['testt', 'tttest'])
    async def _test(self, ctx: Context):
        servers = self.bot.guilds
        print(servers)

    @commands.command(aliases=['vvverify'])
    async def verify(self, ctx: Context):
        view = MyView(ctx)
        embed = discord.Embed(title=f'Верификация на сервере!', description=f'Для прохождения верификации нажмите на кнопку ниже', color=0x3498db)
        await ctx.send(embed=embed, view=view)

    @bot.slash_command(name = "ping", description = "Пинг бота")
    async def _ping(self, ctx):
        ping_value = round(self.bot.latency * 1000)
        emb = discord.Embed(
            title=f"Пинг: `{ping_value}`ms"
        )
        await ctx.respond(embed=emb)

    @bot.slash_command(name = "bot", description = "Информация о боте")
    async def _bot(self, ctx):
      channel = ctx.channel or channel
      emb = discord.Embed(
            title=f"Привет", description=f"Я мультифункциональный бот-модератор для IT серверов дискорда!\nЧто бы узнать мои команды напиши `!help`\n\n**Сервер поддержки:**\n[Тут](https://discord.com/invite/yVSSf8B9m8) сервер поддержки бота!"
        )
      ping_value = round(self.bot.latency * 1000)
      servers = len(self.bot.guilds)
      commands = len(self.bot.commands)

      emb.add_field(name=f"Мой пинг: ", value=f"`{ping_value}`ms", inline=False),
      emb.add_field(name=f"Я работаю на:", value=f"{servers} серверах", inline=False),
      emb.add_field(name=f"Количество команд: ", value=f"{commands}", inline=False),

      await ctx.respond(embed=emb)

    @bot.slash_command(name = "monitoring", description = "Мониторинг бота")
    async def _monitoring(self, ctxt):
      channel = ctx.channel or channel
      emb = discord.Embed(
            title=f"Мониторинг бота",
        )

      ping_value = round(self.bot.latency * 1000)
      servers = len(self.bot.guilds)
      commands = len(self.bot.commands)

      emb.add_field(name=f"Перезапуск бота бил: ", value=f"{date}", inline=False),
      emb.add_field(name=f"Нагрузка на процессор хостинга: ", value=f"{cpu()}%", inline=False),
      emb.add_field(name=f"Пинг: ", value=f"`{ping_value}`ms", inline=False),
      emb.add_field(name=f"Я работаю на:", value=f"{servers} серверах", inline=False),
      emb.add_field(name=f"Количество команд: ", value=f"{commands}", inline=False),
      emb.add_field(name=f"Количество ядер в системе: ", value=f"{psutil.cpu_count()}", inline=False),
      emb.add_field(name=f"Комп на котором сервер, бил запущен ", value=f"{psutil.boot_time()} секунд назад.", inline=False)

      await ctx.respond(embed=emb)

    # Информация о сервере
    @bot.slash_command(name = "server", description = "Информация о сервере")
    async def stats(self, ctx):
     name = str(ctx.guild.name)
     description = str(ctx.guild.description)
     owner = str(ctx.guild.owner)
     id = str(ctx.guild.id)
     mcount = str(ctx.guild.member_count)

     tchcount = len([x for x in ctx.guild.channels if x.type != discord.ChannelType.voice if x.type != discord.ChannelType.category])
     vchcount = len([x for x in ctx.guild.channels if x.type == discord.ChannelType.voice])
     cchcount = len([x for x in ctx.guild.channels if x.type == discord.ChannelType.category])
     rcount = len([x for x in ctx.guild.roles])
     ucount = len([x for x in ctx.guild.members if not x.bot])

     emb = discord.Embed(
         title=f'Информация о сервере {ctx.guild.name}'
     )
     emb.add_field(name="Владелец сервера:", value=owner, inline=True)
     emb.add_field(name="ID сервера:", value=id, inline=False)
     emb.add_field(name="Количество участников сервера:", value=mcount, inline=False)
     emb.add_field(name="Количество участников сервера (без ботов):", value=f'{ucount}', inline=False)
     emb.add_field(name='Количество ролей', value=f'{rcount}', inline=False)
     emb.add_field(name='Дата создания:', value=f'{ctx.guild.created_at.strftime("%Y.%m.%d, %H:%M")}', inline=False)
     emb.add_field(name='Количество каналов:', value=f'> Текстовых: {tchcount}\n> Голосовых: {vchcount}\n> Категорий: {cchcount}',
                  inline=False)
     await ctx.respond(embed=emb)

    @bot.slash_command(name = "userinfo", description = "Информация о пользователе")
    async def _userinfo(self, ctx, member: discord.Member = None):
      if member == None:
            embed = discord.Embed(
                description=f"**Отметьте участника для просмотра его информации как аргумент!**",
                colour=0xe74c3c,
            )

            await ctx.respond(embed=embed)
      else:
        t = member.status
        if t == discord.Status.online:
            d = ":green_circle: В сети"
        if t == discord.Status.offline:
            d = ":black_circle: Не в сети"
        if t == discord.Status.idle:
            d = ":crescent_moon: Не активен"
        if t == discord.Status.dnd:
            d = ":no_entry: Не беспокоить"

        value1 = member.activity

        embed = discord.Embed(
            description=f'**Информация о пользователе**\n'
                        f'\n**Имя: **{member.display_name}\n'
                        f'**Статус: **{d}\n'
                    #    f'**Роль на сервере: **{member.top_role.mention}\n'
                        f'**Дата создания: **{member.created_at.strftime("%d.%m.%Y")}\n',
            color=ctx.author.color, )
        embed.set_footer(text=f'ID: {member.id}')
        await ctx.respond(embed=embed)

    @bot.slash_command(name = "channel", description = "Информация о канале")
    async def channelstats(self, ctx, channel: discord.TextChannel = None):
        if channel == None:
            channel = ctx.channel
        else:
            channel = channel
        embed = discord.Embed(
            title=f"Информация о канале `{channel.name}`",
            description=f"{'Катеригория: `{}'.format(channel.category.name) if channel.category else 'У этого канала нету катеригории!`'}`",
            colour=0x979c9f
        )

        if channel.slowmode_delay == 0:
            slow_mode = "Отключен"

        fields = [
            ("Названия канала", channel.name, False),
            ("ID канала", channel.id, False),
            ("Позиция канала в списке", channel.position, False),
            ("Медленый режим", slow_mode, False),
            ("Когда был создан канал", channel.created_at, False),
        ]
        for name, value, inline in fields:
            embed.add_field(name=name, value=value, inline=inline)

        await ctx.respond(embed=embed)


    # Информация о ролях пользователя

    @bot.slash_command(name = "roles", description = "Роли")
    async def _roles(self, ctx, member: discord.Member = None):
      if member == None:
            embed = discord.Embed(
                description=f"**Отметьте участника для просмотра ролей как аргумент!**",
                colour=0xe74c3c,
            )

            await ctx.respond(embed=embed)
      else:
            userPrefix = member

            member_roles = userPrefix.roles
            member_roles.pop(0)
            member_roles.reverse()
            x = ''
            for i in member_roles:
              element = str(i.id)
              result = f'<@&{element}>'
              if len(member_roles) <= 5:
                x += f'{result}\n'
              else:
                x += f'- {result} -'

            embed = discord.Embed(
            description=f"{userPrefix.mention} список ролей:\n\n{x}",
            color=ctx.author.color)
            await ctx.respond(embed=embed)

    @bot.slash_command(name = "usd", description = "Курс доллара")
    async def _usd(self, ctx):
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

       # res = f"USD💵\n🇺🇦{uah}\n🇷🇺{rub}\n🇪🇺{eur}\n🇬🇧{gbp}\n🇵🇱{pln}"
        embed = discord.Embed(title=f"USD 💵",
        description=f"🇺🇦 {uah}\n🇷🇺 {rub}\n🇪🇺 {eur}\n🇬🇧 {gbp}\n🇵🇱 {pln}",
        color=0x979c9f)
        await ctx.respond(embed=embed)

    @bot.slash_command(name = "euro", description = "Курс евро")
    async def _eur(self, ctx):
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

            embed = discord.Embed(title=f"EUR 💶",
            description=f"🇺🇦 {uah}\n🇷🇺 {rub}\n🇺🇸 {usd}\n🇬🇧 {gbp}\n🇵🇱 {pln}",
            color=0x979c9f)
            await ctx.respond(embed=embed)

    @bot.slash_command(name = "pln", description = "Курс злотих")
    async def _pln(self, ctx):
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

        embed = discord.Embed(title=f"PLN 🇵🇱",
        description=f"🇺🇸 {usd}\n🇷🇺 {rub}\n🇪🇺 {eur}\n🇺🇦 {uah}\n🇬🇧 {gbp}",
        color=0x979c9f)
        await ctx.respond(embed=embed)

    @bot.slash_command(name = "gbp", description = "Курс фунта")
    async def _gbp(self, ctx):
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

        embed = discord.Embed(title=f"GBP 💷",
        description=f"🇺🇸 {usd}\n🇷🇺 {rub}\n🇪🇺 {eur}\n🇺🇦 {uah}\n🇵🇱 {pln}",
        color=0x979c9f)
        await ctx.respond(embed=embed)

    @bot.slash_command(name = "rub", description = "Курс рубля")
    async def _rub(self, ctx):
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

        embed = discord.Embed(title=f"RUB 🇷🇺",
        description=f"🇺🇸 {usd}\n🇺🇦 {uah}\n🇪🇺 {eur}\n🇬🇧 {gbp}\n🇵🇱 {pln}",
        color=0x979c9f)
        await ctx.respond(embed=embed)

    @bot.slash_command(name = "uah", description = "Курс гривни")
    async def _uah(self, ctx):
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

        embed = discord.Embed(title=f"UAH 🇺🇦",
        description=f"🇺🇸 {usd}\n🇷🇺 {rub}\n🇪🇺 {eur}\n🇬🇧 {gbp}\n🇵🇱{pln}",
        color=0x979c9f)
        await ctx.respond(embed=embed)

    # Аватарка пользователя
'''
    @commands.command()
    async def avatar(self, ctx, member: discord.Member = None):
        if member == None:
            userPrefix = ctx.message.author
        else:
            userPrefix = member

        emb = discord.Embed(
            title=f"Аватарка пользователя {userPrefix.display_name}", color=ctx.author.color)
        emb.set_image(url=str(userPrefix.avatar_url))
        await ctx.send(embed=emb)
'''
