import xlwt
from xlwt import Workbook

wb = Workbook()

sheet1 = wb.add_sheet('Sheet 1')
#
# p2 = []
# for i in range(1,10):
#     p2.append(11*(i))
#
# p3_11 = []
# p3 = []
# for i in range(100,1000):
#     if(str(i)[0] == str(i)[2]):
#         if(i % 11 == 0):
#             p3_11.append(i)
#         else:
#             p3.append(i)
#
# p4_11 = []
# p4d11 = []
# p4 = []
# for i in range(1000,10000):
#     if(str(i)[0] == str(i)[3] and str(i)[1] == str(i)[2]):
#         if(i % 11 == 0):
#             p4_11.append(i)
#             p4d11.append(int(i/11))
#         else:
#             p4.append(i)
#
# p5_11 = []
# p5d11 = []
# p5 = []
# for i in range(10000,100000):
#     if(str(i)[0] == str(i)[4] and str(i)[1] == str(i)[3]):
#         if(i % 11 == 0):
#             p5_11.append(i)
#             p5d11.append(int(i/11))
#         else:
#             p5.append(i)
#
# p6_11 = []
# p6d11 = []
# p6 = []
# for i in range(100000,1000000):
#     if(str(i)[0] == str(i)[5] and str(i)[1] == str(i)[4] and str(i)[2] == str(i)[3]):
#         if(i % 11 == 0):
#             p6_11.append(i)
#             p6d11.append(int(i/11))
#         else:
#             p6.append(i)

# p7_11 = []
# p7d11 = []
# p7 = []
# for i in range(1000000,10000000):
#     if(str(i)[0] == str(i)[6] and str(i)[1] == str(i)[5] and str(i)[2] == str(i)[4]):
#         if(i % 11 == 0):
#             p7_11.append(i)
#             p7d11.append(int(i/11))
#         else:
#             p7.append(i)

#
# p8_11 = []
# p8d11 = []
# p8 = []
# for i in range(10000000,100000000):
#     if(str(i)[0] == str(i)[7] and str(i)[1] == str(i)[6] and str(i)[2] == str(i)[5] and str(i)[3] == str(i)[4]):
#         if(i % 11 == 0):
#             p8_11.append(i)
#             p8d11.append(int(i/11))
#         else:
#             p8.append(i)


p9_11 = []
p9d11 = []
p9 = []
for i in range(100000000,1000000000):
    if(str(i)[0] == str(i)[8] and str(i)[1] == str(i)[7] and str(i)[2] == str(i)[6] and str(i)[3] == str(i)[5]):
        if(i % 11 == 0):
            p9_11.append(i)
            p9d11.append(int(i/11))
        else:
            p9.append(i)
# print(*p7d11,' ')

# print(*p2, sep=', ')
# print(*p3, sep=', ')
# print(*p3_11, sep=', ')
# print(*p4, sep=', ')
# print(*p4_11, sep=', ')
# print(*p5, sep=', ')
# print(*p5_11, sep=', ')
# print(*p6, sep=', ')
# print(*p6d11, sep=', ')
# print(*p6_11, sep=', ')
# for i in p
#
# for i in range(len(p2)):
#     sheet1.write(int(i/9),i%9,p2[i])
#
# for i in range(len(p3_11)):
#     sheet1.write(int(i/9)+1,(i%9),p3_11[i])

# print(len(p4_11),len(p5_11),len(p6_11))
#
# for i in range(len(p4d11)):
#     sheet1.write(int(i/10),i%10,p4d11[i])
#
# for i in range(len(p4_11)):
#     sheet1.write(int(i/10),(i%10)+11,p4_11[i])
#
# for i in range(len(p5d11)):
#     sheet1.write(int(i/10)+10,i%10,p5d11[i])
#
# for i in range(len(p5_11)):
#     sheet1.write(int(i/10)+10,(i%10)+11,p5_11[i])

# for i in range(len(p7d11)):
#     sheet1.write(int((i+1)/10),((i+1)%10),p7d11[i])

for i in range(len(p8d11)):
    sheet1.write(int((i)/10),((i)%10),p8d11[i])

wb.save('palindrome89.xls')
