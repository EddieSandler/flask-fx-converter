from flask import Flask,flash, request, render_template, redirect, session
from currency_converter import make_api_call, get_currency_symbol

app = Flask(__name__)
app.secret_key = 'moresecrets'


@app.route('/')
def display_form():
    '''displays form for user input'''
    return render_template('fx_input.html')


@app.route('/get_input', methods=['GET', 'POST'])
def get_user_input():
    '''retrieves user input and stores in Session'''

    form_inputs = {
        'from_currency': request.form.get('currency_1'),
        'to_currency': request.form.get('currency_2'),
        'amount': request.form.get('amount'),
    }
    session['form_inputs'] = form_inputs
    return redirect('/make_api_call/')


@app.route('/make_api_call/', methods=['GET'])
def fx_conversion():
    '''calls api and returns results which is saved in session'''

    response=session['form_inputs']
    amount = response.get('amount')
    from_currency = response.get('from_currency')
    to_currency =response.get('to_currency')
    result=make_api_call(amount,from_currency,to_currency)
    status=result['success']


    if status is False:
        flash(f"error-{result['error']['type']}")
        return redirect('/')
    else :
        session['result']=result
        return redirect('/render_results')


@app.route('/render_results/', methods=['GET', 'POST'])
def show_results():
    symbol=get_currency_symbol(session['result']['query']['to'])
    amount=str(round(session['result']['result'],2))

    return render_template('fx_output.html',symbol=symbol,amount=amount)






#  {
#   "info": {
#     "quote": 149.058013,
#     "timestamp": 1698693424
#   },
#   "privacy": "https://currencylayer.com/privacy",
#   "query": {
#     "amount": 100,
#     "from": "USD",
#     "to": "JPY"
#   },
#   "result": 14905.8013,
#   "success": true,
#   "terms": "https://currencylayer.com/terms"

#  }