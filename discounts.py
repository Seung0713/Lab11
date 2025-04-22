price = float(input("Enter the price: "))

bf = input("Is it black friday [y/n]: ")

if bf == "y":
    price *= .60

discount = input("Do you have a coupon [y/n]: ")

if discount == "y":
    price *= .95

ed = input("Do you have an employee discount [y/n]: ")

if ed == "y":
    price *= .80

print(f"The final price is: ${price:.2f}")