import warnings
import httpx
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем ID вашего канала
CHANNEL_ID = '-1002195444815'  # замените на ваш реальный ID канала

# URL для получения случайного фото кота
CAT_API_URL = "https://api.thecatapi.com/v1/images/search"

# Определяем обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Отправляем пользователю приветственное сообщение
    await update.message.reply_text('Hello!')

# Определяем обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Текст, который будет отправлен в ответ на команду /help
    help_text = (
        "Вот доступные команды:\n"
        "/start - Запустить бота и получить приветственное сообщение.\n"
        "/help - Показать это сообщение с подсказками.\n"
        "/cat - Получить случайное фото кота.\n"
        "/send_message - Отправить сообщение в канал.\n"
    )
    # Отправляем сообщение с текстом помощи
    await update.message.reply_text(help_text)

# Обработчик для команды /cat
async def cat_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    async with httpx.AsyncClient() as client:
        response = await client.get(CAT_API_URL)
        response.raise_for_status()  # Проверка на ошибки запроса
        cat_data = response.json()
        
        # Получаем URL первого изображения из ответа
        cat_photo_url = cat_data[0]['url']
        await update.message.reply_photo(photo=cat_photo_url)

# Обработчик для команды /send_message
async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Текст сообщения для отправки в канал
    message_text = "Это тестовое сообщение отправлено ботом в канал!"
    
    # Отправляем сообщение в канал
    await context.bot.send_message(chat_id=CHANNEL_ID, text=message_text)
    
    # Отправляем подтверждение пользователю
    await update.message.reply_text("Сообщение отправлено в канал.")

if __name__ == '__main__':
    # Создаем приложение Telegram с использованием токена вашего бота
    application = ApplicationBuilder().token('7350577031:AAHUg8KkDvYgnoHN4lT3jCShns4eBXf3O-8').build()

    # Добавляем обработчики команд в приложение
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('cat', cat_command))
    application.add_handler(CommandHandler('send_message', send_message))

    # Запускаем бота
    application.run_polling()
