import random
import discord
from discord.ext import commands

import control

bot = commands.Bot(command_prefix="?", intents=discord.Intents.all())

@bot.command()
async def forward(ctx):
    control.forward()






bot.run("MTAwMTExMDY0NzQ5NDQyNjYyNA.G_-kba.Fw6EauyAwo7UYlPZYzJ5qXjcHRJk8WtpPuZNc8")