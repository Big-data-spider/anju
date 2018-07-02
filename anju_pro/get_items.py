from selenium import webdriver
from lxml import etree
import time

'''
xpath

需要点击的地方

电话：
xpath('//div[@class="card-phone-click"]')

配套更多：
('//li[class="peitao-item peitao-item-more"]')

城市名：
.xpath('//div[@id="switch_apf_id_5"]/text()').extract()
.replace(' ','')
.replace('\n','')
title:
.xpath('//h3[@class="house-title"]/text()')

pics:
.xpath('//div[@class="img_wrap"]/img/@data-src').extract()

phone_num:
.xpath('//div[@class="card-phone-click phone-hover"]/span/text()')

contacts:
.xpath('//h2[@class="broker-name"]/text()')

rent_money:
.xpath('//span[@class="price"]/em/text()')

type(租金压缴方式):
.xpath('//span[@class="type"]/text()')

套型和所属楼层：
.xpath('//li[@class="house-info-item l-width"]/span[2]/text()')

面积和朝向：
.xpath('//li[@class="house-info-item"]/span[2]/text()')

小区:
.xpath('//li[@class="house-info-item l-width"]/a[1]/text()')

本地地区:
.xpath('//li[@class="house-info-item l-width"]/a/text()')

配套设施：
.xpath('//li[@class="peitao-item has"]/text()')

详情介绍:
.xpath('//div[@class="auto-general"]/text()')
或
.xpath('//div[@class="auto-general"]/*/text()')

地址:
请参考小区


'''


def get_info(url):
    '''
    获取页面和各项目
    :param url:
    :return:
    '''
    # 无ui模式运行
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome(chrome_options=option)
    driver.get(url)
    print('#' * 35 + 'OK' + '#' * 35)

    # 判断有没有需要点击的事件
    content = driver.page_source
    dom = etree.HTML(content)
    if len(dom.xpath('//div[@class="card-phone-click"]')) != 0:
        elem = driver.find_element_by_xpath('//div[@class="card-phone-click"]')
        elem.click()
    if len(dom.xpath('//li[class="peitao-item peitao-item-more"]')) != 0:
        elem = driver.find_element_by_xpath('//li[class="peitao-item peitao-item-more"]')
        elem.click()
    time.sleep(5)
    # 新的源码
    con_reget = driver.page_source
    dom_reget = etree.HTML(con_reget)

    # city, district, title, rental_type, phone_num, contacts, url_now, rent, lease, area, heading, community, address, detail, facility, advantage, pic

    # 城市名
    cityname = dom_reget.xpath('//div[@id="switch_apf_id_5"]/text()')
    city = cityname[0].replace('\n', '').replace(' ', '')
    print(city)

    district = dom_reget.xpath('//li[@class="house-info-item l-width"]/a/text()')[0]
    print(district)

    title = dom_reget.xpath('//h3[@class="house-title"]/text()')[0]
    print(title)

    rental_type = '请咨询联系人'
    print(rental_type)

    phone_num = dom_reget.xpath('//div[@class="card-phone-click phone-hover"]/span/text()')[0]
    print(phone_num)

    contacts = dom_reget.xpath('//h2[@class="broker-name"]/text()')[0]
    print(contacts)

    url_now = url
    print(url_now)

    rent = dom_reget.xpath('//span[@class="price"]/em/text()')[0]
    print(rent)

    lease = dom_reget.xpath('//span[@class="type"]/text()')[0]
    print(lease)

    area = dom_reget.xpath('//li[@class="house-info-item l-width"]/span[2]/text()')
    heading = dom_reget.xpath('//li[@class="house-info-item"]/span[2]/text()')
    areas = area[0] + '\t' + heading[0]
    headings = area[1] + '\t' + heading[1]

    print(areas)
    print(headings)

    community = dom_reget.xpath('//li[@class="house-info-item l-width"]/a[1]/text()')[0]
    print(community)

    address = '请咨询联系人'
    print(address)

    detail = dom_reget.xpath('//div[@class="auto-general"]/text()')
    if len(detail) == 1:
        detail = detail
        # print(detail)
    elif len(detail) > 1:
        detail = dom_reget.xpath('//div[@class="auto-general"]/*/text()')
        new_list = []
        for strs in detail:
            new_strs = strs.replace('\n', '').replace(' ', '').replace('，','').replace('\t','')
            new_list.append(new_strs)
            detail = new_list
    else:
        detail = '未提供描述'
    print(detail)

    facility = dom_reget.xpath('//li[@class="peitao-item has"]/div/text()')
    if len(facility) != 0:
        facility = facility
    else:
        facility = '业主未提供此方面的信息'
    print(facility)

    advantage = '未添加描述'
    print(advantage)

    pic = dom_reget.xpath('//div[@class="img_wrap"]/img/@data-src')
    print(pic)

    return city, district, title, rental_type, phone_num, contacts, url_now, rent, lease, area, heading, community, address, detail, facility, advantage, pic

# url = 'https://yan.zu.anjuke.com/fangyuan/1164176099?from=Filter_8'
#
# get_info(url)
