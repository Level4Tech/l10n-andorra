# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# List of contributors:
# Marc Tormo <marc@batista10.cat>

{
    'name': 'Andorra - Accounting',
    'version': '18.0.1.0.3',
    'summary': 'PGCE, IGI, retencions IRPF i posicions fiscals (Andorra).',
    'author': 'Batista10',
    'website': 'https://www.batista10.cat',
    'countries': ['ad'],
    'category': 'Accounting/Localizations/Account Charts',
    'icon': '/account/static/description/l10n.png',
    'description': """
Localització comptable — Andorra
=================================

* Plantilles de pla general comptable (PGCE simplificat i complet)
* Plantilles d'impostos (IGI) i retencions (IRPF)
* Posicions fiscals
""",
    'depends': [
        'account',
        'base_iban',
        'base_vat',
    ],
    'data': [
        'data/account.account.tag.csv',
    ],
    'installable': True,
    'application': False,
    'license': 'AGPL-3',
}
