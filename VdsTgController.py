from subprocess import check_output 
import telebot
import time

bot = telebot.TeleBot("781:227")#Токен
id = 840059257 #id владельца
@bot.message_handler(content_types=["text"])


def main(message):
   if (id == message.chat.id): #Производим идентификацию пользователя
      command = message.text  #Сюда попадает сама команда
      try: 
         bot.send_message(message.chat.id, check_output(command, shell = True))
      except:
         bot.send_message(message.chat.id, "Не могу это сделать")
if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except:
            time.sleep(15) #Атдыхаем если падаем



#github.com/5trife922/
