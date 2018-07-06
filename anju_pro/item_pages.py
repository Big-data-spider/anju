import numpy
import time
import IO3
import json
import requests
from fake_useragent import UserAgent
from lxml import etree


def get_pglist():
    '''
    列表读取
    :return:
    '''
    texts = open('./work_file/all_page.json', 'r').read()
    lists = json.loads(texts)

    return lists

def get_content(url):
    '''
    获取页面内容
    :param url:
    :return:
    '''
    # 随机UA
    ua = UserAgent().random
    headers = {'User-agent': ua}

    # 页面内容
    texts = requests.get(url=url, headers=headers).text
    # xpath适配前置
    dom = etree.HTML(texts)

    return texts, dom


def get_itpg_url(url):
    '''
    租房信息的url列表
    :param url:
    :return:
    '''
    text, dom = get_content(url)
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
        IO3.rtfile_input(jstr, './work_file/items_urls.json')
        print('#' * 35)




##############################################################

# url = "https://hb.zu.anjuke.com/?from=navigation"
#
# get_itpg_url(url)
