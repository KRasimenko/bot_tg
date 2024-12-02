from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Привет! Я бот-счётчик слов. Отправь мне текст, и я посчитаю количество слов."
    )

async def count_words(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text  # Получаем текст, отправленный пользователем
    word_count = len(text.split())  # Подсчитываем количество слов
    await update.message.reply_text(f"В вашем тексте {word_count} слов(а).")




if __name__ == "__main__":
    
    TOKEN = "7254123080:AAE9ByfS5iT25wL5jK_wM-YlOn27jmxQlxE"  

    # Создание приложения бота
    app = ApplicationBuilder().token(TOKEN).build()

    # Обработчики команд и сообщений
    app.add_handler(CommandHandler("start", start))  # Команда /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, count_words))  # Обработка текста

    print("Бот запущен. Нажмите Ctrl+C для остановки.")
    app.run_polling()

    app.add_handler(CommandHandler("start", start))  # Команда /start
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, count_words))  # Обработка текста
    app.run_polling()