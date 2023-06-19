# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Serversidescripting(Document):
       


    #frappe.get_doc(doctype,name)
    # def validate(self):
    #     self.get_document()
    # def get_document(self):
    #     doc=frappe.get_doc("Client side scripting",self.client_side_doc)
    #     frappe.msgprint(("The first name is {0} and age is {1}").format(doc.firstname,doc.age))
    
    #frappe.new_doc(doctype,name)    
    # def validate(self):
    #     self.new_document()
    # def new_document(self):
    #     doc=frappe.new_doc("Client side scripting")  
    #     doc.firstname="nidhi"
    #     doc.lastname="patel"
    #     doc.age=21
    #     doc.append("familymembers",{"name":"shruti","relation":"sister","age":23})
    #     doc.insert()
    
    # #frappe.del_doc(doctype,name)    
    # def validate(self):
    #     self.delete_document()
    # def delete_document(self):
    #     doc=frappe.delete_doc("Client side scripting","PR-0002")  
    
    
    # # frappe.db.exist(doctype,name)
    # def validate(self):
    #     if frappe.db.exist("Client side scripting","PR-0003"):
    #         frappe.msgprint("The document is exist in database")
    #     else:
    #         frappe.msgprint("The document does not exist in database")
    
    # # frappe.db.count(dtoctype,filters)
    # def validate(self):
        # doc_count=frappe.db.count("Client side scripting",{"enable":1})
        # frappe.msgprint(("The enable document count is {0}").format(doc_count))
          
    # frappe.db.sql(query,filter,as_dict)
    def validate(self):
        self.sql
    def sql(self):
        data=frappe.db.sql("select firstname,age from `tabClient side scripting` where enable=1",as_dict=1)
        for d in data:
            frappe.msgprint("The parent first name is {0} and last name is {1}").format(d.firstname,d.age)
        
        
    # def validate(self):
    #     frappe.msgprint(("hello my full name is '{0}'").format(self.firstname+ " "+self.middlename+" "+self.lastname))
    
    # def validate(self):
    #     for row in self.get("familymembers"):
    #         frappe.msgprint(("{0}. The family member name is '{1}' and relation is '{2}'").format(row.name,row.relation))
    
    
    
    # def before_save(self):
    #     frappe.throw("hello frappe from before_save event")
        
    # def before_insert(self):
    #     frappe.throw("hello frappe from before_insert event")
        
    # def after_insert(self):
    #     frappe.throw("hello frappe from after_insert event")
    
    # def on_update(self):
    #     frappe.throw("hello frappe from on_update event")
    
    # def before_submit(self):
    #     frappe.throw("hello frappe from before_submit event")
    
    # def on_submit(self):
    #     frappe.throw("hello frappe from on_submit event")
    
    # def on_cancel(self):
    #     frappe.throw("hello frappe from on_cancel event")
    
    # def on_trash(self):
    #     frappe.throw("hello frappe from on_trash event")
    
    # def after_delete(self):
    #     frappe.throw("hello frappe from after_delete event")