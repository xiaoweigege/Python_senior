from collections.abc import Sized

# 我们去检查某个类是否有某种方法


class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)


com = Company(['xiaowei', 'gege'])
print(len(com))

# hasattr 查询 类中 是否有这个属性
print(hasattr(com, '__len__'))
# 我们在某种情况下希望判定某个对象的类型
print(isinstance(com, int))
print(isinstance(com, Sized))

# 我们需要强制某个子类必须实现某些方法
# 实现了一个web框架，继承cache(redis, cache, memeorychache)
# 我们需要设计一个抽象基类, 指定子类必须实现某些方法
# 如何去模拟一个抽象基类
# 下面方式的缺点是 只有用到这个方法的时候 如果没有重写 则会 报异常


class CacheBase(object):
    """
    缓存基类
    """
    def get(self, key):

        raise NotImplementedError

    def set(self, key, value):
        raise NotImplementedError


class RedisCache(CacheBase):
    def get(self, key):
        pass

    def set(self, key, value):
        print(key, value)


redis = RedisCache()
redis.set('k', 'v')


import abc

# 这种情况之下 如果子类没有定义父类的方法 则会报错
# TypeError: Can't instantiate abstract class RedisCache with abstract methods get, set
# 在实例化 子类的 时候就报错了,我们必须要重新实现 get set 方法


class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key, value):
        pass


class RedisCache(CacheBase):
    pass


redis = RedisCache()
redis.get('')