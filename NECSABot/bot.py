#IMPORTS
import os
import commands 

#import web_server

import discord

#RETRIEVING TOKENS

MY_TOKEN = os.environ['api-token']
SERVER = "NECSA"

class NECSABot(discord.Client):

    async def on_ready(self):
        print(self.user.name)
        print(self.user.id)
        print('---------')
        
    async def on_message(self, message):
        if message.channel.name == "bot-testing":
          if message.author == self.user:
            return

          lower_msg = message.content.lower()

          is_nsfw = warden.nsfwCheck(lower_msg)
          if is_nsfw:
              censored_message = warden.censorMessage(lower_msg)
              await message.delete()
              await message.channel.send(f"""Here's a censored version of {message.author.mention}'s message: {censored_message}""")



    async def on_member_join(self, member):
        
      #ASSIGNS COMMUNITY ROLE TO NEWCOMERS

      role = discord.utils.get(self.guilds[0].roles, name = "Community")
      await member.add_roles(role)
      print(member.name)

      #WELCOMES WITH A WELCOME CARD
      channel = self.get_channel(840618502863585370)
      customizer.welcomeCard("download1.png", "Aileron-Regular.otf", 60, member.avatar_url, member.guild.member_count, member.name)
      await channel.send(f"""Welcome to NECSA!, {member.mention}""")
      await channel.send(file=discord.File("text.png"))

#web_server.keep_alive()
      
intents = discord.Intents.default()
intents.members = True

bot = NECSABot(intents=intents)
warden = commands.warden()
customizer = commands.customizer()

bot.run(MY_TOKEN)
