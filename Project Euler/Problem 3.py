def factor(x):
    temp = []
    for i in range(2, int(x/2)):
        if x % i == 0:
            temp.append(factor(i))
            temp.append(factor(x/i))
            return temp
    return x

num = 0
x = 600851475143
print(factor(x))
