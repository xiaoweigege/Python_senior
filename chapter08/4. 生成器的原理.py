import dis
import inspect

frame = None


def foo():
    bar()


def bar():
    global frame
    frame = inspect.currentframe()


def gen():
    name = 'xiaowei'
    yield 1
    age = 23
    yield 2


# foo()
# print(frame.f_code)
# print(frame.f_back)
# print(dis.dis(foo))
gen_func = gen()
print(dis.dis(gen_func))
print(gen_func.gi_frame.f_lasti)
print(gen_func.gi_frame.f_locals)
next(gen_func)
print(gen_func.gi_frame.f_lasti)
print(gen_func.gi_frame.f_locals)
next(gen_func)
print(gen_func.gi_frame.f_lasti)
print(gen_func.gi_frame.f_locals)
# f_lasti 会记录最近执行的代码的位置, 位置可以用dis.dis 来查看 他是PyFrameObject 对象
# f_locals 会记录变量

# 1. Python 中 函数的工作原理
# Python.exe 会用一个PyEval_EvalFramEx(C函数) 去执行foo 函数
# 首先会创建一个栈帧 Python一切皆对象, 栈帧对象, 字节码对象
# 当foo调用子函数bar ,又会创建一个栈帧, 所有的栈帧都是分配在堆内存上，
# 这就决定了栈帧可以独立于调用者存在
