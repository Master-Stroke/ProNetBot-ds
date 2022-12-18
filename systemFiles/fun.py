import json
import random
import discord
from discord.ext import commands
from discord import Option
from datetime import timedelta
from random import choice
from requests import get

bot = discord.Bot()

class Fun(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    @bot.slash_command(name = "8ball", description = "Получить рандомный ответ от бота")
    async def eightball(self, ctx, *, question: commands.clean_content):
      """ Consult 8ball to receive an answer """
      if question == None:
            embed = discord.Embed(
                description=f"**Введите вопрос к боту как аргумент!**",
                colour=0xe74c3c,
            )

            await ctx.respond(embed=embed)
      else:
        ballresponse = [
            "Да", "Нет", "хмм...", "Очень сомнительно",
            "Конечно", "Без сомнения", "Возможно",
            "Ты думай", "не... (╯°□°）╯︵ ┻━┻" ]

        answer = random.choice(ballresponse)
        embed = discord.Embed(
                description=f"🎱 **Вопрос:** {question}\n**Ответ:** {answer}",
                colour=0x546e7a,
            )
        await ctx.respond(embed=embed)

    # Подбросить монетку
    @bot.slash_command(name = "coin", description = "Подкинуть монетку")
    async def coin(self, ctx):
        x = random.randint(0, 1)
        if x == 0:
            value = 'Монетка летит... Выпадает **Орёл**'
        if x == 1:
            value = 'Монетка летит... Выпадает **Решка**'

        embed = discord.Embed(
            description=value,
            color=ctx.author.color)
        await ctx.respond(embed=embed)

    # Рандомное фото Хауди Хо

    @bot.slash_command(name = "howdy", description = "Рандомное фото хауди хо")
    async def _howdy(self, ctx):
        with open("systemFiles/package.json") as file:
            data_json = json.load(file)

        emb = discord.Embed(title="Howdy Ho", color=ctx.author.color)
        emb.set_image(url=random.choice(data_json["howdyho"]))
        await ctx.respond(embed=emb)

    @bot.slash_command(name = "mem", description = "Рандомный IT мем")
    async def _mem(self, ctx):
        with open("systemFiles/package.json") as file:
            data_json = json.load(file)

        emb = discord.Embed(title="IT Мем", color=ctx.author.color)
        emb.set_image(url=random.choice(data_json["mems"]))
        await ctx.respond(embed=emb)

    # Говорящий бен, но не разговаривает

    @bot.slash_command(name = "ben", description = "Вопрос к бену")
    async def ben(self, ctx, question: commands.clean_content):
        answer = ['Да', 'Нет', 'Хо-хо-хо']
        if question == None:
            embed = discord.Embed(
                description=f"**Введите вопрос Бену как аргумент!**",
                colour=0xe74c3c,
            )

            await ctx.respond(embed=embed)
        else:
            embed = discord.Embed(
                description=f'**{random.choice(answer)}**',
                color=0xe67e22)
            await ctx.respond(embed=embed)

    # Рандомное фото Nsfw
 #   @bot.slash_command(name = "nsfw", description = "Рандомное nsfw фото")
  #  @commands.is_nsfw()
    #async def nsfw(self, ctx):
     #   with open("systemFiles/package.json") as file:
      #      data_json = json.load(file)
#
 #       emb = discord.Embed(title=":underage: NSFW", color=ctx.author.color)
  #      emb.set_image(url=random.choice(data_json["nsfw"]))
   #     await ctx.respond(embed=emb)

    @bot.slash_command(name = "nsfw", description = "Рандомное nsfw фото")
    async def _nsfw(self, ctx, ptype=None):
        if not ctx.channel.nsfw:
            emb = discord.Embed(description="**Текущий канал должен быть nsfw!**", color=0xe74c3c)
            await ctx.respond(embed=emb)
            return
        if not ptype:
            emb = discord.Embed(title="**Используйте:**", description="**`/nsfw <cosplay, hental, ass, pgif, swimsult, thigh, hass, boobs, hboobs, pussy, anal, blowjob, tentacle>`**")
            await ctx.respond(embed=emb)
        else:
           path = 'https://nekobot.xyz/api/image?type=' + ptype

           response = get(path)

           if response.ok:
               await ctx.respond(response.json()['message'])

   #     else:
    #        log_error(f'{response.status_code} {response.json()["message"]}')
 #   @commands.command()
  #  @commands.is_not_nsfw()
   # async def nsfw(self, ctx):
    #    await ctx.message.add_reaction('❌')
     #   emb = discord.Embed(title="Текущий канал должен быть nsfw!")
      #  await ctx.send(embed=emb)
