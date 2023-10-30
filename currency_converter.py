import requests
from forex_python.converter import CurrencyCodes

c = CurrencyCodes()
access_key = '7142dec52324fdfeab97629c473f72d0'
base_url = 'http://api.exchangerate.host/convert?access_key='

def make_api_call(amount, from_currency, to_currency):
    url = f'{base_url}{access_key}&from={from_currency}&to={to_currency}&amount={amount}&format=1'

    response = requests.get(url=url)
    result = response.json()
    return result




def get_currency_symbol(currency_code):
    return c.get_symbol(currency_code.upper())
