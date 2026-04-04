import requests
response = requests.get('https://www.anaconda.com/get')
if response.status_code == 200:
    print("Библиотека работает корректно")
    print(" Ответ сервера (JSON): ", response.json())
else:
    print(" Ошибка ", response.status_code)