# Python3.3 新加了 yield from语法
from itertools import chain


def g1(iterable):
    yield iterable


def g2(iterable):
    yield from iterable


def my_chain(*args, **kwargs):
    for my_iterable in args:
        yield from my_iterable
        # for vaule in my_iterable:
        #     yield vaule


my_list = [1, 2, 3]
my_dict = {
    'xiaowei1': 'http://www.baidu.com',
    'xiaowei2': 'http//www.xiaoweigege.top'
}
# 例子1
# 3个item 同时循环
# for vaule in my_chain(my_list, my_dict, range(5, 10)):
#     print(vaule)

# 例子2
# yield 拿到什么yield什么
for value in g1(range(1, 10)):
    print(value)

# yield from 如果是可迭代对象, 则一个个yield出去
for value in g2(range(1, 10)):
    print(value)

# 例子3
# 1.mian调用方 g3(委托生成器), gen 子生成器
# 2.yield from 会在调用方与子生成器之间建立一个双向通道


def g3(gen):
    yield from gen


def main():
    g = g3(range(10))
    g.send(None)

main()

