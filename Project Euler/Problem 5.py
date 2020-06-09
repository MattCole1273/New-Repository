num = 0
count = 2520
while num == 0:
    count += 20
    for x in range(1,21):
        if count % x == 0:
            if x == 20:
                num = count
        else:
            break
print(num)
