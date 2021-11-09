from odoo import fields, models, api, _
from odoo.exceptions import ValidationError

NOTICE_TYPE = [
    ('normal', 'Normal'),
    ('urgent', 'Urgent'),
]


class EchartsNotice(models.Model):
    _name = 'echarts.notice'
    _description = 'Echarts Notice'

    name = fields.Char(string='Name')
    ntype = fields.Selection(selection=NOTICE_TYPE, required=True, default='normal', string='Notice Type')
    title = fields.Char(string='Title', required=True)
    content = fields.Text(string='Context', required=True)
    is_valid = fields.Boolean(string='Is Valid', default=True)
