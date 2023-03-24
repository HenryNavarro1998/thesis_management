from odoo import api, fields, models


class CollegeCarrer(models.Model):

    _name = 'carrer'
    _description = 'Carrer'

    name = fields.Char('Name', required=True)
    technical_name = fields.Char('Technical Name')
    certificate_ids = fields.Many2many('evaluation.certificate', string='Evaluation Certificates')
