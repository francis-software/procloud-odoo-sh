{
    'name': 'Slack Odoo Connector',
    'version': '1.0',
    'summary': 'A slack connector and sync tool to take your Odoo record communication to the next level.',
    'sequence': 10,
    'description': """A slack connector .""",
    'category': 'Productivity',
    'website': 'https://www.procloud.consulting',
    'license': 'AGPL-3',
    'depends': ['base'],
    'data': [
        'security/ir_model_access.xml', #This line references your security file # other data files like views
    ],
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}

