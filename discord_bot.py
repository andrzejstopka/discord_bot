import os
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyBot(commands.Bot):
    def __init__(self, command_prefix):
        super().__init__(command_prefix)

        @self.command(name="chat")
        async def chat_response(ctx):
            if ctx.message.author == self.user:
                return

            await ctx.send('GPT')

bot = MyBot(command_prefix='!')
bot.run(TOKEN)



