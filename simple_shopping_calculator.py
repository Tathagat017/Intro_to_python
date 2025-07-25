price1 = input("Enter the price of the first item: ")
quantity1 = input("Enter the quantity of the first item: ")
price2 = input("Enter the price of the second item: ")
quantity2 = input("Enter the quantity of the second item: ")
price3 = input("Enter the price of the third item: ")
quantity3 = input("Enter the quantity of the third item: ")
total_cost = (float(price1) * float(quantity1) +
              float(price2) * float(quantity2) +
              float(price3) * float(quantity3))
tax = total_cost * 0.085
print(f"Subtotal: {total_cost:.2f}")
print(f"Tax (8.5%): {tax:.2f}")
print(f"Total cost: {total_cost+(tax):.2f}")