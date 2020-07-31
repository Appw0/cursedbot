from discord.ext import commands


class OwnerCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    # Hidden means it won't show up on the default help.
    @commands.command(name='loadc', hidden=True)
    @commands.is_owner()
    async def load_cog(self, ctx, *, cog: str):

        try:
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='unloadc', hidden=True)
    @commands.is_owner()
    async def unload_cog(self, ctx, *, cog: str):

        try:
            self.bot.unload_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='reloadc', hidden=True)
    @commands.is_owner()
    async def reload_cog(self, ctx, *, cog: str):

        try:
            self.bot.unload_extension(cog)
            self.bot.load_extension(cog)
        except Exception as e:
            await ctx.send(f'**`ERROR:`** {type(e).__name__} - {e}')
        else:
            await ctx.send('**`SUCCESS`**')

    @commands.command(name='logoff', hidden=True)
    @commands.is_owner()
    async def logoff_bot(self, ctx):
        await ctx.send('later skaters! \N{CALL ME HAND}')
        await self.bot.logout()


def setup(bot):
    bot.add_cog(OwnerCog(bot))
