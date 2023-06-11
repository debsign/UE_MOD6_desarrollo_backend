import requests
import json


# RecipeDestroyAPIView
endpoint = 'http://localhost:8000/api_view/recipe/2/destroy/'

# DESTROY
res = requests.delete(endpoint)

print(res.status_code)

try:
    response_data = res.json()
    print(response_data)
except json.decoder.JSONDecodeError:
    if res.status_code == 204:
        print("Receta borrada.")
    else:
        print("Error")