uf = input("Enter the unit you are converting from: ")
ut = input("Enter the unit you are converting to: ")
tu = float(input(f"Enter the temperature in {uf}: "))
ntc = 0
final = 0
if uf == "Fahrenheit":
    ntc = (tu - 32) * 5/9
elif uf == "Kelvin":
    ntc = tu - 273.15
else:
    ntc = tu
if ut == "Fahrenheit":
    final = (ntc * 9/5) + 32
elif ut == "Kelvin":
    final = (ntc + 273.15)
else:
    final = ntc
print(f"That is {final:.1f} degrees {ut}.")