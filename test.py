from pyecharts.charts import Timeline, Geo
from pyecharts import options as opts
from pyecharts.datasets import COORDINATES
from pyecharts.globals import ChartType
import info

keyword = 'a'
city_count_dic = info.location_code.copy()
COORDINATES.cutoff = 0.75
map0 = (
    Geo(init_opts=opts.InitOpts(

        # 设置宽度、高度
        width='1300px',
        height='650px',
        bg_color='grey',
        theme='white'
    )
    )
        .add_schema(maptype="china")
        .add(
        keyword, [list(z) for z in zip(city_count_dic.keys(), city_count_dic.values())],
        type_="scatter"
    )
        .set_global_opts(
        title_opts=opts.TitleOpts(title=f"关于{keyword}的搜索指数", pos_left="center", pos_bottom="90%"),
        legend_opts=opts.LegendOpts(pos_left="5%", pos_bottom="10%"),
        visualmap_opts=opts.VisualMapOpts(max_=max(city_count_dic.values()), min_=1,
                                          range_text=['搜索指数颜色:', ''], pos_bottom="10%")
    )
        .set_series_opts(label_opts=opts.LabelOpts(is_show=False))
)
