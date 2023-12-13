import discord, random, json, requests
from discord.ext import commands

class catPics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
    
    def get_quote(self):
        response = requests.get("https://api.thecatapi.com/v1/images/search")
        json_data = json.loads(response.text)
        quote = json_data[0]["url"]
        return(quote)

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def catpics(self, ctx):
        quote = self.get_quote()
        await ctx.reply(f"{quote}")

async def setup(bot):
    await bot.add_cog(catPics(bot))