import pytest
from api_ya_disk import YandexApiDisk
import requests


instance = YandexApiDisk()
folder_name = 'Test'    # Произвольное имя папки для теста


def teardown():
    params = {"path": folder_name, 'permanently': True}
    response = requests.delete(url=instance.url, headers=instance.headers, params=params)
    if response.status_code == 204:
        print(f'Папка "{folder_name}" удалена.')
    else:
        print('Что-то пошло не так...')


def test_get_status_connect():
    assert instance.get_status_connect() == 200


def test_get_token():
    assert isinstance(instance.get_token(), str)


def test_add_folder():
    assert folder_name in instance.add_folder(folder_name)['href']
