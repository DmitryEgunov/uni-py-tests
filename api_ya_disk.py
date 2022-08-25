import requests
import time


class YandexApiDisk:

    def __init__(self):
        self.token = self.get_token()
        self.url = "https://cloud-api.yandex.net/v1/disk/resources"
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)
                }

    def get_token(self):
        with open('/home/dmitry/Обучение_python/питон/Professional_PYTHON/task_6/token.txt', 'r') as file:
            token = file.read().strip()
        return token

    def get_status_connect(self):
        response = requests.get(url=self.url + '/files', headers=self.headers)
        return response.status_code

    def add_folder(self, folder_name):
        # Добавляем папку в корневой каталог Яндекс.Диск
        params = {"path": folder_name}
        response = requests.put(self.url, headers=self.headers, params=params)
        return response.json()

if __name__=='__main__':
    ya_api_disk = YandexApiDisk()
    # print(ya_api_disk)
    # print(ya_api_disk.add_folder('123'))
    # print(ya_api_disk.get_status_connect())
    # print(ya_api_disk.get_token())
