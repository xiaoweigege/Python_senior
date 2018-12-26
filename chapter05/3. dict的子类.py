
# 不建议继承list和dict


class MyDict(dict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value * 2)


my_dict = MyDict()
my_dict['one'] = 2
print(my_dict)


from collections import UserDict


class MyDict(UserDict):
    def __setitem__(self, key, value):
        super().__setitem__(key, value ** 2)


my_dict = MyDict(one=1)
print(my_dict)