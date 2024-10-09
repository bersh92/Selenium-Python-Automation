
def test_case_4_verify_user_can_be_filtered_by_name(app):
    app.orangeHrm.openUrl('https://www.google.com')
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_on_filter()
    app.orangeHrm.popUp.set_username('Admin')
    app.orangeHrm.popUp.click_on_search()
    app.assert_that(app.orangeHrm.hrAdministration.get_list_of_user_names()).is_equal_to(['Admin'])