import requests
import time


def get_wallet_balance(wallet_address, api_key):
    api_url = f"https://api.bscscan.com/api?module=account&action=balance&address={wallet_address}&apikey={api_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        balance = int(data['result']) / 10 ** 18  
        return balance
    else:
        print("Error occurred while fetching wallet balance.")
        return None

def monitor_wallet(wallet_address):
    previous_balance = get_wallet_balance(wallet_address, api_key)

    while True:
        current_balance = get_wallet_balance(wallet_address, api_key)

        if current_balance is not None:
            if current_balance > previous_balance:
                print(f"Balance increased: {current_balance} BNB")

            elif current_balance < previous_balance:
                print(f"Balance decreased: {current_balance} BNB")

            previous_balance = current_balance

        time.sleep(1)


# Example usage
# wallet_address = "0x997cc123cf292f46e55e6e63e806cd77714db70f"
wallet_address = "0xeb2d2f1b8c558a40207669291fda468e50c8a0bb"
api_key = "DNNHKJUGDV31EDEVD1NFT23ASZ5BIBSZB9"
monitor_wallet(wallet_address)
