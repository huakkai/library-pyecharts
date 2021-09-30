from odoo import http
import json
import random
from pyecharts.charts import Bar
from pyecharts import options as opts
from pyecharts.globals import ThemeType

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
        Bar(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
            .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
            .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
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
    c = (
        Bar(init_opts=opts.InitOpts(theme=ThemeType.LIGHT))
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [5, 20, 36, 10, 75, 90])
            .add_yaxis("商家B", [15, 6, 45, 20, 35, 66])
            .set_global_opts(title_opts=opts.TitleOpts(title="主标题", subtitle="副标题"))
            .dump_options_with_quotes()
    )
    return c
