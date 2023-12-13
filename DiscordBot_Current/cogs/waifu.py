import discord
import requests
from discord.ext import commands

class WaifuImages(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    # Method to fetch a waifu image from waifu.im API
    def get_waifu_image(self):
        # For this example, I'm using the SFW 'waifu' category. You can change this as needed.
        response = requests.get("https://api.waifu.im/search")
        if response.status_code == 200:
            json_data = response.json()
            image_url = json_data['images'][0]['url']
            return image_url
        else:
            return "Sorry, I couldn't fetch an image at this time."

    # Command to fetch and send a waifu image
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def waifu(self, ctx):
        # Call the get_waifu_image method to fetch an image
        image_url = self.get_waifu_image()
        # Send the image URL as a reply
        if image_url.startswith("http"):
            embed = discord.Embed()
            embed.set_image(url=image_url)
            await ctx.reply(embed=embed)
        else:
            await ctx.reply(image_url)

async def setup(bot):
    await bot.add_cog(WaifuImages(bot))
