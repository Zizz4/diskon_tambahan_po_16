{
    'name': 'Additional discount for PO',
    'version': '16.0.1.1.0',
    'summary': 'Additional discount for PO',
    'description': """Insert an additional discount for PO""",
    'category': 'Inventory/Purchase',
    'author': 'Muhamad Syahril Aziz',
    'license': 'LGPL-3',
    'depends': ['purchase', 'account'],
    'data': ['views/diskon_tambahan.xml',
             'report/diskon_tambahan_report.xml'],
    'images': ['static/description/icon.svg'],
    'installable': True,
    'auto_install': False
}
