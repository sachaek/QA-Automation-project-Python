import requests
import os

url = 'http://example.com/song.mp3'
response = requests.get(url)

with open('song.mp3', 'wb') as file:
    file.write(response.content)


class MyComputer:
    project_path = ""
    def __init__(self, link):
        self.link = link
        self.response = requests.get(self.link)

    def download_file(self, path):
        with open(f'{path}+/file.exe', 'wb') as file:
            file.write(self.response.content)

    def get_file_size(self, path):
        file_info = os.stat(path)
        file_size = file_info.st_size
        return file_size




        """BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

>>> BASE_DIR
'/home/user/projects/myproject'
>>> os.path.dirname(BASE_DIR)
'/home/user/projects'"""


import os

file_info = os.stat('path_to_your_file')
file_size = file_info.st_size
print('Размер файла:', file_size, 'байт')

