
from flask import Flask, render_template, request
from web3 import Web3, exceptions

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        infura_url, address = request.form["Endpoint"], request.form["Address"]
        web3 = Web3(Web3.HTTPProvider(infura_url))
        connect_status = web3.is_connected()
        if connect_status:
            print("Successfully connected!")
            balance = get_balance(address, web3)
            if not balance:
                return render_template('index.html', invalid_address=True)
            return render_template('index.html', balance=balance)
        return render_template('index.html', invalid_endpoint=True)
    return render_template('index.html')



@app.route('/balance/<address>')
def get_balance(address, web3):
    print(f"{web3.eth.block_number}")
    try:
        balance = web3.eth.get_balance(address)
        return web3.from_wei(balance, "ether")
    except exceptions.InvalidAddress:
        return None


if __name__ == '__main__':
    app.run(debug=True)

