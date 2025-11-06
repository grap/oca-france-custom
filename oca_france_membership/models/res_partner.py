# Copyright 2025-Today OCA France
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import _, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    def create_membership_invoice(self, product, amount):
        invoices = super().create_membership_invoice(product, amount)
        if not product.membership_fee_by_odoo_worker:
            return invoices
        for invoice_line in invoices.mapped("invoice_line_ids").filtered(
            lambda x: x.product_id == product
        ):
            worker_qty = invoice_line.move_id.partner_id.odoo_worker_qty
            if worker_qty > 1:
                invoice_line.name += _(
                    "\n(For %(worker_qty)d Workers).", worker_qty=worker_qty
                )
                invoice_line.quantity = worker_qty
        return invoices
