import requests
from bs4 import BeautifulSoup

cookie = 'BDUSS=复制cookie到此处'

headers = {
    "Connection": "keep-alive",
    "Accept": "application/json, text/plain, */*",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Dest": "empty",
    "Referer": "https://index.baidu.com/v2/main/index.html",
    "Accept-Language": "zh-CN,zh;q=0.9",
    "Cookie": cookie,
}

location_code = {
    '济南': 1, '贵阳': 2, '六盘水': 4, '南昌': 5, '九江': 6, '鹰潭': 7,
    '抚州': 8, '上饶': 9, '赣州': 10, '重庆': 11, '包头': 13, '鄂尔多斯': 14, '巴彦淖尔': 15,
    '锡林郭勒盟': 19, '呼和浩特': 20, '赤峰': 21, '通辽': 22, '呼伦贝尔': 25,
    '武汉': 28, '大连': 29, '黄石': 30, '荆州': 31, '襄阳': 32, '黄冈': 33, '荆门': 34, '宜昌': 35, '十堰': 36,
    '随州': 37, '恩施': 38, '鄂州': 39, '咸宁': 40, '孝感': 41, '仙桃': 42, '长沙': 43, '岳阳': 44, '衡阳': 45,
    '株洲': 46, '湘潭': 47, '益阳': 48, '郴州': 49, '福州': 50, '三明': 52, '龙岩': 53, '厦门': 54,
    '泉州': 55, '漳州': 56, '上海': 57, '遵义': 59, '娄底': 66, '怀化': 67, '常德': 68,
    '天门': 73, '潜江': 74, '滨州': 76, '青岛': 77, '烟台': 78, '临沂': 79, '潍坊': 80, '淄博': 81, '东营': 82,
    '聊城': 83, '菏泽': 84, '枣庄': 85, '德州': 86, '宁德': 87, '威海': 88, '柳州': 89, '南宁': 90, '桂林': 91,
    '贺州': 92, '贵港': 93, '深圳': 94, '广州': 95, '宜宾': 96, '成都': 97, '绵阳': 98, '广元': 99, '遂宁': 100,
    '巴中': 101, '内江': 102, '泸州': 103, '南充': 104, '德阳': 106, '广安': 108, '资阳': 109,
    '自贡': 111, '攀枝花': 112, '达州': 113, '雅安': 114, '吉安': 115, '昆明': 117, '玉林': 118, '河池': 119,
    '玉溪': 123, '楚雄': 124, '南京': 125, '苏州': 126, '无锡': 127, '北海': 128, '钦州': 129, '防城港': 130,
    '百色': 131, '梧州': 132, '东莞': 133, '丽水': 134, '金华': 135, '萍乡': 136, '景德镇': 137, '杭州': 138,
    '西宁': 139, '银川': 140, '石家庄': 141, '衡水': 143, '张家口': 144, '承德': 145, '秦皇岛': 146, '廊坊': 147,
    '沧州': 148, '温州': 149, '沈阳': 150, '盘锦': 151, '哈尔滨': 152, '大庆': 153, '长春': 154, '四平': 155,
    '连云港': 156, '淮安': 157, '扬州': 158, '泰州': 159, '盐城': 160, '徐州': 161, '常州': 162, '南通': 163,
    '天津': 164, '西安': 165, '兰州': 166, '郑州': 168, '镇江': 169, '宿迁': 172, '铜陵': 173, '黄山': 174,
    '宣城': 176, '巢湖': 177, '淮南': 178, '宿州': 179, '六安': 181, '滁州': 182, '淮北': 183,
    '阜阳': 184, '马鞍山': 185, '安庆': 186, '蚌埠': 187, '芜湖': 188, '合肥': 189, '辽源': 191, '松原': 194,
    '云浮': 195, '佛山': 196, '湛江': 197, '江门': 198, '惠州': 199, '珠海': 200, '韶关': 201, '阳江': 202,
    '茂名': 203, '潮州': 204, '揭阳': 205, '中山': 207, '清远': 208, '肇庆': 209, '河源': 210, '梅州': 211,
    '汕头': 212, '汕尾': 213, '鞍山': 215, '锦州': 217, '铁岭': 218, '丹东': 219,
    '营口': 221, '抚顺': 222, '阜新': 223, '葫芦岛': 225, '张家界': 226, '大同': 227, '长治': 228,
    '忻州': 229, '晋中': 230, '太原': 231, '临汾': 232, '运城': 233, '晋城': 234, '朔州': 235, '阳泉': 236,
    '吕梁': 237, '海口': 239, '三亚': 243, '儋州': 244, '新余': 246, '南平': 253,
    '宜春': 256, '保定': 259, '唐山': 261, '南阳': 262, '新乡': 263, '开封': 264, '焦作': 265, '平顶山': 266,
    '许昌': 268, '永州': 269, '铜川': 271, '安康': 272, '宝鸡': 273, '商洛': 274, '渭南': 275,
    '汉中': 276, '咸阳': 277, '榆林': 278, '庆阳': 281, '定西': 282, '武威': 283, '酒泉': 284,
    '张掖': 285, '嘉峪关': 286, '台州': 287, '衢州': 288, '宁波': 289, '眉山': 291, '邯郸': 292, '邢台': 293,
    '伊春': 295, '大兴安岭': 297, '黑河': 300, '鹤岗': 301, '绍兴': 303, '嘉兴': 304, '湖州': 305,
    '舟山': 306, '平凉': 307, '天水': 308, '白银': 309, '吐鲁番': 310, '哈密': 312, '阿克苏': 315,
    '克拉玛依': 317, '齐齐哈尔': 319, '佳木斯': 320, '牡丹江': 322, '绥化': 324,
    '乌兰察布': 331, '兴安盟': 333, '大理': 334, '昭通': 335, '红河': 337, '曲靖': 339, '丽江': 342, '金昌': 343,
    '陇南': 344, '临夏': 346, '临沧': 350, '济宁': 352, '泰安': 353, '莱芜': 356, '日照': 366, '安阳': 370,
    '驻马店': 371, '信阳': 373, '鹤壁': 374, '周口': 375, '商丘': 376, '洛阳': 378, '漯河': 379, '濮阳': 380, '三门峡': 381,
    '阿勒泰': 383, '喀什': 384, '和田': 386, '亳州': 391, '吴忠': 395, '固原': 396, '延安': 401, '邵阳': 405, '通化': 407,
    '白山': 408, '白城': 410, '甘孜': 417, '铜仁': 422, '安顺': 424, '毕节': 426, '文山': 437, '保山': 438,
    '阿坝': 457, '拉萨': 466, '乌鲁木齐': 467, '石嘴山': 472, '中卫': 480, '来宾': 506, '北京': 514, '日喀则': 516,
    '那曲': 655, '林芝': 656, '玉树': 659, '伊犁哈萨克': 660, '思茅': 662, '香港': 663, '澳门': 664, '崇左': 665,
    '济源': 667, '文昌': 670, '甘南': 673, '昌都': 678, '临高县': 680, '神农架': 687, '阿拉尔': 692, '图木舒克': 693
}


def request_with_cookies(url, cookies, timeout=30):
    header = headers.copy()
    header["Cookie"] = cookies
    response = requests.get(url, headers=headers, timeout=timeout)  # 发起请求
    if response.status_code != 200:
        raise requests.Timeout  # 请求异常: 一般为超时异常
    return response  # 返回响应内容


def is_cookies_valid(cookies):  # 检查cookies是否可用: 通过访问百度首页并检查相关元素是否存在
    URL_BAIDU = "https://www.baidu.com/"
    response = request_with_cookies(URL_BAIDU, cookies)  # 使用cookie请求百度首页, 获取响应内容
    html = response.text  # 获取响应的页面源代码
    soup = BeautifulSoup(html, "lxml")  # 解析页面源代码
    flag1 = soup.find("a", class_="quit") is not None  # "退出登录"按钮(a标签)是否存在
    flag2 = soup.find("span", class_="user-name") is not None  # 用户名(span标签)是否存在
    flag3 = soup.find("a", attrs={"name": "tj_login"}) is None  # "登录"按钮(a标签)是否存在
    return flag3 and (flag1 or flag2)  # cookies可用判定条件: 登录按钮不存在且用户名与退出登录按钮至少存在一个
