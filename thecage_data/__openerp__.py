{
    'name': 'Initialization data',
    'version': '1.0.0',
    'author': 'IT-Projects LLC, Veronika Kotovich',
    'license': 'LGPL-3',
    'website': 'https://twitter.com/vkotovi4',
    'category': 'Other',
    'description': """

    """,
    'depends': ['l10n_sg',
                'pitch_booking',
                'multi_company',
                'sms_sg',
                'sale_order_hide_tax',
                'res_partner_phone',
                'account_analytic_analysis',
                'booking_calendar_analytic',
                'website_sale_order_company',
                'invoice_sale_order_line_group',
                ],
    'data': [
        'data.xml',
        'views/view.xml',
        'security/ir.model.access.csv',
    ],
    'installable': False,
    'auto_install': False,
}
