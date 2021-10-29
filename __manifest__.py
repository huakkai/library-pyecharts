# -*- coding: utf-8 -*-
{
    'name': 'Library pyecharts',
    'version': '13.0.0.1',
    'description': '',
    'author': 'huaqiangyan@163.com',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'data/echarts_type_data.xml',
        'data/dashboard_data.xml',
        'views/assets_backend.xml',
        'views/home.xml',
        'views/echarts_type_view.xml',
        'views/dashboard.xml',
    ],
    'qweb': ['static/src/xml/*.xml'],
    'js': ['static/src/js/*.js'],
}
