from flask import Flask, request, render_template, redirect, session, flash
from currency_converter import make_api_call, get_currency_symbol,display_result_page

app = Flask(__name__)
app.secret_key = 'moresecrets'


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
    if 'data' in session:
        data=session['data']
        amount = data.get('amount')
        from_currency = data.get('from_currency')
        to_currency = data.get('to_currency')
    if not all((amount,from_currency, to_currency)):
        return 'incomplete data'

    result=make_api_call(amount,from_currency,to_currency)
    if result:
        session['result'] = result
        return redirect('/render_results/')
    else:
        return 'API call failed'


@app.route('/render_results/', methods=['GET', 'POST'])
def show_results():
    '''displays result of currency conversion and adds currency symbol '''
    return display_result_page(session)

