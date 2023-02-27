from odoo import models, fields, api


class Student(models.Model):

    _name = 'student'
    _description = 'Student of the University'

    name = fields.Char('Name', required=True)
    id_document = fields.Char('Identity Document', required=True)
