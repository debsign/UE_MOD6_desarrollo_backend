import requests


# IngredientDestroyAPIView
endpoint = 'http://localhost:8000/api_view/ingredient/1/update/'

# DESTROY
res = requests.put(endpoint, json={'name':'Patata', 'quantity':300})

print(res.status_code)
print(res.json())