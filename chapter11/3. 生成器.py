# 传统函数调用 A->B->C
# 我们需要一个可以暂停的函数,并且可以在适当的时候恢复该函数继续执行
# 所以出现了协程-> 有多个入口函数, 或者叫 可以暂停的函数(可以向暂停的地方传入值)


# 1. 生成器不仅可以产出值, 还可以接受值
# 2. 启动生成器方式有两种, next(), send()
# 3. throw close 报异常

# 上方3个点,能基本完成协程的需求

def gen_func():
    # 这段代码 可以产出值, 可以接受值(调用方传递进来的值)
    html = yield 'http://www.baidu.com'
    print(html)
    yield 2
    yield 3


if __name__ == '__main__':
    gen = gen_func()
    # 在调用send发送非None值之前, 我们必须启动一次生成器, 方式有两种, next send(None)
    # url = next(gen)
    url = gen.send(None)
    print(url)
    # 关闭生成器 下面执行会报错
    # gen.close()
    # 在生成器执行到的地方抛一个异常
    gen.throw(Exception, 'download err')
    # send方法可以传递值进入生成器内部,同时还可以重启生成器执行到下一个yield的位置
    data = gen.send('hello')
    print(data)
