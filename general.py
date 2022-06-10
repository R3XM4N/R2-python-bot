import discord
from discord.ext import commands

class general(commands.Cog, name = "general"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(description="Profile picture of this bot", category="general")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def r2pfp(self, ctx: commands.Context):
        await ctx.channel.send("R2 space theme", file=discord.File("pics\Important\R2pfp.png"))

def setup(bot):
    bot.add_cog(general(bot))