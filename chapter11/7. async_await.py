# Python 为了将语义变得更加明确, 就引入了async和await关键词用户定义原生协程

# 1. await 只能在 async 的函数中出现
# 2. async 函数中 不能出现yield from
import time
import types
import gevent


async def downloader(url):

    return '小伟'


@types.coroutine
def down_html():
    yield 'xiaoweigege'


async def download_url(url):
    html = await downloader(url)
    xiaowei = await down_html()
    return html, xiaowei


if __name__ == '__main__':
    coro = downloader('http:www.baidu.com')
    # next(None)
    coro.send(None)
    coro.send(None)
    print(coro)
