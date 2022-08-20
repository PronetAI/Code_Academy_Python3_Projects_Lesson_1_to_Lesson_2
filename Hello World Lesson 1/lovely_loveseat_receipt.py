# All of the prices for each of the products
lovely_loveseat_price,stylish_settee_price,luxurious_lamp_price=254.00,180.50,52.15

# Descriptions for each for the products
lovely_loveseat_description="Lovely Loveseat. Tufted polyester blend on wood. 32 inches high x 40 inches wide x 30 inches deep. Red or white."
stylish_settee_description="Stylish Settee. Faux leather on birch. 29.50 inches high x 54.75 inches wide x 28 inches deep. Black."
luxurious_lamp_description="Luxurious Lamp. Glass and iron. 36 inches tall. Brown with cream shade."

# Initializing general variables
sales_tax=0.088
customer_one_total=0
customer_one_itemization=""

# Adding all of the items the user purchased
customer_one_total+=lovely_loveseat_price
customer_one_itemization+="\n"+lovely_loveseat_description
customer_one_total+=stylish_settee_price
customer_one_itemization+="\n\n"+stylish_settee_description
customer_one_total+=luxurious_lamp_price
customer_one_itemization+="\n\n"+luxurious_lamp_description
customer_one_tax=customer_one_total*sales_tax
customer_one_total+=customer_one_tax


# Printing out all the information
print("Customer One Items:")
print(customer_one_itemization + "\n")
print("Customer One Total:")
print("$",customer_one_total)
