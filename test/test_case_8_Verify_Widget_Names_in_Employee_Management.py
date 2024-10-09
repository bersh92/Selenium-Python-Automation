
list_of_expected_widgets = ['Quick Access', 'Time At Work', 'Employees on Leave Today', 'Latest News', 'Latest Documents', 'Performance Quick Feedback', "Current Year's Leave Taken by Department", 'Buzz Latest Posts', 'Leave Taken on Each Day of the Week Over Time', 'Leave Scheduled in Each Month', 'Leave Taken on Each Calendar Month Over the Years', 'Headcount by Location', 'Annual Basic Payment by Location', 'My Actions']

def test_case_8_verify_retrieval_of_widget_names_in_employee_management_component(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button("Employee Management")
    app.orangeHrm.employeeManagement.click_home()
    app.assert_that(sorted(app.orangeHrm.employeeManagement.get_widgets_headers())).is_equal_to(sorted(list_of_expected_widgets))