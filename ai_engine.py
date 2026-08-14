import os
import google.generativeai as genai

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Waxaan isticmaaleynaa gemini-1.5-flash oo aad u dhakhso badan
model = genai.GenerativeModel('gemini-1.5-flash')

def generate_ai_response(prompt, user_name="User"):
    try:
        system_instruction = f"You are Pastrator, an advanced AI assistant created for Telegram. The user's name is {user_name}. Respond professionally, clearly, and concisely without using any emojis in your response."
        
        response = model.generate_content(f"{system_instruction}\n\nUser: {prompt}")
        return response.text
    except Exception as e:
        return "System error encountered. Please try again in a moment."
