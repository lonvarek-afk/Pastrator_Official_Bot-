import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME, MAX_HISTORY_MESSAGES
from database import get_user_history, save_user_history, get_user_language

genai.configure(api_key=GEMINI_API_KEY)

def generate_ai_response(user_id: int, prompt: str) -> str:
    lang = get_user_language(user_id)
    
    # System Instruction lagu saleeyay identity-ga Pastrator
    system_instruction = (
        "You are Pastrator 🤖, a smart, friendly, and natural AI assistant inside Telegram. "
        "Provide direct, clear, and well-formatted answers (using bold, markdown, bullet points, code blocks). "
        f"Default language preferred by user is '{lang}'. If the user asks in another language or requests translation, obey their immediate request."
    )
    
    model = genai.GenerativeModel(
        model_name=GEMINI_MODEL_NAME,
        system_instruction=system_instruction
    )
    
    # History fetching
    history = get_user_history(user_id)
    
    # Trim history to keep token usage within free limit
    if len(history) > MAX_HISTORY_MESSAGES:
        history = history[-MAX_HISTORY_MESSAGES:]
        
    chat = model.start_chat(history=history)
    
    try:
        response = chat.send_message(prompt)
        
        # Save updated history
        updated_history = []
        for msg in chat.history:
            updated_history.append({
                "role": msg.role,
                "parts": [p.text for p in msg.parts]
            })
        save_user_history(user_id, updated_history)
        
        return response.text
    except Exception as e:
        # Error handling oo aan crash samaynayn
        return "⚠️ Pastrator wuxuu gaaray xadka isticmaalka AI-ga ee hadda. Fadlan mar dambe isku day."
