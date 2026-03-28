from telebot import TeleBot
from config import ADMINS


#<<<<<<<<<<<<<CODE>>>>>>>>>>>>>>#
def check_message(type, message):
    if message.from_user.id in ADMINS:
        return
    chat_member = app.get_chat_member(message.chat.id, message.from_user.id)
    if chat_member.status == 'creator' or chat_member.status == 'administrator':
        return
    if chat_member.status == 'left' and chat_member.user.username == 'GroupAnonymousBot':
        return
    if message.text.find('@') != -1:
        app.delete_message(message.chat.id, message.message_id)
    elif message.text.find('t.me') != -1:
        app.delete_message(message.chat.id, message.message_id)
    elif message.text.find('http://') != -1 or message.text.find('https://') != -1:
        app.delete_message(message.chat.id, message.message_id)
    elif message.text.find('.com') != -1 or message.text.find('.ir') != -1:
        app.delete_message(message.chat.id, message.message_id)
