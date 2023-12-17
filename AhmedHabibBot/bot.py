import discord

import responses

import TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged on as {client.user}")
        
@client.event
async def on_message(message):
    
    user_msg = message.content
    
    print(f"Message from {message.author}: {user_msg}")
        
    if message.author == client.user:
        return
    
    response = responses.handle_response(user_msg)
    if len(response) != 0:
        await message.channel.send(response)
        
client.run(TOKEN.TOKEN)