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
    ('first', 'First Member'),
    ('second', 'Second Member'),
]


class EvaluationCertificate(models.Model):

    _name = 'evaluation.certificate'
    _description = 'Evaluation Certificate Model for management thesis'

    name = fields.Char('Tittle of Work', required=True)
    display_name = fields.Char('Display Name', compute='_compute_display_name')
    place = fields.Selection(PLACE_OPTIONS, 'Place', required=True)
    presentation_date = fields.Datetime('Presentation Date', required=True)
    approved_status = fields.Selection(
        APPROVED_STATUS, 'Certificate Status', default='refused')
    professor_line_ids = fields.One2many(
        'professor.line', 'certificate_id', 'Professors')
    student_line_ids = fields.One2many(
        'student.line', 'certificate_id', 'Students')
    tutor_id = fields.Many2one('professor', 'Tutor')
    tutor_cace = fields.Char(related='tutor_id.cace')
    document_file = fields.Binary('Documento adjunto')

    carrer_ids = fields.Many2many(
        'carrer', string='Carrer', compute="compute_carrer", store=True)
    student_ids = fields.Many2many(
        'student', string='Student', compute="compute_student", store=True)

    def evaluate_certificate(self):
        return {
            'name': 'Evaluar',
            'type': 'ir.actions.act_window',
            'res_model': 'evaluation.certificate.wizard',
            'view_mode': 'form',
            'target': 'new',
        }

    @api.depends('name')
    def _compute_display_name(self):
        for certificate in self:
            certificate.display_name = (certificate.name if len(
                certificate.name) <= 64 else (certificate.name[:64] + '...'))

    @api.depends('student_line_ids')
    def compute_carrer(self):
        for certificate in self:
            carrers = certificate.student_line_ids.mapped(
                'student_id.carrer_id')
            certificate.carrer_ids = carrers

    @api.depends('student_line_ids')
    def compute_student(self):
        for certificate in self:
            students = certificate.student_line_ids.mapped('student_id')
            certificate.student_ids = students


class ProfessorLine(models.Model):

    _name = 'professor.line'
    _description = 'Professor Line Model for management thesis professors'

    certificate_id = fields.Many2one('evaluation.certificate', 'Certificate')
    professor_id = fields.Many2one('professor', 'Professor', required=True)
    professor_document = fields.Char(related='professor_id.document')
    professor_cace = fields.Char(related='professor_id.cace')
    jury_type = fields.Selection(JURY_TYPE, 'Jury Type', required=True)


class StudentLine(models.Model):

    _name = 'student.line'
    _description = 'Student Line Model for management thesis students'

    certificate_id = fields.Many2one('evaluation.certificate', 'Certificate')
    student_id = fields.Many2one('student', 'Student', required=True)
    student_document = fields.Char(related='student_id.document')
    student_carrer = fields.Many2one(related='student_id.carrer_id')
    student_degree = fields.Char(related='student_id.carrer_name')
