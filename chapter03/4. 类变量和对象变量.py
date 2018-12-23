
class A(object):
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y


a = A(3, 2)
# 解释一下a.aa 这个属性， 首先在当前对象当中查找有没有aa 如果没有 aa 向上查找,  从类对象中查找

# a.aa = 10 在当前变量中 发现没有 则 新建了一个aa 变量  他不会再向上查找 A.aa 还是没有变化
a.aa = 10

print(a.x, a.y, a.aa)
print(A.aa)

# 抛异常
# print(A.x)
