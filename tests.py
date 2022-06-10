import discord
from discord.ext import commands

class test(commands.Cog, name = "test"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(description="Profile picture", category="general")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def mypfp(self, ctx: commands.Context):
        authorus = ctx.author
        authoname = authorus.name
        pfp = authorus.avatar_url
        embed = discord.Embed(title=authoname + "'s profile picture", color=0xe512ef)
        embed.set_image(url=(pfp))
        await ctx.channel.send(embed=embed)

def setup(bot):
    bot.add_cog(test(bot))


# if message.content.upper().startswith('TEST'):
#     user = message.server.get_member("116273596605049942") # Fake snowflake, will not work
#     if not user:
#         return # Can't find the user, then quit
#     pfp = user.avatar_url
#     embed=discord.Embed(title="test", description='{}, test'.format(user.mention) , color=0xecce8b)
#     embed.set_image(url=(pfp))
#     await client.send_message(message.channel, embed=embed)
