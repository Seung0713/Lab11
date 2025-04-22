bread = int(input("How much money do you have: "))
candy_bars = bread // 4
wrappers = candy_bars
while wrappers >= 3:
    additional_bars = wrappers // 3
    candy_bars += additional_bars
    wrappers = wrappers % 3 + additional_bars

print(f"You can purchase {candy_bars} candy bars!")
