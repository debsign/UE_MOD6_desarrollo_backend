import requests


# RecipeDestroyAPIView
endpoint = 'http://localhost:8000/api_view/recipe/1/update/'

# DESTROY
res = requests.put(endpoint, json={'title':'Ensalada de patata y queso','steps':'Paso 1: Cortar las patatas y el queso, Paso 2: Mezclar los ingredientes, Paso 3: Aliñar con aceite y especias'})

print(res.status_code)
print(res.json())