import IO3
import json
import time
import item_pages
import get_items
import write_dbs
import random
import os

'''
1.从文件获取页码列表
2.从页码地址获取房源列表
3.从房源地址获取房源信息
4.将处理好的房源信息url加入已完成列表
5.下一个房源
##############################
6.异常处理（滑动验证码）
7.模拟浏览
8.其他验证处理

'''


def get_finish_list():
    # 获取完成列表
    path = 'F:\\project\\anju\\res\\'
    files = os.listdir(path)
    # 已经有数据的url列表
    done_list = []
    json_list = []

    # 提取文件内容
    for file in files:

        if 'json' in file:

            # 准确获取一个txt的位置，利用字符串的拼接
            txt_path = path + file
            files = open(txt_path, 'r', encoding='utf-8')
            try:
                texts = str(files.read())
                dict_s = json.load(texts)
            except:
                # texts = files.read()
                dict_s = json.load(files)
            # dict_s = json.loads(files)
            files.close()
            url = dict_s["url_now"]
            url = str(url)
            done_list.append(url)
            json_list.append(dict_s)

    jStr = json.dumps(json_list, ensure_ascii=False, indent=1)
    fd = open('One.json', 'w', encoding='utf-8')
    fd.write(jStr)
    fd.close()
    print(done_list)
    return done_list


def step_one():
    '''
    # 步骤1-2
    #:return:
    :return:
    '''
    try:
    # 获取列表
        file = open('./work_file/page_list.json', 'r')
        jstr = file.read()
        page_list = json.loads(jstr)
        # 去重
        page_list = list(set(page_list))
        # 获取完成列表
        # fin_list = get_finish_list()
        # print(page_list)
        # 遍历获取房源列表
        random.shuffle(page_list)

        for urls in page_list:
            it_pglist = item_pages.get_itpg_url(urls)
            # 遍历获取房源信息
            for url2 in it_pglist:
                # 判断是否在数据库里
                if write_dbs.data_check(url2) != True:
                    # 判断是否采集过
                    # if url2 not in fin_list:
                    # 判断数据异常不操作
                    if get_items.get_info(url2) != None:
                        print('#' * 35 + '信息不在已完成列表' + '#' * 35)
                        city, district, title, rental_type, phone_num, contacts, url_now, rent, lease, area, heading, community, address, detail, facility, advantage, pic, region, province = get_items.get_info(
                            url2)

                        # 保存到json的内容
                        detel = {
                            "region": region,
                            "province": province,
                            "city": city,
                            "district": district,
                            "title": title,
                            "rental_type": rental_type,
                            "url_now": url_now,
                            "rent": rent,
                            "lease": lease,
                            "area": area,
                            "heading": heading,
                            "community": community,
                            'address': address,
                            "contacts": contacts,
                            "phone": phone_num,
                            "detail": detail,
                            "facility": facility,
                            "advantage": advantage,
                            "pics": pic
                        }
                        # 保存操作
                        jStr = json.dumps(detel, ensure_ascii=False, indent=1)
                        IO3.rtfile_time_with_path(jStr, 'json')
                        # 入库
                        write_dbs.data_in(detel)


            else:
                print('#' * 35 + '当前页面以前处理过了' + '#' * 35)
    except:
        print('#' * 20 + '出问题了么，稍微休息15秒恢复一下' + '#' * 20)
        time.sleep(15)
        step_one()


step_one()

# 1.从文件获取页码列表
# 2.从页码地址获取房源列表
# 3.从房源地址获取房源信息
# 4.将处理好的房源信息url加入已完成列表
# 5.下一个房源

# 6.异常处理（滑动验证码）
# 7.模拟浏览
# 8.其他验证处理
