def chek(func):
    def wraper(*args):
        name = args[0]
        age = args[1]
        if age < 0: age = 1
        func(name, age)
    return wraper
    
@chek
def welc_win(name, age):
    print(f"your name {name}. Age: {age}")


welc_win("Tom", 28)
welc_win("Bob", -7)