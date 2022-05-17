import discord
from discord.ext import commands
import os

client=commands.Bot(command_prefix='!', status=discord.Status.idle)

@client.event
async def on_ready():
	print('Started')

client.run(os.environ["DISCORD_TOKEN"], bot=False)
