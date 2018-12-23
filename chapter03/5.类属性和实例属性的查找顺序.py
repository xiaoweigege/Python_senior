
class A(object):
    name = 'A'

    def __init__(self):
        self.name = 'obj A'


# 查看顺序 由下而上 先从实例中查找对象, 如果实例中没有此属性 则从 类 中去查找属性, 再没有则抛异常

a = A()
print(a.name)


class D(object):
    pass


class B(D):
    pass


class C(D):
    pass


class A(B, C):
    pass


# mro 查询
# Python 3 采用C3算法来实现
print(A.__mro__)


class D(object):
    pass


class E(object):
    pass


class B(D):
    pass


class C(E):
    pass


class A(B, C):
    pass


print(A.__mro__)
