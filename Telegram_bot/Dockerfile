FROM python:3.9
WORKDIR /app
COPY Telegram_bot.py .
COPY requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
CMD ["python", "Telegram_bot.py"]