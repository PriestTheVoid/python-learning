def deco(func):
    def wraper(*args):
        res = func(*args)
        if res < 0: res = 1
        return res
    return wraper

def test(func):
    def wraper(*args):
        wrap = func(*args)
        print("************************")
        print(wrap)
        print("************************")
    return wraper

@test
@deco

def multiply(a, b):
    return a * b

multiply(5,3)
multiply(5,-3)