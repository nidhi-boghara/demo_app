// Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt
/* eslint-disable */

frappe.query_reports["Server side scripting Script Report"] = {
	"filters": [
		{
			"fieldname":"name",
			"label":"Server side scripting",
			"fieldtype":"Link",
			"options":"Server side scripting"
		},
		{
			"fieldname":"birthdate",
			"label":"birthdate",
			"fieldtype":"Date",
			// "options":"Server side scripting"
		},
		{
			"fieldname":"age",
			"label":"Age",
			"fieldtype":"Data",
			// "options":"Server side scripting"
		}
	]
};