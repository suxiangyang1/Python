# 循环结构


# for in 循环

import random
sum = 0
for x in range(1, 101, 2):    # range第三个参数表示每次递增的值
    print(x)
    sum += x
print(sum)

# while循环
# 猜数字游戏


answers = random.randint(1, 101)
counter = 0

while True:
    counter += 1
    number = int(input("请输入一个1至100之间的数字： "))
    if number > answers:
        print("大了一点 ")
    elif number < answers:
        print("小了一点 ")
    else:
        print("你猜对了")
        break    # 可以提前终止循环，但是只能终止当前循环;还有一个循环是continue
print("你一共猜了%d次" % counter)
if counter > 7:
    print("你的智商不在线呀，继续加油")


# 输入九九乘法表

for i in range(1, 10):
    for j in range(1, i + 1):
        print('%d * %d = %d' % (i, j, i * j), end='\t')
    print()


# 计算两个数的最小公倍数和最大公因数

x = int(input("请输入第一个整数： "))
y = int(input("请输入第二个个整数： "))

if x > y:
    x, y = y, x
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d之间的最大公因数是%d' % (x, y, factor))
        print('%d和%d之间的最小公倍数是%d' % (x, y, x * y // factor))
        break
