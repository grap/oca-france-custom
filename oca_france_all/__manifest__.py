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
        # OCA/geospatial
        "web_leaflet_lib",
        "web_view_leaflet_map",
        "web_view_leaflet_map_partner",
        # OCA/mail
        "mail_debrand",
        # OCA/partner-contact
        "partner_disable_gravatar",
        "partner_firstname",
        # OCA/server-auth
        "user_log_view",
        # OCA/server-backend
        "base_user_role",
        # OCA/server-brand
        "disable_odoo_online",
        "portal_odoo_debranding",
        "remove_odoo_enterprise",
        # OCA/server-tools
        "module_change_auto_install",
        # OCA/server-ux
        "base_technical_features",
        # OCA/social
        "res_company_mastodon_link",
        # OCA/web
        "web_dialog_size",
        "web_editor_disable_chatgpt",
        "web_favicon",
        "web_no_bubble",
        "web_refresher",
        "web_remember_tree_column_width",
        "web_responsive",
        "web_save_discard_button",
        "web_theme_classic",
        # OCA/website
        "website_company_mastodon_link",
        "website_odoo_debranding",
        "website_partner_form",
        "website_search_header",
        # Odoo
        "contacts",
        "membership",
        "website",
    ],
    "maintainers": ["petrus-v", "legalsylvain"],
    "data": [],
    "demo": [],
}
