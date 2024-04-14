import allure
import pytest
import requests

from order import Order
from user import User


class TestCreateOrder:
    @allure.title("Проверка создания заказа авторизованным пользователем")
    def test_create_order_with_authorization(self, user_data):
        headers = {'authorization': user_data[3]}
        payload = Order().create_order_payload(1)
        response = requests.post(Order.order_url, headers=headers, data=payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка создания заказа с ингредиентами")
    @pytest.mark.parametrize(
        'ingredients_count',
        [1, 5, 10]
    )
    def test_create_order_with_ingredients(self, ingredients_count):
        payload = Order().create_order_payload(ingredients_count)
        response = requests.post(Order.order_url, data=payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка создания заказа без ингредиентов")
    def test_create_order_without_ingredients(self):
        response = requests.post(Order.order_url, data={'ingredients': ''})
        assert response.status_code == 400 and 'Ingredient ids must be provided' in response.text

    @allure.title("Проверка создания заказа с неверным хэшем ингредиентов")
    def test_create_order_incorrect_hash(self):
        response = requests.post(Order.order_url, data={'ingredients': ['000', '42']})
        assert response.status_code == 500 and 'Internal Server Error' in response.text






