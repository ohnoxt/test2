import telebot
import os
import random
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

from flask import Flask, request

token = "1025431666:AAGatwV4qwAs_HGfjJinLbYAZNUaSwopRsY"
bot = telebot.TeleBot(token)
server = Flask(__name__)

@send_action(ChatAction.TYPING)
def my_handler(bot, update):
    pass

@bot.message_handler(commands=['start'])
def start_command(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,True)
    user_markup.row('/start','/stop')
    user_markup.row('Русский язык','English language')
    bot.send_message(message.chat.id,"Выберите ваш язык\nChoose your language", reply_markup=user_markup)    

def log(message,answer):
    print("\n ------------")
    from datetime import datetime
    print(datetime.now())
    print("Сообщение от {0} {1}. (id = {2}) \n Текст - {3}".format(message.from_user.first_name,message.from_user.last_name, str(message.from_user.id), message.text))

def RussianLanguage(message):
    bot.send_message(message.chat.id,"Добро пожаловать, "+message.chat.first_name)
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('Магазины','Карта')
    user_markup.row('Кинотеатр','Наше отделение')
    user_markup.row('Главное меню')
    bot.send_message(message.chat.id,"Я польщен тем что вы выбрали меня, сейчас пожалуйста выберите нужную вам команду, "+message.chat.first_name, reply_markup=user_markup)
    

def EnglishLanguage(message):
    bot.send_message(message.chat.id,"Welcome, "+message.chat.first_name)
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('Shops','Map')
    user_markup.row('Cinema','Our location')
    user_markup.row('Main menu')
    bot.send_message(message.chat.id,"I'm very flattered that you chose me, now please select what you need, "+message.chat.first_name, reply_markup=user_markup)
    

