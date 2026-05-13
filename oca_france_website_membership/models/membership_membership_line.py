# Copyright 2026-Today OCA France
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models
from odoo.tools import frozendict


class MembershipMembershipLine(models.Model):
    _inherit = "membership.membership_line"

    odoo_worker_qty = fields.Integer(related="partner.odoo_worker_qty")

    def search(self, *args, **kwargs):
        if self.env.context.get("membership_line_order_by_workers"):
            _kwargs = frozendict(kwargs, order="odoo_worker_qty desc")
            return super().search(*args, **_kwargs)
        return super().search(*args, **kwargs)
