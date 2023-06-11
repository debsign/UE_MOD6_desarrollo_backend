import requests
import json


# IngredientDestroyAPIView
endpoint = 'http://localhost:8000/api_view/ingredient/2/destroy/'

# DESTROY
res = requests.delete(endpoint)

print(res.status_code)

try:
    response_data = res.json()
    print(response_data)
except json.decoder.JSONDecodeError:
    if res.status_code == 204:
        print("Ingrediente borrado.")
    else:
        print("Error")