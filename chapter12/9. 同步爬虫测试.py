import time
import requests
from lxml import etree

url = 'https://so.gushiwen.org/gushi/sanbai.aspx'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko)'
                  ' Chrome/75.0.3770.100 Safari/537.36'
}
number = 0
start_time = time.time()
response = requests.get(url, headers=headers)

html = etree.HTML(response.content)

items = html.xpath('//div[@class="sons"]/div/span/a')
for item in items:
    # name = item.xpath('./text()')[0]
    link = 'https://so.gushiwen.org' + item.xpath('./@href')[0]

    response = requests.get(link, headers=headers)
    html = etree.HTML(response.content)
    name = html.xpath('//div[@class="cont"]/h1/text()')[0]
    content = '\n'.join(html.xpath('//div[@class="sons"][1]//div[@class="contson"]/text()'))

    line = [name, content]
    number += 1
    print(line)

last_time = time.time()

print(f'耗时: {last_time-start_time}s', number)