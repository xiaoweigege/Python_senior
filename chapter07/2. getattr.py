# __getattr__, __getattribute__
# __getattr__ 在查找不到属性的时候使用


class User(object):
    def __init__(self):
        self.name = 'xw'
        self.birthday = '1996-9-2'
        self.info = dict(
            qq=240942649,
            phone=17719302389
        )

    # 找不到属性 进入这个函数
    def __getattr__(self, item):
        data = self.info.get(item)
        if not data is None:
            return data
        return 'get not find {}'.format(item)

    # 不管找不找的到, 无条件进入这个函数
    def __getattribute__(self, item):
        return '哈哈'


if __name__ == '__main__':
    user = User()
    print(user.name)
    # 类中并没有定义age, 类中写了 __getattr__函数, 并没有报错，而是进入了__getattr__ 函数的逻辑当中去
    print(user.age)
    print(user.qq)
