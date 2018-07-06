import IO3
import json
import time
import numpy
import item_pages
import get_items
import get_city_info





def step_one():
    '''
    步骤1-2
    :return:
    '''

    pass
    # file = open('./work_file/page_list.json','r')
    # jstr = file.read()
    # page_list = json.loads(jstr)
    #
    # print(page_list)

# step_one()


##########################################################

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