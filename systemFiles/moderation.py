import asyncio
import discord
import datetime
from discord.ext import commands


class Moder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot  

    @commands.command(aliases=["m"])
    @commands.has_permissions(kick_members=True)
    async def mute(self, ctx: commands.Context, member: discord.Member, time: int = 1, *, reason: str = None) -> None:
        role: discord.Role = await commands.RoleConverter().convert(ctx, "Muted")
        await member.add_roles(role, reason=reason)
        await add_entry(self.db, COMMANDS["MUTE"].collection, ctx.message.author, member, reason)

        replacement: dict = {"{member}": member.mention, "{time}": time, "{reason}": reason or ""}
        await ctx.send(embed=CommandEmbed(
            replace_placeholders(COMMANDS["MUTE"].title, replacement),
            replace_placeholders(COMMANDS["MUTE"].description, replacement),
            member,
        ))

        await asyncio.sleep(time * 60)
        await member.remove_roles(role)
        
    @commands.command(aliases=["nick"])
    @commands.guild_only()
    @commands.has_permissions(manage_nicknames=True)
    async def nickname(self, ctx, member: discord.Member, *, name=None):
        """ Nicknames a user from the current server. """
        try:
            await member.edit(nick=name, reason="need")
            message = f"Имя **{member.name}'s** поменято на ник **{name}**"
            if name is None:
                message = f"Сброс **{member.name}'s** ника"
            await ctx.send(message)
        except Exception as e:
            await ctx.send(e)    

    # Очистка чата
 #   @commands.command(aliases=['m'])
   # @commands.has_permissions(ban_members=True)
 #   async def mute(self, ctx, member: discord.Member = None, tim=None, reason=None):
    #    time = tim*60
  #      await member.timeout_for(duration=datetime.timedelta(seconds=time), reason=reason)

    # Очистка чата
    @commands.command(aliases=['clear', 'cls'])
    @commands.has_permissions(manage_messages=True)
    async def _clear(self, ctx, amount=None):
        if amount == None:
            await ctx.send('Введите количество сообщений для очистки как аргумент')
        else:
            await ctx.channel.purge(limit=int(amount))
            channel = self.bot.get_channel(ctx.channel.id)

            embed = discord.Embed(
               title=f"`{ctx.author.name}` удалил сообщенния в `{ctx.channel.name}`",
               description=f"{amount} сообщенний было удалено",
               colour=0xBF8040,
            )

            await channel.send(embed=embed)

    # Бан юзеров

    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            await ctx.send('Отметьте участника для бана как аргумент')
        else:
            await member.ban(reason=reason)
            embed = discord.Embed(
                title=f"`{ctx.author.name}` забанил: `{member.name}`",
                description=f"Причина: `{reason}`",
                colour=0xBF8040,
            )

            await ctx.send(embed=embed)

    # Кик участников

    @commands.command()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, member: discord.Member = None, *, reason=None):
        if member == None:
            await ctx.send('Отметьте участника для изгнания как аргумент')
        else:
            await member.kick(reason=reason)

            await ctx.send(f'{member} был выгнан с сервера!')
            embed = discord.Embed(
                title=f"`{ctx.author.name}` кикнул: `{member.name}`",
                description=f"Причина: `{reason}`",
                colour=0xBF8040,
            )

            await ctx.send(embed=embed)

    # Установка медленного режима

    @commands.command()
    @commands.has_permissions(manage_channels=True)
    async def slowmode(self, ctx, seconds: int = None):
        if seconds == None:
            await ctx.send('Отметьте время медленого режима как аргумент')
        else:
            await ctx.channel.edit(slowmode_delay=seconds)
            await ctx.send(f"Задержка в этом канале установленно на {seconds} секунд!")
