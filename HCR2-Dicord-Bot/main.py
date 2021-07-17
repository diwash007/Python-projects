import discord
import os
from discord.ext import commands
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()
env_path = Path(".") / ".env"
load_dotenv(dotenv_path=env_path)

client = commands.Bot(command_prefix="*",help_command=None)

@client.command()
async def load(ctx, extension):
	client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')

@client.command()
async def reload(ctx, extension):
	client.unload_extension(f'cogs.{extension}')
	client.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
	if filename.endswith('.py'):
		client.load_extension(f'cogs.{filename[:-3]}')

BOT_TOKEN = os.getenv("TOKEN")
client.run(BOT_TOKEN)