a = input("введите ваше имя: ").lower()

def name(a):

    if a == "oracle" or "priestess":
        print(f"Glad to see you... {a}")

    else:
        print(f"Welcome back, {a}")

name(a)