import random
import requests
from fake_useragent import UserAgent
from lxml import etree
import numpy
import time
import IO3
import json
import re


def regx(key, pattern):
    # 正则匹配
    pattern1 = re.compile(pattern)
    matcher1 = re.search(pattern1, key)

    if matcher1 == None:
        # print(None)
        return None
    else:
        res = matcher1.group(0)
        # print(res)
        return res


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
    IO3.rtfile_input(in_list, './work_file/index_list.json')
    # 首页列表
    return index_list


def get_zfpg(url):
    '''
    有些房产租房信息不在此标签内，使用正则匹配即可
    获取各地租房页
    :param url:
    :return:
    '''
    texts, dom = get_content(url)

    # 解决上版本代码会识别不了在第三顺位的租房链接获取错误的问题
    if len(dom.xpath('//a[@class="a_navnew"]/@href')) != 0:
        top_list = dom.xpath('//a[@class="a_navnew"]/@href')
        # print(top_list)
        for keys in top_list:
            keys = keys.strip()
            # print(keys + '\t___sign001')
            # print(type(keys))
            patrn = r'(https\:\/\/\w+\.zu\.anjuke\.com)'
            if regx(keys, patrn) != None:
                zu_url = regx(keys, patrn)
                # print(zu_url)
                return zu_url

    else:
        print('%s抱歉没有找到租房分类，检查一下，然后下一个' % url)
        return None


def get_pages(url, pagelist):
    '''
    获取租房分页
    :param url:
    :return:
    '''
    try:
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
            print('*' * 70)
            return pagelist
    except:
        print('貌似网络中断了一下？那休息一下吧')
        time.sleep(numpy.random.randint(5, 10))
        return None


def pg_list():
    '''
    1.各地首页列表
    2.各地租房页列表
    3.所有分页链接列表
    :return:
    '''
    f = open('./work_file/all_page.json', encoding='utf-8')
    ALL_page = json.load(f)
    index_list = json.load(open('./work_file/index_list.json', encoding='utf-8'))
    if index_list != None:
        random.shuffle(index_list)
        print(index_list)
        # 首页列表获得各地首页
        for i in index_list:
            print(i)
            print('-------------------001-------------------')
            i = i.strip()
            i = i.replace(' ', '')
            city_pg = get_zfpg(i)
            print(city_pg)
            if city_pg != None:
                # 获得租房页
                print('-------------------002-------------------')
                city_pg = city_pg.replace(' ', '')
                pg_list = [city_pg]
                # 获得分页列表
                pages = get_pages(city_pg, pg_list)
                if pages != None:

                    print(pages)
                    # 分页列表加入全部列表

                    for k in pages:
                        print('-------------------003-------------------')
                        k = k.strip()

                        # 判断是否加入页面列表
                        if k not in ALL_page:
                            ALL_page.append(k)
                            print(ALL_page)
                            jstr = json.dumps(ALL_page, ensure_ascii=False, indent=1)
                            IO3.rtfile_input(jstr, './work_file/all_page.json')
                    print('*' * 70 + '\r\n')
                    index_list.remove(i)
                    print('处理完毕，此地址从列表中除去%s' % i)
                    jstr = json.dumps(index_list, ensure_ascii=False, indent=1)
                    IO3.rtfile_input(jstr, './work_file/index_list.json')
                    time.sleep(numpy.random.randint(3, 10))
            else:
                index_list.remove(i)
                print('废弃，此地址从列表中除去%s' % i)
                jstr = json.dumps(index_list, ensure_ascii=False, indent=1)
                IO3.rtfile_input(jstr, './work_file/index_list.json')
                time.sleep(numpy.random.randint(3, 7))

    return ALL_page


def save():
    '''
    存储
    :return:
    '''
    try:
        lis = pg_list()
        lis = json.dumps(lis, ensure_ascii=False, indent=1)
        IO3.rtfile_input(lis, './work_file/page_list.json')
    except:
        print('缓一会继续吧')
        time.sleep(15)
        save()


save()
