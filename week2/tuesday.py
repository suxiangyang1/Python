# 字符串常用方法的练习


def main():
    str1 = 'hello world'
    # 通过内置函数len计算字符串的长度
    print(len(str1))  # 13
    # 获得字符串首字母大写的拷贝
    print(str1.capitalize())
    # 获得字符串每个单词首字母的大写
    print(str1.title())
    # 获得字符串大写后的结果
    print(str1.upper())
    # 从字符串中查找子串所在的位置
    print(str1.find('or'))
    # 检查字符串是否以指定的字符串开头
    print(str1.startswith('he'))
    print(str1.startswith('hel'))
    # 检查字符串是否以指定的字符串结尾
    print(str1.endswith('ld'))
    # 将字符串以指定的宽度居中，并且在两侧填充指定的字符串
    print(str1.center(50, '*'))
    # 将字符串以指定的宽度靠右放置，左侧填充指定的字符
    print(str1.rjust(50, '*'))

    str2 = 'abc123456'
    # 检查字符串是否以数字构成
    print(str2.isdigit())
    # 检查字符串是否以字母构成
    print(str2.isalpha())
    # 检查字符串是否以数字和字母构成
    print(str2.isalnum())

    str3 = 'hell0@126.com'
    print(str3)
    # 获得字符串修剪左右两侧空格之后的拷贝
    print(str3.strip())


if __name__ == '__main__':
    main()
