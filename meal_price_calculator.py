child_meal = float(input("What is the price of a child's meal? "))
adult_meal = float(input("What is the price of a adult's meal? "))
children_num = int(input("How many children are there? "))
adults_num = int(input("How many adults are there? "))
sales_tax_rate = float(input("What is the sales tax rate? "))

subtotal = child_meal * children_num + adult_meal * adults_num

print()

print(f"Subtotal: ${subtotal:.2f}")

sales_tax = subtotal * sales_tax_rate / 100
print(f"Sales Tax: ${sales_tax:.2f}")

total = subtotal + sales_tax
print(f"Total: ${total:.2f}")

print()

payment_amount = float(input("What is the payment amount? "))
str(print (f"Change: ${payment_amount - total:.2f}"))

#We can add add an additional feature for tip amount
print()
tip = float(input("How much do you want to tip? "))
str(print (f"Total including tip: ${tip + total:.2f}"))

#And a final message
print()
print("Thanks for choosing us!")


