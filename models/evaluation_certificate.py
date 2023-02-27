# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

PLACE_OPTIONS = [
    ('chilemex', 'Chilemex'),
    ('asia', 'Villa Asia'),
    ('atlantico', 'Ciudad Universitaria'),
    ('online', 'Video Conferencia'),
    ('admin', 'Edificio Adiministrativo')
]

APPROVED_STATUS = [
    ('refused', 'Refused'),
    ('approved', 'Approved'),
]


class EvaluationCertificate(models.Model):

    _name = 'evaluation.certificate'
    _description = 'Evaluation Certificate Model for management thesis'

    name = fields.Char('Tittle of Work', required=True)
    place = fields.Selection(PLACE_OPTIONS, 'Place', required=True)
    presentation_date = fields.Datetime('Presentation Date', required=True)
    approved_status = fields.Selection(
        APPROVED_STATUS, 'Certificate Status', default='refused')

    student_line_ids = fields.One2many(
        'student.line', 'certificate_id', 'Students')

    carrer_id = fields.Many2one('college.carrer', 'College Carrer')

    def action_approve_certificate(self):
        self.write({'approved_status': 'approved'})

    def action_refuse_certificate(self):
        self.write({'approved_status': 'refused'})


class StudentLine(models.Model):

    _name = 'student.line'
    _description = 'Student Line Model for management thesis students'

    certificate_id = fields.Many2one(
        'evaluation.certificate', 'Certificate')

    student_id = fields.Many2one('student', 'Student')