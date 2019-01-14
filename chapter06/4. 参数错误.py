
def add(a, b):
    a += b
    return a


class Company(object):
    def __init__(self, staffs=[]):
        self.staffs = staffs

    def add(self, name):
        self.staffs.append(name)

    def remove(self, name):
        self.staffs.remove(name)


if __name__ == '__main__':

    # 错误例子
    com1 = Company(['xw1', 'xw2'])
    com1.add('xw3')
    print(com1.staffs)


    # 奇怪了, Company 对象 虽然有默认参数，但是为什么 com2,com3 实例 添加name的时候, 为什么这个list共用了呢
    # 有两个原因引起的
    # 1. 传入了一个list 这是一个可变的对象
    # 2. com2, com3 都没有自己传递list 进去, 而是使用了 默认参数 List
    # com2, com3 公用了同一个 默认的list
    # 由这个__defaults__ 可以看出 这个对象是有一个默认值为list 的
    # 可是为什么com1 没有发生这样的情况呢, 因为com1 自己传递了一个List 进去, 没有使用默认的
    # 记住了, list 这类的 最好不要使用默认的，当多个实例化之后，会共用一个 会造成 混乱

    print(Company.__init__.__defaults__)
    com2 = Company()
    com2.add('com2')
    print(com2.staffs)
    com3 = Company()
    com3.add('com3')
    print(com2.staffs)
    print(com3.staffs)

    # # 数值  在 函数里面 局部变化
    # a = 1
    # b = 2
    # c = add(a, b)
    # print(c)
    # print(a, b)
    #
    # # list a也发生了变化, 因为 list 在函数当中 直接传递的 是内存地址, 而 数值 只是传递的引用
    # # 这样做的原因是因为, 数据较小 复制一份 无妨, list 的话当很大的时候，再复制一份 到函数当中, 将会造成很大的内存空间
    # a = [1, 2]
    # b = [3, 4]
    # c = add(a, b)
    # print(c)
    # print(a, b)


