from keyboards import get_language_inline_keyboard
from database import set_user_language

def register_language_handlers(bot):
    @bot.message_handler(func=lambda msg: msg.text == "🌐 Choose Language")
    def ask_language(message):
        bot.send_message(
            message.chat.id,
            "Fadlan dooro luuqada aad doorbidayso / Please choose your preferred language:",
            reply_markup=get_language_inline_keyboard()
        )

    @bot.callback_query_handler(func=lambda call: call.data.startswith("lang_"))
    def set_language_callback(call):
        user_id = call.from_user.id
        lang_code = call.data.split("_")[1]
        
        set_user_language(user_id, lang_code)
        
        messages = {
            "so": "Afka waxaa loo beddelay Soomaali 🇸🇴",
            "en": "Language set to English 🇬🇧",
            "ar": "تم تغيير اللغة إلى العربية 🇸🇦"
        }
        
        reply_msg = messages.get(lang_code, "Language updated!")
        bot.answer_callback_query(call.id, reply_msg)
        bot.send_message(call.message.chat.id, reply_msg)
