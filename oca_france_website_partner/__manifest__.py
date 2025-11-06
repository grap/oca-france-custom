# Copyright 2025-Today OCA France
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "OCA France Customization - Website Partner Module",
    "summary": "Website Partner customization for the OCA France Instance",
    "version": "18.0.1.1.0",
    "license": "AGPL-3",
    "author": "GRAP, OCA France",
    "maintainers": ["legalsylvain"],
    "website": "https://www.oca-france.fr",
    "depends": ["oca_france_base", "website_partner"],
    "auto_install": True,
    "data": ["views/website_partner_templates.xml"],
    "demo": ["demo/res_partner.xml"],
}
