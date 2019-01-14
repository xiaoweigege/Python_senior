from threading import Condition, Thread

# 条件变量, 用于复杂的线程间同步
# 在调用with cond之后才能调用wait 或者notify方法
# condition 有两层锁, 一把底层锁 会在调用wait方法的时候释放
# 上面的锁会在每次调用wait的时候分配一把并放入到condition的等待队列中,
# 等到notify方法的唤醒


class XiaoAi(Thread):
    def __init__(self, cond):
        super().__init__(name='小爱')
        self.cond = cond

    def run(self):
        with self.cond:
            # 等待通知, 通知来了 就执行下方的
            self.cond.wait()
            print('{}: {}'.format(self.name, '在'))
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '好啊'))
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '君住长江尾'))
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '共饮长江水'))
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '此恨何时几'))
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '定不负相思意'))


class TianMao(Thread):
    def __init__(self, cond):
        super().__init__(name='天猫')
        self.cond = cond

    def run(self):
        with self.cond:
            print('{}: {}'.format(self.name, '小爱同学'))
            # 通知其他线程执行
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '我们来对古诗吧'))
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '我住长江头'))
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '日日思君不见君'))
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '此水几时休'))
            self.cond.notify()
            self.cond.wait()
            print('{}: {}'.format(self.name, '只愿君心似我心'))
            self.cond.notify()


if __name__ == '__main__':
    condition = Condition()
    xiaoai = XiaoAi(condition)
    tianmao = TianMao(condition)

    xiaoai.start()
    tianmao.start()