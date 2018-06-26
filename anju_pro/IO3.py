from datetime import *
import json

'''
临时数据读写工具
'''


def time_now():
    now_time = datetime.now().strftime("%Y%m%d%H%M%S")
    print(now_time)

    return now_time


def filename():
    filename = input('你的文件名带后缀：')
    # filename = pressin + '.txt'

    return filename


def rtfile(content):
    '''
    保存内容
    :param content:
    :return:
    '''
    try:
        fd = open(filename(), 'w',encoding='utf-8')
        try:
            fd.write(content)

        finally:
            fd.close()

    except IOError:
        print
        "file not there"


def rtfile_input(content, inputname):
    '''
    保存内容
    :param content:
    :return:
    '''
    try:
        fd = open(inputname, 'w')
        try:
            fd.write(content)

        finally:
            fd.close()

    except IOError:
        print("file not there")


def rtfile_time(content, sufx):
    '''
    保存内容
    :param content:
    :return:
    '''
    try:
        fd = open((time_now() + '.' + sufx), 'w')
        try:
            fd.write(content)

        finally:
            fd.close()

    except IOError:
        print("file not there")


def readfile():
    '''
    读取内容
    :return:
    '''
    try:
        fd = open(filename(), 'r')

        try:
            all_text = fd.read()

        finally:
            fd.close()

    except IOError:
        print('open error')


    return all_text
