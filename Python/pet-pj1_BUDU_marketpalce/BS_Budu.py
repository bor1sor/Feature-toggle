import requests
from bs4 import BeautifulSoup

def test_page_content():
    url = "https://budu.ru/" 
    expected_content = "Blog" 

    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'
    }

    try:
        # Получаем HTML-код страницы
        response = requests.get(url)
        response.raise_for_status()  # Проверяем, что запрос успешен (статус 200)

        # Парсим HTML-код с помощью BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')

        # Проверяем наличие ожидаемого контента на странице
        assert expected_content in soup.get_text(), f"Ожидаемый контент '{expected_content}' не найден на странице."

        print("Тест пройден: ожидаемый контент найден на странице.")

    except requests.exceptions.RequestException as e:
        print(f"Ошибка при выполнении запроса: {e}")
    except AssertionError as e:
        print(e)

if __name__ == "__main__":
    test_page_content()