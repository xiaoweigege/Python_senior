import time
from multiprocessing import Process, Queue, Pool, Manager, Pipe

# 多进程不能用这个Queue了
# from queue import Queue

# multiprocessing.Queue 不能用于进程池


def producer(pipe):
    # queue.put('a')
    pipe.send('xiaowei')
    time.sleep(2)


def consumer(pipe):
    time.sleep(2)
    # data = queue.get()

    print(pipe.recv())


if __name__ == '__main__':
    # multiprocessing.Queue 不能用于进程池
    # queue = Queue(10)
    queue = Manager().Queue(10)
    my_producer = Process(target=producer, args=(queue,))
    my_consumer = Process(target=consumer, args=(queue,))
    # my_producer.start()
    # my_consumer.start()
    #
    # my_producer.join()
    # my_consumer.join()

    pool = Pool(2)
    pool.apply_async(producer, args=(queue,))
    pool.apply_async(consumer, args=(queue, ))
    pool.close()
    pool.join()

    # Pipe 进程通信
    # pipe 的性能高于queue

    recevie_pipe, send_pipe = Pipe()
    my_producer = Process(target=producer, args=(recevie_pipe,))
    my_consumer = Process(target=consumer, args=(send_pipe,))
    my_producer.start()
    my_consumer.start()

    my_producer.join()
    my_consumer.join()


