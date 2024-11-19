# Telegram Channel Bot

This is a Telegram bot that uses the Gilas Moderation API to moderate comments in a Telegram channel. It automatically deletes comments that are flagged by the moderation API.

## Prerequisites

- Python 3.7 or higher
- A Telegram bot token
- A Gilas API key (https://gilas.io/)

## Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/m-ariany/telegram-channel-bot.git
   cd telegram-channel-bot

   pip install -r requirements.txt
   ```

2. **Set up environment variables:**

   You need to set up the following environment variables:

   - `BOT_TOKEN`: Your Telegram bot token.
   - `GILAS_API_KEY`: Your Gilas API key.

   You can set these in your terminal session like this:

   ```bash
   export BOT_TOKEN='your-telegram-bot-token'
   export GILAS_API_KEY='your-gilas-api-key'
   ```

   Alternatively, you can create a `.env` file in the project root and add the variables there:

   ```
   BOT_TOKEN=your-telegram-bot-token
   GILAS_API_KEY=your-gilas-api-key
   ```

3. **Run the bot:**

   Start the bot by running the following command:

   ```bash
   python main.py
   ```

   The bot will start polling for messages and will automatically delete any comments flagged by the Gilas Moderation API.

## How to set up a Telegram bot and add it as an Admin to a channel?

- Create a bot using Telegram BotFather.
- Ensure your bot has the following settings:
   - Group Privacy: Off
   - Channel Admin Rights:
      - Manage Channel
      - Delete Messages
   - Group Admin Rights:
      - Manage Chat
      - Delete Messages
- Add your bot to your channel as an admin (this can be tricky):
   - First, add your bot as a subscriber to the channel.
      - If this is not possible, add it along with some regular users (this is the trick).
   - Then promote it to admin with the required permissions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.