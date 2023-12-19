from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

# Note: Update the access_key with your own key
url = 'http://api.exchangerate.host/live?access_key=ffb1f0efc7a9f09199444f042cd50fd5'

def get_exchange_rate(from_currency, to_currency):
    response = requests.get(url)
    data = response.json()

    if 'error' in data:
        return None

    quotes = data.get('quotes', {})
    rate_key = f"{from_currency}{to_currency}"

    if rate_key in quotes:
        return quotes[rate_key]
    else:
        return None

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        from_currency = request.form['from_currency'].upper()
        to_currency = request.form['to_currency'].upper()
        amount = float(request.form['amount'])

        exchange_rate = get_exchange_rate(from_currency, to_currency)

        if exchange_rate is not None:
            converted_amount = round(amount * exchange_rate, 2)
            return jsonify({'result': f'{amount} {from_currency} is equal to {converted_amount} {to_currency}'})

        error_message = f'Invalid currency code or exchange rate unavailable for {from_currency} to {to_currency}'
        print(error_message)
        return jsonify({'error': error_message}), 400

    return render_template('index.html', result=None)

if __name__ == '__main__':
    app.run(debug=True)
