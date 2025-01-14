import telebot
import os

# Токен доступу до MekdasBot
TOKEN = '8046134885:AAE948QVWQ4AHO2AgZtZrucgijw1UVZXgyI'
bot = telebot.TeleBot(TOKEN)

# Файл для збереження ідей
IDEAS_FILE = 'ideas.txt'

# Команда старту
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привіт! Я MekdasBot 🤖. Надсилай свої ідеї, і я їх збережу. Використовуй команду /ideas, щоб переглянути всі нотатки.")

# Команда для перегляду збережених ідей
@bot.message_handler(commands=['ideas'])
def show_ideas(message):
    if os.path.exists(IDEAS_FILE):
        with open(IDEAS_FILE, 'r') as file:
            ideas = file.read()
        if ideas:
            bot.reply_to(message, f"Ось твої ідеї:{ideas}")
        else:
            bot.reply_to(message, "Ще немає збережених ідей.")
    else:
        bot.reply_to(message, "Файл з ідеями ще не створений.")

# Основна функція для збереження ідей
@bot.message_handler(func=lambda message: True)
def save_idea(message):
    idea = message.text
    with open(IDEAS_FILE, 'a') as file:
        file.write(idea + '\n')
    bot.reply_to(message, "Ідея збережена! 🔖")

# Запуск бота
print("MekdasBot запущено...")
bot.polling()
