import telebot
import config

bot = telebot.TeleBot(config.token)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Hey, how are u?")


@bot.message_handler(content_types=["text"])
def repeate_all_messages(message):
    bot.send_message(message.chat.id, message.text)


bot.polling()
