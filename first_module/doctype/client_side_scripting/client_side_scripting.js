// Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
// For license information, please see license.txt

frappe.ui.form.on('Client side scripting', {
	refresh: function(frm) {
		// frappe.msgprint("Hello Sigzen")
		// frappe.throw("hello sigzen from different method")

		// after_save:function(frm)
		// {
		// 	frappe.msgprint(__("The full name is '{0}'",
		// 	                 [frm.doc.firstname+" "+frm.doc.middlename+""+frm.doc.lastname]))
		// }
		if(frm.is_new())
		{
			frm.set_intro("Now you can create a new client side  scripting doctype")

		}
        // validate:function(frm)
		// {
		// 	frm.set_value('Full Name',frm.doc.firstname+""+frm.doc.middlename+""frm.doc.lastname)
		// }
	// refresh: function(frm)
	// {
	// 		frm.add_custom_button('Click me button',()=>{
	// 			frappe.msgprint(__('You clicked me'));
	// 		})
	// }	

	}
});
