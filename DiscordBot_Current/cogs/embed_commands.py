import discord
import random
from discord.ext import commands

class embed_commands(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.gifs = {
            'good_luck': ['https://c.tenor.com/nKE3fkQlJOMAAAAM/good-luck-fighting.gif', 'https://c.tenor.com/tTSmnRmlWjUAAAAC/good-luck-anime.gif',
                'https://c.tenor.com/OKoyV34l5JQAAAAC/good-luck-sign-of-the-cross.gif', 'https://c.tenor.com/MZ6C4OO8HvcAAAAC/pikachu-good-luck.gif',
                'https://acegif.com/wp-content/gifs/good-luck-13.gif', 'https://c.tenor.com/P07pbQA_cjAAAAAC/good-luck-adventure-time.gif',
                'https://c.tenor.com/kQLNIz-0FgkAAAAC/good-luck-taken.gif', 'https://c.tenor.com/cmqX6WK0oxQAAAAC/good-luck-captain-america.gif'],

            'good_morning': ['https://media2.giphy.com/media/WaYIFw9ZiEn1fPcH8Y/giphy.gif?', 'https://i.pinimg.com/originals/0f/41/8a/0f418a807d4d1e40fb8428b04b86e72f.gif',
                'https://i.pinimg.com/originals/e5/8e/30/e58e300d3a2f068314db9c567a8b2772.gif', 'https://i.pinimg.com/originals/b9/36/b3/b936b3188601b9376c72ed358dac45d8.gif',
                'https://www.gifcen.com/wp-content/uploads/2022/02/funny-good-morning-gif-3.gif', 'https://c.tenor.com/kAaTGOhxGLYAAAAC/inosuke-demon.gif',
                'https://c.tenor.com/kDAyvJIaw7EAAAAd/poppyseedies.gif', 'https://c.tenor.com/CFuuZZSyQUkAAAAC/good-morning-wake-up.gif',
                'https://c.tenor.com/OH5Vd-yZHrUAAAAC/good-morning-skeleton-meme.gif', 'https://c.tenor.com/TZuZJYTomgwAAAAC/good-morning-morning.gif',
                'https://c.tenor.com/_rp_yHj7Nn4AAAAd/good-morning.gif', 'https://c.tenor.com/yK-webGfL84AAAAC/good-morning-wishes.gif', 'https://media1.giphy.com/media/ujh2qQvMVlZflF1mPQ/giphy.gif?'],

            'brilliant':    ['https://media.giphy.com/media/26BRBKqUiq586bRVm/giphy.gif', 'https://media.giphy.com/media/3otPoFIPdGqzjUWpeE/giphy.gif',
                'https://media.giphy.com/media/TjGFDxbbZRYjv9vpCL/giphy.gif', 'https://media.giphy.com/media/8jn9eiO3HjT0pU3zqe/giphy.gif',
                'https://media.giphy.com/media/SXgIu2UVUj4UwbyaGz/giphy.gif', 'https://media.giphy.com/media/W1wC5ye0qPoTQ6Gzhd/giphy.gif'],
            
            'how_are_we_doing': ['https://media1.giphy.com/media/3ohA2FAHazPGAEsgYo/giphy.gif?', 'https://media.giphy.com/media/XUyYa4TRSX66Y2dCzr/giphy.gif',
                'https://media.giphy.com/media/l2YWhoXYKGiN7IVDW/giphy.gif', 'https://media.giphy.com/media/l2Je1kFLMlL9AJStG/giphy.gif',
                'https://media.giphy.com/media/TFhtlAv944YWTJhk5u/giphy.gif', 'https://media.giphy.com/media/BCYyBrWW4520w/giphy.gif'],
        }

    def create_embed(self, description, gif_category):
        embed = discord.Embed(
            colour=discord.Colour.random(),
            description=description
        )
        embed.set_image(url=random.choice(self.gifs[gif_category]))
        return embed

    # helpme command with good luck gif
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def helpme(self, ctx):
        description = (f" **Goooooood mooooooorning {ctx.author.name}!!!** The commands are as follows: \n"
        "- **!quote/!q** to read my wonderful quotes, \n"
        "- **!sbot** to read my catchphrase, \n"
        "- **!catpics** for pictures of cats, \n"
        "- **!animequote** for random anime quotes by their characters and the name of the anime, \n"
        "- **!biryani** for an image of our favourite dish, \n"
        "- **!advice** if you are feeling lost and need advice, \n"
        "- **!fc/!fortunecookie** to read your fortune and lucky numbers for today! \n"
        "- **!inspire** to feel inspired! \n"
        "- **!colour** for a random colour! \n"
        "- **!daily** for your daily stats! \n"
        "- **!tt/!tradingtips** for some sound financial advice! \n"
        "- **!yesno** with a question afterwards for my expert and final opinion! \n"
        "- **!gm** and **@someone** to give them a special goooooooood moooooooooorning!!!!! \n "
        "- **!gl** and **@someone** to wish them good luck!\n"
        "- **!how** to say How are we doing guys?\n"
        "- **!br** to say brilliant!\n"
        "- **!trans/!translate** [language to translate to] [text] to translate!\n"
        "- **!todo/!do** for my advice on what to do today, \n"
        "- **!truth/!truthr** for truth or dare.. or a cheeky R rated truth or dare! \n"
        "- **!????** There's a hidden command, can you guess it? :eyes: \n"
        " Also team, there's a **cooldown** on my commands! **Good luck!!!!**")
        embed = self.create_embed(description, 'good_luck')
        await ctx.reply(embed=embed)

    # gl command
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def gl(self, ctx, member: discord.Member):
        description = f"Good luck! {member.mention}"
        embed = self.create_embed(description, 'good_luck')
        await ctx.reply(embed=embed)

    # hello command
    @commands.command()
    @commands.cooldown(1, 15, commands.BucketType.user)
    async def hello(self, ctx):
        await ctx.reply('Hello!')

    # shahrukh command
    @commands.command(pass_context=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def sbot(self, ctx):
        description = f"Goooooooood mooooooooooorninggg!!! {ctx.author.mention}"
        embed = self.create_embed(description, 'good_morning')
        await ctx.reply(embed=embed)

    # br command
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def br(self, ctx):
        description = f"Brilliant!"
        embed = self.create_embed(description, 'brilliant')
        await ctx.reply(embed=embed)

    # how command
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def how(self, ctx):
        description = f"How are we doing guys?"
        embed = self.create_embed(description, 'how_are_we_doing')
        await ctx.reply(embed=embed)

    # gm command
    @commands.command()
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def gm(self, ctx, member: discord.Member):
        description = f"{ctx.author.mention} says Goooooooooooooooood moooooooooooooooorning!!!!!!! {member.mention}"
        embed = self.create_embed(description, 'good_morning')
        await ctx.reply(embed=embed)

async def setup(bot):
    await bot.add_cog(embed_commands(bot))

# old
# import discord, random
# from discord.ext import commands
# from discord.embeds import Embed
# from discord import colour

# class embed_commands(commands.Cog):

#     def __init__(self, bot):
#         self.bot = bot

#     # helpme command with good luck gif

#     @commands.command()
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def helpme(self, ctx):
#         good_luck = ['https://c.tenor.com/nKE3fkQlJOMAAAAM/good-luck-fighting.gif', 'https://c.tenor.com/tTSmnRmlWjUAAAAC/good-luck-anime.gif',
#     'https://c.tenor.com/OKoyV34l5JQAAAAC/good-luck-sign-of-the-cross.gif', 'https://c.tenor.com/MZ6C4OO8HvcAAAAC/pikachu-good-luck.gif',
#     'https://acegif.com/wp-content/gifs/good-luck-13.gif', 'https://c.tenor.com/P07pbQA_cjAAAAAC/good-luck-adventure-time.gif',
#     'https://c.tenor.com/kQLNIz-0FgkAAAAC/good-luck-taken.gif', 'https://c.tenor.com/cmqX6WK0oxQAAAAC/good-luck-captain-america.gif']
#         embed = discord.Embed(
#             colour=(discord.Colour.random()),
#             description=f" **Goooooood mooooooorning {ctx.author.name}!!!** The commands are as follows: \n"
#             "- **!quote/!q** to read my wonderful quotes, \n"
#             "- **!shahrukh** to read my catchphrase, \n"
#             "- **!biryani** for an image of our favourite dish, \n"
#             "- **!advice** if you are feeling lost and need advice, \n"
#             "- **!fc/!fortunecookie** to read your fortune and lucky numbers for today! \n"
#             "- **!inspire** to feel inspired! \n"
#             "- **!colour** for a random colour! \n"
#             "- **!daily** for your daily stats! \n"
#             "- **!tt/!tradingtips** for some sound financial advice! \n"
#             "- **!yesno** with a question afterwards for my expert and final opinion! \n"
#             "- **!gm** and **@someone** to give them a special goooooooood moooooooooorning!!!!! \n "
#             "- **!gl** and **@someone** to wish them good luck!\n"
#             "- **!how** to say How are we doing guys?\n"
#             "- **!br** to say brilliant!\n"
#             "- **!trans/!translate** [language to translate to] [text] to translate!\n"
#             "- **!todo/!do** for my advice on what to do today! \n"
#             " Also team, there's a **cooldown** on my commands! **Good luck!!!!**"
#         )
#         embed.set_image(url=(random.choice(good_luck)))
#         await ctx.reply(embed = embed)
#     #
#     #  command saying good luck
#     @commands.command()
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def gl(self, ctx, member:discord.Member):
#         good_luck = ['https://c.tenor.com/nKE3fkQlJOMAAAAM/good-luck-fighting.gif', 'https://c.tenor.com/tTSmnRmlWjUAAAAC/good-luck-anime.gif',
#     'https://c.tenor.com/OKoyV34l5JQAAAAC/good-luck-sign-of-the-cross.gif', 'https://c.tenor.com/MZ6C4OO8HvcAAAAC/pikachu-good-luck.gif',
#     'https://acegif.com/wp-content/gifs/good-luck-13.gif', 'https://c.tenor.com/P07pbQA_cjAAAAAC/good-luck-adventure-time.gif',
#     'https://c.tenor.com/kQLNIz-0FgkAAAAC/good-luck-taken.gif', 'https://c.tenor.com/cmqX6WK0oxQAAAAC/good-luck-captain-america.gif']
#         description = f"Good luck! {member.mention}"
#         embed = discord.Embed(
#         colour=(discord.Colour.random()),
#         description=description

#     )
#         embed.set_image(url=(random.choice(good_luck)))
#         await ctx.reply(embed=embed)
#     # await ctx.send(member.mention)

#     @commands.command()
#     @commands.cooldown(1, 15, commands.BucketType.user)
#     async def hello(self, ctx):
#             await ctx.reply('Hello!')



#     @commands.command(pass_context = True , aliases=['shah', 'shahr', 'shahru', 'shahruk'])
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def shahrukh(self, ctx):
#         good_morning_gifs = ['https://media2.giphy.com/media/WaYIFw9ZiEn1fPcH8Y/giphy.gif?', 'https://i.pinimg.com/originals/0f/41/8a/0f418a807d4d1e40fb8428b04b86e72f.gif',
#     'https://i.pinimg.com/originals/e5/8e/30/e58e300d3a2f068314db9c567a8b2772.gif', 'https://i.pinimg.com/originals/b9/36/b3/b936b3188601b9376c72ed358dac45d8.gif',
#     'https://www.gifcen.com/wp-content/uploads/2022/02/funny-good-morning-gif-3.gif', 'https://c.tenor.com/kAaTGOhxGLYAAAAC/inosuke-demon.gif',
#     'https://c.tenor.com/kDAyvJIaw7EAAAAd/poppyseedies.gif', 'https://c.tenor.com/CFuuZZSyQUkAAAAC/good-morning-wake-up.gif',
#     'https://c.tenor.com/OH5Vd-yZHrUAAAAC/good-morning-skeleton-meme.gif', 'https://c.tenor.com/TZuZJYTomgwAAAAC/good-morning-morning.gif',
#     'https://c.tenor.com/_rp_yHj7Nn4AAAAd/good-morning.gif', 'https://c.tenor.com/yK-webGfL84AAAAC/good-morning-wishes.gif', 'https://media1.giphy.com/media/ujh2qQvMVlZflF1mPQ/giphy.gif?']

#         embed = discord.Embed(
#         colour=(discord.Colour.random()),
#         description=f"Goooooooood mooooooooooorninggg!!! {ctx.author.mention}"
#     )
#         embed.set_image(url=(random.choice(good_morning_gifs)))
#         await ctx.reply(embed=embed)

#     # command tagging someone and saying brilliant!!

#     @commands.command()
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def br(self, ctx):
#         brilliant_gifs = ['https://media.giphy.com/media/26BRBKqUiq586bRVm/giphy.gif', 'https://media.giphy.com/media/3otPoFIPdGqzjUWpeE/giphy.gif',
#     'https://media.giphy.com/media/TjGFDxbbZRYjv9vpCL/giphy.gif', 'https://media.giphy.com/media/8jn9eiO3HjT0pU3zqe/giphy.gif',
#     'https://media.giphy.com/media/SXgIu2UVUj4UwbyaGz/giphy.gif', 'https://media.giphy.com/media/W1wC5ye0qPoTQ6Gzhd/giphy.gif']
#         description = f"Brilliant!"
#         embed = discord.Embed(
#             colour=(discord.Colour.random()),
#             description=description

#     )
#         embed.set_image(url=(random.choice(brilliant_gifs)))
#         await ctx.reply(embed=embed)

#     # command tagging someone and saying how are we doing guys?

#     @commands.command()
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def how(self, ctx):
#         how_are_we_doing_guys_gifs = ['https://media1.giphy.com/media/3ohA2FAHazPGAEsgYo/giphy.gif?', 'https://media.giphy.com/media/XUyYa4TRSX66Y2dCzr/giphy.gif',
#     'https://media.giphy.com/media/l2YWhoXYKGiN7IVDW/giphy.gif', 'https://media.giphy.com/media/l2Je1kFLMlL9AJStG/giphy.gif',
#     'https://media.giphy.com/media/TFhtlAv944YWTJhk5u/giphy.gif', 'https://media.giphy.com/media/BCYyBrWW4520w/giphy.gif']
#         description = f"How are we doing guys?"
#         embed = discord.Embed(
#         colour=(discord.Colour.random()),
#         description=description

#     )
#         embed.set_image(url=(random.choice(how_are_we_doing_guys_gifs)))
#         await ctx.reply(embed=embed)

#     # command tagging someone and saying gooooooooooood moooooooooooorningggg

#     @commands.command()
#     @commands.cooldown(1, 10, commands.BucketType.user)
#     async def gm(self, ctx, member:discord.Member):
#         good_morning_gifs = ['https://media2.giphy.com/media/WaYIFw9ZiEn1fPcH8Y/giphy.gif?', 'https://i.pinimg.com/originals/0f/41/8a/0f418a807d4d1e40fb8428b04b86e72f.gif',
#     'https://i.pinimg.com/originals/e5/8e/30/e58e300d3a2f068314db9c567a8b2772.gif', 'https://i.pinimg.com/originals/b9/36/b3/b936b3188601b9376c72ed358dac45d8.gif',
#     'https://www.gifcen.com/wp-content/uploads/2022/02/funny-good-morning-gif-3.gif', 'https://c.tenor.com/kAaTGOhxGLYAAAAC/inosuke-demon.gif',
#     'https://c.tenor.com/kDAyvJIaw7EAAAAd/poppyseedies.gif', 'https://c.tenor.com/CFuuZZSyQUkAAAAC/good-morning-wake-up.gif',
#     'https://c.tenor.com/OH5Vd-yZHrUAAAAC/good-morning-skeleton-meme.gif', 'https://c.tenor.com/TZuZJYTomgwAAAAC/good-morning-morning.gif',
#     'https://c.tenor.com/_rp_yHj7Nn4AAAAd/good-morning.gif', 'https://c.tenor.com/yK-webGfL84AAAAC/good-morning-wishes.gif', 'https://media1.giphy.com/media/ujh2qQvMVlZflF1mPQ/giphy.gif?']

#         description = f"{ctx.author.mention} says Goooooooooooooooood moooooooooooooooorning!!!!!!! {member.mention}"
#         embed = discord.Embed(
#         colour=(discord.Colour.random()),
#         description=description

#     )
#         embed.set_image(url=(random.choice(good_morning_gifs)))
#         await ctx.reply(embed=embed)

# async def setup(bot):
#     await bot.add_cog(embed_commands(bot))
