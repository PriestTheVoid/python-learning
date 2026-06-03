a = None

while a != 99:

    a = int(input("Введите число: "))

    if a > 0:
        print("число положжительное")
    elif a == 0:
        print("число равняется нулю")
    else:
        print("число отрицательное")