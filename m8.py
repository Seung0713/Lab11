def flatten(nested_list):
    flat_list = []
    for item in nested_list:
        if isinstance(item, list):
            flat_list.extend(flatten(item))
        else:
            flat_list.append(item)
    return flat_list

def mystery1(n):
    a, b, c, d, e = 1, 2, 3, 4, 5
    while n > 0:
        a, b, c, d, e = b, c, d, e, a - c + e
        n -= 1
    return a

def mystery2(number):
    if number == 0:
        return 0
    else:
        return number % 10 + mystery2(number // 10)

def collatz_sequence(n):
    while n != 1:
        print(n, end=" ")
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    print("1 ")