import discord
import responses
import tictactoe
from TOKEN import TOKEN

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready()-> None:
    print(f"Logged on as {client.user}")
        
@client.event
async def on_message(message: discord.Message)-> None:

    user_msg: str = message.content
    
    print(f"Message from {message.author}: {user_msg}")
        
    if message.author == client.user:
        return
    if user_msg.startswith("!"):
        if user_msg == "!tictactoe":
            await tictactoe.startGame(message.author, client, message.channel)
    else:
        response = responses.handle_response(user_msg)
        if len(response) != 0:
            await message.channel.send(response)
            
def run_discord_bot():
    client.run(TOKEN)