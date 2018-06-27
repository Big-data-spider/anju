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
    texts = requests.get(url=url, headers=headers).text
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

    index_list = dom.xpath('//div[@class="city_list"]/a/@href')
    print(index_list)
    print('*' * 30)

    in_list = json.dumps(index_list, ensure_ascii=False, indent=1)
    IO3.rtfile_input(in_list, 'index_list.json')
    # 首页列表
    return index_list


def get_zfpg(url):
    '''
    获取各地租房页
    :param url:
    :return:
    '''
    texts, dom = get_content(url)
    if len(dom.xpath('//*[@id="glbNavigation"]/div/ul/li[4]/a/@href')) != 0:
        zu_url = dom.xpath('//*[@id="glbNavigation"]/div/ul/li[4]/a/@href')
        print(zu_url[0])
        print('*' * 30)
        return zu_url[0]
    else:
        print('%s这里没租房信息么？打开看一下' % url)
        time.sleep(numpy.random.randint(3, 6))
        return None


def get_pages(url, pagelist):
    '''
    获取租房分页
    :param url:
    :return:
    '''
    texts, dom = get_content(url)
    if len(dom.xpath('//a[@class="aNxt"]/@href')) != 0:
        next_page = dom.xpath('//a[@class="aNxt"]/@href')
        next_url = next_page[0]
        print(next_url + '       ---------->added')
        pagelist.append(next_url)
        time.sleep(numpy.random.randint(3, 6))
        return get_pages(next_url, pagelist)
    else:
        print(pagelist)
        print('*' * 30)
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
    f = open('all_page.json', encoding='utf-8')
    ALL_page = json.load(f)
    index_list = get_in_pg()
    # 首页列表获得各地首页
    for i in index_list:
        print('-------------------001-------------------')
        i = i.strip()
        # print(i)
        # print(type(i))
        i = i.replace(' ', '')
        city_pg = get_zfpg(i)
        print(city_pg)
        if city_pg != None:
            # if city_pg not in ALL_page:
            # 获得租房页
            # for j in city_pglist:
            # print(type(j))
            # print(j)
            print('-------------------002-------------------')
            city_pg = city_pg.replace(' ', '')
            pg_list = [city_pg]
            # 获得分页列表
            pages = get_pages(city_pg, pg_list)
            print(pages)
            # 分页列表加入全部列表
            for k in pages:
                print('-------------------003-------------------')
                k = k.strip()
                # print(type(k))
                if k not in ALL_page:
                    ALL_page.append(k)
                    print(ALL_page)
                    jstr = json.dumps(ALL_page, ensure_ascii=False, indent=1)
                    IO3.rtfile_input(jstr, 'all_page.json')
            print('*' * 30 + '\r\n')
            time.sleep(numpy.random.randint(3, 10))
        else:
            time.sleep(numpy.random.randint(3, 7))

    return ALL_page


def save():
    '''
    存储
    :return:
    '''
    lis = pg_list()
    lis = json.dumps(lis, ensure_ascii=False, indent=1)
    IO3.rtfile_input(lis, 'page_list.json')


save()
