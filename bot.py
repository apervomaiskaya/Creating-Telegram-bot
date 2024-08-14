from telegram import Update, PhotoSize
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackContext

async def handle_photo(update: Update, context: CallbackContext):
    if update.message and update.message.photo:
        photo_file_id = update.message.photo[-1].file_id
        # Дальнейшая обработка photo_file_id
        print(f"Received photo with file_id: {photo_file_id}")
    else:
        print("No photo found in the update")

# Убедись, что ты настроил обработчик для фото
def main():
    application = Application.builder().token('7350577031:AAHUg8KkDvYgnoHN4lT3jCShns4eBXf3O-8').build()

    # Обработчики команд и сообщений
    photo_handler = MessageHandler(filters.PHOTO, handle_photo)
    application.add_handler(photo_handler)

    # Запуск приложения
    application.run_polling()

if __name__ == '__main__':
    main()
