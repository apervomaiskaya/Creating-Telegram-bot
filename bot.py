import logging
import httpx
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO,
    handlers=[
        logging.FileHandler("bot.log"),  # Логи будут записываться в bot.log
        logging.StreamHandler()  # Логи будут также выводиться в консоль
    ]
)
logger = logging.getLogger(__name__)

# ID вашего канала для уведомлений
CHANNEL_ID = '-1002195444815'

# Команда /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # non_existent_variable = 1 / 0  # Это вызовет деление на ноль и исключение
    await update.message.reply_text('Hello!')
    logger.info(f"Пользователь {update.effective_user.first_name} начал взаимодействие с ботом.")


# Команда /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    help_text = (
        "Вот доступные команды:\n"
        "/start - Запустить бота и получить приветственное сообщение.\n"
        "/help - Показать это сообщение с подсказками.\n"
        "/cat - Получить случайное фото кота.\n"
        "/send_message - Отправить сообщение в канал.\n"
    )
    await update.message.reply_text(help_text)
    logger.info(f"Пользователь {update.effective_user.first_name} запросил помощь.")

# Команда /cat
async def cat_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        response = httpx.get("https://api.thecatapi.com/v1/images/search")
        response.raise_for_status()
        cat_image_url = response.json()[0]["url"]
        await update.message.reply_photo(photo=cat_image_url)
        logger.info(f"Пользователь {update.effective_user.first_name} получил случайное фото кота.")
    except httpx.HTTPStatusError as e:
        await update.message.reply_text("Не удалось получить фото кота.")
        logger.error(f"Ошибка при получении фото кота: {e}")
        # Уведомить вас в канал о проблеме
        await context.bot.send_message(chat_id=CHANNEL_ID, text=f"Произошла ошибка: {e}")

# Команда /send_message
async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message_text = "Это тестовое сообщение отправлено ботом в канал!"
    await context.bot.send_message(chat_id=CHANNEL_ID, text=message_text)
    await update.message.reply_text("Сообщение отправлено в канал.")
    logger.info(f"Сообщение отправлено в канал.")

if __name__ == '__main__':
    application = ApplicationBuilder().token('7350577031:AAHUg8KkDvYgnoHN4lT3jCShns4eBXf3O-8').build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(CommandHandler('help', help_command))
    application.add_handler(CommandHandler('cat', cat_command))
    application.add_handler(CommandHandler('send_message', send_message))

    application.run_polling()
