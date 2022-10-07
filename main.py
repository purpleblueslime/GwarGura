import interactions
import os 

bot = interactions.Client(token=os.getenv('token'))

@bot.command(
  name='a',
  description='a',
)
async def a(ctx: interactions.CommandContext):
  await ctx.send('<a:SharkA:983957663912194088>')

bot.start()