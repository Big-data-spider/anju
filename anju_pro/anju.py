import requests
from fake_useragent import UserAgent
from lxml import etree
import numpy
import time
import IO3
import json


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
    texts = requests.get(url, headers=headers).text
    # xpath适配前置
    dom = etree.HTML(texts)

    return texts, dom


def get_in_pg():
    '''
    获取各地首页
    :param url:
    :return:
    '''
    url = 'https://www.anjuke.com/sy-city.html'
    texts, dom = get_content(url)

    index_list = dom.xapth('//div[@class="city_list"]/a/@href').extract()
    print(index_list)
    print('*' * 30)

    return index_list


def get_zfpg(url):
    '''
    获取各地租房页
    :param url:
    :return:
    '''
    texts, dom = get_content(url)
    zu_url = dom.xpath('//*[@id="glbNavigation"]/div/ul/li[4]/a/@href').extract()
    print(zu_url[0])

    return zu_url[0]


def get_pages(url, pagelist):
    '''
    获取租房分页
    :param url:
    :return:
    '''
    texts, dom = get_content(url)
    if len(dom.xpath('//a[@class="aNxt"]/@href')) != 0:
        next_page = dom.xpath('//a[@class="aNxt"]/@href').extract()
        next_url = next_page[0]
        pagelist.append(next_url)
        time.sleep(numpy.random.randint(3, 6))
        return get_pages(next_url, pagelist)
    else:
        print(pagelist)
        return pagelist


def pg_list():
    #     pass
    #
    #
    # def main():
    '''
    1.各地首页列表
    2.各地租房页列表
    3.所有分页链接列表
    :return:
    '''
    ALL_page = []
    index_list = get_in_pg()
    # 首页列表获得各地首页
    for i in index_list:
        city_pglist = get_zfpg(i)
        # 获得租房页
        for j in city_pglist:
            pg_list = [j]
            # 获得分页列表
            pages = get_pages(j, pg_list)
            # 分页列表加入全部列表
            for k in pages:
                ALL_page.append(k)
                time.sleep(1)

    return ALL_page


def save():
    '''
    存储
    :return:
    '''
    lis = pg_list()
    lis = json.dumps(lis, ensure_ascii=False, indent=1)
    IO3.rtfile_input(lis, 'page_list.json')


# save()
