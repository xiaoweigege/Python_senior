import time
import multiprocessing


def get_html(n):
    time.sleep(n)
    # print('get html {}'.format(n))
    return n


class GetHtml(multiprocessing.Process):
    def __init__(self, n):
        super().__init__()
        self.n = n

    def run(self):
        time.sleep(self.n)
        print('get html {}'.format(self.n))
        return self.n


if __name__ == '__main__':
    process = multiprocessing.Process(target=get_html, args=(2, ))
    process.start()
    print('end process')
    process1 = GetHtml(3)
    process1.start()
    print('end process1')

    # 进程池
    pool = multiprocessing.Pool(5)
    for index in range(10):
        result = pool.apply_async(get_html, args=(2,))
        print(result.get())
    # 禁止添加进程了
    pool.close()
    # 等待
    pool.join()

    # imap
    for result in pool.imap(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))

    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print("{} sleep success".format(result))