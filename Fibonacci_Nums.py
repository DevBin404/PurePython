# #FIRST NUMBERS
# b = [1, 2]
# while b[-1]<4000000:
#     c = b[-2]+b[-1]
#     b.append(c)
# #FIBONATCCI NUMBERS
# b.pop(-1)
# d = list(filter(lambda x: x % 2 == 0, b))
# print(d)
# a = sum(d)
# print(a)


def Fibo(max):
    nums = []
    a, b = 0, 1
    while max > len(nums):
        nums.append(b)
        a, b = b, a+b
    return nums


print(Fibo(10000000))
