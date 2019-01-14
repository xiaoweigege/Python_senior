# GIL 全称 global interpreter lock
# Python 中的一个线程对应于C语言中的一个线程
# GIL 使得, 同一时刻只有一个线程运行在一个CPU上执行字节码, 无法将多个线程映射到多个CPU上执行
# GIL 会根据执行的字节码行数、时间片释放GIL、I/O操作


# import dis
# def add(a):
#     a += 1
#
# print(dis.dis(add))
total = 0


def add():
    global total
    for _ in range(1000000):
        total += 1


def desc():
    global total
    for _ in range(1000000):
        total -= 1


if __name__ == '__main__':
    from threading import Thread
    thread1 = Thread(target=add)
    thread2 = Thread(target=desc)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)