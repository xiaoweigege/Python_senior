
class A(object):
    def __init__(self):
        print('A')

    def get(self):
        print('A_ get')


class B(A):
    def __init__(self):
        super().__init__()
        print('B')

    def get(self):
        # super() 用来调用父类的方法, 假设我在子类从重写了父类的方法, 但是我还是想要调用父类的方法, 就可以用super()
        super().get()
        print('B_ get')
        super().get()


# 下面例子 解释是否是调用父类的构造函数
class A(object):
    def __init__(self):
        print('A')


class B(A):
    def __init__(self):
        print('B')
        super().__init__()


class C(A):
    def __init__(self):
        print('C')
        super().__init__()


class D(B, C):
    def __init__(self):
        print('D')
        super().__init__()

"""
这次执行结果为
D
B
C
A
到了B 之后 不是去调用A 了 而是去调用C 由此看出 并是不直接调用父类
而是MRO的顺序来调用的
"""


if __name__ == '__main__':
    # b = B()
    # b.get()
    d = D()
    print(D.__mro__)