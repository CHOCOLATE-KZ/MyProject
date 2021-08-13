#д.з отправляем у меня сегодня день рождение | бот отправляет открытку
#отправляем мне грустно, он пишет не грусти

from telebot import *


TOKEN = "1934658582:AAFleJFHFNuaZ3ZVtbxrt1io6WpmUI2a7mk"
bot = TeleBot(TOKEN)

@bot.message_handler(content_types=['text'])
def no_sad(message):
    if message.text == "мне грустно" or message.text == "Мне грустно":
        bot.send_message(message.chat.id, "Не грусти, всё будет хорошо)☺️")
    elif message.text == "др" or message.text == "Др":
        photo = open("birthday-1061.jpg", 'rb')
        bot.send_photo(message.chat.id, photo)



# @bot.message_handler(content_types=['text'])
# def send_img(message):
#     if message.text == "др":
#         photo = open("birthday-1061.jpg", 'rb')
#         bot.send_photo(message.chat.id, photo)



bot.polling()