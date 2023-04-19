from odoo import models, api, fields


APPROVED_STATUS = [
    ('refused', 'Refused'),
    ('approved', 'Approved'),
    ('retuned', 'Returned'),
    ('honorific', 'Honorific'),
    ('publication', 'Publication'),
]


class EvaluationCertificateWizard(models.TransientModel):
    _name = 'evaluation.certificate.wizard'
    _description = ''

    evaluation_state = fields.Selection(
        APPROVED_STATUS, string='Status', required=True)

    def evaluate(self):
        for wizard in self:
            active_model = self.env.context.get('active_model')
            model_id = self.env.context.get('active_id')

            certificate = self.env[active_model].browse([model_id])
            certificate.write({'approved_status': wizard.evaluation_state})
        return True
