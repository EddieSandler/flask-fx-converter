from unittest import TestCase
import requests
from flask import session
from app import app
from currency_converter import make_api_call, get_currency_symbol

app.config['TESTING'] = True

class FLaskTests(TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_display_form_route(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

    def test_get_input_route(self):
        response = self.app.post('/get_input', data=dict(currency_1='USD', currency_2='EUR', amount='100'))
        self.assertEqual(response.status_code, 302)

    def test_make_api_call(self):
        with app.test_client() as client:
            resp = requests.get('http://api.exchangerate.host/convert?access_key=7142dec52324fdfeab97629c473f72d0&from=USD&to=USD&amount=100&format=1')
            self.assertEqual(resp.status_code, 200)

    def test_get_currency_symbol(self):
        symbol = get_currency_symbol('usd')
        self.assertEqual(symbol, '$')

    def test_show_results(self):
        with app.test_request_context('/render_results/'):
            with app.test_client() as client:
                # Simulate session data
                session['result'] = {
                    'query': {'to': 'USD'},  # Simulate required session data
                    'result': 100.12345  # Simulate the result value
                }

                # Simulate the symbol and amount values instead of calling the functions
                with client.session_transaction() as sess:
                    sess['result'] = session['result']
                response = client.get('/render_results/')

                self.assertEqual(response.status_code, 200)





