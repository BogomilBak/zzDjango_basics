# import telegram
#
# telegram_bot_token = "5831829509:AAHpxyQxG3hsQSNKf4sK3uaLK4aSOSEQtgI"
# telegram_chat_id = "1838700998"
#
# telegram_bot = telegram.Bot(telegram_bot_token)
# telegram_bot.send_message(telegram_chat_id, 'hello')


import requests

def send_to_telegram(message):

    apiToken = '5831829509:AAHpxyQxG3hsQSNKf4sK3uaLK4aSOSEQtgI'
    chatID = '-812877533'
    apiURL = f'https://api.telegram.org/bot{apiToken}/sendMessage'

    try:
        response = requests.post(apiURL, json={'chat_id': chatID, 'text': message})
        print(response.text)
    except Exception as e:
        print(e)

send_to_telegram("Hello from Python!")