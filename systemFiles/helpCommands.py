import discord
from discord.ext import commands
from config import settings


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(aliases=['help', 'помощь'])
    async def _help(self, ctx, helpCommand=None):
        prefix = settings['prefix']
        botId = discord.utils.get(ctx.guild.members, id=settings['id'])

        # общий help
        if helpCommand == None or helpCommand == 'help':
            embed = discord.Embed(
                description=f'**Информация о командах:**\n'
                            f'\nВы можете получить детальную справку по каждой команде\n'
                            f'Например: `{prefix}help server`\n'
                            f'\n:bar_chart: Информация\n'
                            f'`{prefix}help` `{prefix}rules` `{prefix}server` `{prefix}channel` `{prefix}user` `{prefix}roles` `{prefix}bot` `{prefix}ping`'
                            f'\n:toolbox: Модерация\n'
                            f'`{prefix}ban` `{prefix}kick` `{prefix}clear` `{prefix}slowmode` `{prefix}report`'
                            f'\n:dollar: Курс валют\n'
                            f'`{prefix}usd` `{prefix}eur` `{prefix}uah` `{prefix}rub` `{prefix}pln` `{prefix}gbp`'
                            f'\n:joystick: Развлечение\n'
                            f'`{prefix}coin` `{prefix}howdy` `{prefix}ben`'
                            f'\n⠀',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        # помощь раздела информации
        elif helpCommand == 'serverinfo' or helpCommand == 'server':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}serverinfo`:**\n'
                            f'\nКоманда позволяет получить информацию о сервере\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}server`\n'
                            f'`{prefix}serverinfo`',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'channel' or helpCommand == 'channelinfo':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}channel`:**\n'
                            f'\nКоманда позволяет получить информацию о канале\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}channel`\n'
                            f'`{prefix}channelinfo`',
                color=ctx.author.color)
            await ctx.send(embed=embed)   

        elif helpCommand == 'info' or helpCommand == 'bot':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}bot`:**\n'
                            f'\nКоманда позволяет получить информацию о боте\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}bot`\n'
                            f'`{prefix}info`',
                color=ctx.author.color)
            await ctx.send(embed=embed) 

        elif helpCommand == 'report':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}report`:**\n'
                            f'\nКоманда позволяет пожаловаться на пользователя\n'
                            f'\nКоманда должна бить ответом на сообщенния:\n'
                            f'`{prefix}report`',
                color=ctx.author.color)
            await ctx.send(embed=embed) 

        elif helpCommand == 'dollar' or helpCommand == 'usd':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}usd`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}usd`\n'
                            f'`{prefix}dollar`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'euro' or helpCommand == 'eur':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}usd`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе евро\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}eur`\n'
                            f'`{prefix}euro`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'hryvnia' or helpCommand == 'uah':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}usd`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}usd`\n'
                            f'`{prefix}dollar`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'ruble' or helpCommand == 'rub':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}usd`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}usd`\n'
                            f'`{prefix}dollar`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'zlota' or helpCommand == 'pln':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}usd`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}usd`\n'
                            f'`{prefix}dollar`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'pound' or helpCommand == 'gbp':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}usd`:**\n'
                            f'\nКоманда позволяет получить информацию о курсе доллара\n'
                            f'\nКоманда приминяется без аргументов:\n'
                            f'`{prefix}usd`\n'
                            f'`{prefix}dollar`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'userinfo' or helpCommand == 'user':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}userinfo`:**\n'
                            f'\nКоманда позволяет получить информацию о пользователе\n'
                            f'\nКоманда приминяется как с аргументом так и без:\n'
                            f'`{prefix}user`\n'
                            f'`{prefix}user <@пользователь>`\n'
                            f'`{prefix}userinfo`\n'
                            f'`{prefix}userinfo <@пользователь>`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'roles' or helpCommand == 'myroles':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}roles`:**\n'
                            f'\nКоманда позволяет получить информацию о всех ролях пользователя\n'
                            f'\nКоманда приминяется как с аргументом так и без:\n'
                            f'`{prefix}myroles`\n'
                            f'`{prefix}roles`\n'
                            f'`{prefix}roles <@пользователь>`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        # помощь раздела развлечение
        elif helpCommand == 'coin':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}coin`:**\n'
                            f'\nКоманда позволяет подкинуть монетку\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}coin`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'howdy' or helpCommand == 'howdyho':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}howdy`:**\n'
                            f'\nКоманда позволяет получить рандомное фото Хауди Хо\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}howdy`\n'
                            f'`{prefix}howdyho`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'ben':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}ben`:**\n'
                            f'\nКоманда позволяет получить ответ на вопрос от Бена\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}ben <вопрос>`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

    #    elif helpCommand == 'nsfw':
    #        embed = discord.Embed(
      #          description=f'**Информация о командe `{prefix}nsfw`:**\n'
    #                        f'\nКоманда позволяет получить nsfw аниме фото\n'
       #                     f':warning: Команду можно применить только в NSFW чатах\n'
    #                        f'\nКоманда приминяется без аргумента:\n'
       #                     f'`{prefix}nsfw`\n'
     #                       f'⠀',
      #          color=ctx.author.color)
      #      await ctx.send(embed=embed)

        elif helpCommand == 'ping':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}ping`:**\n'
                            f'\nКоманда позволяет получить пинг бота\n'
                            f'\nКоманда приминяется без аргумента:\n'
                            f'`{prefix}ping`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        # помощь раздела Модерирование
        elif helpCommand == 'ban':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}ban`:**\n'
                            f'\nКоманда позволяет забанить пользователя на сервере\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}ban <участник>`\n'
                            f'`{prefix}ban <участник> <причина>`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'kick':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}kick`:**\n'
                            f'\nКоманда позволяет увыгнать пользователя с сервера\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}kick <участник>`\n'
                            f'`{prefix}kick <участник> <причина>`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'cls' or helpCommand == 'clear':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}clear`:**\n'
                            f'\nКоманда позволяет удалить сообщения в канале\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}cls <количество сообщений>`\n'
                            f'`{prefix}clear <количество сообщений>`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

        elif helpCommand == 'slowmode':
            embed = discord.Embed(
                description=f'**Информация о командe `{prefix}slowmode`:**\n'
                            f'\nКоманда позволяет установить медленный режим в канале\n'
                            f'\nКоманда приминяется с аргументом:\n'
                            f'`{prefix}slowmode <время задержки>`\n',
                color=ctx.author.color)
            await ctx.send(embed=embed)

 #       elif helpCommand == 'mute':
  #          embed = discord.Embed(
  #              description=f'**Информация о командe `{prefix}mute`:**\n'
   #                         f'\nКоманда позволяет замьютить участника на сервере\n'
    #                        f':warning: Команду работает только если у everyone отключены все права\n'
   #                         f'\nКоманда приминяется с аргументом:\n'
   #                         f'`{prefix}mute <участник>`\n'
    #                        f'`{prefix}mute <участник> <время в секундах>`\n'
    #                        f'⠀',
   #             color=ctx.author.color)
  #          embed.set_footer(text=' by illia841 ©',
  #                           icon_url="https://i.ibb.co/0hDpXRf/00.png")
   #         await ctx.send(embed=embed)
#
        else:
            await ctx.send('Упс.. Я не могу найти информацию о такой команде.')
            print(helpCommand)