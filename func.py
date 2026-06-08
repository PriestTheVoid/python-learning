def test(a):
    if a <= 0:
        print("начали!")
        return
    else:
        print(a)
        return test(a-1)
    
test(3)