import discord
import random
from discord.ext import commands,tasks

class Utils(commands.Cog):
	def __init__(self, client):
		self.client = client

	@commands.command()
	async def server(self, ctx):
	    server = ctx.message.guild

	    roles = str(len(server.roles))
	    emojis = str(len(server.emojis))
	    channels = str(len(server.channels))

	    embeded = discord.Embed(title=server.name, description='Server Info', color=0xEE8700)
	    embeded.set_thumbnail(url=server.icon_url)
	    embeded.add_field(name="Created on:", value=server.created_at.strftime('%d %B %Y at %H:%M UTC+3'), inline=False)
	    embeded.add_field(name="Server ID:", value=server.id, inline=False)
	    embeded.add_field(name="Users on server:", value=server.member_count, inline=True)
	    embeded.add_field(name="Server owner:", value=server.owner, inline=True)

	    embeded.add_field(name="Server Region:", value=server.region, inline=True)
	    embeded.add_field(name="Verification Level:", value=server.verification_level, inline=True)
	    embeded.add_field(name="Role Count:", value=roles, inline=True)
	    embeded.add_field(name="Emoji Count:", value=emojis, inline=True)
	    embeded.add_field(name="Channel Count:", value=channels, inline=True)

	    await ctx.send(embed=embeded)

	@commands.command()
	async def ping(self, ctx):
		embed = discord.Embed(title=f"Ping: {round(self.client.latency * 1000)}ms", color=0xFF5733)
		await ctx.send(embed=embed)

def setup(client):
	client.add_cog(Utils(client))