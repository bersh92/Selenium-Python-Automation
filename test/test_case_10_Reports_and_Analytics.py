from helpers.utils import Utils

random_name = Utils.generate_random_string()

def test_case_10_verify_folders_creation_functionality(app):
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Reports and Analytics")
    app.orangeHrm.reportsAnalytics.wait_for_page_loading()
    app.orangeHrm.reportsAnalytics.click_on_new_folder_button()
    app.orangeHrm.popUp.reportsAnalytics.input_new_folder_name(random_name)
    app.orangeHrm.popUp.reportsAnalytics.click_on_save_button()
    app.assert_that(app.orangeHrm.reportsAnalytics.get_manipulation_meassage_text()).is_equal_to("Successfully Saved")
    app.orangeHrm.reportsAnalytics.wait_for_page_loading()
    app.assert_that(app.orangeHrm.reportsAnalytics.get_folder_names_list()).contains(random_name)
    app.orangeHrm.reportsAnalytics.find_and_click_delete_button_for_folder(random_name)
    app.orangeHrm.reportsAnalytics.confirm_folder_deleting()
    app.assert_that(app.orangeHrm.reportsAnalytics.get_manipulation_meassage_text()).is_equal_to("Successfully Deleted")
    app.assert_that(app.orangeHrm.reportsAnalytics.get_folder_names_list()).does_not_contain(random_name)
