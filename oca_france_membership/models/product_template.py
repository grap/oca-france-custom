# Copyright 2025-Today OCA France
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import api, fields, models


class ProductTemplate(models.Model):
    _inherit = "product.template"

    membership_fee_by_odoo_worker = fields.Boolean(
        compute="_compute_membership_fee_by_odoo_worker",
        readonly=False,
        store=True,
        string="If Checked, the membership fee will be multiplicated by the"
        " quantity of Odoo workers in the company to compute the total"
        " amount to invoice.",
    )

    @api.depends("membership")
    def _compute_membership_fee_by_odoo_worker(self):
        for template in self:
            template.membership_fee_by_odoo_worker = template.membership
