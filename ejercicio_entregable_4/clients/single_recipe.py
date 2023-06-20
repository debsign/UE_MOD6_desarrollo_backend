import requests

# UserRetrieveAPIView
endpoint = 'http://localhost:8000/api_view/recipe/1'

# GET
res = requests.get(endpoint)

print(res.status_code)
print(res.json())