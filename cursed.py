from discord.ext import commands
import discord
import traceback


def get_prefix(bot, message):

    prefixes = ['<']

    if not message.guild:
        return ''

    return commands.when_mentioned_or(*prefixes)(bot, message)


cogs = ['cogs.owner', 'cogs.cursed']

bot = commands.Bot(command_prefix=get_prefix, case_insensitive=True, description='I AM cursedbot. FEAR ME!')

if __name__ == '__main__':
    for cog in cogs:
        bot.load_extension(cog)


@bot.event
async def on_ready():
    print(f'Logged in as: {bot.user.name} - {bot.user.id}\nVersion: {discord.__version__}\n')

    await bot.change_presence(activity=discord.Streaming(name="cursed images", url="https://www.twitch.tv/c"))


# @bot.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         print('no found')
#     else:
#         print(error)
with open('token.txt') as f:
    token = f.readline()

bot.run(token, bot=True, reconnect=True)
