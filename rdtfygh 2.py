import telebot
import random
global att
global ran
att = 1
gama = 0
ran = 0

bot = telebot.TeleBot("6970732933:AAHMB2BKUoui8o0_RCjUN7b_8h5JcEr0TUk")
@bot.message_handler(commands=["start"])
def start(m,res=False):
    bot.send_message(m.chat.id, 'Это игра "Угадай число". Нужно отгадать число за 6 попыток и я буду говорить больше или меньше')
    bot.send_message(m.chat.id, "Отправте любой символ, чтобы продолжить")
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global att
    global ran
    global gama
    if gama == 0:
        ran = random.randint(0,100)
        gama = 1
        bot.send_message(message.chat.id, 'Хорошо, начинаем игру')
    else:
        '''
        try:
            att < 6:
        except ValueError:
            '''
        bot.send_message(message.chat.id, 'Попытка ' + str(att) + "...")
        if int(message.text) == ran:
            gama = 0
            bot.send_message(message.chat.id, 'Ура, победа. Вы отгадали число ' + str(ran) + " за " + str(att) + " попыток")
            att = 0
            bot.send_message(message.chat.id, "Отправте любой символ, чтобы продолжить")
        else:
            if att < 6:
                if int(message.text) > ran:
                    bot.send_message(message.chat.id, 'Число меньше' )
                if int(message.text) < ran:
                    bot.send_message(message.chat.id, 'Число больше' )
            else:
                gama = 0
                att = 0
                bot.send_message(message.chat.id, 'Вндгшплрмцфкыу, ты праиграл. Число было ' + str(ran))
                bot.send_message(message.chat.id, "Отправте любой символ, чтобы продолжить")
        att += 1
bot.polling(none_stop=True, interval=0)