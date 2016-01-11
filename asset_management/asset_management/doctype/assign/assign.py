# -*- coding: utf-8 -*-
# Copyright (c) 2015, Frappe and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import _
from frappe.model.document import Document



class Assign(Document):
	print "in Assign class--"
	
	def validate(self):
		
		for item in doc.asset_table:
			if not item.serial_no:
   				frappe.throw('Item {0} should not there'.format(item.idx))
