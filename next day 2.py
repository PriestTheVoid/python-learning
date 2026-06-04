p = 12345
l = "user"

pas = int(input("введите пароль: "))
log = input("введите логин: ")


while pas != p or log != l:

    print("неверный логин или пароль.")

    pas = int(input("введите пароль: "))
    log = input("введите логин: ")

    if pas == p and log == l:
        print("доступ разрешён.")
        break