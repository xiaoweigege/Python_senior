
# 生成器函数, 只有函数中有yield关键字就是生成器函数


def gen_func():
    yield 1
    yield 2


def func():
    return 1


def fib(index):
    fib_list = [0, 1]
    if index < 2:
        return fib_list
    else:
        for i in range(2, index):
            fib_list.append(fib_list[i-2] + fib_list[i-1])
        return fib_list


def gen_fib(index):
    a, b = 0, 1
    for i in range(index):
        yield a
        a, b = b, a + b


if __name__ == '__main__':
    # 生成器对象, Python编译字节码的时候产生的
    gen = gen_func()
    print(next(gen))
    for v in gen:
        print(v)
    re = func()
    fi = fib(50)
    print(fi)
    fib_gen = gen_fib(50)
    for v in fib_gen:
        print(v)
