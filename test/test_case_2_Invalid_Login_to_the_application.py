
def test_case_1_login_to_the_application(app):
    app.orangeHrm.openUrl()
    app.orangeHrm.click_login_button()
    app.assert_that(app.orangeHrm.get_username_error()).is_equal_to('Username cannot be empty')
    app.assert_that(app.orangeHrm.get_password_error()).is_equal_to('Password cannot be empty')