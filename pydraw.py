from pyecharts.charts import Timeline, Geo
from pyecharts import options as opts
from pyecharts.datasets import COORDINATES
from datetime import datetime, timedelta


def draw_timeline_with_map(message, keyword):
    COORDINATES.cutoff = 0.75  # 地名匹配模糊程度
    tl = Timeline(init_opts=opts.InitOpts(
                width='1300px',
                height='650px',
                bg_color='grey',
                theme='white'
            ))
    tl.add_schema(is_auto_play=False, is_loop_play=True, control_position='left', play_interval=1000)
    start = message['济南']['startDate']
    start = datetime.strptime(start, "%Y-%m-%d").date()
    maxIndex = message['济南'][keyword].copy()
    maxIndex = list(map(int, maxIndex))
    maxIndex.sort()
    maxIndex = maxIndex[3]
    if maxIndex > 1000:
        maxIndex = maxIndex - maxIndex % 1000
    elif maxIndex > 100:
        maxIndex = maxIndex - maxIndex % 100
    for i in range(1, 8):
        city_count_dic = message.copy()
        for key in city_count_dic.keys():
            try:
                city_count_dic[key] = int(city_count_dic[key][keyword][i - 1])
            except:
                city_count_dic[key] = city_count_dic['济南']

        map0 = (
            Geo(init_opts=opts.InitOpts(
                width='1300px',
                height='650px',
                bg_color='grey',
                theme='white'
            )
            )
                .add_schema(maptype="china")
                .add(keyword, [list(z) for z in zip(city_count_dic.keys(), city_count_dic.values())],
                     type_="scatter")
                .set_global_opts(
                title_opts=opts.TitleOpts(title=f"关于{keyword}的搜索指数", pos_left="center", pos_bottom="90%"),
                legend_opts=opts.LegendOpts(pos_left="5%", pos_bottom="10%"),
                visualmap_opts=opts.VisualMapOpts(max_=maxIndex, min_=1, range_text=['搜索指数颜色:', ''], pos_bottom="10%")
                # getMax(city_count_dic.values(), 15)
            )
                .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
        )
        # 给时间轴增加某天的map和天数
        thisday = str(start + timedelta(days=i - 1))
        tl.add(map0, thisday)
    return tl


def find_k(test_list, k):
    flag = test_list[0]
    test_list.pop(0)
    l_list = [i for i in test_list if i < flag]
    r_list = [i for i in test_list if i >= flag]

    # 结果递归的基线条件
    if len(r_list) == k - 1:
        return flag
    elif len(r_list) > k - 1:
        return find_k(r_list, k)
    else:
        # 因为test_list.pop(0)让test_list少了一个元素，所以下面需要+1
        gap = len(test_list) - len(l_list) + 1
        k = k - gap
        return find_k(l_list, k)


def getMax(Nlist, k):
    Nlist = list(Nlist)
    maxIn = find_k(Nlist, k)
    if maxIn > 200000:
        maxIn = 200000
    elif maxIn > 100000:
        maxIn = 100000
    elif maxIn > 50000:
        maxIn = 50000
    elif maxIn > 10000:
        maxIn = 10000
    elif maxIn > 5000:
        maxIn = 5000
    elif maxIn > 100:
        maxIn = maxIn - maxIn % 100
    elif maxIn > 10:
        maxIn = maxIn - maxIn % 10
    else:
        maxIn = 10
    return maxIn
