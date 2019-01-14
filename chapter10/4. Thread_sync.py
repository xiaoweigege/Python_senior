# 线程同步
# 1. 用锁会影响性能
# 2. 锁会引起死锁
# 3. RLock 可重入的锁 在同一个线程当中可以多次 acquire 注意 acquire的次数 和 release 次数一致
from threading import Thread, Lock

total = 0
lock = Lock()


def add():
    global total
    for _ in range(1000000):
        # 获取锁
        lock.acquire()
        total += 1
        # 释放锁
        lock.release()


def desc():
    global total
    for _ in range(1000010):
        with lock:
            total -= 1


if __name__ == '__main__':

    thread1 = Thread(target=add)
    thread2 = Thread(target=desc)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    print(total)