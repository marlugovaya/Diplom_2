import allure
import requests

from order import Order
from user import User


class TestGetOrder:
    @allure.title("Проверка получения заказов авторизованного пользователя")
    def test_get_order_with_authorization(self, user_data):
        headers = {'authorization': user_data[3]}
        payload = {
            'email': user_data[0],
            'password': user_data[1],
            'name': user_data[2]
        }
        response = requests.get(Order.order_url, headers=headers, data=payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка получения заказов неавторизованного пользователя")
    def test_get_order_without_authorization(self, user_data):
        payload = {
            'email': user_data[0],
            'password': user_data[1],
            'name': user_data[2]
        }
        response = requests.get(Order.order_url, data=payload)
        assert response.status_code == 401 and response.json()['success'] == False

