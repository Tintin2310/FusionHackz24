
from flask import Flask, render_template, request
from web3 import Web3, exceptions
from ether_converter import convert_eth_to_currency

app = Flask(__name__)

@app.route('/', methods=["POST", "GET"])
def index():
    # If method is post then performing the balance check from given input
    if request.method == "POST":
        infura_url, address, currency = request.form["Endpoint"], request.form["Address"], request.form["currency_code"]   
        web3 = Web3(Web3.HTTPProvider(infura_url))
        connect_status = web3.is_connected()
        if connect_status:
            print("Successfully connected!")
            balance = get_balance(address, web3)
            if not balance:
                # If address is invalid then displaying the error to the UI
                return render_template('index.html', invalid_address=True)
            # If everything as expected then converting the balance to given currency and displaying it to the UI
            amount = convert_eth_to_currency(balance, currency=currency.lower())
            return render_template('index.html', balance=balance, converted_amount=amount, currency=currency)
        # If invalid enpoint displaying the error to the UI
        return render_template('index.html', invalid_endpoint=True)
    # Home page empty data UI
    return render_template('index.html')



def get_balance(address, web3):
    try:
        balance = web3.eth.get_balance(address)
        # Convert to ether value and returning it
        return web3.from_wei(balance, "ether")
    except exceptions.InvalidAddress:
        return None


if __name__ == '__main__':
    app.run(debug=True)

