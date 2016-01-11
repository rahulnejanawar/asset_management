from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label":_("Documents"),
			"icon":"icon-star",
			"items":[
				{
					"type":"doctype",
					"name":"Assign",
					"description":_("Assign asset to an Employee."),
				},
				{
					"type":"doctype",
					"name":"Stock Entry",
					"description":_("Record Item Movement."),
				},
				{
					"type":"doctype",
					"name":"Purchase Receipt",
					"description":_("Goods received from Suppliers."),
				},
				{
					"type":"doctype",
					"name":"Employee",
					"description":_("Employee Record."),
				},
				{
					"type":"doctype",
					"name":"Serial No",
					"description":_("Single unit of an Item."),
				},
				{
					"type":"doctype",
					"name":"Item",
					"description":_("All Products or Items."),
				},
			]
		}
	]
