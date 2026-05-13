# Copyright 2026-Today OCA France
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class MembershipMembershipLine(models.Model):
    _inherit = "membership.membership_line"

    odoo_worker_qty = fields.Integer(related="partner.odoo_worker_qty")

    def search(self, domain, offset=0, limit=None, order=None):
        if self.env.context.get("membership_line_order_by_workers"):
            order = "odoo_worker_qty desc"
        return super().search(domain, offset=offset, limit=limit, order=order)
