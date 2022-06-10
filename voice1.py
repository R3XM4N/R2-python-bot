import discord
from discord.ext import commands
import time

class voice1(commands.Cog, name = "voice"):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(description="You know what this is", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def anarchy(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/oldest.mp3"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="THATS A LOT OF DAMAGE.", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def damage(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/now-thats.mp3"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="F ur dog.", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def f_ur_dog(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/donddog.mp3"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="I DOND DOG", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def i_dond_dog(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/idonddog.mp3"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="michal jordan", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def michael_jordan(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/michaljordan.mp3"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="60s", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def jamal(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",
                                               source="sounds/jamal-says-every-60-seconds-in-africa-a-minute-passes_1.mp3"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="Gotta move that gear up!", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def move_up(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(
            discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/Engineer_moveup01.wav"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="Why are you gay.", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def gay(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(
            discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/gay.mp3"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="You picked the wrong house fool!", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def big_smoke(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/big_smoke.wav"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="...", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def arm_fuck(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/senator1.mp3"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="Not_implemented", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def combustible_lemon(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe", source="sounds/Cave_Johnson_eighties_outro11.wav"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="Not_implemented", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def take_lemon_back(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",
                                               source="sounds/Cave_Johnson_eighties_outro09.wav"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="This is the part where he kills you.", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def pwhe_killsyou(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",
                                               source="sounds/Wheatley_bw_a4_death_trap01.wav"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="Not_implemented.", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def cake_bake(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",
                                               source="sounds/GLaDOS_14_part1_entry-2.wav"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()

    @commands.command(description="Not_implemented.", category="voice")
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def senpie(self, ctx: commands.Context):
        vc = ctx.author.voice.channel
        connection = await vc.connect()
        connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",
                                               source="sounds/senpai.wav"))
        while connection.is_playing():
            time.sleep(0.2)
        await connection.disconnect()
    #
    # @commands.command(description="Not_implemented.", category="voice")
    # @commands.cooldown(1, 15, commands.BucketType.user)
    # async def stand(self, ctx: commands.Context):
    #     vc = ctx.author.voice.channel
    #     connection = await vc.connect()
    #     connection.play(discord.FFmpegPCMAudio(executable="ffmpeg/bin/ffmpeg.exe",
    #                                            source="sounds/4-23 It Has To Be This Way (Original Version).wav"))
    #     while connection.is_playing():
    #         time.sleep(0.2)
    #     await connection.disconnect()

def setup(bot):
    bot.add_cog(voice1(bot))