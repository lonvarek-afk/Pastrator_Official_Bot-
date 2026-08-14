from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def get_main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    
    # Safka 1-aad: Ask anything
    btn_ask = KeyboardButton("🤖 Ask Anything")
    
    # Safka 2-aad: History & Choose language
    btn_history = KeyboardButton("📜 History")
    btn_lang = KeyboardButton("🌐 Choose Language")
    
    # Safka 3-aad: Introduction
    btn_intro = KeyboardButton("ℹ️ Introduction")
    
    markup.row(btn_ask)
    markup.row(btn_history, btn_lang)
    markup.row(btn_intro)
    
    return markup

def get_language_inline_keyboard():
    markup = InlineKeyboardMarkup()
    btn_en = InlineKeyboardButton("🇬🇧 English", callback_data="lang_en")
    btn_so = InlineKeyboardButton("🇸🇴 Somali", callback_data="lang_so")
    btn_ar = InlineKeyboardButton("🇸🇦 العربية", callback_data="lang_ar")
    
    markup.row(btn_en)
    markup.row(btn_so)
    markup.row(btn_ar)
    
    return markup
