# 打印杨辉三角

# 例子
# 1
# 1 2 1
# 1 3 3 1


# def main():
#     num = int(input('Number of rows: '))
#     # 初始化一个二维数组，例如num=3,得到[[],[],[]]
#     yh = [[]] * num
#     for row in range(len(yh)):
#         # [None]代表初始化一个空的数组
#         yh[row] = [None] * (row + 1)
#         for col in range(len(yh[row])):
#             if col == 0 or col == row:
#                 yh[row][col] =1
#             else:
#                 yh[row][col] = yh[row-1][col] + yh[row-1][col-1]
#             #     如果打印结束换行
#             print(yh[row][col],end='\t')
#         print()
#
#
# if __name__ == '__main__':
#     main()


# 跑马灯文字

# 引入时间模块 , 还要os模块来处理文件和目录
import os
import time
# 引入彩色模块
from termcolor import colored


def main():
    content = 'Coding应当是一生的事业，而不仅仅是20岁的青春'
    color = ['grey', 'red', 'green', 'yellow', 'blue']
    i = 0
    while True:
        # 清理屏幕上的输出
        os.system('cls')
        index = i % len(color)
        print()
        print(colored(content, color[index]))
        # 休眠1000毫秒
        time.sleep(1)
        content = content[1:] + content[0]


if __name__ == '__main__':
    main()
