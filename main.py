import discord
from discord.ext import commands
import  asyncio

cogs = ["general.py", "tests.py","voice1.py"]
token = "ODU3Mjc4NzU3MzI4NjUwMjQw.YNNRDw.TFWxaliukrXNJZ33dBU1CEFnRlo"

#set's prefix
bot = commands.Bot(command_prefix=">")

bot.remove_command("help")

for cog in cogs:
    bot.load_extension(cog[:-3])

@bot.event
async  def on_ready():
    print("Loading finnished")
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="out for >commands"))



bot.run(token)
