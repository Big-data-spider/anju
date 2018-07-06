from pymongo import MongoClient
import re
import time
import json
import random


def data_in(content):
    '''
    数据入库
    '''
    try:
        name = 'Xstc'
        pwd = '1231512315'
        client = MongoClient('mongodb://47.104.220.29:27017')
        db = client.One
        db.authenticate(name, pwd, mechanism='SCRAM-SHA-1')
        rents = db.rent

        detel = content
        post_id = rents.insert_one(detel).inserted_id
        print(post_id)
        print('#' * 35 + '入库完成' + '#' * 35)
        time.sleep(1)
        # 关闭资源
        client.close()
    except:
        print('看来数据库连接失败了，等一会在操作？')
        time.sleep(15)
        data_in(content)


def data_check(url):
    '''
    查询字典中已有数据
    输出已有数据的url列表
    :return:
    '''
    try:
        # 数据查询
        name = 'Xstc'
        pwd = '1231512315'
        client = MongoClient('mongodb://47.104.220.29:27017')
        # client = MongoClient('mongodb://{ct_mongodb}:{ct\@mogodb}@{47.104.220.29}:{27017}')
        db = client.One
        # db.authenticate(name, pwd, mechanism='SCRAM-SHA-1')
        db.authenticate(name, pwd, mechanism='SCRAM-SHA-1')
        rents = db.rent
        bol = False
        for u in rents.find({'url_now': re.compile(url)}):
            bol = True

        print(bol)
        print(time.ctime())
        client.close()
        return bol
    except:
        print('看来数据库连接失败了，等一会在操作？')
        time.sleep(15)


def db_chck():
    fin = open('One.json')
    # fin = fin.read()

    fin_list = json.load(fin, encoding='utf-8')
    random.shuffle(fin_list)
    for dics in fin_list:
        url = dics['url_now']
        # print(url)
        if data_check(url) == False:
            data_in(dics)
            print('此条目之前不在数据库，现在已经入库了。')
            time.sleep(1)


def main():
    while True:
        db_chck()
        time.sleep(1800)

# main()
