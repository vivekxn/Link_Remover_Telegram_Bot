from telebot import TeleBot
from bot import check_message
from config import TOKEN

app = TeleBot(TOKEN)


@app.edited_message_handler(func=lambda message: True)
def edit_message(message):
    check_message("edit", message)


@app.message_handler(func=lambda message: True)
def new_message(message):
    check_message("new", message)

if __name__ == '__main__':
    app.infinity_polling()
