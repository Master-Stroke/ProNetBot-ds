import discord
from discord.ext import commands
from config import settings

bot = discord.Bot()

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @bot.slash_command(name = "help", description = "Помощь по командам бота")
    async def _help(self, ctx, helpcommand=None):
        prefix = settings['prefix']
        botId = discord.utils.get(ctx.guild.members, id=settings['id'])

        # общий help
        if helpcommand == None or helpCommand == 'help':
          if ctx.guild.id == 975057574326050946:
             embed = discord.Embed(
                description=f'**Информация о командах:**\n'
                            f'\nВы можете получить детальную справку по каждой команде\n'
                            f'Например: `{prefix}help server`\n'
                            f'\n:bar_chart: Информация\n'
                            f'`{prefix}help` `{prefix}server` `{prefix}channel` `{prefix}userinfo` `{prefix}roles` `{prefix}bot` `{prefix}monitoring` `{prefix}ping`'
                            f'\n:toolbox: Модерация\n'
                            f'`{prefix}ban` `{prefix}kick` `{prefix}nick` `{prefix}clear` `{prefix}slowmode`'
                            f'\n:notes: Музыка\n'
                            f'`{prefix}join` `{prefix}leave` `{prefix}play` `{prefix}pause` `{prefix}resume` `{prefix}now` `{prefix}remove` `{prefix}skip` `{prefix}volume` `{prefix}queue` `{prefix}stop`'
                            f'\n:dollar: Курс валют\n'
                            f'`{prefix}usd` `{prefix}euro` `{prefix}uah` `{prefix}rub` `{prefix}pln` `{prefix}gbp`'
                            f'\n:joystick: Развлечение\n'
                            f'`{prefix}coin` `{prefix}howdy` `{prefix}ben` `{prefix}8ball` `{prefix}mem` `{prefix}nsfw`'
                            f'\n⠀',)
          else:
             embed = discord.Embed(
                description=f'**Информация о командах:**\n'
                            f'\nВы можете получить детальную справку по каждой команде\n'
                            f'Например: `{prefix}help server`\n'
                            f'\n:bar_chart: Информация\n'
                            f'`{prefix}help` `{prefix}server` `{prefix}channel` `{prefix}userinfo` `{prefix}roles` `{prefix}bot` `{prefix}monitoring` `{prefix}ping`'
                            f'\n:toolbox: Модерация\n'
                            f'`{prefix}ban` `{prefix}kick` `{prefix}nick` `{prefix}clear` `{prefix}slowmode`'
                            f'\n:notes: Музыка\n'
                            f'`{prefix}join` `{prefix}leave` `{prefix}play` `{prefix}pause` `{prefix}resume` `{prefix}now` `{prefix}remove` `{prefix}skip` `{prefix}volume` `{prefix}queue` `{prefix}stop`'
                            f'\n:dollar: Курс валют\n'
                            f'`{prefix}usd` `{prefix}euro` `{prefix}uah` `{prefix}rub` `{prefix}pln` `{prefix}gbp`'
                            f'\n:joystick: Развлечение\n'
                            f'`{prefix}coin` `{prefix}howdy` `{prefix}ben` `{prefix}8ball` `{prefix}mem` `{prefix}nsfw`'
                            f'\n⠀',
                            
                color=ctx.author.color)
          await ctx.respond(embed=embed)
        # помощь раздела информации

        elif helpCommand == 'nsfw':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}nsfw`:**\n'
                            f'\nКоманда позволяет получить nsfw аниме фото\n'
                            f':warning: Команду можно применить только в NSFW чатах\n'
                            f'\nКоманда приминяется c аргументамы:\n'
                            f'`{prefix}nsfw <cosplay, hental, ass, pgif, swimsult, thigh, hass, boobs, hboobs, pussy, anal, blowjob, tentacle>`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpcommand == 'mem':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}mem`:**\n'
                            f'\nКоманда позволяет получить рандомный мем с базы мемов где 100+ мемов\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}mem`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpcommand == '8ball' or helpcommand == '8ball':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}8ball`:**\n'
                            f'\nКоманда позволяет получить рандомный ответ то бота\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}8ball <вопрос>',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpcommand == 'monitoring' or helpcommand == 'monitoring':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}monitoring`:**\n'
                            f'\nКоманда позволяет посмотреть мониторинг бота\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}monitoring',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpcommand == 'cq' or helpcommand == 'cq':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}cq`:**\n'
                            f'\nКоманда позволяет очередь музыки\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}cq',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpcommand == 'stop' or helpcommand == 'stop':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}stop`:**\n'
                            f'\nКоманда позволяет остановить проигрования музыки\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}stop',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpcommand == 'queue' or helpcommand == 'queue':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}queue`:**\n'
                            f'\nКоманда позволяет очередь проигрвоания музыки\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}queue',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpcommand == 'volume' or helpcommand == 'volume':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}volume`:**\n'
                            f'\nКоманда позволяет изменить громкость музыки которая щас играет\n'
                            f'\nКоманда приминяется с аргументамы:\n'
                            f'`{prefix}volume <громкость музыки>',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpcommand == 'skip' or helpcommand == 'skip':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}skip`:**\n'
                            f'\nКоманда позволяет пропустить музыку которая щас играет\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}skip',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpcommand == 'remove' or helpcommand == 'remove':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}remove`:**\n'
                            f'\nКоманда позволяет убрать музыку с очереди\n'
                            f'\nКоманда приминяется с аргументамы:\n'
                            f'`{prefix}remove <номер музыки в очереди>',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpcommand == 'now' or helpcommand == 'now':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}now`:**\n'
                            f'\nКоманда позволяет посмотреть какая музыка щас играет\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}now',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpCommand == 'resume' or helpCommand == 'resume':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}resume`:**\n'
                            f'\nКоманда позволяет продолжить воспроизведения музыки\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}resume',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpCommand == 'pause' or helpCommand == 'pause':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}play`:**\n'
                            f'\nКоманда позволяет поставить на паузу музыку в голосом чате\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}pause`',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpCommand == 'play' or helpCommand == 'play':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}play`:**\n'
                            f'\nКоманда позволяет включить музыку в голосом чате\n'
                            f'\nКоманда приминяется с аргументамы:\n'
                            f'`{prefix}play <ссылка на музыку или названия музыки>`',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpCommand == 'leave' or helpCommand == 'leave':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}leave`:**\n'
                            f'\nКоманда отключает бота от голосового чата\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}leave`',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpCommand == 'join' or helpCommand == 'join':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}join`:**\n'
                            f'\nКоманда поделючает бота к голосовому чату\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}join`',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpCommand == 'nick' or helpCommand == 'nick':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}nick`:**\n'
                            f'\nКоманда позволяет изменить ник пользователя на сервере\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}nick <имя пользователя> <будущий ник>`',
                color=ctx.author.color)
            await ctx.respond(embed=embed)
        
        elif helpCommand == 'server':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}server`:**\n'
                            f'\nКоманда позволяет получить информацию о сервере\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}server`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'channel':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}channel`:**\n'
                            f'\nКоманда позволяет получить информацию о канале\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}channel`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'bot':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}bot`:**\n'
                            f'\nКоманда позволяет получить информацию о боте\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}bot`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'usd':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}usd`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}usd`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'euro':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}euro`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе евро\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}euro`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'uah':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}uah`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}uah`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'rub':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}rub`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}usd`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'pln':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}pln`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}pln`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'gbp':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}gbp`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}gbp`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'userinfo':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}userinfo`:**\n'
                            f'\nКоманда позволяет получить информацию о пользователе\n'
                            f'\nКоманда приминяется как с аргументом:\n'
                            f'`{prefix}userinfo <@пользователь>`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'roles':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}roles`:**\n'
                            f'\nКоманда позволяет получить информацию о всех ролях пользователя\n'
                            f'\nКоманда приминяется как с аргументом:\n'
                            f'`{prefix}roles <@пользователь>`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        # помощь раздела развлечение
        elif helpCommand == 'coin':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}coin`:**\n'
                            f'\nКоманда позволяет подкинуть монетку\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}coin`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'howdy':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}howdy`:**\n'
                            f'\nКоманда позволяет получить рандомное фото Хауди Хо\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}howdy`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'ben':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}ben`:**\n'
                            f'\nКоманда позволяет получить ответ на вопрос от Бена\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}ben <вопрос>`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'ping':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}ping`:**\n'
                            f'\nКоманда позволяет получить пинг бота\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}ping`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        # помощь раздела Модерирование
        elif helpCommand == 'ban':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}ban`:**\n'
                            f'\nКоманда позволяет забанить пользователя на сервере\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}ban <участник>`\n'
                            f'`{prefix}ban <участник> <причина>`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'kick':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}kick`:**\n'
                            f'\nКоманда позволяет увыгнать пользователя с сервера\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}kick <участник>`\n'
                            f'`{prefix}kick <участник> <причина>`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'clear':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}clear`:**\n'
                            f'\nКоманда позволяет удалить сообщения в канале\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}clear <количество сообщений>`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        elif helpCommand == 'slowmode':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}slowmode`:**\n'
                            f'\nКоманда позволяет установить медленный режим в канале\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}slowmode <секунди задержки>`\n',
                color=ctx.author.color)
            await ctx.respond(embed=embed)

        else:
            embed = discord.Embed(
                description=f'**Я не могу найти информацию о такой команде.**',
                color=0xe74c3c)
            await ctx.respond(embed=embed)
            print(helpCommand)
