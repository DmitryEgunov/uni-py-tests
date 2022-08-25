import pytest
from api_ya_disk import YandexApiDisk


instance = YandexApiDisk()


def test_get_status_connect():
    assert instance.get_status_connect() == 200


def test_get_token():
    assert isinstance(instance.get_token(), str)


def test_add_folder():
    assert 'Test' in instance.add_folder('Test')['href']
