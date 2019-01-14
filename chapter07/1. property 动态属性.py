from datetime import datetime, date


class User(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    # property 可以将方法 变成 属性
    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value


if __name__ == '__main__':
    user = User('汪伟', date(1996, 9, 2))
    user.age = 18
    print(user._age)
    print(user.age)
