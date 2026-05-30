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
        # Odoo
        "account",
        "base_iban",
        "base_vat",
        "calendar",
        "contacts",
        "l10n_fr_account",
        "membership",
        "project_account",
        "project_todo",
        "website",
        "website_blog",
        "website_crm",
        "website_project",
        # OCA/account-financial-reporting
        "account_financial_report",
        # OCA/account-financial-tools
        "account_dashboard_banner",
        "account_lock_date_update",
        "account_move_name_sequence",
        "account_usability",
        # OCA/account-payment
        "account_payment_method_base",
        # OCA/account-reconcile
        "account_reconcile_oca",
        # OCA/bank-statement-import
        "account_statement_import_file",
        "account_statement_import_file_reconcile_oca",
        # OCA/community-data-files
        "account_tax_unece",
        # OCA/edi
        "account_invoice_facturx",
        # OCA/geospatial
        "web_leaflet_lib",
        "web_view_leaflet_map",
        "web_view_leaflet_map_partner",
        # OCA/l10n-france
        "l10n_fr_mis_reports",
        # OCA/mail
        "mail_debrand",
        # OCA/mis-builder
        "mis_builder",
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
        # OCA/server-env
        "server_environment",
        "server_environment_ir_config_parameter",
        # OCA/server-tools
        "module_analysis",
        "module_change_auto_install",
        # OCA/server-ux
        "base_technical_features",
        "date_range_account",
        # OCA/social
        "res_company_mastodon_link",
        "res_partner_mastodon_link",
        "res_partner_linkedin_link",
        # OCA/vertical-association
        "website_membership_non_paid_member",
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
        "web_environment_ribbon",
        # OCA/website
        "website_company_mastodon_link",
        "website_odoo_debranding",
        "website_partner_form",
        "website_search_header",
        # oca-france/oca-france-custom
        "oca_france_base",
        "oca_france_membership",
        "oca_france_website_membership",
        "oca_france_website_partner",
        # akretion/bank-statement-import-api
        "account_statement_import_api",
        "account_statement_import_api_qonto",
        "account_statement_import_in_invoice_api",
        "account_statement_import_in_invoice",
    ],
    "maintainers": ["petrus-v", "legalsylvain"],
    "data": [],
    "demo": [],
}
