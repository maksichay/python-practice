import requests

response = requests.get("https://api.exchangerate-api.com/v4/latest/USD")
data = response.json()

def get_amount():
    while True:
        user_input = input("Введите сумму: ")
        try:
            amount = float(user_input)
            if amount <= 0:
                print("Сумма должна быть положительной!")
            else:
                return amount
        except ValueError:
            print("Это не число! Введите снова.")

def convert_to_usd(amount, currency_code):
    rate = data["rates"][currency_code]
    return round(amount / rate, 2)

def main():
    print("=== Конвертер в USD ===")
    currency = input("Выберите валюту (RUB, BYN, KZT): ").upper()

    if currency not in ("RUB", "BYN", "KZT"):
        print("Такой валюты нет!")
        return

    amount = get_amount()
    result = convert_to_usd(amount, currency)
    print(f"{amount} {currency} = {result} USD")

main()