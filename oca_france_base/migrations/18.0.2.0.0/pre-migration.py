# Copyright 2026-Today OCA France
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from openupgradelib import openupgrade


@openupgrade.migrate()
def migrate(env, version):
    openupgrade.logged_query(
        env.cr,
        """
        UPDATE res_partner
            SET odoo_worker_qty = 0
            WHERE odoo_worker_qty is null;""",
    )
