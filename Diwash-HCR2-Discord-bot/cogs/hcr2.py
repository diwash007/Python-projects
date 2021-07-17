import discord
import random
import os
from discord.ext import commands,tasks
from itertools import cycle
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

PASS = os.getenv("PASS")
USER = os.getenv("USER")
DB = os.getenv("DB")

class Hcr2(commands.Cog):

	def __init__(self, client):
		self.client = client
		self.con = psycopg2.connect(database=DB, user=USER, password=PASS)
		self.maps = ["Countryside", "Forest", "City", "Mountain", "Rustbucket Reef", "Winter", "Mines", "Desert Valley", "Beach", "Backwater bog", "Racer Glacier", "Patchwork Plant", "Gloomvale", "Sky Rock Outpost", "Forest Trials", "Intense City", "Raging Winter"]
		self.vehicles = ["Hill Climber", "Scooter", "Bus", "Hill Climber Mk. 2", "Tractor", "Motocross","Dune Buggy", "Sports Car", "Monster Truck", "Rotator", "Super Diesel", "Chopper", "Tank", "Snowmobile", "Monowheel", "Rally Car", "Formula", "Racing Truck", "Hot Rod", "Super Car", "Super Bike", "Moonlander"]

	# events
	@commands.Cog.listener()
	async def on_ready(self):
		await self.client.change_presence(activity=discord.Game("HCR2 | Type *help"))
		print("Bot is online")

	# commands
	@commands.command()
	async def help(self, ctx):
		embed = discord.Embed(title="Help", description="*<command_name> <value>", color=0xFF5733)
		embed.set_thumbnail(url="https://fingersoft.com/app/uploads/2021/04/leagues-rolling-out-fb-1-819x1024.jpg")
		await ctx.send(embed=embed)

	@commands.command()
	async def start(self, ctx, day=1):
		map = random.choice(self.maps)
		vehicle = random.choice(self.vehicles)
		id = ctx.message.guild.id
		with self.con:
			with self.con.cursor() as cur:
				cur.execute("INSERT into servers (server_id, map, vehicle) VALUES (%s,%s,%s)",(id, map, vehicle))
				self.con.commit()
		embed=discord.Embed(title=f"{day} day adventure tournament started.", description=f"The challenge for next {int(day)*24} hours is {vehicle} in {map}", color=0xFF5733)
		await ctx.send(embed=embed)
		await ctx.send(id)


	@commands.command()
	async def end(self, ctx):
		with self.con:
			with self.con.cursor() as cur:
				cur.execute("TRUNCATE TABLE servers")
				self.con.commit()
	# @start.error
	# async def on_command_error(self, ctx, error):
	# 	await ctx.send("Tornament is already running!")
		

def setup(client):
	client.add_cog(Hcr2(client))