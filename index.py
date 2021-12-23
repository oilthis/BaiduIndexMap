import requests
import info
from datetime import date, timedelta, datetime


def decrypt(key, data):  # 指数数据解密
    cipher2plain = {}  # 密文明文映射字典
    plain_chars = []  # 解密得到的明文字符
    for i in range(len(key) // 2):
        cipher2plain[key[i]] = key[len(key) // 2 + i]
    for i in range(len(data)):
        plain_chars.append(cipher2plain[data[i]])
    index_list = "".join(plain_chars).split(",")  # 所有明文字符拼接后按照逗号分隔
    index_list = ["0" if x == "" else x for x in index_list]
    return index_list


def get_index_data(keys, start=None, location=None):
    words = [[{"name": keys, "wordType": 1}]]
    words = str(words).replace(" ", "").replace("'", "\"")
    today = date.today()
    if start is None:
        start = today - timedelta(days=8)
    else:
        start = datetime.strptime(start, "%Y-%m-%d").date()
    end = str(start + timedelta(days=6))
    start = str(start)
    if location is None:
        area = 0
    else:
        area = info.location_code.get(location)
    url = f'http://index.baidu.com/api/SearchApi/index?area={area}&word={words}&startDate={start}&endDate={end}'
    res = requests.get(url, headers=info.headers).json()
    data = res['data']
    uniqid = data['uniqid']
    url = f'http://index.baidu.com/Interface/ptbk?uniqid={uniqid}'
    res = requests.get(url, headers=info.headers)
    ptbk = res.json()['data']
    result = {"startDate": start, "endDate": end}
    for userIndexe in data['userIndexes']:
        name = userIndexe['word'][0]['name']
        index_all = userIndexe['all']['data']
        result[name] = decrypt(ptbk, index_all)
    return result
