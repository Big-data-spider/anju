import time
from selenium import webdriver
from lxml import etree

def click_phone(url):
    driver = webdriver.Chrome()
    driver.get(url)
    elem = driver.find_element_by_xpath('//div[@class="card-phone-click"]')
    elem.click()
    # driver.refresh()
    time.sleep(5)
    texts = driver.page_source
    dom = etree.HTML(texts)
    num = dom.xpath('//div[@class="card-phone-click phone-hover"]/span/text()')
    # num = dom.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/div[2]/span/text()')
    print(num)
    
    return num



# url = 'https://fz.zu.anjuke.com/fangyuan/1161621364?from=Filter_6'
# click_phone(url)