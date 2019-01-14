import contextlib


@contextlib.contextmanager
def fileopen(filename):
    # 这句话类似  魔法函数  __enter__
    print('file open')
    # yield 返回的 是由with接收的内容
    yield {}
    # 这句话类型  魔法函数  __exit__
    print('file close')


with fileopen('xiaowei.txt') as file:
    # 具体操作

    print('file processing')

