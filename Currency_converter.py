def usd_to_ngn(amount):
    exchange_rate = 1500  # example rate
    return amount * exchange_rate

usd = float(input("Enter amount in USD: "))
ngn = usd_to_ngn(usd)

print("Amount in NGN:", ngn)
