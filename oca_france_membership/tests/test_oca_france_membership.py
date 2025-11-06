# Copyright 2025-Today OCA France
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo.tests import tagged

from odoo.addons.membership.tests.common import TestMembershipCommon


@tagged("post_install", "-at_install")
class TestMembership(TestMembershipCommon):
    def test_no_odoo_worker(self):
        self.membership_1.membership_fee_by_odoo_worker = True
        invoice = self.partner_1.create_membership_invoice(self.membership_1, 50.0)
        self.assertEqual(invoice.amount_untaxed, 50.0)

    def test_many_odoo_workers_fee_proportional(self):
        self.partner_1.odoo_worker_qty = 20
        self.membership_1.membership_fee_by_odoo_worker = True
        invoice = self.partner_1.create_membership_invoice(self.membership_1, 50.0)
        self.assertEqual(invoice.amount_untaxed, 1000.0)

    def test_many_odoo_workers_fee_no_proportional(self):
        self.partner_1.odoo_worker_qty = 20
        self.membership_1.membership_fee_by_odoo_worker = False
        invoice = self.partner_1.create_membership_invoice(self.membership_1, 50.0)
        self.assertEqual(invoice.amount_untaxed, 50.0)
