from odoo import models, fields, api


class Professor(models.Model):

    _name = 'professor'
    _description = 'Professor of the University'

    name = fields.Char('Name', required=True)
    id_document = fields.Char('Identity Document', required=True)
    times_in_jury = fields.Integer('Times in Jury')
