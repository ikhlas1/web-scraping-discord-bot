import discord
import os
# import search_runpee # search class we will impelement later

from dotenv import load_dotenv
load_dotenv()


# instantiate discord client

client = discord.Client(discord.Intents.all())


# discord event to check when the bot is online


@client.event
async def on_ready():
    print(f'{client.user} is now online!')


@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi khai {member.name}, welcome to my Discord server!'
    )


@client.event
async def on_message(message):
    # make sure bot doesn't respond to it's own messages to avoid infinite loop
    if message.author == client.user:
        return
    # lower case message
    message_content = message.content.lower()

    if message.content.startswith(f'$khai'):
        await message.channel.send('''Hello there khai! I\'m the Mehdi's bot from El. 
    Sorry but I really need to go to the bathroom khai... Please read the retards manual by typing $helpkhai or $commandskhai while I'm away bitch.''')


# get bot token from .env and run client
# has to be at the end of the file
client.run(os.getenv('TOKEN'))
