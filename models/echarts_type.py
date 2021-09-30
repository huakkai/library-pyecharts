from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class EchartsType(models.Model):
    _name = 'echarts.type'
    _description = 'Echarts Type'

    name = fields.Char(string='Name')
    etype = fields.Char(string='Etype')
    is_toolbox = fields.Boolean(string='Display ToolboxOpts')
    is_title = fields.Boolean(string='Display TitleOpts')
    title = fields.Char(string='TitleOpts')
    is_subtitle = fields.Boolean(string='Display SubTitle')
    subtitle = fields.Char(string='SubTitle')
