from odoo import api, fields, models


class CollegeCarrer(models.Model):

    _name = 'college.carrer'

    name = fields.Char('Name', required=True)
    certificate_ids = fields.One2many(
        'evaluation.certificate', 'carrer_id', 'Evaluation Certificates')
