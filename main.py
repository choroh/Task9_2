'''
Netology
Задача 9.2
У Яндекс.Диска есть очень удобное и простое API. Для описания всех его методов существует Полигон.
Нужно написать программу, которая принимает на вход путь до файла на компьютере и сохраняет на Яндекс. Диск с таким же именем.

    Все ответы приходят в формате json;
    Загрузка файла по ссылке происходит с помощью метода put и передачи туда данных;
    Токен можно получить кликнув на полигоне на кнопку "Получить OAuth-токен".

HOST: https://cloud-api.yandex.net:443

Важно: Токен публиковать в github не нужно, переменную для токена нужно оставить пустой!
'''
import requests


class YaUploader:
    #  Авторизация на Яндексе
    def __init__(self, token: str):
        self.token = token
        self.APT_BASE_URL = 'https://cloud-api.yandex.net/'
        self.headers = {'Authorization': OAuth}

    def upload(self, file_path: str):
        #  Получаем ссылку для загрузки файла на Яндекс диск в папку Netology
        req = requests.get(self.APT_BASE_URL + 'v1/disk/resources/upload', params={'path': 'Netology/test.txt'}, headers=self.headers)
        upload_url = req.json().get('href')  # ссылка

        #  Открываем файл для отправки и отправляем по полученной ссылке
        with open(file_path, 'r', encoding='utf-8') as f:
            data = f.read()
        req1 = requests.put(upload_url, headers=self.headers, files={'file': data})
        print(req1.status_code)


OAuth = ''
file_path = 'files/test.txt'
uploader = YaUploader(OAuth)
result = uploader.upload(file_path)

