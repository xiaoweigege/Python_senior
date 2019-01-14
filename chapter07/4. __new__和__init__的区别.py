
class User(object):
    def __new__(cls, *args, **kwargs):
        # 类生成的过程
        # __new__ 是用来控制对象的生成过程, 在对象生成之前
        print(' __new__')
        return super().__new__(cls)

    def __init__(self):
        # __init__ 是用来完善对象的
        print('__init__')
        pass

# __new__ 是用来控制对象的生成过程, 在对象生成之前
# __init__ 是用来完善对象的
# 如果__new__方法不返回对象, 则不会调用__init__函数


if __name__ == '__main__':
    user = User()
