import discord
from discord.ext import commands

class kick_ban_unban(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_loaded(self, ctx):
        ctx.send('Kick ban and unban loaded :)')
        print('cog loaded')

    @commands.command()
    async def ban(self, ctx, member : discord.member, *, reason=None):
        await member.ban(reason=reason)
        await ctx.send(f'banned \n{member.mention}')

    @commands.command()
    async def kick(self, ctx, member : discord.member, *, reason=None):
        await member.kik(reason=reason)
        await ctx.send(f'kicked \n{member.mention}')

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')

        for ban_entry in banned_users:
            user = ban_entry.user

            if (user.name, user.descriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send(f'unbanned {user.mention}')
                return

def setup(client):
    client.add_cog(kick_ban_unban(client))
