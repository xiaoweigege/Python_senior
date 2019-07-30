import time
import asyncio
import aiohttp
from lxml import etree


def extract_html(html):
    """
    处理html
    :param html:
    :return:
    """
    html = etree.HTML(html)
    items = html.xpath('//div[@class="sons"]/div/span/a')
    for item in items:
        # name = item.xpath('./text()')[0]
        link = 'https://so.gushiwen.org' + item.xpath('./@href')[0]
        yield link


async def parse_detail(session, url):
    """
    处理详情
    :param html:
    :return:
    """
    html = await fetch(session, url)
    html = etree.HTML(html)

    name = html.xpath('//div[@class="cont"]/h1/text()')[0]
    content = '\n'.join(html.xpath('//div[@class="sons"][1]//div[@class="contson"]/text()'))

    line = [name, content]
    print(line)
    global number
    number += 1


async def fetch(session, url):
    """
    发送请求
    :param url:
    :return:
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'

    }
    async with session.get(url, headers=headers) as response:
        print('url status: {}'.format(response.status))
        if response.status in [200, 201]:
            data = await response.text()
            return data
        else:
            return None


async def main(loop):
    """
    主函数
    :return:
    """
    index_url = 'https://so.gushiwen.org/gushi/sanbai.aspx'
    # session = aiohttp.ClientSession()
    async with aiohttp.ClientSession() as session:
        html = await fetch(session, index_url)
        if html is not None:
            for link in extract_html(html):
                await parse_detail(session, link)


if __name__ == '__main__':

    number = 0
    start_time = time.time()
    loop = asyncio.get_event_loop()

    loop.run_until_complete(main(loop))

    last_time = time.time()

    print(f'耗时: {last_time-start_time}s', number)

