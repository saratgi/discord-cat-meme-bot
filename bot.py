import os
from dotenv import load_dotenv
import discord
import requests
import json

# Load environment variables from the .env file
load_dotenv()

# Get the discord bot token 
TOKEN = os.getenv("DISCORD_TOKEN")

# Get a random meme image URL from meme-api.com
def get_meme():
    # Request meme data from the API
    response = requests.get("https://meme-api.com/gimme/catmemes")
    # Convert the JSON response text into a Python dictionary
    json_data = json.loads(response.text)
    # Return only the image URL from the API data
    return json_data["url"]

# Create a custom Discord client
class MyClient(discord.Client):
    # Runs when the bot successfully logs in
    async def on_ready(self):
        print(f"Logged on as {self.user}!")

# Runs whenever a new message is sent
    async def on_message(self, message):
        # Ignore messages sent by the bot itself
        if message.author == self.user:
            return
        
        # Respond with a meme when a user types $meme
        if message.content.startswith("$meme"):
            await message.channel.send(get_meme())
        
        # Respond with a greeting when a user types $hello
        elif message.content.startswith("$hello"):
            await message.channel.send("Hello!")

# Enable message content access so the bot can read commands
intents = discord.Intents.default()
intents.message_content = True

# Create and start the bot
client = MyClient(intents=intents)
client.run(TOKEN)


