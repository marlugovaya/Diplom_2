import allure
import requests

from user import User


class Order:
    ingredients_url = 'https://stellarburgers.nomoreparties.site/api/ingredients'
    order_url = 'https://stellarburgers.nomoreparties.site/api/orders'

    @allure.step('Получаем хэш ингредиента')
    def get_ingredient_hash(self, ingredient_id):
        response = requests.get(self.ingredients_url)
        ingredient_hash = response.json()['data'][ingredient_id]['_id']
        return ingredient_hash

    @allure.step("Создаем список из заданного количества игредиентов")
    def create_order_payload(self, ingredient_count):
        for i in range(ingredient_count):
            payload = {
                'ingredients': [self.get_ingredient_hash(i)]
            }
            return payload
