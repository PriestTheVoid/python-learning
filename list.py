nums = [1,2,3,6,45,8,4]

def perebor(list):
    for i in list:
        print(i)

perebor(nums)

nums.append(9)

perebor(nums)