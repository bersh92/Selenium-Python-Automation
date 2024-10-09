
def test_case_5_verify_that_a_users_status_can_be_enabled_or_disabled(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.login_to_the_application()
    app.assert_that(app.orangeHrm.get_header_text()).is_equal_to('Employee Management')
    app.orangeHrm.sideMenu.click_on_side_menu_button('HR Administration')
    app.orangeHrm.hrAdministration.click_on_filter()
    app.orangeHrm.popUp.set_username('ghrtjtj')
    app.orangeHrm.popUp.click_on_search()
    app.assert_that(app.orangeHrm.hrAdministration.is_list_of_users_displayed()).is_equal_to(False)