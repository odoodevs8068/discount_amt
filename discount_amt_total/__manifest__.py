{
    'name': "Discount Total Amount",
    'version': '1.2',
    'summary': 'Total Discount Amount In Total Footer',
    'sequence': 10,
    'author': "JD DEVS",
    'depends': ['base','account'],
    'data' : [    ],
    'assets': {
        'web.assets_backend': [
            "discount_amt_total/static/src/css/sty.css",
            "discount_amt_total/static/src/xml/tax_totals_widget.xml",
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
    'images': ['static/description/assets/screenshots/banner.png'],
    'icon': "/discount_amt_total/static/description/icon.png",
    'license': 'AGPL-3',
}

