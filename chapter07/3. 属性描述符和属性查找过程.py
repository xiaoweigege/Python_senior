import numbers
from datetime import datetime


class IntField(object):
    value = None

    def __set__(self, instance, value):
        if not isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        if value < 0:
            raise ValueError('positive value need')
        self.value = value

    def __get__(self, instance, owner):
        return self.value

    def __delete__(self, instance):
        del self.value


class User(object):
    age = IntField()


if __name__ == '__main__':
    user = User()
    user.age = 1
    print(user.age)
    print(user.__dict__)
    print(User.__dict__)

"""
    如果user是某个类的实例, 那么user.age(以及等价的getarrt(user, 'age'))
    首先调用__getattribute__ 如果类定义了__getattr__方法, 那么在__getattribute__抛出
    AttributeError 的时候就会调用__getattr__, 而对于描述符(__get__) 的调用,则发生在__getattribute__内部的
    user = User(), 那么User.age 顺序如下:
    1. 如果'age' 是出现在User或其基类的__dict__中, 且age是data descriptor(属性描述符),那么调用其 __get__
    2. 如果'age' 是出现在obj的 __dict__ 中, 那么直接返回obj.__dict__['age']
    3. 如果'age' 是出现在User或其基类的__dict__中
        3.1 如果age是non-data descriptor, 那么调用其__get__方法
        3.2 否则返回 __dict__['age']
    4. 如果User有__getattr__方法, 调用__getattr__方法,否则抛出AttributeError
    
    注: 当类中定义了 __get__ __set__ __delete__ 则此对象为属性描述符
"""