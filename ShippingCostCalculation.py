weight = 8.4

# "Ground Shipping""

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

cost_of_ground_shipping = weight * price_per_pound + flat_charge

# "Premium Ground Shipping""
cost_of_premium_ground_shipping = 125.00

print('Cost of ground shipping: $', cost_of_ground_shipping)
print('Cost of premium ground shipping: $', cost_of_premium_ground_shipping)

#  “Drone Shipping”.

weight_for_drone_shipping = 1.99
flat_charge_for_drone_shipping = 0
price_per_pound_for_drone_shipping = 1

if weight_for_drone_shipping <= 2:
    price_per_pound_for_drone_shipping *= 4.50
elif 2 < weight_for_drone_shipping <= 6:
    price_per_pound_for_drone_shipping *= 9.00
elif 6 < weight_for_drone_shipping <= 10:
    price_per_pound_for_drone_shipping *= 12.00
else:
    price_per_pound_for_drone_shipping *= 14.25

cost_of_drone_shipping = weight_for_drone_shipping * price_per_pound_for_drone_shipping + flat_charge_for_drone_shipping

print('Cost of drone shipping: $', cost_of_drone_shipping)
