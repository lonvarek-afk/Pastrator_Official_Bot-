import os
import telebot
from dotenv import load_dotenv
from keyboards import main_keyboard, language_keyboard
from ai_engine import generate_ai_response

load_dotenv()
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    first_name = message.from_user.first_name or "there"
    welcome_text = (
        f"Haye {first_name}!\n\n"
        "Waxan ahay Pastrator. Kaaliyahaaga AI ee gudaha Telegram. "
        "Waxaad i weydiin kartaa su'aalo, qori kartaa code, tarjumi kartaa qoraallo, "
        "baran kartaa waxyaabo cusub, ama sameyn kartaa fikrado.\n\n"
        "Kaliya ii soo dir fariin ama dooro khaanadaha hoose."
    )
    bot.send_message(message.chat.id, welcome_text, reply_markup=main_keyboard())

@bot.message_handler(func=lambda message: True)
def handle_all_messages(message):
    text = message.text
    first_name = message.from_user.first_name or "User"
    
    if text == "Ask Anything":
        bot.reply_to(message, "I weydii wax kasta.")
    elif text == "Choose Language":
        bot.send_message(message.chat.id, "Please choose your preferred language:", reply_markup=language_keyboard())
    elif text == "History":
        bot.reply_to(message, "Taariikhda wadahadalka waa nadiif.")
    elif text == "Introduction":
        send_welcome(message)
    else:
        # Soo tus 'typing...' action inta AI-gu jawaabta soo diyaarinayo
        bot.send_chat_action(message.chat.id, 'typing')
        
        response = generate_ai_response(text, user_name=first_name)
        bot.reply_to(message, response)

if __name__ == "__main__":
    bot.infinity_polling()
