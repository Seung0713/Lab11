w = input("Enter a word: ")
l = input("Enter the letter to count: ")
num = 0

for i in w:
    if i == l:
        num += 1
print(f"{l} appears {num} times.")