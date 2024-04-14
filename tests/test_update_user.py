import allure
import pytest
import requests

from user import User


class TestUpdateUser:

    @allure.title("Проверка изменения данных авторизованного пользователя")
    @pytest.mark.parametrize(
        'email, password, name',
        [
            (None, None, 'new_name_'),
            ('new_email_', None, None),
            (None, 'new_password_', None)
        ]
    )
    def test_update_user_with_authorisation(self, email, password, name, user_data):
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        headers = {'authorization': user_data[3]}
        response = requests.patch(User.url + 'api/auth/user', headers=headers, data=payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @pytest.mark.parametrize(
        'email, password, name',
        [
            (None, None, 'new_name_'),
            ('new_emаil_', None, None),
            (None, 'new_password_c', None)
        ]
    )
    @allure.title("Проверка изменения данных неавторизованного пользователя")
    def test_update_user_without_authorisation(self, email, password, name, user_data):
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        response = requests.patch(User.url + 'api/auth/user', headers=None, data=payload)
        assert response.status_code == 401 and 'You should be authorised' in response.text
