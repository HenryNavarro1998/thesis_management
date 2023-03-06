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
    ('retuned', 'Returned'),
    ('honorific', 'Honorific'),
    ('publication', 'Publication'),
]

JURY_TYPE = [
    ('president', 'President'),
    ('first', 'First Jury'),
    ('second', 'Second Jury'),
]


class EvaluationCertificate(models.Model):

    _name = 'evaluation.certificate'
    _description = 'Evaluation Certificate Model for management thesis'

    name = fields.Char('Tittle of Work', required=True)
    place = fields.Selection(PLACE_OPTIONS, 'Place', required=True)
    presentation_date = fields.Datetime('Presentation Date', required=True)
    approved_status = fields.Selection(
        APPROVED_STATUS, 'Certificate Status', default='refused')
    professor_line_ids = fields.One2many(
        'professor.line', 'certificate_id', 'Professors')
    student_line_ids = fields.One2many(
        'student.line', 'certificate_id', 'Students')
    tutor_id = fields.Many2one('professor', 'Tutor')

    def action_approve_certificate(self):
        self.write({'approved_status': 'approved'})

    def action_refuse_certificate(self):
        self.write({'approved_status': 'refused'})


class ProfessorLine(models.Model):

    _name = 'professor.line'
    _description = 'Professor Line Model for management thesis professors'

    certificate_id = fields.Many2one('evaluation.certificate', 'Certificate')
    professor_id = fields.Many2one('professor', 'Professor', required=True)
    jury_type = fields.Selection(JURY_TYPE, 'Jury Type', required=True)


class StudentLine(models.Model):

    _name = 'student.line'
    _description = 'Student Line Model for management thesis students'

    certificate_id = fields.Many2one('evaluation.certificate', 'Certificate')
    student_id = fields.Many2one('student', 'Student', required=True)
    student_document = fields.Char(related='student_id.document')
    student_carrer = fields.Many2one(related='student_id.carrer_id')
