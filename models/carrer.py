from odoo import api, fields, models


class CollegeCarrer(models.Model):

    _name = 'carrer'
    _description = 'Carrer'

    name = fields.Char('Name', required=True)
    certificate_ids = fields.Many2many(
        'evaluation.certificate', string='Evaluation Certificates')
