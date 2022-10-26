import asyncio
import discord
from discord.ext import commands


class Moder(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Очистка чата
    @commands.command(aliases=['clear', 'cls'])
    @commands.has_permissions(manage_messages=True)
    async def _clear(self, ctx, amount=None):
        if amount == None:
            await ctx.send('Введите количество сообщений для очистки как аргумент')
        else:
            await ctx.channel.purge(limit=int(amount + 1))
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
    async def ban(self, ctx, member: discord.Member = None, reason=None):
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
    async def kick(self, ctx, member: discord.Member = None, reason=None):
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

    # Мьют участников
'''
    @commands.command()
    @commands.has_permissions(manage_roles=True)
    async def mute(self, ctx, member: discord.Member = None, time=None):
        if member == None:
            await ctx.send('Отметьте участника для мьюта как аргумент')
        else:
            await ctx.guild.create_role(name="MG-muted", permissions=discord.Permissions(permissions=1024))
            mute_role = discord.utils.get(ctx.guild.roles, name="MG-muted", can_send_message=false)
            await member.add_roles(mute_role)

            if time == None:
                await ctx.send(f"{member.mention} был замьючен!")
            else:
                await ctx.send(f"{member.mention} был замьючен на {time} секунд!")
                await asyncio.sleep(int(time))
                await member.remove_roles(mute_role)
'''