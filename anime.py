import discord
from discord.ext import commands

class anime(commands.Cog, name = "anime"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(description="Why would you write this one?", category = "anime")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def nicotine(self,ctx: commands.Context):
        await ctx.author.send(file=discord.File("pictures/anime/nicotine.png"))

def setup(bot):
    bot.add_cog(anime(bot))