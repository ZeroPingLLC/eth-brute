from web3 import Web3
import requests
import time

# Funktion, um ein neues Ethereum-Wallet zu erstellen
def create_eth_wallet():
    w3 = Web3()
    account = w3.eth.account.create()
    private_key = account._private_key.hex()
    public_key = account.address
    return private_key, public_key

# Funktion, um die Balance einer Adresse über die Etherscan-API zu überprüfen
def check_balance(address, api_key):
    url = f"https://api.etherscan.io/api?module=account&action=balance&address={address}&tag=latest&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    balance = int(data['result']) / 10**18  # Umrechnen von Wei in Ether
    return balance

# Hauptfunktion, die das Wallet erstellt und die Balance prüft
def main():
    api_key = 'YOUR-API-KEY-HERE-FROM-https://etherscan.io'
    found = False
    while not found:
        private_key, public_key = create_eth_wallet()
        balance = check_balance(public_key, api_key)
        
        # Prüfen, ob die Balance mehr als 0 ist
        if balance > 0:
            with open('wallet.txt', 'a') as f:
                f.write(f"Private Key: {private_key}, Public Key: {public_key}, Balance: {balance} ETH\n")
            print(f"Found a wallet with a balance! Private Key: {private_key}\nPublic Key: {public_key}\nBalance: {balance} ETH")
            found = True
        else:
            print(f"No balance found for {public_key}. Trying another wallet...")
        time.sleep(1)  # Pause von 1 Sekunde zwischen den Anfragen, um Rate Limits zu vermeiden

if __name__ == "__main__":
    main()
