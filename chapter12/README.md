# asyncio并发编程
1. 事件循环
2. 协程嵌套
3. call_soon, call_later, call_at, call_soon_threadsafe
4. ThreadPollExecutor + asyncio
5. asyncio模拟http请求
6. future 和 task
7. asyncio同步和通信
8. aiohttp 实现高并发爬虫


## asyncio介绍
- 包含各种特定系统实现的模块化事件循环
- 传输和协议抽象
- 对TCP,UDP,SSL,子进程,延时调用以及其他的具体支持
- 模仿futures模块但适用于事件循环适用的Future类
- 基于yield from 的协议和任务, 可以让你用顺序的方式编写并发代码
- 必须使用一个将产生阻塞IO的调用时,有接口可以把这个事件转移到线程池
- 模仿threading模块中的同步原语、可以用在单线程内的协程之间
