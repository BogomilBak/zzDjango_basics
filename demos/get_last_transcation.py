import requests


def get_last_transaction(wallet_address, api_key):
    api_url = f"https://api.bscscan.com/api?module=account&action=txlist&address={wallet_address}&startblock=0&endblock=99999999&sort=desc&apikey={api_key}"
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        if data['status'] == '1' and data['message'] == 'OK':
            last_transaction = data['result'][0]
            return last_transaction
        else:
            print("Error occurred while fetching transaction data.")
    else:
        print("Error occurred while fetching transaction data.")
    return None

api_key = "DNNHKJUGDV31EDEVD1NFT23ASZ5BIBSZB9"
wallet_address = "0xeb2d2f1b8c558a40207669291fda468e50c8a0bb"
get_last_transaction(wallet_address, api_key)