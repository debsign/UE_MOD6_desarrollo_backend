import requests
import json

# IngredientListCreateAPIView
endpoint = 'http://localhost:8000/api_view/ingredient/'

# GET
res = requests.get(endpoint)

try:
    response_data = res.json()
    if res.status_code == 200:
        for index, item in enumerate(response_data):
            print(f"Ingrediente {index + 1}:")
            print(item)
            print("-----------------------")
    else:
        print(res.status_code)
except json.decoder.JSONDecodeError:
    print(f"Error: {res.status_code}")
        