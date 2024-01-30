import requests
from decimal import Decimal

def get_eth_to_currency_price(currency):
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "ethereum",
        "vs_currencies": currency
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        print(currency, data, "ethereum" in data, currency in data["ethereum"])
        if "ethereum" in data and currency in data["ethereum"]:
            return data["ethereum"][currency]
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinGecko API: {e}")
        return None

def convert_eth_to_currency(eth_amount, currency):
    eth_to_currency_price = get_eth_to_currency_price(currency)
    print(type(eth_to_currency_price))

    if eth_to_currency_price is not None:
        currency_amount = round(Decimal(eth_amount) * Decimal(eth_to_currency_price), 3)
        return currency_amount
    else:
        return None

if __name__ == "__main__":
    try:
        eth_amount = float(input("Enter the amount of Ether (ETH): "))
        currency = input("Enter the currency code: ")
        currency_amount = convert_eth_to_currency(eth_amount)

        if currency_amount is not None:
            print(f"{eth_amount} ETH is approximately {currency_amount:.2f} {currency}.")
        else:
            print("Failed to fetch exchange rate. Please try again later.")

    except ValueError:
        print("Invalid input. Please enter a valid numeric value for ETH.")
