from telegram.ext import Updater, CommandHandler

# Bot-Token von @BotFather
BOT_TOKEN = "8121562412:AAEGl1lCP47AaZdmbCRXDLVDEbc8gLWRjgw"

# Start-Befehl
def start(update, context):
    update.message.reply_text("Hallo! Ich bin dein Telegram-Bot. Nutze /help für mehr Informationen.")

# Hauptfunktion
def main():
    # Bot-Instanz erstellen
    updater = Updater(BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Befehle hinzufügen
    dispatcher.add_handler(CommandHandler("start", start))

    # Bot starten
    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()