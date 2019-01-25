# PEP380
# result = yield from EXPR 可以简化成下面这样
# 说明:
# _i: 子生成器, 同时也是一个迭代器
# _y: 子生成器生成的值
# _r: yield from 表达式最终的值
# _s: 调用方通过send()发送的值
# _e: 异常对象

EXPR = list()

# 简易版本yield from
def yield_from(EXPR):
    # EXPR 是一个可迭代对象, _i其实是一个子生成器
    _i = iter(EXPR)
    try:
        # 预激子生成器, 把产生的第一个值存在_y中
        _y = next(_i)
    except StopIteration as _e:
        # 如果抛出异常, 那么就将异常对象value取出
        _r = _e.value
    else:
        # 尝试执行这个循环, 委托生成器会阻塞
        while True:
            # 生产子生成器的值, 等待调用方send()值,发送过来的值保存到_s
            _s = yield _y
            try:
                # 转发_s 并尝试向下执行
                _y = _i.send(_s)
            except StopIteration as e:
                # 如果子生成器抛出异常, 那么就获取异常对象
                _r = e.value
                break
    # _r 就是整个表达式的值
    result = _r
    return result


# 1. 子生成器可能只是一个迭代器, 并不是一个作为协程的生成器, 所以它不支持.throw() 和 .close()方法
# 2. 如果子生成器支持.throw() .close()方法, 但是在子生成器内部, 这两个方法都会抛异常
# 3. 调用方让子生成器自己抛出异常
# 4. 当调用方next()或者send(None)时, 都要在子生成器上调用next()函数,当调用方使用send()发送非None值时, 才调用子生成器send()方法
import sys
# 完整版本yield from
def yield_from(EXPR):
    _i = iter(EXPR)
    try:
        _y = next(_i)
    except StopIteration as _e:
        _r = _e.value
    else:
        while True:
            try:
                _s = yield _y
            except GeneratorExit as _e:
                try:
                    _m = _i.close
                except AttributeError:
                    pass
                else:
                    _m()
                raise _e
            except BaseException as _e:
                _x = sys.exc_info()
                try:
                    _m = _i.throw
                except AttributeError:
                    raise _e
                else:
                    try:
                        _y = _m(*_x)
                    except StopIteration as _e:
                        _r = _e.value
                        break
            else:
                try:
                    if _s is None:
                        _y = next(_i)
                    else:
                        _y = _i.send(_s)
                except StopIteration as _e:
                    _r = _e.value
                    break

    result = _r
    return result

# 总结关键点
# 1. 子生成器生产的值, 都是直接传给调用方的; 调用方通过send()发送的值都是直接传递给子生成器的; 如果发送的是None
#    会调用子生成器的__next__()方法, 如果不是None, 会调用子生成器的send()方法
# 2. 子生成器退出的时候, 最后的return EXPR, 会触发一个StopIteration(EXPR)异常
# 3. yield from 表达式的值, 是子生成器终止时, 传递给StopIteration异常的第一个参数
# 4. 如果调用的时候出现StopIteration异常, 委托生成器会恢复运行, 同时其他的异常会向上'冒泡'
# 5. 传入委托生成器的异常里, 除了GeneratorExit之外,其他的所有异常全部传递给子生成器的.throw()方法;如果调用throw()
#    的时候出现了StopIteration异常, 那么就恢复委托生成器的运行,其他的异常全部向上'冒泡'
# 6. 如果在委托生成器上调用.close()或传入GeneratorExit异常, 会调用子生成器的close()方法, 没有的话就不调用
#    如果在调用close()的时候抛出异常, 那么就向上'冒泡',否则的话委托生成器会抛出GeneratorExit异常
