# 什么是迭代协议
# 迭代器是什么?
# 迭代器是访问集合类元素的一种方式, 一般用来遍历数据
# 迭代器和以下标的访问方式不一样
# 迭代器是不能返回的
# 迭代器提供了一种惰性方式，只有在访问数据的时候才去计算数据或者读取数据
# list[0] __getitem__ 实现
# 迭代器用 __item__实现

from collections.abc import Iterable, Iterator

a = [1, 2]
# Iterable 可迭代类型
# Iterator 迭代器类型
print(isinstance(a, Iterable))
print(isinstance(a, Iterator))