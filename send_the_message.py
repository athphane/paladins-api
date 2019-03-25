import telepot
from env import telegram_api_key

def sendMessage(chat_id, message) :
    bot = telepot.Bot(telegram_api_key)
    bot.sendMessage(chat_id, message ,parse_mode="Markdown", disable_web_page_preview=1)

def sendMessageInlineKeyboard(chat_id, message, keyboard) :
    bot = telepot.Bot(telegram_api_key)
    bot.sendMessage(chat_id, message, reply_markup = keyboard)