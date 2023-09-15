from flask import Flask, render_template, jsonify, request
import requests

app = Flask(__name__)


def get_currencies(source):
    url = source
    response = requests.get(url)

    return response.json()

@app.route("/")
def index():
    currencies = [cur for cur in get_currencies('https://www.cbr-xml-daily.ru/daily_json.js')['Valute'].keys()]

    return render_template('index.html', currencies=currencies)

@app.route('/api/rates', methods=['GET'])
def get_rates():
    currencies = get_currencies('https://www.cbr-xml-daily.ru/daily_json.js')
    first_cur = request.args.get('from')
    second_cur = request.args.get('to')
    value = int(request.args.get('value'))
    if first_cur == 'RUB' and second_cur == 'RUB':
        return jsonify(
            {
                'result': value
            }
        )
    elif first_cur == 'RUB':
        return jsonify(
            {
                'result': round(
                    value / (currencies['Valute'][second_cur]['Value']
                             / currencies['Valute'][second_cur]['Nominal']), 4
                )
            }
        )
    elif second_cur == 'RUB':
        return jsonify(
            {
                'result': round(
                    value * currencies['Valute'][first_cur]['Value']
                    / currencies['Valute'][first_cur]['Nominal'], 4
                )
            }
        )
    value = (value * (currencies['Valute'][first_cur]['Value'] / currencies['Valute'][first_cur]['Nominal'])
             / (currencies['Valute'][second_cur]['Value'] / currencies['Valute'][second_cur]['Nominal']))

    return jsonify(
        {
            'result': round(value, 4)
        }
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
