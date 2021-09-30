from odoo import fields, models, api, _
from odoo.exceptions import ValidationError


class EchartsType(models.Model):
    _name = 'echarts.type'
    _description = 'Echarts Type'

    name = fields.Char(string='Name')
    etype = fields.Char(string='Etype')
