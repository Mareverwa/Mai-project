import telebot
import requests

TOKEN = '5761330839:AAEPHPeYqaluMQEhxdPvjwc_taY4rKoFyMs'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "type currency code e.g EUR for euro to get the exchange rate, the base currency is always the USD: ")

@bot.message_handler(content_types=['text'])
def get_user_text(message):
    params =  {
        'access_key' : '39ef71316134661a5eea6ed6',
        'rates' : message.text.upper()
    }
    print(message.text)
    results = requests.get('https://open.er-api.com/v6/latest/USD',params)
    try:
        bot.send_message(message.chat.id,f"Current Echange Rate: 1 USD  {results.json()['rates'][str(message.text).upper()]}")
    except:
         bot.send_message(message.chat.id,"Please type a currency code e.g EUR")




bot.polling(non_stop=True)