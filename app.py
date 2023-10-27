from flask import Flask, request, render_template, redirect, session
import requests

from forex_python.converter import CurrencyCodes


app = Flask(__name__)
app.secret_key = 'moresecrets'
c = CurrencyCodes()
access_key = '7142dec52324fdfeab97629c473f72d0'
base_url = 'http://api.exchangerate.host/convert?access_key='


@app.route('/')
def display_form():
    '''displays form for user input'''





    return render_template('fx_input.html')


@app.route('/get_input', methods=['GET', 'POST'])
def get_user_input():
    '''retrieves user input and stores in Session'''

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
    '''calls api and returns results which is saved in session'''
    if 'data' in session and 'result' in session and 'result' in session['result']:
        amount = session['data']['amount']
        from_currency = session['data']['from_currency']
        to_currency = session['data']['to_currency']
    else:
        return 'error- That is some baaad input'

    url = f'{base_url}{access_key}&from={from_currency}&to={to_currency}&amount={amount}&format=1'


    response = requests.get(url=url)
    
    if response.status_code == 200:
        result = response.json()
        session['result'] = result
        return redirect('/render_results/')



@app.route('/render_results/', methods=['GET', 'POST'])
def show_results():
    '''displays result of currency conversion and adds currency symbol '''

    symbol = c.get_symbol(session['data']['to_currency'].upper())
    exchange=str(round(session['result']['result'],2))




    return render_template('fx_output.html',symbol=symbol,exchange=exchange)

