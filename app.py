import requests
from datetime import datetime
from flask import Flask,request,render_template


app = Flask(__name__)

app.config.SECRET_KEY = 'moresecrets'


@app.route('/',methods=['GET','POST'])
def fx_conversion():
    access_key = '7142dec52324fdfeab97629c473f72d0'
    from_currency = 'USD' #get from form
    to_currency = 'EUR'   #get from form
    amount = '25'         #get from form
    format = '1'           #what is this ?
    base_url = 'http://api.exchangerate.host/convert?access_key='

    url = f'{base_url}{access_key}&from={from_currency}&to={to_currency}&amount={amount}&format={format}'

    response = requests.get(url=url)
    if response.status_code == 200:
        data = response.json()
        print(f'you converted {amount} of {data["query"]["from"]} to {data["result"]} of {data["query"]["to"]}.the rate is {data["info"]["quote"]} ')
        timestamp = data["info"]["timestamp"]
        human_readable_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S')
        print(f'timestamp of transaction : {human_readable_time}')

        my_test_1=request.form.get('currency_1')
        my_test_2=request.form.get('currency_2')
        my_test_3=request.form.get('amount')

        print(f'from {my_test_1}')
        print(f'to: {my_test_2}')
        print(f'amount: {my_test_3}')





    return render_template('fx_converter.html')
