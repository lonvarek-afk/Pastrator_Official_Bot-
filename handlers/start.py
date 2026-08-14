from keyboards import get_main_keyboard

INTRO_TEXT = (
    "🤖 *Pastrator*\n\n"
    "Pastrator waa kaaliyahaaga AI ee gudaha Telegram.\n\n"
    "Waxaad weydiin kartaa su'aalo, qori kartaa code, turjumi kartaa qoraallo, "
    "baran kartaa waxyaabo cusub, samayn kartaa fikrado, soo koobi kartaa qoraallo, iyo wax badan.\n\n"
    "Kaliya ii soo dir fariin, waan ku caawinayaa."
)

def register_start_handlers(bot):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.send_message(
            message.chat.id,
            f"Soolaalama! 👋\n\n{INTRO_TEXT}",
            parse_mode="Markdown",
            reply_markup=get_main_keyboard()
        )

    @bot.message_handler(func=lambda msg: msg.text == "ℹ️ Introduction")
    def show_intro(message):
        bot.send_message(
            message.chat.id,
            INTRO_TEXT,
            parse_mode="Markdown",
            reply_markup=get_main_keyboard()
        )
