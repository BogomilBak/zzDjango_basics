import requests
import time


def get_wallet_balance(wallet_address, bsc_api_token):
    api_url = f"https://api.bscscan.com/api?module=account&action=balance&address={wallet_address}&apikey={bsc_api_token}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        balance = int(data['result'])
        return balance
    else:
        print("Error occurred while getting wallet balance.")
        return None


def send_to_telegram(telegram_token, chat_id, message):
    apiURL = f'https://api.telegram.org/bot{telegram_token}/sendMessage'

    try:
        requests.post(apiURL, json={'chat_id': chat_id, 'text': message})
    except Exception as e:
        print(e)


def monitor_wallet(wallet_address, telegram_chat_id, telegram_token, bsc_api_token):
    previous_balance = get_wallet_balance(wallet_address, bsc_api_token)

    while True:
        current_balance = get_wallet_balance(wallet_address, bsc_api_token)

        if current_balance != previous_balance:
            message = f"New DEXTOOLS transaction! Check https://bscscan.com/address/0x997cc123cf292f46e55e6e63e806cd77714db70f"
            # message = "TEST"
            send_to_telegram(telegram_token, telegram_chat_id, message)
            previous_balance = current_balance

        time.sleep(1)


wallet_address = "0x997cc123cf292f46e55e6e63e806cd77714db70f"   # REAL ONE
# wallet_address = "0xeb2d2f1b8c558a40207669291fda468e50c8a0bb"
telegram_bot_token = "5831829509:AAHpxyQxG3hsQSNKf4sK3uaLK4aSOSEQtgI"
telegram_chat_id = "-812877533"
api_key = "DNNHKJUGDV31EDEVD1NFT23ASZ5BIBSZB9"


monitor_wallet(wallet_address, telegram_chat_id, telegram_bot_token, api_key)
