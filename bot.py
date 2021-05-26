import telebot
from telebot import types
import request_handler

# При запуске бота сюда нужно вставить ваш Telegram Api Key!!!
bot = telebot.TeleBot('Token')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    itembtn1 = types.KeyboardButton('/rules')
    itembtn2 = types.KeyboardButton('/about')
    markup.add(itembtn1, itembtn2)

    bot.send_message(message.chat.id,
                     f'Hi {message.from_user.first_name} 👋\nЩоб побачити правила напишіть "/rules"\nЩоб побачити опис напишіть "/about"',
                     reply_markup=markup)


@bot.message_handler(commands=['rules'])
def rules_message(message):
    bot.send_message(message.chat.id, 'Правила надсилання правильного запиту:\n\n\
🔸 Запишіть кожне окреме слово, розділене пробілом.\n\n\
🔸 Запит переважно повинен бути англійською мовою.\n\n\
🔸 Не повинен містити помилок у словах.')


@bot.message_handler(commands=['about'])
def about_message(message):
    bot.send_message(message.chat.id,
                     'Телеграм Бот написанний на Python для ВИКОНАННЯ КУРСОВОЇ РОБОТИ З ДИСЦИПЛІНИ <МАТЕМАТИЧНЕ МОДЕЛЮВАННЯ В ЛІНГВІСТИЦІ> :\n\n'
                     'Були викорастанні таки бібліотеки, як:\n'
                     '🔸 telebot\n'
                     '🔸 requests\n'
                     '🔸 beautifulsoup4\n\n'
                     'Бот шукає ваш запит у Вікіпедії, і якщо такий є, він починає аналізувати сторінку, від нього отримує фрагмент тексту та посилання на зображення, яке потім відправляє користувачеві.')


@bot.message_handler(content_types=['text'])
def send_info(message):
    print(message.from_user.first_name, message.text)
    try:
        keyboard = types.InlineKeyboardMarkup()
        url_button = types.InlineKeyboardButton(text='Wikipedia', url=request_handler.get_info(message.text)['url'])
        keyboard.add(url_button)
        bot.send_message(message.chat.id, request_handler.get_info(message.text)['img'], '\n')
        try:
            bot.send_message(message.chat.id, request_handler.get_info(message.text)['text'], reply_markup=keyboard)
        except:
            bot.send_message(message.chat.id, message.text, reply_markup=keyboard)
    except:
        bot.send_message(message.chat.id, 'Введіть правильне повідомлення.\n Для отримання правил напишіть "/ rules"')


bot.polling(none_stop=True)
