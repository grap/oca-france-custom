# Copyright 2025-Today OCA France
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "OCA France Customization - Membership Module",
    "summary": "Membership customization for the OCA France Instance",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "GRAP, OCA France",
    "maintainers": ["legalsylvain"],
    "website": "https://www.oca-france.fr",
    "depends": ["oca_france_base", "membership"],
    "auto_install": True,
    "data": [
        "views/view_product_template.xml",
    ],
    "demo": [
        "demo/product_template.xml",
        "demo/res_partner.xml",
    ],
}
