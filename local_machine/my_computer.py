import requests
import os

url = 'http://example.com/song.mp3'
response = requests.get(url)

with open('song.mp3', 'wb') as file:
    file.write(response.content)


class MyComputer:
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, link: str, size_mb: float):
        self.link = link

    def download_file(self, path):
        response = requests.get(self.link)
        with open(f'{path}+/sbis_plugin.exe', 'wb') as file:
            file.write(response.content)

    def get_file_size(self, path, file_name):
        file_info = os.stat(path + f"/{file_name}")
        file_size = file_info.st_size
        return file_size

    def check_file_size(self):
        self.download_file(self.project_path)
        size = self.get_file_size(self.project_path, "sbis_plugin.exe")
        print(size)

