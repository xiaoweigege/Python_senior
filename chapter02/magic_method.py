
class Nums(object):
    # __abs__

    def __init__(self, number):
        self.num = number

    def __abs__(self):
        return abs(self.num)


num = Nums(-50)
print(abs(num))


class MyVector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        re_vector = MyVector(self.x + other.x, self.y + other.y)
        return re_vector

    def __str__(self):
        return 'x: {}, y: {}'.format(self.x, self.y)


v1 = MyVector(1, 2)
v2 = MyVector(3, 4)
v3 = v1 + v2
print(type(v3))


class MyNumber(object):
    def __init__(self, x):
        self.x = x

    def __add__(self, other):
        return self.x + other.x

    def __int__(self):
        return self.x

    def __str__(self):
        return '{}'.format(self.x)


n1 = MyNumber(1)
n2 = MyNumber(5)
n3 = n1 + n2
print(type(n3))
print(n3)
