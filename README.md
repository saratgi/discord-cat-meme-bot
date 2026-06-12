# Discord Cat Meme Bot

A simple Discord bot that sends a random cat meme when a user types a command.

## Preview

<img src="assets/preview.gif" alt="Discord Cat Meme Bot preview" width="500">

## Features

- Sends a greeting when the user types `$hello`
- Fetches random cat memes when the user types `$meme`
- Uses a `.env` file to keep the Discord bot token private
- Ignores its own messages to avoid self-replies

## Built With

- Python
- discord.py
- requests
- python-dotenv

## What I Learned

- How to create a basic Discord bot with Python
- How to use environment variables to keep tokens private
- How to use a `.env` file with `python-dotenv`
- How to use `.gitignore` to avoid uploading sensitive files
- How to document project dependencies with `requirements.txt´
- How to fetch data from a public API using `requests`
- How to read JSON response data and use specific values from it
- How to make a bot respond to simple text commands 

## How to Run

Install the required packages:

```bash
pip install -r requirements.txt
```

Create a `.env` file in the project folder and add your Discord bot token:

```env
DISCORD_TOKEN=your_discord_bot_token_here
```
You can use .env.example as a template for this file.

Run the bot:

```bash
python bot.py
```

## Commands

| Command  | Description             |
|----------|-------------------------|
| `$hello` | Sends a greeting message |
| `$meme`  | Sends a random cat meme  |

## Notes

The real `.env` file is ignored with `.gitignore`so the bot token is not uploaded to GitHub.


