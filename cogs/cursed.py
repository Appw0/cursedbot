from discord.ext import commands
import typing
import traceback


class CursedCog(commands.Cog, name='Cursed Commands'):
    """The commands for begining the battle of cursed media"""

    cursed_channels = {}

    def __init__(self, bot):
        self.bot = bot

    def is_cursed_channel():
        def predicate(ctx):
            return ctx.message.channel in CursedCog.cursed_channels
        return commands.check(predicate)

    @commands.command(name='begin', aliases=['start'])
    @commands.guild_only()
    async def begin_cursed1(self, ctx, rounds: typing.Optional[int] = 1):
        """Begin the battle of cursed media"""
        await ctx.send('<:ey:738522865049272451>\nLET US BEGIN!\nPOST YOUR MOST CURSED!')
        CursedCog.cursed_channels[ctx.message.channel] = {'rounds': rounds, 'messages': []}

    @begin_cursed1.error
    async def begin_cursed1_error(self, ctx, error):
        # print('ERRRRR')
        #
        if isinstance(error, commands.BadArgument):
            await ctx.send('CURSED FAILURE. NUMBERS ONLY!')
        else:
            print(repr(error))

    @commands.command(name='end', aliases=['count', 'tally', 'finish', 'score'])
    @commands.guild_only()
    @is_cursed_channel()
    async def count_and_finish_cursed1(self, ctx):
        """Finish the round, and tally the scores"""
        # await ctx.send('NOTHING HAPPENS!')
        members = {}

        for message in CursedCog.cursed_channels[ctx.message.channel]['messages']:
            if message != ctx.message:
                message_score = 0
                message_react_count = 0
                reacted = []

                if message.author not in members:
                    members[message.author] = {'score': 0, 'score2': 0, 'count': 0}

                if members[message.author]['count'] < CursedCog.cursed_channels[ctx.message.channel]['rounds']:
                    for reaction in message.reactions:
                        try:
                            number = {'0️⃣': 0, '1️⃣': 1, '2️⃣': 2, '3️⃣': 3, '4️⃣': 4, '5️⃣': 5, '6️⃣': 6, '7️⃣': 7, '8️⃣': 8, '9️⃣': 9, '🔟': 10}[reaction.emoji]
                        except KeyError as e:
                            e.args
                        else:
                            react_users = await reaction.users().flatten()
                            for user in react_users:
                                if user not in reacted and user != message.author:
                                    # print('reeee')
                                    reacted.append(user)
                                    message_score += number
                                    message_react_count += 1

                    message_score_avg = message_score / message_react_count

                    members[message.author]['score'] += message_score_avg
                    members[message.author]['score2'] += message_score
                    members[message.author]['count'] += 1

        long_boi = []
        # print(members)
        long_boi.append('{:<15} | {:<6}| {}'.format('Name', 'Score', 'Alt Score'))
        for member, val in members.items():
            long_boi.append('{:<15} | {:<5} | {}'.format(str(member.display_name), val['score'], val['score2']))
        long_boi = '\n'.join(long_boi)
        await ctx.send('BEHOLD!\n\n```\n\n{}```'.format(long_boi))

    @count_and_finish_cursed1.error
    async def count_and_finish_cursed1_error(self, ctx, error):
        print(repr(error))
        traceback.print_exc()

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.channel in CursedCog.cursed_channels:
            CursedCog.cursed_channels[message.channel]['messages'].append(message)


def setup(bot):
    bot.add_cog(CursedCog(bot))
