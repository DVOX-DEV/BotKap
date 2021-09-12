import discord
from discord.ext import commands

client = commands.Bot(command_prefix='K!')

token = 'ODg2MzAzNDI5NzQyNDQwNDU4.YTzoZA.21SkVZvEFYzv8Tx61JagZZjNBjM'

cmds = 'K!cmds \nK!ping, \nK!clear("*insert amount*"), \nK!purge(clear all), \nK!ban, \nK!unban, \nK!kick'

@client.event
async def on_ready():
    print('ready')

@client.command()
async def cmds(ctx):
    await ctx.send(cmds)

@client.command()
async def ping(ctx):
    await ctx.send(f'{round(client.latency) * 1000}ms')

@client.command()
@commands.has_permissions(administrator=True)
async def clear(ctx, amount=6):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'cleard {amount} messages')
    await ctx.channel.purge(limit=2)
    return

@client.command()
@commands.has_permissions(administrator=True)
async def purge(ctx):
    await ctx.channel.purge()
    await ctx.send('Removed all messages')
    await ctx.channel.purge(limit=2)
    return

@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'banned {member.mention}')

@client.command()
@commands.has_permissions(administrator=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'kicked {member.mention}')

@client.command()
@commands.has_permissions(administrator=True)
async def unban(self, ctx, *, Member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.descriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned')
                return

client.run(token)
