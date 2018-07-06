
import os.path
import json

def done_lis():
    '''
    已经拿到数据的项目的地址列表
    :return:
    '''

    # 获取目录下所有文件
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
            files = open(txt_path, 'r')
            try:
                texts = files.read()
            except:
                pass
            dict_s = json.loads(texts)
            files.close()
            url = dict_s["url_now"]
            url = str(url)
            done_list.append(url)
            json_list.append(dict_s)

    jStr = json.dumps(json_list, ensure_ascii=False, indent=1)
    fd = open('One.json', 'w')
    fd.write(jStr)
    fd.close()
    print(done_list)
    return done_list

# 合并json数据到一个文件中
# done_lis()
