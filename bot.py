import telebot
from telebot import types

TOKEN = "YOUR_BOT_TOKEN"
ADMIN_ID = YOUR_USER_ID

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button = types.KeyboardButton("Оставить заявку")
    markup.add(button)

    bot.send_message(
        message.chat.id,
        "Здравствуйте! Нажмите кнопку ниже, чтобы оставить заявку.",
        reply_markup=markup
    )

@bot.message_handler(func=lambda message: message.text == "Оставить заявку")
def request(message):
    bot.send_message(message.chat.id, "Напишите ваш запрос:")
    bot.register_next_step_handler(message, send_to_admin)

def send_to_admin(message):
    text = f"Новая заявка:\n\nОт: @{message.from_user.username}\nID: {message.from_user.id}\n\nСообщение:\n{message.text}"
    
    bot.send_message(ADMIN_ID, text)
    bot.send_message(message.chat.id, "Спасибо! Ваша заявка отправлена.")

print("Bot started...")
bot.infinity_polling()
