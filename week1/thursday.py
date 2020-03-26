# else / if / elif  的小练习


# 练习 英制单位与公制单位厘米互换

value = float(input("请输入长度： "))
unit = input("请输入单位：")
if unit == 'in' or \
        unit == '英寸':
    print('%f英寸 = %f厘米' % (value, value * 2.54))
elif unit == 'cm' or \
        unit == '厘米':
    print('%f厘米 = %f英寸' % (value, value / 2.54))
else:
    print('请输入有效的单位')


# 百分制成绩转化为等级制成绩
# (目的：成绩 >= 90 输出A；成绩 在80至90[不包括90]输出B；依次轮流 ......)

score = float(input("请输入成绩："))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print("等级： " + grade)


# 输入三条边 ，如果能构成三角形就计算周长和面积

a = float(input("请输入第一条边： "))
b = float(input("请输入第二条边： "))
c = float(input("请输入第三条边： "))

if a+b > c and \
    a+c > b and \
        b+c > a:
    print('周长: %f' % (a+b+c))
    # 海伦公式
    p = (a+b+c) / 2
    area = (p * (p-a) * (p-b) * (p-c)) ** 0.5
    print('面积：%f' % (area))
else:
    print("不能构成三角形")
