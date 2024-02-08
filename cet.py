BASE_CURRENCY = 'USD'       
TARGET_CURRENCY = 'EUR'     
FIXED_EXCHANGE_RATE = 1.08  # Fixed exchange rate as of (February 2024 )

def get_exchange_rate(base_currency, target_currency):
    if base_currency == BASE_CURRENCY and target_currency == TARGET_CURRENCY:
        return FIXED_EXCHANGE_RATE
    else:
        raise ValueError(f"Unsupported currency pair: {base_currency} to {target_currency}")

def convert_currency(amount, base_currency, target_currency):
    exchange_rate = get_exchange_rate(base_currency, target_currency)
    if exchange_rate is not None:
        converted_amount = amount * exchange_rate
        return converted_amount
    else:
        return None

# Usage:
amount_to_convert = 100  # Enter amount, 100 is example.
converted_amount = convert_currency(amount_to_convert, BASE_CURRENCY, TARGET_CURRENCY)
if converted_amount is not None:
    print(f"{amount_to_convert} {BASE_CURRENCY} is equal to {converted_amount:.2f} {TARGET_CURRENCY}")
else:
    print("Conversion failed.")
