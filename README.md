# HackerNewsDiscordFeed

HackerNewsDiscordFeed is a Discord bot that sends daily messages with the latest best stories from Hacker News.

## Features

- Fetches the top stories from Hacker News daily
- Sends a message to a specified Discord channel with the story titles, scores, and URLs

## Requirements

- Python 3.10 or higher
- A Discord account

## Setup Instructions

### 1. Create a Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications).
2. Click on "New Application" and give your application a name.
3. Go to the "Bot" section in the left sidebar and click "Add Bot". Confirm the action.
4. Under the "TOKEN" section, click "Copy" to copy your bot token. You'll need this token later.
5. In the "OAuth2" section, go to the "URL Generator".
   - Select the `bot` scope.
   - Under "Bot Permissions", select `Send Messages` and any other permissions your bot needs.
   - Copy the generated URL and open it in a new tab to invite your bot to your server.

### 2. Clone the Repository

```sh
git clone https://github.com/yourusername/HackerNewsDiscordFeed.git
cd HackerNewsDiscordFeed
```

### 3. Set Up Environment Variables

Create a .env file in the root directory of your project and add your sensitive credentials:

`.env file`

```sh
DISCORD_BOT_TOKEN=your_discord_bot_token_here
CHANNEL_ID=your_channel_id_here
```

### 4. Install Dependencies

This project uses Poetry for dependency management. If you don't have Poetry installed, you can install it by following the official guide.

Install the dependencies:

```sh
poetry install
```

### 5. Run the Bot

To run the bot, use the following command:

```sh
poetry run python -m hackernewsdiscordfeed.bot
```

## Running Tests

This project uses pytest for testing. To run the tests, use the following command:

```sh
poetry run pytest
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
