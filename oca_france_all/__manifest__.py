# Copyright 2025-Today OCA France
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    "name": "OCA France Customization - All",
    "summary": "Reproduce OCA France Instance installing all dependencies",
    "version": "18.0.1.0.0",
    "license": "AGPL-3",
    "author": "Pierre Verkest, OCA France",
    "website": "https://www.oca-france.fr",
    "depends": [
        # OCA France
        "oca_france_base",
        "oca_france_membership",
        "oca_france_website_membership",
        "oca_france_website_partner",
        # OCA
        "base_technical_features",
        "disable_odoo_online",
        "mail_debrand",
        "module_change_auto_install",
        "partner_disable_gravatar",
        "portal_odoo_debranding",
        "remove_odoo_enterprise",
        "res_company_mastodon_link",
        "web_dialog_size",
        "web_editor_disable_chatgpt",
        "web_no_bubble",
        "web_refresher",
        "web_remember_tree_column_width",
        "web_responsive",
        "web_save_discard_button",
        "web_theme_classic",
        "website_company_mastodon_link",
        "website_partner_form",
        "website_odoo_debranding",
        "website_search_header",
        # Odoo
        "contacts",
        "membership",
        "website",
    ],
    "maintainers": ["petrus-v"],
    "data": [],
    "demo": [],
}
