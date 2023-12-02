
#Input Validation
item = input("Name of the item?: ")

while True:
    try:
        price = float(input("How much is the item?: "))
        amount = int(input("Amount Purchasing?: "))
        break  # Break out of the loop if inputs are valid
    except ValueError:
        print("Invalid input. Please enter valid numerical values.")

name_of_customer = input("Name of Purchaser?: ")
address = input("Shipping Address?: ")


#Formatting
print()
print(f"------Billing Info------\n"
      f"\nContact Name: {name_of_customer}\n"
      f"Shipping Address: {address}\n"
      f"Item: {item}\n"
      f"Quantity: {amount}\n")
#using constants
SALES_TAX = 0.042
LIMIT = 100
#Refactoring Functions
def calculate_total_amount(price, amount, sales_tax):
    return (price * amount) * sales_tax + (price * amount)

# ...

totalamount = calculate_total_amount(price, amount, SALES_TAX)
