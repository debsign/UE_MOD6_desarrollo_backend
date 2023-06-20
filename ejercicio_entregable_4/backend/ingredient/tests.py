from rest_framework import status
from rest_framework.test import APITestCase
from .models import Ingredient

# vamos a testear si podemos crear los usuarios
class IngredientTestCase(APITestCase):
    def setUp(self):
        # creamos un ingrediente para usar en las pruebas
        self.ingredient = Ingredient.objects.create(name='Bacon', quantity=100)

    def test_ingredient_creation(self):
        # le pasamos el dato para crear el ingredient
        data = {'name':'Bacon', 'quantity':100}
        # le decimos la url que usamos para crearlo, más el tipo post
        res = self.client.post('/ingredients/', data)
        # importante saber que esto no se va a guardar en nuestra base de datos, si no en una ddbb temporal
        # lo que queremos saber es si el código de respuesta es igual al 201, lo que significará que ha sido creado
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
    
    def test_ingredient_retrieval(self):
        # petición get para obtener el ingrediente creado
        res = self.client.get(f'/ingredients/{self.ingredient.id}/')
        # lo que queremos saber es si el código de respuesta es igual al 200, lo que significará que se ha obtenido correctamente
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # comprobamos que el ingrediente que obtenemos es el que hemos creado
        self.assertEqual(res.data['name'], 'Bacon')

    def test_ingredient_update(self):
        # petición patch para actualizar el nombre del ingrediente
        res = self.client.patch(f'/ingredients/{self.ingredient.id}/', {'name': 'Panceta'})
        # lo que queremos saber es si el código de respuesta es igual al 200, lo que significará que se ha modificado correctamente
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # actualizamos el objeto de la ddbb
        self.ingredient.refresh_from_db()
        # comprobamos que el ingrediente que obtenemos se llama con el nuevo nombre
        self.assertEqual(self.ingredient.name, 'Panceta')

    def test_ingredient_deletion(self):
        # petición delete para borrar el ingrediente
        res = self.client.delete(f'/ingredients/{self.ingredient.id}/')
         # lo que queremos saber es si el código de respuesta es igual al 204, lo que significará que no hay contenido en la respuesta
        self.assertEqual(res.status_code, status.HTTP_204_NO_CONTENT)
        # usamos assertRaises para verificar que se genera una excepción Ingredient.DoesNotExist cuando se intenta obtener un ingrediente que ha sido eliminado
        # assertRaises(exception, callable, *args, **kwds)
        self.assertRaises(Ingredient.DoesNotExist, Ingredient.objects.get, id=self.ingredient.id)
