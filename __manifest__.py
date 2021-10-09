# -*- coding: utf-8 -*-
{
    'name': 'Library pyecharts',
    'version': '12.0.0.1',
    'description': '',
    'author': 'huaqiangyan@163.com',
    'depends': ['web'],
    'data': [
        'security/ir.model.access.csv',
        'data/echarts_type_data.xml',
        'data/dashboard_data.xml',
        # 'views/assets_backend.xml',
        'views/home.xml',
        'views/echarts_type_view.xml',
        'views/dashboard.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'library_pyecharts/static/src/js/echarts.min.js',
            'library_pyecharts/static/src/js/china.js',
            'library_pyecharts/static/src/js/load_echarts_bar.js',
            'library_pyecharts/static/src/css/sb-admin-2.min.css',
        ],
        'web.assets_qweb': [
            'library_pyecharts/static/src/xml/**/*',
        ],
    },
}
