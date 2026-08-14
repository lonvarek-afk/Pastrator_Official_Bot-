import os
from groq import Groq

api_key = os.getenv("GROQ_API_KEY")
client = Groq(api_key=api_key) if api_key else None

def generate_ai_response(prompt, user_name="User"):
    if not client:
        return "System error: Groq API Key is missing."
        
    try:
        system_instruction = (
            f"You are Pastrator, an advanced AI assistant built for Telegram. "
            f"The user's name is {user_name}. Respond professionally, clearly, "
            f"and accurately. Do not use any emojis in your response under any circumstances."
        )
        
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=1024
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"Error: {str(e)}"
