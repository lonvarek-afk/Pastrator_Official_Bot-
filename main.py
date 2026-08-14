import telebot
from config import TELEGRAM_BOT_TOKEN
from database import init_db
from handlers.start import register_start_handlers
from handlers.language import register_language_handlers
from handlers.history import register_history_handlers
from handlers.chat import register_chat_handlers

# Bilow Database-ka
init_db()

# Initialize Telegram Bot
bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)

# Dhaqan-gelinta Handlers-ka
register_start_handlers(bot)
register_language_handlers(bot)
register_history_handlers(bot)
register_chat_handlers(bot)

if __name__ == "__main__":
    print("🤖 Pastrator Bot wuu shaqaynayaa...")
    bot.infinity_polling(skip_pending=True)
