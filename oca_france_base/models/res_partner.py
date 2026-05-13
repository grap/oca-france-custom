# Copyright 2025-Today OCA France
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import fields, models


class ResPartner(models.Model):
    _inherit = "res.partner"

    odoo_worker_qty = fields.Integer(
        string="Odoo Workers",
        help="Number of people working on Odoo."
        " (Developer, trainer, functional, management staff)."
        " This information will be used to calculate the amount"
        " of the membership fee for the association.",
        default=0,
    )
