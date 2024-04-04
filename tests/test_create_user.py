import allure
import pytest
import requests

from user import User


class TestCreateUser:
    @allure.title("Проверка создания уникального пользователя")
    def test_create_user_all_required_fields_ok(self):
        user = User()
        user_data = user.create_user_return_user_data()
        assert user.response.status_code == 200
        user.delete_user(user_data[3])

    @allure.title("Проверка создания пользователя, который уже зарегистрирован")
    def test_create_user_two_equal_users_error(self):
        user = User()
        user_data = user.create_user_return_user_data()
        payload = {
            'email': user_data[0],
            'password': user_data[1],
            'name': user_data[2]
        }
        response = requests.post(user.url + 'api/auth/register', data=payload)
        assert response.status_code == 403

    @allure.title("Проверка создания пользователя без заполнения одного из обязательных полей")
    @pytest.mark.parametrize(
        'email, password, name',
        [
            ('', 'password', 'name'),
            ('email', '', 'name'),
            ('email', 'password', '')
        ]
    )
    def test_create_user_without_field_error(self, email, password, name):
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/register', data=payload)
        assert response.status_code == 403






