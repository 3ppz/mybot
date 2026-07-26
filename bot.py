import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

TOKEN = '6171144221:AAGNDQGvo-YkEjUED50cxi26SL7PtllKc_4'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    markup = InlineKeyboardMarkup()
    markup.row_width = 2
    
    btn_blue = InlineKeyboardButton('أزرق 🔵', callback_data='blue')
    btn_red = InlineKeyboardButton('أحمر 🔴', callback_data='red')
    btn_green = InlineKeyboardButton('أخضر 🟢', callback_data='green')
    
    markup.add(btn_blue, btn_red, btn_green)
    
    bot.send_message(message.chat.id, "أهلاً بك! اختر لوناً من الأزرار أدناه:", reply_markup=markup)

bot.infinity_polling()
