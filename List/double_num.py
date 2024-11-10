def double(num):
    for i in range(len(num)):
        num[i] = num[i] * 2
    return num

num = [1, 2, 3, 4, 5]
print(double(num))