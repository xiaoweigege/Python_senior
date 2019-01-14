
# 类也是对象, type 创建类的类

# 函数式动态创建类


def create_class(name):
    if name == 'user':
        class User(object):
            def __str__(self):
                return 'User'

        return User
    elif name == 'company':
        class Company(object):
            def __str__(self):
                return '小伟科技工作室'
        return Company


# type 动态创建类
# name 类名, bases(继承类), dict(属性)


def say(self):
    return 'hello world'


class BaseClass(object):
    @staticmethod
    def answer():
        return 'My nams is BaseClass'


User = type('User', (BaseClass, ), {'name': 'user', '__str__': say})

# 什么是元类？
# 元类是创建类的类
# 对象 <- class(对象) <- type


class MetaClass(type):
    """
    这是一个元类, 因为他继承type
    """
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)


class User(metaclass=MetaClass):

    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'User'

# Python 中类的实例化过程, 他会首先寻找metaclass这个属性,如果找到了就会去调用自己定义的metaclass
# 通过metaclass 去创建User类, 如果User 继承一个类, 他会向上寻找, 如果一直找不到, 他就会调用内置的type去创建
# 如果不用metaclass 直接重写__new__ 是覆盖__new__方法, 用元类的话 可以用一个类来控制类的生成过程
# 这样就是将User 生成对象的过程委托 MetaClass 来做了


if __name__ == '__main__':
    # 动态创建类 , 不灵活
    # my_class = create_class('user')
    # print(my_class())
    my_obj = User('小伟')
    print(my_obj)
    # print(my_obj.name)
    # print(my_obj.answer())



