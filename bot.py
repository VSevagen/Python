import telebot

bot = telebot.TeleBot("601087145:AAEDjdnBSglfMSjJ7-zc3Ck3EjDU--P813g")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Sevagen, how are you doing?")
    
@bot.message_handler(func=lambda m:True)
def echo_all(message):
    bot.reply_to(message, message.text)
    
bot.polling()