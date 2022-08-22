weight=1.5
premium_charge=125
ground_cost=0
drone_cost=0
# Ground Shipping 
if weight <= 2:
  ground_cost=((weight*1.50)+20)
elif weight <= 6:
  ground_cost=((weight*3)+20)
elif weight <= 10:
  ground_cost=((weight*4)+20)
else:
  ground_cost=((weight*4.75)+20)
print("With standard ground shipping",weight,"will cost $",ground_cost)
print("Premium Ground Shipping is: $",premium_charge)

# Drone Shipping
if weight <= 2:
  drone_cost=(weight*4.50)
elif weight <= 6:
  drone_cost=(weight*9)
elif weight <= 10:
  drone_cost=(weight*12)
else:
  drone_cost=(weight*14.25)
print("With premium drone shipping",weight,"will cost $",drone_cost)
