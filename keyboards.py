from telebot.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

def main_keyboard():
    markup = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn1 = KeyboardButton("Ask Anything")
    btn2 = KeyboardButton("Choose Language")
    btn3 = KeyboardButton("History")
    btn4 = KeyboardButton("Introduction")
    
    # 2 Midig jira iyo 2 Bidix jira (Grid 2x2)
    markup.add(btn1, btn2)
    markup.add(btn3, btn4)
    return markup

def language_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    btn_so = InlineKeyboardButton("Somali", callback_data="lang_so")
    btn_en = InlineKeyboardButton("English", callback_data="lang_en")
    btn_ar = InlineKeyboardButton("Arabic", callback_data="lang_ar")
    markup.add(btn_so, btn_en, btn_ar)
    return markup
