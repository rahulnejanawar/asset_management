# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "asset_management"
app_title = "Asset Management"
app_publisher = "Frappe"
app_description = "App for managing IT/Fixed Assets"
app_icon = "octicon octicon-device-desktop"
app_color = "#ff6666"
app_email = "rahul@desieats.com"
app_version = "0.0.1"
app_license = "GNU General Public License"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/asset_management/css/asset_management.css"
# app_include_js = "/assets/asset_management/js/asset_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/asset_management/css/asset_management.css"
# web_include_js = "/assets/asset_management/js/asset_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "asset_management.install.before_install"
# after_install = "asset_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "asset_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"asset_management.tasks.all"
# 	],
# 	"daily": [
# 		"asset_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"asset_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"asset_management.tasks.weekly"
# 	]
# 	"monthly": [
# 		"asset_management.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "asset_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "asset_management.event.get_events"
# }

