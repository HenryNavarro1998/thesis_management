# -*- coding: utf-8 -*-
{
    'name': "Thesis Management",
    'summary': "Allows the registration and management of Degree Thesis.",
    'description': "Module developed to fulfill community service.",
    'author': "Alejandra Turen, Fatima Ospina, Henry Guzman and Henry Navarro",
    'category': 'Uncategorized',
    'version': '1.0.0',
    'license': 'LGPL-3',
    'depends': ['base'],
    'data': [
        'security/thesis_management_security.xml',
        'security/ir.model.access.csv',
        'reports/evaluation_certificate_reports.xml',
        'reports/evaluation_certificate_report_view.xml',
        'wizards/evaluation_certificate_wizard_views.xml',
        'views/jury_views.xml',
        'views/evaluation_certificate_views.xml',
        'views/student_views.xml',
        'views/professor_views.xml',
        'views/carrer_views.xml',
        'views/menu_views.xml',
    ],
}
