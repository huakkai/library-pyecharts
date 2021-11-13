from odoo import fields, models, api, _


class View(models.Model):
    _inherit = 'ir.ui.view'

    type = fields.Selection(selection_add=[('bar', 'Bar'), ('pie', 'Pie')])


class ActWindowView(models.Model):
    _inherit = 'ir.actions.act_window.view'

    view_mode = fields.Selection(selection_add=[('bar', "Bar"), ('pie', 'Pie')], ondelete={'bar': 'cascade', 'pie': 'cascade'})
