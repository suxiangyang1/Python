# 函数和模块化  2020 / 3 / 29

# 引入random  使用random()方法，随机生成一个实数
# random.randint(m.n)代表着产生m到n之间的一个整型随机数

import random


# 生成指定长度的验证码
# :param code_len:验证码的长度（默认4个字符）
# :return: 有大小写英文字母和数字生成的随机验证码

#
# def generate_code(code_len = 4):
#     all_chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOQRSTUVWXYZ'
#     last_pos = len(all_chars) - 1
#     code= ''
#     #  ‘ _’也可以用i.j来表示，只是一个循环标准
#     for _ in range(code_len):
#         index = random.randint(0,last_pos)
#         code += all_chars[index]
#     return code
#
# # 调用上面的函数
#
# code = generate_code(6)
# print(code)


# 判断一组文件中图片的个数

# file_list 代表文件个数
# return 图片文件数量

def img_counts(file_list):
    count = 0
    for file in file_list:
        if file.endswith('png') or file.endswith('jpg') or \
                file.endswith('webp') or file.endswith('bmp'):
            count = count + 1
    return count


# 初始化一组文件
some_list = ['1.jpg', '2.png', '3.wav', '4.bpm']
result = img_counts(some_list)
print('一共有', result, '个文件')
