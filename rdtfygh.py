import telebot
bot = telebot.TeleBot("6970732933:AAHMB2BKUoui8o0_RCjUN7b_8h5JcEr0TUk")
@bot.message_handler(commands=["start"])

def start(m,res=False):
    bot.send_message(m.chat.id, 'Сообщение. Эхо.')
@bot.message_handler(content_types=["text"])
def handle_text(message):
    if message.text == "Шутка":
        bot.send_message(message.chat.id, 'ihgjhgj"dcd"dcvdv' )
    elif message.text == "Привет":
        bot.send_message(message.chat.id, "Привет")
    else:
        bot.send_message(message.chat.id, "Вы написали: " + message.text)
        bot.send_message(message.chat.id, "Длина этого сообщения: " + str(len(message.text)))
        a = message.text.split()
        print(a)
        for i in a:
            for j in i:
                bot.send_message(message.chat.id, j)
bot.polling(none_stop=True, interval=0)