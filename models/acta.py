# -*- coding: utf-8 -*-

from odoo import models, fields, api


class TestModel(models.Model):
    _name = 'acta'
    _description = 'thesis_management.thesis_management'

    name = fields.Char('Nombresito')
    value = fields.Integer('Numero')
    description = fields.Text()
    is_check = fields.Boolean()

    @api.onchange('is_check')
    def _onchange_is_check(self):
        for acta in self:
            print('\n\n')
            print('QLQ ALejandra')
            print('\n\n')
            acta.name = acta.name if acta.is_check else 'Pedro'
