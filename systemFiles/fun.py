import json
import random
import discord
from discord.ext import commands


class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Подбросить монетку
    @commands.command()
    async def coin(self, ctx):
        x = random.randint(0, 1)
        if x == 0:
            value = 'Монетка летит... Выпадает **Орёл**'
        if x == 1:
            value = 'Монетка летит... Выпадает **Решка**'

        embed = discord.Embed(
            description=value,
            color=ctx.author.color)
        await ctx.send(embed=embed)

    # Рандомное фото Хауди Хо

    @commands.command(aliases=['howdy', 'howdyho'])
    async def _howdy(self, ctx):
        with open("systemFiles/package.json") as file:
            data_json = json.load(file)

        emb = discord.Embed(title="Howdy Ho", color=ctx.author.color)
        emb.set_image(url=random.choice(data_json["howdyho"]))
        await ctx.send(embed=emb)

    # Говорящий бен, но не разговаривает

    @commands.command()
    async def ben(self, ctx, Question=None):
        answer = ['Да', 'Нет', 'Хо-хо-хо']

        if Question == None:
            await ctx.send('Введите вопрос Бену как аргумент')
        else:
            embed = discord.Embed(
                description=f'**{random.choice(answer)}**',
                color=ctx.author.color)
            await ctx.send(embed=embed)

    # Рандомное фото Nsfw
 #   @commands.command()
  #  @commands.is_nsfw()
 #   async def nsfw(self, ctx):
 #       with open("systemFiles/package.json") as file:
  #          data_json = json.load(file)

    #    emb = discord.Embed(title=":underage: NSFW", color=ctx.author.color)
 #       emb.set_image(url=random.choice(data_json["nsfw"]))
  #      await ctx.send(embed=emb)

    # Ping - pong

    @commands.command()
    async def ping(self, ctx: commands.Context) -> None:
        ping_value = round(self.bot.latency * 1000)

        await ctx.send(
                f"Пинг: `{ping_value}`ms"
        )
