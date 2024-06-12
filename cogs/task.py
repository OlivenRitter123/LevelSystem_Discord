
import discord
from discord.ext import commands, tasks

class Task(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.werbung.start()

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Logged in as {self.bot.user}')
        if not self.werbung.is_running():
            self.werbung.start()

    @tasks.loop(hours=2)
    async def werbung(self):
        try:
            channel = await self.bot.fetch_channel(1235657661744418919)
            await channel.send(
                "╒══════╣Knax Entertainment╠════════╕ \n\n"
                "Was wir euch anbieten! \n\n"
                "『-』Freundliches und aktives Team \n"
                "『-』Schnellen Support\n"
                "『-』Freundliche Community\n"
                "『-』Aktive Updates\n"
                "『-』Aktive giveaways\n"
                "『-』Wöchentliche Events\n\n"
                "Was wir noch suchen!\n\n"
                "『-』Aktive Mitglieder\n"
                "『-』Teammitglieder\n\n"
                "Noch nicht überzeugt?\n"
                "Dann Joine jetzt noch auf unserem Discord und überzeug dich selbst!\n\n"
                "╒══════╣Knax Entertainment╠════════╕\n"
                "https://discord.gg/knax"
            )
        except Exception as e:
            print(f'Error sending message: {e}')

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            try:
                await message.publish()
                print(f'Message published: {message.id}')
            except Exception as e:
                print(f'Error publishing message: {e}')

def setup(bot):
    bot.add_cog(Task(bot))