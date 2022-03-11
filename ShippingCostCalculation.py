weight = 1

# Ground Shipping
flat_charge = 20.00
price_per_pound = 1

if weight <= 2:
    price_per_pound *= 1.50
elif 2 < weight <= 6:
    price_per_pound *= 3.00
elif 6 < weight <= 10:
    price_per_pound *= 4.00
else:
    price_per_pound *= 4.75

cost = weight * price_per_pound + flat_charge

print(cost)