a = 1
b = 'str'
print(type(a))
print(type(int))
print(type(b))
print(type(str))

# 关系为  type 对象生成 int , int对象生成 1
# type -> class -> object
# object 是顶层基类
# type 也是一个类 同时type 也是一个


class Student(object):
    pass


stu = Student()
print(type(stu))
print(type(Student))
print(Student.__bases__)

# type object
print('-------')
print(type.__bases__)
print(object.__bases__)
print(type(object))

# 由此可以看出 type 继承自 object , object 实例化之后是type
# Python 中所有对象都是由type 创建出来的
