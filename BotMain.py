from discord.ext import commands
import discord, datetime, pytz

INTENTS = discord.Intents.default().all()
BOT = commands.Bot(command_prefix="히봇.", intents=INTENTS)

@BOT.command()
async def checkAdmin(ctx:commands.context.Context):
    user = ctx.author
    if not user.guild_permissions.administrator:
        await ctx.send(f"{user.display_name}님은 관리자가 아닙니다.")
        return False
    return True

@BOT.command(aliases=["강퇴"])
async def kick(ctx:commands.context.Context, name, *args):
    guild = ctx.guild
    info = ""
    for str in args:
        info += f"{str} "

    user = guild.get_member_named(name)
    if not await checkAdmin(ctx) or user is None:
        return
    await guild.kick(user=user)

    em = discord.Embed(title=f"{name}님이 추방당했습니다!", description=None, timestamp=datetime.datetime.now(pytz.timezone(zone="UTC")))
    em.add_field(name=None, value=f"추방 사유: {None if info is None else info}", inline=False)
    em.set_footer(text=f"{ctx.author.display_name}", icon_url=ctx.author.display_avatar.url)
    await ctx.send(embed=em)

@BOT.command(aliases=["안녕"])
async def hello(ctx:commands.context.Context):
    await ctx.send(f"{ctx.author.mention}님 안녕하세요!")
    
BOT.run("Token")