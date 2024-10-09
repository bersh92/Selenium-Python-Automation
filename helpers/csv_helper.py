import csv
import os
from helpers.utils import Utils


class CSVHelper:
    download_directory = os.path.join(Utils.get_project_root(), 'files', 'download')

    @staticmethod
    def get_column_values(file_name, column_index, partial_name=False):
        if partial_name:
            file_path = CSVHelper._find_file_by_partial_name(file_name)
            if not file_path:
                raise FileNotFoundError(f"No file matching partial name '{file_name}' found in download directory.")
        else:
            file_path = os.path.join(CSVHelper.download_directory, file_name)

        with open(file_path, mode='r', encoding='utf-8') as file:
            csv_reader = csv.reader(file)
            next(csv_reader)  # Skip header
            return [row[column_index] for row in csv_reader]

    @staticmethod
    def _find_file_by_partial_name(partial_name):
        for file_name in os.listdir(CSVHelper.download_directory):
            if file_name.startswith(partial_name):
                return os.path.join(CSVHelper.download_directory, file_name)
        return None
