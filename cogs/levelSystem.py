from discord.ext import commands
from discord.commands import slash_command, Option
import aiosqlite
import random
import discord

class levelSystem(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.DB = "level.db"

    @staticmethod
    def get_level(xp):
        lvl = 0
        xp_needed = 100 # Start-Erfahrungsbedarf

        while True:
            xp -= xp_needed
            if xp < 0:
                return lvl
            lvl += 1
            xp_needed *= 1.04  # Erfahrungsbedarf um 2% erhöhen


    @commands.Cog.listener()
    async def on_ready(self):
        async with aiosqlite.connect(self.DB) as db:
            await db.execute(
                """
                CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                msg_count INTEGER DEFAULT 0,
                xp INTEGER DEFAULT 0
                )
                """
            )
    async def check_user(self, user_id):
        async with aiosqlite.connect(self.DB) as db:
            await db.execute(
                "INSERT OR IGNORE INTO users (user_id) VALUES (?)", (user_id,)
            )
            await db.commit()


    async def get_xp(self, user_id):
        await self.check_user(user_id)
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute("SELECT msg_count, xp FROM users WHERE user_id = ?", (user_id,)) as cursor:
                result = await cursor.fetchone()

        return result[1]

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author.bot:
            return
        if not message.guild:
            return
        xp = 2;
        await self.check_user(message.author.id)
        async with aiosqlite.connect(self.DB) as db:

            await db.execute(
                "UPDATE users SET msg_count = msg_count + 1, xp = xp + ? WHERE user_id = ?", (2, message.author.id)
            )

            await db.commit()
        new_xp = await self.get_xp(message.author.id)

        old_level = self.get_level(new_xp - xp)
        new_level = self.get_level(new_xp)

        if new_level == old_level:
            return
        if new_level > old_level:
            await message.channel.send(
                f"{message.author.mention} Du hast Level {new_level} erreicht")









    @slash_command()
    async def rank(self, ctx, user: Option(discord.Member, "Gib einen nutzer an", default=None)):
        if user is None:
            user = ctx.author
        xp = await self.get_xp(user.id)
        lvl = self.get_level(xp)

        embed = discord.Embed(
            title="XP und Level",
            description=f"{user.mention} hat **{xp}** XP und ist Level **{lvl}**",
            color=discord.Color.random()
        )
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(text="Made by Olive")
        await ctx.respond(embed=embed)


    @slash_command()
    async def messages(self, ctx, user: Option(discord.Member, "Gib einen Nutzer an", default=None)):
        if user is None:
            user = ctx.author
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute("SELECT msg_count, xp FROM users WHERE user_id = ?", (user.id,)) as cursor:
                result = await cursor.fetchone()
                if result is None:
                    await ctx.respond("Du bist noch nicht in der Datenbank", ephemeral=True)
                    return
                msg_count, xp = result;


        embed = discord.Embed(
            title="Nahrichten",
            description=f"{user.mention} hat **{result[0]}** Nachrichten gesendet",
            color=discord.Color.random()
        )
        embed.set_thumbnail(url=user.avatar.url)
        embed.set_footer(text="Made by Olive")
        await ctx.respond(embed=embed)

    @slash_command()
    async def leaderboard(self, ctx):
        desc = ""
        counter = 1
        async with aiosqlite.connect(self.DB) as db:
            async with db.execute(
                "SELECT user_id, xp FROM users WHERE msg_count > 0 ORDER BY xp DESC LIMIT 10"
            ) as cursor:
                async for user_id, xp in cursor:
                    desc += f"{counter}. <@{user_id}> - {xp} XP\n"
                    counter += 1

        embed = discord.Embed(
            title="Rangliste",
            description=desc,
            color=discord.Color.random()
        )
        embed.set_thumbnail(url=self.bot.user.avatar.url)
        embed.set_footer(text="Made by Olive")
        await ctx.respond(embed=embed)





def setup(bot):
    bot.add_cog(levelSystem(bot))