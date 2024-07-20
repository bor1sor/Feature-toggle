import requests

response = requests.get ('https://budu.com')
assert response.status_code == 200
print (response.status_code)