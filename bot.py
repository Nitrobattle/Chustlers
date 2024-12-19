import os

# Überprüfen, ob BOT_TOKEN geladen wird
print("Lese Umgebungsvariablen...")
print("BOT_TOKEN:", os.getenv("BOT_TOKEN"))

# Hauptprogramm
def main():
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    if not BOT_TOKEN:
        print("BOT_TOKEN ist nicht gesetzt!")
        return

    print("BOT_TOKEN wurde erfolgreich geladen!")

if __name__ == "__main__":
    main()
