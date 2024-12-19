import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Bot-Token aus Umgebungsvariablen laden
BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Hallo! Ich bin dein Telegram-Bot. Nutze /help für mehr Informationen.")

def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN ist nicht gesetzt!")
        return

    # Bot-Anwendung erstellen
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Befehle hinzufügen
    application.add_handler(CommandHandler("start", start))

    # Bot starten
    application.run_polling()

if __name__ == "__main__":
    main()
