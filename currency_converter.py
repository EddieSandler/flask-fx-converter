from flask import render_template,flash
import requests
from forex_python.converter import CurrencyCodes

c = CurrencyCodes()
access_key = '7142dec52324fdfeab97629c473f72d0'
base_url = 'http://api.exchangerate.host/convert?access_key='

def make_api_call(amount, from_currency, to_currency):
    url = f'{base_url}{access_key}&from={from_currency}&to={to_currency}&amount={amount}&format=1'

    response = requests.get(url=url)

    if response.status_code == 200:
        return response.json()
    return None

def get_exchange_value(session):
    result = session.get('result')
    if result:
        try:
            exchange = str(round(session['result']['result'], 2))
        except KeyError:
            # You can modify this to handle the missing key differently
            return None
        return exchange
    return None

def get_currency_symbol(currency_code):
    return c.get_symbol(currency_code.upper())

def display_result_page(session):
    symbol = get_currency_symbol(session['data']['to_currency'])
    exchange = get_exchange_value(session)

    if exchange is None:
        flash('Invalid currency code: please re-enter', 'error')
        return render_template('fx_input.html')

    return render_template('fx_output.html', symbol=symbol, exchange=exchange)