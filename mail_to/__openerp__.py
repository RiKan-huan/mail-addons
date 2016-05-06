# -*- coding: utf-8 -*-
{
    "name": """Show message recipients""",
    "summary": """Allows you be sure, that all discussion participants were notified""",
    "category": "Discuss",
    "images": [],
    "version": "1.0.0",

    "author": "IT-Projects LLC, Pavel Romanchenko",
    "website": "https://it-projects.info",
    "license": "LGPL-3",
    #"price": 9.00,
    #"currency": "EUR",

    "depends": [
        'mail_base',
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        'templates.xml',
    ],
    "qweb": [
        'static/src/xml/recipient.xml',
    ],
    "demo": [],
    "installable": True,
    "auto_install": False,
}