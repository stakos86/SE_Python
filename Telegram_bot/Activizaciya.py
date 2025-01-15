from telegram import Bot


def send_message(chat_id, text):
    bot = Bot(token="8154608335:AAGEEbyODTJR6aVpyUU4VJQ-GTBHcCU4AZc")
    bot.send_message(chat_id=chat_id, text=text)


# Пример использования:
send_message("945946522", "Привет, бот!")
