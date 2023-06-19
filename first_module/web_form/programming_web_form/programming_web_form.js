frappe.ready(function() {
	// bind events here

	// frappe.web_form.after_load = () =>{
	// 	frappe.msgprint("Please fill all values carefully");
	// };

	 frappe.web_form.after_load = () =>{
		frappe.web_form.on('enable',(field,value) => {
			frappe.msgprint("Hii User");
		});
	 }

})