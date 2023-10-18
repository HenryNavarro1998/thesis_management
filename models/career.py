from odoo import api, fields, models


class CollegeCareer(models.Model):
    _name = "career"
    _description = "Models for registration of academic career"

    name = fields.Char("Name", required=True)
    technical_name = fields.Char("Technical Name")
    certificate_ids = fields.Many2many(
        "evaluation.certificate", string="Evaluation Certificates"
    )
