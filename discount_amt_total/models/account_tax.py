from odoo import models, fields, api, _


class AccountTaxInherit(models.Model):
    _inherit = 'account.tax'

    @api.model
    def _get_tax_totals_summary(self, base_lines, currency, company, cash_rounding=None):
        res = super()._get_tax_totals_summary( base_lines, currency, company, cash_rounding)
        total_untaxed_amt = sum(map(lambda l: (l.get('quantity', 0.0) or 0.0) * (l.get('price_unit', 0.0) or 0.0),base_lines ))
        total_after_discount = sum(map(
            lambda l: (l.get('quantity', 0.0) or 0.0) * (l.get('price_unit', 0.0) or 0.0)
                      * (1 - (l.get('discount', 0.0) or 0.0) / 100), base_lines
        ))
        total_discount_amt = total_untaxed_amt - total_after_discount
        res['discount_amt'] = total_discount_amt
        if currency != company.currency_id:
            currency_rate = company.currency_id._get_conversion_rate(currency, company.currency_id, company=None, date=None)
            company_currency_discount_amt = currency_rate * total_discount_amt
            res['company_currency_discount_amt'] = company.currency_id.format(company_currency_discount_amt)
        else:
            res['company_currency_discount_amt'] = False
        return res
