import logging
import requests
import random
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Файл с предсказаниями
PREDICTIONS_FILE = 'predictions.txt'


def get_bot_updates():
    """Получить обновления для бота."""
    url = f"https://api.telegram.org/bot{'8154608335:AAGEEbyODTJR6aVpyUU4VJQ-GTBHcCU4AZc'}/getUpdates"

    try:
        response = requests.get(url)
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка при получении обновлений: {e}")
        return None


def process_updates(updates):
    """Обработка полученных обновлений."""
    if updates is None or not updates:
        return

    for update in updates:
        try:
            chat_id = update['message']['chat']['id']
            text = update['message'].get('text', '')

            if text == '/start':
                start(update)
            elif text:
                handle_prediction(update)
        except KeyError as e:
            logger.error(f"Ошибка при обработке обновления: {e}")


def get_random_prediction():
    """Получить случайное предсказание из файла."""
    try:
        with open(PREDICTIONS_FILE, 'r') as file:
            predictions = file.readlines()
        return random.choice(predictions).strip()
    except FileNotFoundError:
        logger.error(f"Файл с предсказаниями не найден: {PREDICTIONS_FILE}")
        return "Извините, произошла ошибка при получении предсказания."


def start(update: Update, context):
    """Отправить приветственное сообщение и инструкции."""
    update.message.reply_text(
        "Привет! Я бот, который выдает позитивные предсказания на день. "
        "Чтобы получить предсказание, просто отправьте любое сообщение."
    )


def handle_prediction(update: Update, context):
    """Обработка запроса на получение предсказания."""
    prediction = get_random_prediction()
    if prediction:
        update.message.reply_text(prediction)
    else:
        update.message.reply_text("Извините, произошла ошибка при получении предсказания.")


def main():
    """Запуск бота."""
    application = Application.builder().token("8154608335:AAGEEbyODTJR6aVpyUU4VJQ-GTBHcCU4AZc").build()

    # Обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Обработчик сообщений для получения предсказания
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_prediction))

    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    application.run_polling()


if __name__ == '__main__':
    main()
