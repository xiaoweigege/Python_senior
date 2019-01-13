from collections.abc import Iterator


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __iter__(self):
        return MyIterator(self.employee)

    # def __getitem__(self, item):
    #     return self.employee[item]

    def __len__(self):
        return len(self.employee)


class MyIterator(object):

    def __init__(self, employee_list):
        self.employee = employee_list
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        # 真正返回迭代值的逻辑
        try:
            word = self.employee[self.index]
        except IndexError:
            raise StopIteration
        self.index += 1
        return word


if __name__ == '__main__':
    company = Company(['xiaowei', 'qq'])
    # print(company[1])
    # 为什么 Company 没有定义 __iter__ 还能迭代呢 因为很只能 先去查找有没有定义 __iter__ 没有的话 去找__getitem__

    companyx = iter(company)
    while True:
        try:
            print(next(companyx))
        except StopIteration:
            break

    # 其实可迭代对象并不是要实现__getitem__
    # 而是在for的过程中 他会这么调用 iter(company), iter 函数会去查找__iter__函数,如果找不到 再去找__getitem__
    for item in company:
        print(item)

    # my_iteror = MyIterator(['qwer', '1', '2'])
    # print(next(my_iteror))