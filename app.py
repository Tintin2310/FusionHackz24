
from flask import Flask, render_template, request
from web3 import Web3, exceptions

app = Flask(__name__)

infura_url = "Infura_URL"
web3 = Web3(Web3.HTTPProvider(infura_url))

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        print(request.form["Endpoint"], request.form["Address"])
        return render_template('index.html')
    return render_template('index.html')



@app.route('/balance/<address>')
def get_balance(address):
    print(f"{web3.eth.block_number}")

    # Fill in your account here=
    try:
        balance = web3.eth.get_balance(address)
        print(web3.from_wei(balance, "ether"))
    except exceptions.InvalidAddress:
        print("Invalid address!")
    # try:
    #     balance_wei = web3.eth.getBalance(address)
    #     balance_eth = web3.fromWei(balance_wei, 'ether')
    #     return f'Balance of {address}: {balance_eth} ETH'
    # except Exception as e:
    #     return f'Error: {e}'
connect_status = web3.is_connected()

if connect_status:
    get_balance("Wallet_Address")
    print("Successfully connected!")

if __name__ == '__main__':
    app.run(debug=True)

