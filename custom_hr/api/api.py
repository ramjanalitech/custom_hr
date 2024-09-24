import frappe
from frappe.utils import today, add_days

def update_last_sync_of_checkin():
    # Calculate the date for 'today - 1'
    yesterday = add_days(today(), -1)

    # Fetch all Shift Types
    shift_types = frappe.get_all("Shift Type", fields=["name"])

    for shift in shift_types:
        # Update ONLY the last_sync_of_checkin field in the Shift Type doctype to 'yesterday'
        frappe.db.set_value("Shift Type", shift.name, "last_sync_of_checkin", yesterday)

    # Commit the changes
    frappe.db.commit()
