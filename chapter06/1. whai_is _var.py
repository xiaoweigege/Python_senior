# Python 和 Java 中的变量本质不一样, Python的变量实质上是一个指针 int str

# a 指向 1 这个内存地址
a = 1
print(id(a))
# a 指向 abc 的内存地址
a = 'abc'
print(id(a))

# b 指向 [1, 2, 3]
b = [1, 2, 3]
# 将b 赋值给 c  c 同时也指向 [1, 2, 3]
c = b
c.append(4)
print(id(b))
print(id(c))