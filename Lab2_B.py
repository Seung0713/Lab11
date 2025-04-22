income = float(input("Enter your total income this year: "))
taxes = 0
if income > 609351:
    taxes += (income - 609350) * 0.37
    income = 609350
if income > 243726:
    taxes += (income - 243725) * 0.35
    income = 243725
if income > 191951:
    taxes += (income - 191950) * 0.32
    income = 191950
if income > 100526:
    taxes += (income - 100525) * 0.24
    income = 100525
if income > 47151:
    taxes += (income - 47150) * 0.22
    income = 47150
if income > 11601:
    taxes += (income - 11600) * 0.12
    income = 11600
if income > 0:
    taxes += (income - 0) * 0.10
    income -= 0
print(f"You owe ${taxes:.2f} this year.")