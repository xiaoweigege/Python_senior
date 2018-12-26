# 列表推导式
# 1. 提取出1-20之间的奇数
odd_list = [i for i in range(21) if i % 2 == 1]
print(odd_list)

# 2. 逻辑复杂的情况
# 列表生成式性能高于列表操作
def hadle_item(item):
    return item ** 2


odd_list = [hadle_item(i) for i in range(21) if i % 2 == 1]
print(odd_list)


# 生成器表达式, 将列表推导式 中括号 换成小括号就变成了 生成器
odd_gen = (i for i in range(21) if i % 2 == 1)
print(odd_gen.__next__())


# 字典推导式
odd_dict = {'xw': 22, 'xw1': 23, 'xw2': 24}
reversed_dcit = {v: k for k, v in odd_dict.items()}
print(reversed_dcit)

# 集合推导式
odd_set = {v for v in range(10)}
print(odd_set)