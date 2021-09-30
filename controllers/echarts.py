from odoo import http
import json
import random
from pyecharts.charts import Bar
from pyecharts import options as opts

import logging

_logger = logging.getLogger(__name__)


class PyEcharts(http.Controller):
    @http.route('/pyecharts', auth='public', type='http', cors='*', methods=['POST', 'GET'], csrf=False)
    def pyecharts(self):
        return json.dumps(json.loads(bar_base()))


def bar_base():
    c = (
        Bar()
            .add_xaxis(["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"])
            .add_yaxis("商家A", [random.randint(0, 100) for _ in range(6)])
            .add_yaxis("商家B", [random.randint(0, 100) for _ in range(6)])
            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
            .dump_options_with_quotes()
    )
    return c
