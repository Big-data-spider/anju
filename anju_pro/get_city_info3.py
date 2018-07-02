'''

行政区划
城市归属
地区归属
v3.1

'''

import json


def load_dict():
    '''
    读取内容
    :return:
    '''
    f = open('city_list_dict.json', 'r', encoding='utf-8')
    lst = f.read()
    f.close()
    content = json.loads(lst)
    # print(content)

    return content


def get_result(city_name):
    content = load_dict()

    for key, values in content[1].items():
        # 遍历城市
        # print(values)
        for city, short_name in values.items():
            if city_name == city:
                print(key)
                print(city_name)
                provi = key

    for areas, prov in content[0].items():
        # print(prov)
        for p, short_letter in prov.items():
            if p == provi:
                print(areas)
                area = areas

    return area, provi


cityname = '重庆'
get_result(cityname)
