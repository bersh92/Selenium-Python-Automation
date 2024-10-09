import os
import shutil
import random
import string

class Utils:

    @staticmethod
    def generate_random_email(domain='example.com', length=15):
        characters = string.ascii_letters + string.digits
        local_part = ''.join(random.choice(characters) for i in range(length))
        return f"{local_part}@{domain}"

    @staticmethod
    def generate_random_string(length=15):
        characters = string.ascii_letters + string.digits
        random_string = ''.join(random.choice(characters) for i in range(length))
        return random_string

    @staticmethod
    def get_project_root():
        return os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    @staticmethod
    def get_path_to_folder(folder=None, sub_folder=None):
        # Get the project root (this should be defined in your Utils module)
        project_root = Utils.get_project_root()

        # Create a list of parts, filtering out None values
        parts = [project_root, folder, sub_folder]
        parts = [part for part in parts if part is not None]

        # Join the parts to form the final path
        return os.path.join(*parts)

    @staticmethod
    def clear_download_directory():
        download_path = os.path.join(Utils.get_project_root(), 'files', 'download')
        if os.path.exists(download_path):
            shutil.rmtree(download_path)
        os.makedirs(download_path)