import requests

def test_homepage_accessibility():
    response = requests.get('https://budu.ru')
    assert response.status_code == 200, "Главная страница недоступна"