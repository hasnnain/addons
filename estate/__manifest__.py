{
    'name': "Real-Estate Management",
    'version': '1.0',
    'depends': ['base'],
    'author': "Hasnain Mutafa",
    'category': 'Category',
    'description': """
        This is a assignment module of Real-Estate Management!
        Assigned by Axiom.
    """,
    'data': [
'security/ir.model.access.csv',
'views/estate_property_views.xml',
'views/property_type_view.xml',
'views/property_tag_view.xml',
'views/estate_menus.xml',
'views/res_users_view.xml',

    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
