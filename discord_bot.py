import os
import discord
import openai
from discord import Intents
from discord.ext import commands

# 从环境变量中获取 Discord 令牌和 OpenAI API 密钥
DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
OPENAI_API_KEY = os.environ['OPENAI_API_KEY']

# 设置 OpenAI API 密钥
openai.api_key = OPENAI_API_KEY

# 创建 Intents 对象并启用所需的意图
intents = Intents.default()
intents.messages = True
intents.guild_messages = True

# 创建一个带有指定前缀和意图的 bot 实例
bot = commands.Bot(command_prefix="/", intents=intents)

# 定义一个命令 "/g"，它将接收一个 query 参数
@bot.command(name="g")
async def g3(ctx, *, query):
    # 设置 API 请求参数
    model_engine = "gpt-3.5-turbo"

    # 请求 OpenAI API
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}],
        max_tokens=2000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 从响应中提取生成的文本
    generated_text = response.choices[0].message['content'].strip()

    # 将生成的文本发送回 Discord 频道
    await ctx.send(generated_text)

# 定义一个命令 "/gg"，它将接收一个 query 参数
@bot.command(name="gg")
async def g3(ctx, *, query):
    # 设置 API 请求参数
    model_engine = "gpt-4"

    # 请求 OpenAI API
    response = openai.ChatCompletion.create(
        model=model_engine,
        messages=[{"role": "system", "content": "You are a helpful assistant."}, {"role": "user", "content": query}],
        max_tokens=4000,
        n=1,
        stop=None,
        temperature=0.5,
    )

    # 从响应中提取生成的文本
    generated_text = response.choices[0].message['content'].strip()

    # 将生成的文本发送回 Discord 频道
    await ctx.send(generated_text)

# 运行 bot
bot.run(DISCORD_TOKEN)

