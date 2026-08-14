import os
from dotenv import load_dotenv

# Soo rar environment variables-ka
load_dotenv()

TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Luuqadaha la taageero
SUPPORTED_LANGUAGES = {
    "en": "🇬🇧 English",
    "so": "🇸🇴 Somali",
    "ar": "🇸🇦 العربية"
}

# Qaabeynta model-ka Gemini
GEMINI_MODEL_NAME = "gemini-2.5-flash"
MAX_HISTORY_MESSAGES = 10  # Window-ga history-ga si loo yareeyo quota-ga
