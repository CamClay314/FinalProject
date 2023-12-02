
#Input Validation
try:
    price = float(input("How much is the item?: "))
    amount = int(input("Amount Purchasing?: "))
except ValueError:
    print("Invalid input. Please enter a valid numerical value.")
    # Handle this error appropriately (e.g., ask the user to enter the values again)

