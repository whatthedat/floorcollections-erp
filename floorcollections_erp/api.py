import frappe

@frappe.whitelist()
def hello():
    return "Floor Collection ERP"
