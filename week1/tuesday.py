"""
列表排序
Date: 2020/ 4 / 10
"""

list1 = ['orange', 'apple', 'zoo', 'interenationalization', 'blueberry']
list2 = sorted(list1)
# sorted的函数返回列表排序后的拷贝不会修改传入的列表
list3 = sorted(list1, reverse=True)
# 通过key关键字参数指定根据字符串长度进行排序而不是默认的字母表排序
list4 = sorted(list1, key=len)
print(list1)
print(list2)
print(list3)
print(list4)
# 给列表对象发出排序消息直接在列表对象上进行排序
list1.sort(reverse=True)
print(list1)


"""
列表切片
"""

fruits = ['grape', 'apple', 'strawberry', 'waxberry']
fruits += ['pitaya', 'pear', 'mango']
# 列表切片
fruits2 = fruits[1:4]  # ['apple' , 'strawberry' , 'waxberry']
print(fruits2)
# 通过完整切片来复制列表
# ['grape' , 'apple' , 'strawberry' , 'waxberry' ,'pear' , 'mango']
fruits3 = fruits[:]
print(fruits3)
fruits4 = fruits[-3:-1]  # ['pitaya' , 'pear']
print(fruits4)
# 可以通过反向切片操作来获得倒转后的列表的拷贝
# ['mango', 'pear', 'pitaya', 'waxberry', 'strawberry', 'apple', 'grape']
fruits5 = fruits[::-1]
print(fruits5)
