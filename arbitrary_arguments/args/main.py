def calculate_total(*values):
    if not values :
        return "Your cart is empty."
    total = 0
    for value in values:
        total += value

    if total >= 200:
        total *= 0.80  # 20% discount
    elif total >= 100 :
        total *= 0.90  # 10% discount

    return f"Final total: ${total:.2f}"

# Testing the result
print(calculate_total(30, 20, 50))
print(calculate_total(100, 50, 80))
print(calculate_total(150, 100))
print(calculate_total())