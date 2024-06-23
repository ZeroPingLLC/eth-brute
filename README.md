# Ethereum Brute-Force & Wallet Balance Checker

This Python script automatically generates Ethereum wallets and checks if they have a balance using the Etherscan API. If a wallet with a balance greater than zero is found, the script saves the wallet's private key, public key, and balance to a file named `wallet.txt`.

NEW UPDATE HERE :  https://github.com/ZeroPingLLC/eth-brute/releases/tag/v2.0
Release : 24.06.2024


## Prerequisites

Before you run this script, you will need Python installed on your machine. Additionally, you will need to install the following Python libraries:
- `web3`
- `requests`

You can install these with pip:
```bash
pip install web3 requests
```

## Usage

1. **Clone the repository:**
   ```bash
   git clone https://github.com/ZeroPingLLC/eth-brute.git
   cd eth-brute
   ```

2. **Run the script:**
   ```bash
   python3 eth.py
   ```

   The script will continuously generate new Ethereum wallets and check their balances using the Etherscan API. If it finds a wallet with a balance, it will stop and save the details to `wallet.txt`.

## Configuration

You will need an Etherscan API key to use the Etherscan API. Replace the `api_key` variable in the script with your own Etherscan API key:
```python
api_key = 'YOUR_ETHERSCAN_API_KEY' -> get your API key from https://etherscan.io/ for free :)
```

## How It Works

### Wallet Generation
The script uses the `web3.py` library to generate a new Ethereum wallet, which includes a private key and a public key (wallet address).

### Balance Checking
It then checks the balance of the generated wallet using the Etherscan API. If the balance is greater than zero, the script writes the wallet's details to a file.

### Looping
The script runs in a loop, generating wallets and checking their balances until it finds a wallet with a non-zero balance.

## Safety and Legal Notes

- **Security**: Be cautious with handling and storing private keys. Never expose them publicly or use them on unsecured platforms.
- **API Usage**: Be aware of the API usage limits set by Etherscan to avoid being blocked.
- **Ethics and Legality**: Generating and checking random wallets may be seen as unethical or illegal if it involves accessing or attempting to access someone else's assets. Ensure that your use of this script complies with all relevant laws and ethical guidelines.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
