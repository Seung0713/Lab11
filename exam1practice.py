def fourbonacci(n):
    tot = 0
    fir = 1
    sec = 4
    thi = 7
    fou = 8
    if n== 1:
        return fir
    elif n == 2:
        return sec
    elif n == 3:
        return thi
    elif n == 4:
        return fou

    for i in range(5, n + 1):
        tot = (4 * fir) + (3 * sec) + (2 * thi) + (1 * fou)
        fir = sec
        sec = thi
        thi = fou
        fou = tot
    return fou

def odd_squares(num):
    totA = 0
    i = 1
    while totA < num:
        final = i * i
        if final % 2 == 1:
            print(final)
            totA += 1
        i += 1

def diamond(x):
    for i in range(x):
        space_count = abs(i - x // 2)
        for _ in range(space_count):
            print("",end="")
        for j in range(x - space_count * 2):
            print(j+1, end="")
        print()
