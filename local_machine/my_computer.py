import requests
import os


class MyComputer:
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, link: str, size_mb: float):
        self.link = link
        self.size_mb = float(size_mb)

    def download_file(self, path):
        response = requests.get(self.link)
        with open(os.path.join(path, 'sbis_plugin.exe'), 'wb') as file:
            file.write(response.content)

    def get_file_size(self, path, file_name):
        file_info = os.stat(os.path.join(path, f'{file_name}'))
        file_size = file_info.st_size
        return file_size

    def check_file_in_project(self):
        self.download_file(self.project_path)
        real_size = self.get_file_size(self.project_path, "sbis_plugin.exe")
        print(f"real_size bites: {real_size}, expected_size bites: {self.size_mb * 1024 * 1024}")
        real_size_mb = round(real_size / 1_048_576, 2)
        assert real_size_mb == self.size_mb, \
            "File are not similar by size"

