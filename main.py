# Necessary libs
import discord # Discord API
from discord.ext import commands 
import music # music.py

"""
pip install discord.py
pip install youtube_dl
"""

cogs = [music] 

client = commands.Bot(command_prefix="@", intents = discord.Intents.all())

for i in range(len(cogs)):
  cogs[i].setup(client)


client.run("########################") # Bot token goes here.