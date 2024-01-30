import requests
from decimal import Decimal

def get_eth_to_currency_price(currency):
    """Use coingecko API to get the lates ETH conversion rate to given currency

    Arguments:
        currency {str} -- Currency code

    Returns:
        int -- ETH conversion rate to given currency, If any error then returns None and prints to terminal
    """
    # Use coingecko API to get the latest ETH price in the given currency
    url = "https://api.coingecko.com/api/v3/simple/price"
    params = {
        "ids": "ethereum",
        "vs_currencies": currency
    }

    try:
        response = requests.get(url, params=params)
        response.raise_for_status()
        data = response.json()
        if "ethereum" in data and currency in data["ethereum"]:
            return data["ethereum"][currency]
        else:
            return None

    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from CoinGecko API: {e}")
        return None

def convert_eth_to_currency(eth_amount, currency):
    """Gets the latest ETH conversion rate to given currency and converts the given ETH amount to given currency

    Arguments:
        eth_amount  -- Amount of ETH to convert
        currency -- Currency code

    Returns:
        float -- The converted amount in given currency, If any error then returns None
    """
    eth_to_currency_price = get_eth_to_currency_price(currency)

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
