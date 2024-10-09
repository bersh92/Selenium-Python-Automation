import time
from helpers.csv_helper import CSVHelper
from helpers.utils import Utils


def test_demonstration_file_download(app):
    Utils.clear_download_directory()
    app.orangeHrm.open_application_and_login()
    app.orangeHrm.sideMenu.click_on_side_menu_button("Recruitment (ATS)")
    app.orangeHrm.recruitmentAts.wait_for_page_load()
    app.orangeHrm.recruitmentAts.export_to_csv()
    first_column_values = CSVHelper.get_column_values('RecruitmentReport', 0, partial_name=True)
    second_column_values = CSVHelper.get_column_values('RecruitmentReport', 1, partial_name=True)
    third_column_values = CSVHelper.get_column_values('RecruitmentReport', 2, partial_name=True)
    time.sleep(3)