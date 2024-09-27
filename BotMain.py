from discord.ext import commands
import discord

INTENTS = discord.Intents.default().all()
BOT = commands.Bot(command_prefix="히봇 ", intents=INTENTS)

@BOT.command()
async def checkAdmin(ctx:commands.context.Context):
    user = ctx.author
    if not await user.guild_permissions.administrator:
        await ctx.send(f"{user.display_name}님은 관리자가 아닙니다.")
        return False
    return True

@BOT.command()
async def kick(ctx:commands.context.Context, name, info):
    guild = ctx.guild
    if not await checkAdmin(ctx):
        return
    
BOT.run("Token")