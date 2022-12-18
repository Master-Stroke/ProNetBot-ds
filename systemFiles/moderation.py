import asyncio
import discord
import datetime
from discord.ext import commands
from discord import Option
from datetime import timedelta

bot = discord.Bot()

class Moder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  

  #  @bot.slash_command(name = "report", description = "Жалоба на пользователя", guild_ids = [975057574326050946])
 #   @commands.guild_only()
  #  async def nickname(self, ctx, member: discord.Member, *, reason=None):
#{ctx.author.name}

    @bot.slash_command(name = "nick", description = "Смена ника пользователя")
   # @commands.command(aliases=["nick"])
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, name=None):
        """ Nicknames a user from the current server. """
        try:
            await member.edit(nick=name, reason="need")
            embed = discord.Embed(
                title=f"**Имя **{member.name}'s** измененно на ник {name}**",
            )
            if name is None:
                embed = discord.Embed(
                title=f"**Сброс **{member.name}'s** ника**",
                )
            await ctx.respond(embed=embed) #respond send
        except Exception as e:
            await ctx.respond(e) #respond send

    # Очистка чата
 #   @commands.command(aliases=['m'])
   # @commands.has_permissions(ban_members=True)
 #   async def mute(self, ctx, member: discord.Member = None, tim=None, reason=None):
    #    time = tim*60
  #      await member.timeout_for(duration=datetime.timedelta(seconds=time), reason=reason)

    # Очистка чата
    @bot.slash_command(name = "clear", description = "Очистка чата")
#    @commands.command(aliases=['clear', 'cls'])
    @commands.has_permissions(manage_messages=True)
    async def _clear(self, ctx, amount: commands.clean_content):
        if amount == None:
            embed = discord.Embed(
                description=f"**Введите количество сообщений для очистки как аргумент!**",
                colour=0xe74c3c,
            )

            await ctx.respond(embed=embed)
        else:
            await ctx.channel.purge(limit=int(amount))
           # channel = self.bot.get_channel(ctx.channel.id)

            embed = discord.Embed(
               title=f"`{ctx.author.name}` удалил сообщенния в `{ctx.channel.name}`",
               description=f"{amount} сообщенний было удалено",
               colour=0xBF8040,
            )

            await ctx.respond(embed=embed)

    # Кик участников

    @bot.slash_command(name = "kick", description = "Кик пользователя")
    @commands.has_permissions(kick_members=True)
    async def _kick(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            embed = discord.Embed(
                description=f"**Отметьте участника для кика как аргумент!**",
                colour=0xe74c3c,
            )

            await ctx.respond(embed=embed)
        else:
            await member.kick(reason=reason)

          #  await ctx.send(f'{member} был выгнан с сервера!')
            embed = discord.Embed(
                title=f"`{ctx.author.name}` кикнул: `{member.name}`",
                description=f"Причина: `{reason}`",
                colour=0xBF8040,
            )

            await ctx.respond(embed=embed)

    # Бан юзеров

    @bot.slash_command(name = "ban", description = "Бан пользователя")
    @commands.has_permissions(ban_members=True)
    async def _ban(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            embed = discord.Embed(
                description=f"**Отметьте участника для бана как аргумент!**",
                colour=0xe74c3c,
            )

            await ctx.respond(embed=embed)
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title=f"`{ctx.author.name}` забанил: `{member.name}`",
                description=f"Причина: `{reason}`",
                colour=0xBF8040,
            )

            await ctx.respond(embed=embed)

    # Установка медленного режима

    @bot.slash_command(name = "slowmode", description = "Словмод в канале")
    @commands.has_permissions(manage_channels=True)
    async def _slowmode(self, ctx, seconds: commands.clean_content):
        if seconds == None:
            embed = discord.Embed(
                description=f"**Отметьте время медленого режима как аргумент!**",#: commands.clean_content
                colour=0xe74c3c,
            )

            await ctx.respond(embed=embed)
       # if seconds == "off":
        #    await ctx.channel.edit(slowmode_delay=seconds)
         #   embed = discord.Embed(
          #      description=f"**Задержка в этом канале убрана!**",
           #     colour=0x95a5a6,
            #)
            #await ctx.respond(embed=embed)
        else:
            await ctx.channel.edit(slowmode_delay=seconds)
            embed = discord.Embed(
                description=f"**Задержка в этом канале установленно на {seconds} секунд!**",
                colour=0x95a5a6,
            )
            await ctx.respond(embed=embed)
