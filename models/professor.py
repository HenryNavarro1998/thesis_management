from odoo import models, fields, api


class Professor(models.Model):
    _name = "professor"
    _description = "Professor of the University"

    name = fields.Char("Name", required=True)
    document = fields.Char("Identity Document", required=True)
    cace = fields.Char("CACE")
    career_id = fields.Many2one("career", "Career")
    certificate_ids = fields.One2many(
        "evaluation.certificate", "tutor_id", "Evaluation Certificates"
    )
    times_in_jury = fields.Integer(
        "Times in Jury", compute="_compute_times_in_jury"
    )
    signature_image = fields.Image("Signature", max_width=200, max_height=200)

    @api.depends("certificate_ids")
    def _compute_times_in_jury(self):
        for professor in self:
            professor.times_in_jury = len(
                self.env["professor.line"].search(
                    [("professor_id", "=", professor.id)]
                )
            )
