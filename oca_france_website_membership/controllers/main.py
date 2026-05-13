# Copyright 2026-Today OCA France
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo.http import request, route
from odoo.tools import frozendict

from odoo.addons.website_membership.controllers.main import WebsiteMembership


class WebsiteMembership(WebsiteMembership):
    @route()
    def members(self, *args, **kwargs):
        """Inject a context for being queried later on the search
        of the membership lines for ordering result.
        """
        request.env.context = frozendict(
            request.env.context, membership_line_order_by_workers=True
        )
        return super().members(*args, kwargs)
