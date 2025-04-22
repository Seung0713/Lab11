s1 = float(input("Side length 1: "))
s2 = float(input("Side length 2: "))
s3 = float(input("Side length 3: "))
if s1 == s2 and s1 == s3:
    print("This is an equilateral triangle!")
elif s1 != s2 and s1 != s3 and s2 != s3:
        print("This is a scalene triangle!")
else:
        print("This is an isosceles triangle!")

