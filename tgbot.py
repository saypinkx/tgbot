from telebot import *
from telebot import types
token="5955751156:AAGm38Oj5AV4LKdrw2NP769bBwWgOPFLSq0"
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
  keyboard=telebot.types.ReplyKeyboardMarkup(True,True)
  keyboard1=telebot.types.KeyboardButton("Ознакомится")
  keyboard.add(keyboard1)  
  message=bot.send_message(message.chat.id,"Привет, это чат-бот клуба Spectrum в игре Brawl Stars, чтобы ознакомится с основными командами нажми на кнопку",reply_markup=keyboard)
  bot.register_next_step_handler(message,comands)
 
def comands(message):
  keyboard=telebot.types.ReplyKeyboardMarkup(True)
  keyboard0=telebot.types.KeyboardButton(text="Условия вступления")
  keyboard1=telebot.types.KeyboardButton(text="Полезные ссылки")
  keyboard2=telebot.types.KeyboardButton(text="Получить тег клуба")
  keyboard3=telebot.types.KeyboardButton(text="Я вступил в клуб, что дальше?")
  keyboard.add(keyboard0)
  keyboard.add(keyboard2)
  keyboard.add(keyboard3)
  keyboard.add(keyboard1)
  message=bot.send_message(message.chat.id,"Выбери интересующий вопрос нажатием кнопки",reply_markup=keyboard)
  bot.register_next_step_handler(message,information)
@bot.message_handler(content_types="text")
def information(message):
  keyboard=telebot.types.InlineKeyboardMarkup()
  keyboard1=telebot.types.InlineKeyboardButton(text="Написать президенту",url="https://vk.com/saypinkx")
  keyboard.add(keyboard1)  
  if message.text.lower()=="условия вступления":
    bot.send_message(message.chat.id,"Наличие 40к кубков,мифическая лига в одиночной или командной силовой лиге,чтобы вступить, напиши президенту клуба",reply_markup=keyboard)
  elif message.text.lower()=="получить тег клуба":
    bot.send_message(message.chat.id,"#22VOGPLL9")
  elif message.text.lower()=="я вступил в клуб, что дальше?":
    keyboard2=telebot.types.InlineKeyboardMarkup()
    button1=telebot.types.InlineKeyboardButton(text="Записаться в таблицу", url="https://docs.google.com/spreadsheets/d/1t2A1H_h6pBseqyWIXYrRHsGhuMwd5FXR8GI_5j9QM8I/edit?usp=sharing")
    keyboard2.add(button1)   
    bot.send_message(message.chat.id,"Тебе необходимо записаться в таблицу и связаться со своим ответсвенным",reply_markup=keyboard2)
  elif message.text.lower()=="полезные ссылки":
    keyboard0=telebot.types.InlineKeyboardMarkup()
    button2=telebot.types.InlineKeyboardButton(text="Наш Discord сервер",url="https://discord.gg/wDqrZSd")
    button3=telebot.types.InlineKeyboardButton(text="Группа клуба",url="https://vk.com/safterss")
    button4=telebot.types.InlineKeyboardButton(text="Беседа в Telegram ",url="https://t.me/+nTjvycvuAZw0ZDk6 ")
    button5=telebot.types.InlineKeyboardButton(text="Беседа в VK ",url="https://vk.me/join/GfZ4qOoLbPM4a2_6CmmQawlFrScu_7iWXds= ")
    keyboard0.add(button2)
    keyboard0.add(button3)
    keyboard0.add(button4)
    keyboard0.add(button5)
    bot.send_message(message.chat.id,"Полезные ссылки",reply_markup=keyboard0)
  else:
    bot.send_message(message.chat.id,"Я тебя не понимаю :(")
    comands(message)
bot.infinity_polling()