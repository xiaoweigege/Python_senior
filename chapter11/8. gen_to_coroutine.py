# 生成器是可以暂停的函数
# 生成器是有状态的
import inspect


def gen_func():
    yield 1
    return 'xiaowei'


if __name__ == '__main__':
    gen = gen_func()
    state = inspect.getgeneratorstate(gen)
    print(state)
    next(gen)
    state = inspect.getgeneratorstate(gen)
    print(state)
    try:
        next(gen)
    except StopIteration:
        pass
    state = inspect.getgeneratorstate(gen)
    print(state)