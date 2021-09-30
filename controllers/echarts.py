from odoo import http
import json
import random
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.charts import Pie
from pyecharts.faker import Faker

import logging

_logger = logging.getLogger(__name__)


class PyEcharts(http.Controller):
    @http.route('/pyecharts', auth='public', type='http', cors='*', methods=['POST', 'GET'], csrf=False)
    def pyecharts(self):
        return json.dumps({
            'bar1': json.loads(bar1_base()),
            'bar2': json.loads(bar2_base()),
            'bar3': json.loads(bar3_base()),
            'bar4': json.loads(bar4_base()),
        })


def bar1_base():
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [random.randint(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [random.randint(0, 100) for _ in range(6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
            .dump_options_with_quotes()
    )
    return c


def bar3_base():
    c = (
        Pie()
            .add("", [list(z) for z in zip(Faker.choose(), Faker.values())])
            .set_global_opts(title_opts=opts.TitleOpts(title="Pie-基本示例"))
            .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
            .dump_options_with_quotes()
    )
    return c


def bar2_base():
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
            .dump_options_with_quotes()
    )
    return c


def bar4_base():
    x_data = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    y_data = [820, 932, 901, 934, 1290, 1330, 1320]

    c = (
        Line()
            .set_global_opts(
            tooltip_opts=opts.TooltipOpts(is_show=False),
            xaxis_opts=opts.AxisOpts(type_="category"),
            yaxis_opts=opts.AxisOpts(
                type_="value",
                axistick_opts=opts.AxisTickOpts(is_show=True),
                splitline_opts=opts.SplitLineOpts(is_show=True),
            ),
        )
            .add_xaxis(xaxis_data=x_data)
            .add_yaxis(
            series_name="",
            y_axis=y_data,
            symbol="emptyCircle",
            is_symbol_show=True,
            label_opts=opts.LabelOpts(is_show=False),
        )
            .dump_options_with_quotes()
    )
    return c
