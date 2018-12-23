
class A(object):
    pass


class B(A):
    pass


b = B()

# isinstance 能检测是继承过来的
print(isinstance(b, A))

# type 检测不出
print(type(b) == A)
print(type(b) is A)

