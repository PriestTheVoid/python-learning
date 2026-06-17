"""
year = int(input("введите год: "))

if year % 4 == 0:
    print("это весокосный год")
else:
    if year % 100 == 0 and year % 400 == 0:
        print("это весокосный год")
    else:
        print("это не весокосный год")
"""

a = int(input("введите первое число:"))
b = int(input("введите второе число:"))

if a > b:
    print(f"наибольшее число {a}")

elif a == b:
    print("оба числа равны")

else:
    print(f"наибольшее число {b}")
