# 斐波那契数列的前20各数  (也可以使用for循环)

# first = 1
# second = 1
# last = 0
# count=1
# all = 20
# while count <= all:
#     first = second
#     second = last
#     last = first + second
#     count = count + 1
#     print('%d' %last)


# 输出100以内所有的素数


i = 2
print('100以内的所有素数')
for num in range(2, 100):
    for i in range(2, num):
        if num % i == 0:
            break
        else:
            i = i+1
    if i >= num:
        print(num, ' ', end='')
print()
