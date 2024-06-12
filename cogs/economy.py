from discord.ext import commands
from discord.commands import slash_command, Option
import aiosqlite
import random
import discord

class economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.DB = "level.db"

def setup(bot):
    bot.add_cog(economy(bot))