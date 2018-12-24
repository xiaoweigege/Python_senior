# 自省是通过一定机制查询对象的内部结构


class Person(object):
    name = 'User'


class Student(Person):
    def __init__(self, school_name):
        self.school_name = school_name

    def get(self):
        return 'qwe'


if __name__ == '__main__':
    user = Student('北京大学')
    user.__dict__['scholl_addr'] = '北京市'
    print(user.__dict__)
    print(Student.__dict__)
    print(user.name)
    print(dir(user))
