import telebot
from telebot import types
import funcs_bot1
import requests
from telebot.handler_backends import ContinueHandling
# Замени 'TOKEN' на токен твоего бота
# Этот токен ты получаешь от BotFather, чтобы бот мог работать
bot = telebot.TeleBot("7988678579:AAHdVG6Jqlep-8tRS6_aIhj0gl_RBr-hXjM")


@bot.message_handler(commands=['start'])
def button(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item1 = types.InlineKeyboardButton("расскажи про платик", callback_data="plastik")
    item2 = types.InlineKeyboardButton("расскажи про металлы", callback_data="metall")
    item3 = types.InlineKeyboardButton("расскажи про другое", callback_data="other")
    markup.add(item1, item2, item3)
    bot.send_message(message.chat.id, "Этот бот помогает узнавать информацию о материалах и тем самым узнать как их лучше утилизировать", reply_markup=markup)



def button_plastik(message):
    markup = types.InlineKeyboardMarkup(row_width=1)
    item4 = types.InlineKeyboardButton("чем можно заменить", callback_data="plastik_zamena")
    item5 = types.InlineKeyboardButton("информация об утилизации", callback_data="plast_util")
    item6 = types.InlineKeyboardButton("ближайший пункт приема", callback_data="plast_2gis")
    markup.add(item4, item5, item6)
    bot.send_message(message.chat.id, "пластик", reply_markup=markup)


@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    if call.message:
        if call.data == "plastik":
            bot.send_message(call.message.chat.id, button_plastik()) 
              
        elif call.data == "metall":
            bot.send_message(call.message.chat.id, funcs_bot1.metall())
        
        elif call.data == "other":
             bot.send_message(call.message.chat.id, funcs_bot1.dog_memes())

        elif call.data == "plastik_zamena":
            bot.send_message(call.message.chat.id, funcs_bot1.plastik_zamena())
        
        elif call.data == "plast_util":
            bot.send_message(call.message.chat.id, funcs_bot1.plast_util())
        elif call.data == "plast_2gis":
            bot.send_message(call.message.chat.id, funcs_bot1.plast_2gis())
    


bot.polling(non_stop=True)
