# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError

PLACE_OPTIONS = [
    ("chilemex", "Chilemex"),
    ("asia", "Villa Asia"),
    ("atlantico", "University City"),
    ("online", "Video Conference"),
    ("admin", "Administrative building"),
]

APPROVED_STATUS = [
    ("refused", "Refused"),
    ("approved", "Approved"),
    ("returned", "Returned"),
    ("honorific", "Mention Honorific"),
    ("publication", "Mention Publication"),
]

JURY_TYPE = [
    ("president", "President"),
    ("first", "First Member"),
    ("second", "Second Member"),
]


class EvaluationCertificate(models.Model):
    _name = "evaluation.certificate"
    _description = "Evaluation Certificate Model for management thesis"

    name = fields.Char("Tittle of Work", required=True)
    place = fields.Selection(PLACE_OPTIONS, "Place", required=True)
    presentation_date = fields.Datetime("Presentation Date", required=True)
    approved_status = fields.Selection(
        APPROVED_STATUS, "Certificate Status", default="refused"
    )
    professor_line_ids = fields.One2many(
        "professor.line", "certificate_id", "Professors"
    )
    student_line_ids = fields.One2many(
        "student.line", "certificate_id", "Students"
    )
    tutor_id = fields.Many2one("professor", "Tutor")
    tutor_cace = fields.Char(related="tutor_id.cace")
    document_file = fields.Binary("Adjunct document")

    career_ids = fields.Many2many(
        "career", string="Career", compute="compute_career", store=True
    )
    student_ids = fields.Many2many(
        "student", string="Student", compute="compute_student", store=True
    )

    def print_certificate(self):
        action_report = "thesis_management.action_evaluation_certificate_report"
        return self.env.ref(action_report).report_action(self)

    @api.depends("student_line_ids")
    def compute_career(self):
        for certificate in self:
            careers = certificate.student_line_ids.mapped(
                "student_id.career_id"
            )
            certificate.career_ids = careers

    @api.depends("student_line_ids")
    def compute_student(self):
        for certificate in self:
            students = certificate.student_line_ids.mapped("student_id")
            certificate.student_ids = students


class ProfessorLine(models.Model):
    _name = "professor.line"
    _description = "Professor Line Model for management thesis professors"

    certificate_id = fields.Many2one("evaluation.certificate", "Certificate")
    professor_id = fields.Many2one("professor", "Professor", required=True)
    professor_document = fields.Char(related="professor_id.document")
    professor_cace = fields.Char(related="professor_id.cace")
    jury_type = fields.Selection(JURY_TYPE, "Jury Type", required=True)


class StudentLine(models.Model):
    _name = "student.line"
    _description = "Student Line Model for management thesis students"

    certificate_id = fields.Many2one("evaluation.certificate", "Certificate")
    student_id = fields.Many2one("student", "Student", required=True)
    student_document = fields.Char(related="student_id.document")
    student_career = fields.Many2one(related="student_id.career_id")
    student_degree = fields.Char(related="student_id.career_name")
