import telebot

#Conexion con la API de telegram
TOKEN = '6456096274:AAG3-CzzyBpN0OsfaEdgtX8IbCAXB_EVB2k'
bot = telebot.TeleBot(TOKEN)

#Creacion de comandos "/start"
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, 'Hola! estas testeando el chatbot para TP')

@bot.message_handler(commands=['start'])
def send_help(message):
    bot.reply_to(message, 'Puedes interactuar conmigo usando comandos. Por ahora solo respondo /start y /help')


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, message.text)

if __name__ == "__main__":
   bot.polling(none_stop=True) 