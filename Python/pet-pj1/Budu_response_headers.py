import requests

url = "https://budu.ru/"
response = requests.get(url)

# Print Headers
print(response.headers)
