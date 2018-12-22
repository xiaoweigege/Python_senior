
def ask(name='xiaowei'):
    print(name)


class Person(object):
    def __init__(self):
        print('小伟')


def print_type(item):
    print(type(item))


def decorator_func():
    print('dec start')
    return ask


if __name__ == '__main__':
    my_dec = decorator_func()
    my_dec('hahaha')
    # 赋值操作
    # my_fuc = ask
    # my_fuc()
    #
    # my_class = Person
    # my_class()
    #
    # obj_list = list()
    # obj_list.append(ask)
    # obj_list.append(Person)
    # for item in obj_list:
    #     print(item())


