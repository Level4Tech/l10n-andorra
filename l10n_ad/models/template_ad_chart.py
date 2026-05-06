# -*- coding: utf-8 -*-

from odoo import models, _
from odoo.addons.account.models.chart_template import template


class AccountChartTemplate(models.AbstractModel):
    _inherit = 'account.chart.template'

    @template('ad_common')
    def _get_ad_common_template_data(self):
        return {
            'name': _('PGCE'),
            'visible': 0,
            'property_account_receivable_id': 'account_common_430',
            'property_account_payable_id': 'account_common_410',
            'property_account_expense_categ_id': 'account_common_600',
            'property_account_income_categ_id': 'account_common_700',
        }

    @template('ad_common', 'res.company')
    def _get_ad_common_res_company(self):
        cid = self.env.company.id
        return {
            cid: {
                'account_fiscal_country_id': 'base.ad',
                'bank_account_code_prefix': '572',
                'cash_account_code_prefix': '570',
                'transfer_account_code_prefix': '572999',
                'account_sale_tax_id': 'account_tax_template_s_igi45',
                'account_purchase_tax_id': 'account_tax_template_p_igi45',
                'account_default_pos_receivable_account_id': 'account_common_430',
                'income_currency_exchange_account_id': 'account_common_768',
                'expense_currency_exchange_account_id': 'account_common_668',
                'account_journal_early_pay_discount_loss_account_id': 'account_common_606',
                'account_journal_early_pay_discount_gain_account_id': 'account_common_706',
                'default_cash_difference_income_account_id': 'account_common_778',
                'default_cash_difference_expense_account_id': 'account_common_678',
                'deferred_expense_account_id': 'account_common_480',
                'deferred_revenue_account_id': 'account_common_485',
            },
        }

    @template('ad_full')
    def _get_ad_full_template_data(self):
        return {
            'name': _('PGCE Complert'),
            'parent': 'ad_common',
        }

    @template('ad_full', 'res.company')
    def _get_ad_full_res_company(self):
        return {
            self.env.company.id: {
                'bank_account_code_prefix': '572',
                'cash_account_code_prefix': '570',
                'transfer_account_code_prefix': '572999',
                'account_sale_tax_id': 'account_tax_template_s_igi45',
                'account_purchase_tax_id': 'account_tax_template_p_igi45',
            },
        }
