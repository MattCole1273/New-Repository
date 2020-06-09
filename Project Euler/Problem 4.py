big = 0
product = 0
for x in range(100,1000):
    for y in range(100,1000):
        product = x * y
        if len(str(product)) == 5:
            if str(product)[0] == str(product)[4] and str(product)[1] == str(product)[3]:
                if big < product:
                    big = product
        if len(str(product)) == 6:
            if str(product)[0] == str(product)[5] and str(product)[1] == str(product)[4] and str(product)[2] == str(product)[3]:
                if big < product:
                    big = product
print(big)
