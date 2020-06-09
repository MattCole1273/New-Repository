count = 3
num = 5
while count != 10001:
    num += 1
    for x in range(2,num):
        if num/x < x:
            count += 1
            break
        if num % x == 0:
            break

print(num)
