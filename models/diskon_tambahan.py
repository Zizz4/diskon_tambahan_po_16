from odoo import fields, models, api


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    diskon_tambahan = fields.Float(string="Diskon Tambahan (Rp)")

    @api.depends('order_line.taxes_id', 'order_line.price_subtotal', 'amount_total', 'amount_untaxed', 'diskon_tambahan')
    def _compute_tax_totals(self):
        for order in self:
            order_lines = order.order_line.filtered(lambda x: not x.display_type)
            order.tax_totals = self.env['account.tax']._prepare_tax_totals(
                [x._convert_to_tax_base_line_dict() for x in order_lines],
                order.currency_id or order.company_id.currency_id,
            )

    _sql_constraints = [
        (
            "diskon_tambahan_limit",
            "CHECK (diskon_tambahan >= tax_totals)",
            "Diskon tambahan tidak bisa lebih besar dari total harga",
        )
    ]

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"

    def _convert_to_tax_base_line_dict(self):
        vals = super()._convert_to_tax_base_line_dict()
        vals.update({"diskon_tambahan": self.order_id.diskon_tambahan})
        return vals
