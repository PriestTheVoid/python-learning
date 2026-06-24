def deco(func):
    def wraper(*args):
        print("____________________________")
        print("welcome")
        func(*args)
        print("you was autorize in system")
    return wraper

@deco
def info(name, age):
    print(f"{name}, your age {age}")

info("Bob", 24)
info("Tom", 43)