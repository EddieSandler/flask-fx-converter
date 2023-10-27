from flask import Flask, request, render_template, redirect, session
import requests
from datetime import datetime
from forex_python.converter import CurrencyCodes


app = Flask(__name__)
app.secret_key = 'moresecrets'
c = CurrencyCodes()
access_key = '7142dec52324fdfeab97629c473f72d0'
base_url = 'http://api.exchangerate.host/convert?access_key='


@app.route('/')
def display_form():

    return render_template('fx_converter.html')


@app.route('/get_input', methods=['GET', 'POST'])
def get_user_input():
    data = {
        'from_currency': request.form.get('currency_1'),
        'to_currency': request.form.get('currency_2'),
        'amount': request.form.get('amount'),
        'format': '1'
    }
    session['data'] = data

    return redirect('/make_api_call/')


@app.route('/make_api_call/', methods=['GET'])
def fx_conversion():
    amount=session['data']['amount']
    from_currency=session['data']['from_currency']
    to_currency=session['data']['to_currency']
    url = f'{base_url}{access_key}&from={from_currency}&to={to_currency}&amount={amount}&format=1'
    response = requests.get(url=url)
    if response.status_code == 200:
        res = response.json()



        print(f'you converted {amount} of {from_currency} to {to_currency}')
        print(f"quote: {res['info']['quote']}")
        print(f"total: {res['result']}")
        symbol=c.get_symbol(to_currency)
        print(f"symbol: {symbol}")
        

        print(f'The rate is {res["info"]["quote"]} ')

        timestamp = res["info"]["timestamp"]
        human_readable_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        print(f'timestamp of transaction : {human_readable_time}')
        return res


#         print(c.get_symbol('GBP'))
#         print (c.get_symbol('EUR'))



# {
#   "info": {
#     "quote": 0.82326,
#     "timestamp": 1698419583
#   },
#   "privacy": "https://currencylayer.com/privacy",
#   "query": {
#     "amount": 90000000000,
#     "from": "USD",
#     "to": "GBP"
#   },
#   "result": 74093400000,
#   "success": true,
#   "terms": "https://currencylayer.com/terms"
# }