def CinemaEng(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('Timetable','Trailers')
    user_markup.row('Back','Main menu')
    bot.send_message(message.chat.id,"What do you need to see?",reply_markup=user_markup)

def CinemaRus(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('Расписание','Трейлеры')
    user_markup.row('Назад','Главное меню')
    bot.send_message(message.chat.id,"Что вы хотите увидеть?",reply_markup=user_markup)

def ShopsEng(message): 
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('Clothes','Sport shop')
    user_markup.row('Fast-food','Game zone')
    user_markup.row('Back','Main menu')
    bot.send_message(message.chat.id,"Which one do you need?",reply_markup=user_markup)

def ShopsRus(message):
    user_markup = telebot.types.ReplyKeyboardMarkup(True,False)
    user_markup.row('Одежда','Спортивный магазин')
    user_markup.row('Фастфуд','Игровая зона')
    user_markup.row('Назад','Главное меню')
    bot.send_message(message.chat.id,"Какой из этих магазинов вам требуется?",reply_markup=user_markup)


@bot.message_handler(commands=['stop'])
def handle_stop(message):
    hide_markup = telebot.types.ReplyKeyboardRemove()
    bot.send_message(message.from_user.id,'Пока!\nBye!',reply_markup=hide_markup)

@bot.message_handler(content_types=['text'])
def get_message(message):
    answer = "Извините, я еще не научился отвечать на такие сообщения\nSorry, i don't respond for such messages"
    if message.text == 'Русский язык':
        RussianLanguage(message)
    
    elif message.text== 'English language':
        EnglishLanguage(message)
    
    elif message.text== 'Cinema':
        CinemaEng(message)
    
    elif message.text== 'Кинотеатр':
        CinemaRus(message)
    
    elif message.text== 'Shops':
        ShopsEng(message)
    
    elif message.text== 'Магазины':
        ShopsRus(message)
    
    elif message.text == 'Back':
        EnglishLanguage(message)

    elif message.text == 'Назад':
        RussianLanguage(message)

    elif message.text == 'Main menu':
        start_command(message)

    elif message.text == 'Главное меню':
        start_command(message)

    elif message.text == "Карта":
        directory = "/Users/Asus/Desktop/photos/project"
        bot.send_message(message.chat.id,"Отправляю фото")
        # bot.send_photo(message.chat.id, photo=open('/Users/Asus/Desktop/photos/project/1.jpg', 'rb'))
        # bot.send_photo(message.chat.id, photo=open('/Users/Asus/Desktop/photos/project/2.jpg', 'rb'))
        # bot.send_photo(message.chat.id, photo=open('/Users/Asus/Desktop/photos/project/3.jpg', 'rb'))
        bot.send_photo(message.chat.id, photo='https://all-malls.ru/userfiles/shop/large/134_dostyk-plaza.jpg')
        bot.send_photo(message.chat.id, photo='https://all-malls.ru/userfiles/shop/large/135_dostyk-plaza.jpg')
        bot.send_photo(message.chat.id, photo='https://all-malls.ru/userfiles/shop/large/136_dostyk-plaza.jpg')
    elif message.text == "Map":
        directory = "/Users/Asus/Desktop/photos/project"
        bot.send_message(message.chat.id,"Sending photos")
        # bot.send_photo(message.chat.id, photo=open('/Users/Asus/Desktop/photos/project/1.jpg', 'rb'))
        # bot.send_photo(message.chat.id, photo=open('/Users/Asus/Desktop/photos/project/2.jpg', 'rb'))
        # bot.send_photo(message.chat.id, photo=open('/Users/Asus/Desktop/photos/project/3.jpg', 'rb'))
        bot.send_photo(message.chat.id, photo='https://all-malls.ru/userfiles/shop/large/134_dostyk-plaza.jpg')
        bot.send_photo(message.chat.id, photo='https://all-malls.ru/userfiles/shop/large/135_dostyk-plaza.jpg')
        bot.send_photo(message.chat.id, photo='https://all-malls.ru/userfiles/shop/large/136_dostyk-plaza.jpg')
    
    elif message.text == "Расписание":
        document = open('/Users/Asus/Desktop/cinema/timetable/Kino.txt', 'rb')
        bot.send_document(message.chat.id, document)

    elif message.text == "Timetable":
        document=open('/Users/Asus/Desktop/cinema/timetable/Kino.txt', 'rb')
        bot.send_document(message.chat.id,document)
    
    elif message.text == "Трейлеры":
        link = "https://www.youtube.com/watch?v=ruNNUABRpf8"
        bot.send_message(message.chat.id, link)
    
    elif message.text == "Trailers":
        link = "https://www.youtube.com/watch?v=IThXCpk3Oc4"
        bot.send_message(message.chat.id, link)
    
    elif message.text == "Одежда":
        info = "Zara, 50000 тенге, 1 этаж"
        bot.send_message(message.chat.id,info)
    
    elif message.text == "Clothes":
        info = "Zara, 50000 tenge, 1 floor"
        bot.send_message(message.chat.id,info)
    
    elif message.text == "Спортивный магазин":
        info = "Adidas, 100000 тенге, 2 этаж"
        bot.send_message(message.chat.id,info)
    
    elif message.text == "Sport shop":
        info = "Adidas, 100000 tenge, 2 floor"
        bot.send_message(message.chat.id,info)
    
    elif message.text == "Фастфуд":
        info = "Burger king, 5000 тенге, 3 этаж"
        bot.send_message(message.chat.id,info)
    
    elif message.text == "Fast-food":
        info = "Burger king, 5000 tenge, 3 floor"
        bot.send_message(message.chat.id,info)
    
    elif message.text == "Игровая зона":
        info = "X-game, 10000 тенге, 3 этаж"
        bot.send_message(message.chat.id,info)
    
    elif message.text == "Game zone":
        info = "X-game, 10000 tenge, 3 floor"
        bot.send_message(message.chat.id,info)
    
    elif message.text == "Наше отделение":
        bot.send_location(message.from_user.id, 43.233366, 76.956868)
    
    elif message.text == "Our location":
        bot.send_location(message.from_user.id, 43.233366, 76.956868)
    
    elif message.text.lower() == "привет":
        answer = "Приветствую"
        bot.send_message(message.chat.id,answer)
        log(message, answer)
    
    elif message.text.lower() == "как дела?":
        answer = "Хорошо,как у тебя?"
        bot.send_message(message.chat.id,answer)
        log(message,answer)
    
    elif message.text.lower() == "хорошо":
        answer = "Классно, хорошего дня"
        bot.send_message(message.chat.id,answer)
        log(message, answer)

    elif message.text.lower() == "заебись":
        answer = "Пошел нахуй, мудак что ли со мной так общаться. Кем ты себя возомнил вообще?"
        bot.send_message(message.chat.id,answer)
        log(message, answer)
    
    else:
        bot.send_message(message.chat.id,answer)
        log(message, answer)

# bot.polling(none_stop=True,interval=0)

@server.route('/' + token, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200

@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://morning-beyond-77857.herokuapp.com/' + token)
    return "!", 200

if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))