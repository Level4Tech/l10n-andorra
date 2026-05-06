# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

# List of contributors:
# Marc Tormo <marc@batista10.cat>

{
    'name': 'Andorra - Accounting',
    'version': '18.0.1.0.1',
    'summary': 'Andorra: PGCE, IGI, retencions (localització comptable).',
    'author': 'Batista10',
    'website': 'https://www.batista10.cat',
    'category': 'Accounting/Localizations/Account Charts',
    'icon': '/account/static/description/l10n.png',
    'description': """
Localització comptable - Andorra
================================

* Pla general comptable (simplificat i complet)
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
    'application': True,
    'license': 'AGPL-3',
}
