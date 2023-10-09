# import requests
#
# bot_token = "5831829509:AAHpxyQxG3hsQSNKf4sK3uaLK4aSOSEQtgI"
# api_url = f"https://api.telegram.org/bot{bot_token}/getUpdates"
#
# response = requests.get(api_url)
# data = response.json()
#
# chat_id = data["result"][0]["message"]["chat"]["id"]
# print("Chat ID:", chat_id)

import telegram

bot_token = "5831829509:AAHpxyQxG3hsQSNKf4sK3uaLK4aSOSEQtgI"
bot = telegram.Bot(token=bot_token)

updates = bot.get_updates()
for update in updates:
    chat = update.effective_chat
    print("Chat ID:", chat.id, "Chat Title:", chat.title)