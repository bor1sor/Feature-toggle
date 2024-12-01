import requests

url = "https://budu.com/"
response = requests.get(url)

# Print Headers
print(response.headers)
