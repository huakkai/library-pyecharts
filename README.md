# library-pyecharts

#### 介绍

library_pyecharts具有体积小、易扩展、易使用等特点，方便开发人员专注业务层面的逻辑开发，轻松实现多角度的数据展现与分析

![Image text](https://gitee.com/esplets/library-pyecharts/raw/14.0/static/img/example8.png)

![Image text](https://gitee.com/esplets/library-pyecharts/raw/14.0/static/img/example2.png)

![Image text](https://gitee.com/esplets/library-pyecharts/raw/14.0/static/img/example4.jpg)

#### 界面展示支持配置

适配栅格系统：column为界面纵向展示图表数

![Image text](https://gitee.com/esplets/library-pyecharts/raw/14.0/static/img/example5.jpg)

![Image text](https://gitee.com/esplets/library-pyecharts/raw/14.0/static/img/example6.jpg)

![Image text](https://gitee.com/esplets/library-pyecharts/raw/14.0/static/img/example7.jpg)

#### 扩展开发

##### API

```
def heatmap_base():
    value = [[i, j, random.randint(0, 50)] for i in range(24) for j in range(7)]
    c = (
        HeatMap()
            .add_xaxis(Faker.clock)
            .add_yaxis("series0", Faker.week, value)
            .set_global_opts(
            title_opts=opts.TitleOpts(title="HeatMap-基本示例"),
            visualmap_opts=opts.VisualMapOpts(),
        ).dump_options_with_quotes()
    )
    return c
```

##### 基于元数据的自定义配置

```
TODO
```

#### 软件架构

BI


#### 安装教程

pyecharts

#### 使用说明

支持版本：

12.0

...

14.0

#### 参与贡献

1.  Fork 本仓库
2.  新建 Feat_xxx 分支
3.  提交代码
4.  新建 Pull Request

#### 关于

1、本模块完全开源，无任何使用限制，但请在使用代码时保留版权信息

2、为了有持续功能迭代的动力，如果您对此模块感兴趣，请通过star或者fork或者留言或者等等其他方式让我知道你在关注。切忌无脑download，没有意义

3、如果您有好的想法或者建议，请提交代码或者评论意见。Talk is cheap, show me the code.
