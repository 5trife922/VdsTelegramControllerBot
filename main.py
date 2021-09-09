from subprocess import check_output
import config
import telebot
import time



bot = telebot.TeleBot(config.token)#токен
@bot.message_handler(content_types=["text"])

def main(message):
   if (config.uid == message.chat.id): #проверка личности
      comand = message.text  #сама команда
      try:
         bot.send_message(message.chat.id, check_output(comand.lower(), shell = True)) #выполняем команду
      except:
         bot.send_message(message.chat.id, "Я не могу это сделать") #пишем ошибку


if __name__ == '__main__':
    bot.send_message(config.uid, "Я запустился и работаю :)") #информирование о запуске скрипта
    while True:
        try:
            bot.polling(none_stop=True)#запуск бота
        except:
            time.sleep(15)#Атдыхаем после падения
