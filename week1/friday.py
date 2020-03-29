# 输入一个整数判断它是不是素数(除了1和自身，其他都不能被整除的自然数/不包括1/)


# start: 计数从 start 开始。默认是从 0 开始。例如range（5）等价于range（0， 5）;
# stop: 计数到 stop 结束，但不包括 stop。例如：range（0， 5） 是[0, 1, 2, 3, 4]没有5
# step：步长，默认为1。例如：range（0， 5） 等价于 range(0, 5, 1)


# 引入math
from math import sqrt

num = int(input("请输入一个整数: "))
end = int(sqrt(num))
is_prime = True

# 为什么可以求出素数
# 原因：range(2,end+1)中的值可以组成[2,num(或num-1或者其他的））之间所有的非素数
# 例子：num = 8 ,range(2,end+1)={2，3}所有可以组成{2，4，6，8，9}，用8除与{2,3}可以看作用8除以{2，4，6，8，9}【如果除以
# {2，4，6，8，9}中的一个余数为0，那必定也是能整除{2,3}，另外到9之后就不能整除。】
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)


# 输入两个正整数计算他们的最大公约数和最小公倍数

x = int(input('x= '))
y = int(input('y= '))

# 如果x大于交换他们的值
if x > y:
    # 通过下面的的操作，转换x，y的值
    x, y = y, x
# 从两个数中较小的数做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and \
            y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x*y // factor))
        break
