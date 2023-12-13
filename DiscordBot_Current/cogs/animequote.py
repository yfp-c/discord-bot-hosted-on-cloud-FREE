import discord
import random
import json
import requests
from discord.ext import commands

class AnimeQuotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to fetch an anime quote from the AnimeChan API
    def get_anime_quote(self):
        response = requests.get("https://animechan.xyz/api/random")
        json_data = json.loads(response.text)
        if 'error' not in json_data:
            quote = json_data["quote"]
            anime = json_data["anime"]
            character = json_data["character"]
            return f"{quote} \n\n~ {character} from {anime}"
        else:
            return "Sorry, I couldn't fetch a quote at this time. It has probably been ratelimited for an hour (free api)."

    # Listener to ignore bot's own messages
    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

    # Command to fetch and send an anime quote
    @commands.command()
    @commands.cooldown(1, 60, commands.BucketType.user)
    async def animequote(self, ctx):
        # Call the get_anime_quote method to fetch an anime quote
        quote = self.get_anime_quote()
        # Send the anime quote as a reply
        await ctx.reply(f"```\n 🌟 {quote} 🌟```")

async def setup(bot):
    await bot.add_cog(AnimeQuotes(bot))
