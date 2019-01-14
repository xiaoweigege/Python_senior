# try except finally


def exe_try():
    try:
        print('code start')
        raise KeyError
        return 1
    except KeyError:
        print('KeyError')
        return 2
    else:
        print('else err')
        return 3
    finally:
        print('finally')
        return 4


# 上下文管理器协议 with
class Sample(object):
    def __enter__(self):
        # 在此获取资源
        print('enter')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 在此释放资源
        print('exit')

    def do_something(self):
        print('doing something')


if __name__ == '__main__':
    result = exe_try()
    print(result)
    """
    结果居然为4
    为什么不是2 
    因为
    except 捕获了 KeyError 只是将return 2 押进了栈
    到了finally 再将4 押进栈, 最后从栈里面获取返回值, 就是4 
    """

    with Sample() as sample:
        sample.do_something()


