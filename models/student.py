from odoo import models, fields, api, _


class Student(models.Model):
    _name = "student"
    _description = "Student of the University"

    name = fields.Char("Name", required=True)
    document = fields.Char("Identity Document", required=True)
    career_id = fields.Many2one("career", "College career", required=True)
    career_name = fields.Char(
        "Career Degree", related="career_id.technical_name"
    )
