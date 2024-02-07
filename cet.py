import requests

API_KEY = 'your_api_key_here'
BASE_CURRENCY = 'USD'

def get_exchange_rate(base_currency, target_currency):
    url = f'https://api.exchangeratesapi.io/latest?access_key={API_KEY}&base={base_currency}'
    response = requests.get(url)
    data = response.json()
    if target_currency in data['rates']:
        return data['rates'][target_currency]
    else:
        return None

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None
