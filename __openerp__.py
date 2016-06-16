{
    'name':'ITI HR',
    'version': '1.0',
    'depends':['hr','hr_attendance','hr_holidays','hr_contract'],
    'description': """
ITI HRR
==========================
    """,
    'data': [
        'myodoo_view.xml',
        'security/myodoo_security.xml',
        'security/ir.model.access.csv',
        'views/first_report.xml',
        'views/leaves_report.xml',
        'myodoo_report.xml',
        'wizard/hr_holidays_summary_employee_view.xml',
        'wizard/hr_employee_salary.xml',

    ],
}