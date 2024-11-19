import os
from openai import OpenAI
import logging
from telegram import Update
from telegram.ext import Application, MessageHandler, filters, ContextTypes

logging.basicConfig(level=logging.ERROR)

# Set your API keys
BOT_TOKEN = os.getenv("BOT_TOKEN")
client = OpenAI(
   api_key=os.getenv("GILAS_API_KEY"), 
   base_url="https://api.gilas.io/v1/" # https://gilas.io
)

# Function to send text to the Gilas Moderation API
def moderate_comment(comment_text):
    try:
        response = client.moderations.create(input=comment_text,model="omni-moderation-latest")
        return response.results[0].flagged
    except Exception as e:
        logging.error(f"Error moderating comment: {e}")
        return False

# Handler for comments in the channel
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message:
        comment_text = update.message.text
        user_id = update.message.from_user.id
        message_id = update.message.message_id
        chat_id = update.message.chat_id
        # Check if the comment is flagged by Gilas Moderation API
        flagged = moderate_comment(comment_text)
        if flagged:
            try:
                await context.bot.delete_message(chat_id=chat_id, message_id=message_id)
                logging.info(f"Deleted flagged comment from user {user_id}: {comment_text}")
            except Exception as e:
                logging.error(f"Error deleting message: {e}")

def main():
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(MessageHandler(filters.ALL, handle_message))
    print("Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
