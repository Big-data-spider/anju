import anju
import time
import numpy
import IO3
import json
from fake_useragent import UserAgent


def get_pages(url, pagelist):
    '''
    获取租房分页
    :param url:
    :return:
    '''
    texts, dom = anju.get_content(url)
    if len(dom.xpath('//a[@class="aNxt"]/@href')) != 0:
        next_page = dom.xpath('//a[@class="aNxt"]/@href')
        next_url = next_page[0]
        print(next_url+'---------->added')
        pagelist.append(next_url)
        time.sleep(numpy.random.randint(3, 6))
        return get_pages(next_url, pagelist)
    else:
        print(pagelist)
        print('*' * 30)
        return pagelist


def main():
    url = 'https://as.zu.anjuke.com/'
    # anju.get_content(url)
    pg_lsit = [url]
    fin_list = get_pages(url, pg_lsit)
    fin_list = json.dumps(fin_list, ensure_ascii=False, indent=1)
    IO3.rtfile_input(fin_list,'as.json')


# main()

def rdfile():
    f = open('all_page.json',encoding='utf-8')
    ss = json.load(f)
    print(ss)

rdfile()