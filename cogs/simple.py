from discord.ext import commands


class SimpleCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.command(name='repeat', aliases=['copy', 'mimic'])
    async def do_repeat(self, ctx, *, our_input: str):
        """Repeat it again tony"""
        await ctx.send(our_input)

    @commands.command(name='add', aliases=['plus'])
    @commands.guild_only()
    async def do_addition(self, ctx, first: int, second: int):
        """I cannot do math"""
        total = first + second
        await ctx.send(f'The sum of **{first}** and **{second}**  is  **{total}**')


def setup(bot):
    bot.add_cog(SimpleCog(bot))
