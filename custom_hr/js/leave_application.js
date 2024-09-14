frappe.ui.form.on('Leave Application', {
    refresh: function(frm) {
        frm.add_custom_button(__('Whatsapp SMS'), function() {
            // Add logic for Whatsapp SMS here if required
        });
    },

    before_submit: async function(frm) {
        const current_user = frappe.session.user;

        // Fetch employee's linked user email
        let employee_email = await get_employee_email(frm.doc.employee);

        if (employee_email) {
            // Block submission if current user is the same as the employee's linked email
            if (current_user === employee_email) {
                frappe.throw(__('You cannot submit your own leave application.'));
            }
        }
    }
});

// Helper function to fetch employee's linked email (user_id)
async function get_employee_email(employee_id) {
    try {
        let response = await frappe.call({
            method: "frappe.client.get_value",
            args: {
                doctype: "Employee",
                filters: { name: employee_id },
                fieldname: "user_id"
            }
        });

        if (response && response.message) {
            return response.message.user_id;
        }
    } catch (error) {
        console.error('Error fetching employee email:', error);
        frappe.msgprint(__('Could not fetch employee details.'));
    }
    return null;
}
