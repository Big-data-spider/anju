import requests
from fake_useragent import UserAgent
from lxml import etree
import numpy
import time
import IO3
import json
import anju


def get_pglist():
    '''
    列表读取
    :return:
    '''
    texts = open('all_page.json', 'r').read()
    lists = json.loads(texts)

    return lists


def get_itpg_url(url):
    '''
    租房信息的url列表
    :param url:
    :return:
    '''
    text, dom = anju.get_content(url)
    iturl_list = dom.xpath('//a[@class="img"]/@href')
    print(iturl_list)

    return iturl_list


def it_urls():
    '''
    列表批处理和保存
    :return:
    '''
    lists = get_pglist()
    itpgs = []
    for i in lists:
        itpgs = sum(itpgs, get_itpg_url(i))
        time.sleep(numpy.random.randint(3, 6))
        print(itpgs)
        jstr = json.dumps(itpgs, ensure_ascii=False, indent=1)
        IO3.rtfile_input(jstr, 'items_urls.json')
        print('#' * 35)




##############################################################

# url = "https://hb.zu.anjuke.com/?from=navigation"
#
# get_itpg_url(url)
