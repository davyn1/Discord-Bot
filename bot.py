# install necessary packages when run in an environment
from pip._internal import main as pipmain

pipmain(['install', 'hikari'])
pipmain(['install', 'hikari-lightbulb'])

# import necessary packages
import hikari
import lightbulb


# instantiate a bot and run it
bot = lightbulb.BotApp(token='MTAwNzgxNTY4MjM1Mzc5OTIzOQ.G8yYAw.9GXvICOVSVedw9QcSy-v4q_8svjEOx7Hewnj9I',
                       default_enabled_guilds=1007816405246279740
                       )


@bot.listen(hikari.StartedEvent)
async def on_started(event):
    print('Bot has started!')


@bot.command
@lightbulb.command('group', 'This is a group')
@lightbulb.implements(lightbulb.SlashCommandGroup)
async def group(ctx):
    pass

@group.child
@lightbulb.command('subcommand', 'This is a subcommand')
@lightbulb.implements(lightbulb.SlashSubCommand)
async def subcommand(ctx):
    await ctx.respond('I am a subcommand!')

@bot.command
@lightbulb.option('num1', 'The first number', type=int) #type is optional, default is str
@lightbulb.option('num2', 'The second number', type=int)
@lightbulb.command('add', 'Add two numbers together')
@lightbulb.implements(lightbulb.SlashCommand)
async def add(ctx):
    await ctx.respond(ctx.options.num1 + ctx.options.num2)


bot.load_extensions_from('./extensions')
bot.run()
