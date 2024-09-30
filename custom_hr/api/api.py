# import frappe
# from frappe.utils import today, add_days

# def update_last_sync_of_checkin():
#     # Calculate the date for 'today - 1'
#     yesterday = add_days(today(), seconds=-1)

#     # Fetch all Shift Types
#     shift_types = frappe.get_all("Shift Type", fields=["name"])

#     for shift in shift_types:
#         # Update ONLY the last_sync_of_checkin field in the Shift Type doctype to 'yesterday'
#         frappe.db.set_value("Shift Type", shift.name, "last_sync_of_checkin", yesterday)

#     # Commit the changes
#     frappe.db.commit()

# # import frappe
# # from frappe.utils import nowdate, get_datetime

# # def update_last_sync_of_checkin():
# #     # Set the date to today with time 23:59:00
# #     end_of_day = get_datetime(f"{nowdate()} 23:59:00")

# #     # Fetch all Shift Types
# #     shift_types = frappe.get_all("Shift Type", fields=["name"])

# #     for shift in shift_types:
# #         # Update ONLY the last_sync_of_checkin field in the Shift Type doctype to today 23:59:00
# #         frappe.db.set_value("Shift Type", shift.name, "last_sync_of_checkin", end_of_day)

# #     # Commit the changes
# #     frappe.db.commit()

# import frappe
# from frappe.utils import now_datetime, add_to_date

# def update_last_sync_of_checkin():
#     # Get the current date and time, then subtract 1 minute
#     one_minute_ago = add_to_date(now_datetime(), minutes=-1)

#     # Fetch all Shift Types
#     shift_types = frappe.get_all("Shift Type", fields=["name"])

#     for shift in shift_types:
#         # Update ONLY the last_sync_of_checkin field in the Shift Type doctype to 'today - 1 minute'
#         frappe.db.set_value("Shift Type", shift.name, "last_sync_of_checkin", one_minute_ago)

#     # Commit the changes
#     frappe.db.commit()

import frappe
from frappe.utils import add_days, get_datetime, today

def update_last_sync_of_checkin():
    # Get yesterday's date and set the time to 23:59:00
    yesterday_end_of_day = get_datetime(f"{add_days(today(), -1)} 23:59:00")

    # Fetch all Shift Types
    shift_types = frappe.get_all("Shift Type", fields=["name"])

    for shift in shift_types:
        # Update ONLY the last_sync_of_checkin field in the Shift Type doctype to 'yesterday 23:59:00'
        frappe.db.set_value("Shift Type", shift.name, "last_sync_of_checkin", yesterday_end_of_day)

    # Commit the changes
    frappe.db.commit()
