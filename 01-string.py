#  -------------------------------
# 练习一
s = input("输入一串全部小写的英语：")
print("全部转化为大写后：%s\n" % (s.upper()))            # 把所有字符中的小写字母转换成大写字母

s = input("输入一串全部大写的英语：")
print("全部转化为大写后：%s\n" % (s.lower()))            # 把所有字符中的大写字母转换成小写字母

s = input("输入一串全部小写的英语句子：")
print("首字母转化为大写后：%s\n" % (s.capitalize()))     # 把第一个字母转化为大写字母，其余小写

s = input("输入一串全部小写的英语句子（必须带空格）：")
print("每个单词首字母转化为大写后：%s\n" % (s.title()))   # 把每个单词的第一个字母转化为大写，其余小写
