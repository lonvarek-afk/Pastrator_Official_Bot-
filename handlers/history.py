from database import get_user_history

def register_history_handlers(bot):
    @bot.message_handler(func=lambda msg: msg.text == "📜 History")
    def show_history(message):
        user_id = message.from_user.id
        history = get_user_history(user_id)
        
        if not history:
            bot.send_message(
                message.chat.id,
                "Wax conversation history ah weli ma lihid. 🤖\n\nIska qor fariin ama su'aal si aan wada sheekaysano!"
            )
            return
        
        formatted_history = "📜 *Conversation History (Recent Messages):*\n\n"
        for msg in history:
            role = "👤 You" if msg.get("role") == "user" else "🤖 Pastrator"
            parts = "".join(msg.get("parts", []))
            # Soo koob fariinta dhererkeeda si aysan u noqon wall of text
            short_parts = (parts[:120] + '...') if len(parts) > 120 else parts
            formatted_history += f"*{role}:*\n{short_parts}\n\n"
            
        bot.send_message(
            message.chat.id,
            formatted_history,
            parse_mode="Markdown"
        )
