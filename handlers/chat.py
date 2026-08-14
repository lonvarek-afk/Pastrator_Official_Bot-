from database import get_user_language
from ai_engine import generate_ai_response

def register_chat_handlers(bot):
    @bot.message_handler(func=lambda msg: msg.text == "🤖 Ask Anything")
    def ask_anything_button(message):
        user_id = message.from_user.id
        lang = get_user_language(user_id)
        
        prompt_msgs = {
            "so": "I weydii wax kasta. 🤖",
            "en": "Sure — ask me anything. 🤖",
            "ar": "بالتأكيد — اسألني أي شيء. 🤖"
        }
        
        msg_text = prompt_msgs.get(lang, "Sure — ask me anything. 🤖")
        bot.send_message(message.chat.id, msg_text)

    @bot.message_handler(func=lambda msg: True, content_types=['text'])
    def handle_natural_chat(message):
        # Haddii uu yahay button-yada kale, iska dhaaf halkan ha ku shaqayn
        if message.text in ["📜 History", "🌐 Choose Language", "ℹ️ Introduction"]:
            return
            
        user_id = message.from_user.id
        user_prompt = message.text
        
        # Ogeysii user-ka in bot-ku uu fekerayo
        bot.send_chat_action(message.chat.id, 'typing')
        
        # AI Response
        ai_reply = generate_ai_response(user_id, user_prompt)
        
        try:
            bot.send_message(
                message.chat.id,
                ai_reply,
                parse_mode="Markdown"
            )
        except Exception:
            # Haddii Markdown-ka uu la yimaado formatting error, u dir plain text
            bot.send_message(
                message.chat.id,
                ai_reply
            )
