import requests
import os


class MyComputer:
    """
    Represents a computer instance capable of downloading and checking the size of a file.

    Attributes:
        project_path (str): The path to the project directory.

    Args:
        link (str): The URL of the file to be downloaded.
        size_mb (float): The expected size of the file in megabytes.

    Methods:
        download_file(path): Downloads the file from the specified URL
            and saves it to the given path.
        get_file_size(path, file_name): Retrieves the size of the file
            located at the specified path and with the given name.
        check_file_in_project(): Downloads the file, checks its size,
            and raises an assertion error if the size does not match the expected size.
    """
    project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

    def __init__(self, link: str, size_mb: float):
        """
        Initializes a MyComputer instance.

        Args:
        link (str): The URL of the file to be downloaded.
        size_mb (float): The expected size of the file in megabytes.
        """
        self.link = link
        self.size_mb = float(size_mb)

    def download_file(self, path):
        """
        Downloads the file from the specified URL and saves it to the given path.

        Args:
        path (str): The directory path where the file should be saved.
        """
        response = requests.get(self.link)
        with open(os.path.join(path, 'sbis_plugin.exe'), 'wb') as file:
            file.write(response.content)

    def get_file_size(self, path, file_name):
        """Retrieves the size of the file located at the specified path and with the given name."""
        file_info = os.stat(os.path.join(path, f'{file_name}'))
        file_size = file_info.st_size
        return file_size

    def check_file_in_project(self):
        """
        Downloads the file, checks size, and raises an assertion
        error if the size does not match the expected size.
        """
        self.download_file(self.project_path)
        real_size = self.get_file_size(self.project_path, "sbis_plugin.exe")
        print(f"real_size bites: {real_size}, expected_size bites: {self.size_mb * 1024 * 1024}")
        real_size_mb = round(real_size / 1_048_576, 2)
        assert real_size_mb == self.size_mb, \
            "Files are not similar by size"

