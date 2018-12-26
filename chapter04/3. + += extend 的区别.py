a = [1, 2]
b = a + [3, 4]
# 这种类型不同会报错 can only concatenate list (not "tuple") to list
# b = a + (3, 4)
print(b)
# 而 += 不会报TypeError, += 接收任意序列类型 其实 += 最终调用的是extend方法, 最终去 for 循环迭代 append 进去
a += (3, 4)
print(a)

a.extend(range(6))
print(a)
