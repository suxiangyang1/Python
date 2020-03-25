# 语言基础 Day1(2020 / 3 / 25)

import math

# 将华氏温度转化位摄氏温度
# 公式：C = （F - 32）/ 1.8
f = float(input("请输入华氏温度:  "))
c = (f - 32) / 18
print('%.1f华氏度 = %.1f摄氏度' % (f, c))

# 计算圆的周长和面积
r = float(input("请输入半径： "))
perimeter = 2 * math.pi * r
area = math.pi * r * r
print('周长：%.2f' % perimeter)
print('面积：%.2f' % area)

# 判断一个年份是否位瑞年
year = int(input("请输入年份："))
is_leap = (year % 4 == 0 and year % 100 != 0) or \
    year % 400 == 0
print(is_leap)
