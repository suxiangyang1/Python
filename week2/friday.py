# 输入import this  可以获得很好的东西

"""
集合综合操作
set() 函数创建一个无序不重复元素集
"""

# 创建结合的各种方法
# 字面量语法

set1 = {1, 2, 3, 3, 3, 2}
print(set1)
print('Length=', len(set1))
# 构造器语法
set2 = set(range(1, 10))
set3 = set((1, 2, 3, 3, 2, 1))
print(set2, set3)
# 推到式语法
set4 = {num for num in range(1, 100) if num % 3 == 0 or num % 5 == 0}
print(set4)

# 集合添加删除元素
set1.add(4)
set1.add(5)
set2.update({11, 12})
set2.discard(5)
if 4 in set2:
    set2.remove(4)
print(set1, set2)
print(set3.pop())
print(set3)
