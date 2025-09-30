import requests
def convert_currency(amount, from_currency, to_currency):
    """
    Convert amount from one currency to another using an API.
    Uses the exchangerate-api.com free endpoint.
    """
    url = f"https://api.exchangerate-api.com/v4/latest/{from_currency.upper()}"
    try:
        response = requests.get(url)
        data = response.json()
        if "rates" not in data:
            print("Error fetching rates:", data)
            return None
        rates = data["rates"]
        if to_currency.upper() not in rates:
            print(f"Currency {to_currency} not found in rates.")
            return None
        rate = rates[to_currency.upper()]
        converted_amount = amount * rate
        return converted_amount
    except Exception as e:
        print("An error occurred:", e)
        return None

if __name__ == "__main__":
    print("Currency Converter")
    try:
        amount = float(input("Enter amount: "))
        from_currency = input("From currency (e.g. USD): ").strip()
        to_currency = input("To currency (e.g. EUR): ").strip()
        result = convert_currency(amount, from_currency, to_currency)
        if result is not None:
            print(f"{amount} {from_currency.upper()} = {result:.2f} {to_currency.upper()}")
        else:
            print("Conversion failed.")
    except ValueError:
        print("Invalid input. Please enter a valid number for amount.")
