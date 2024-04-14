import allure
import requests

from user import User


class TestLoginUser:

    @allure.title("Проверка авторизации существующего пользователя")
    def test_login_existed_user_ok(self):
        user = User()
        user_data = user.create_user_return_user_data()
        email = user_data[0]
        password = user_data[1]
        payload = {
            'email': email,
            'password': password,
        }
        response = requests.post(user.url + 'api/auth/login', data=payload)
        assert response.status_code == 200 and response.json()['success'] == True

    @allure.title("Проверка авторизации под неверным логином и паролем")
    def test_login_existed_user_ok(self):
        payload = {
            'email': 'this_is_incorrect_email',
            'password': 'this_is_incorrect_password',
        }
        response = requests.post('https://stellarburgers.nomoreparties.site/api/auth/login', data=payload)
        assert response.status_code == 401 and 'email or password are incorrect' in response.text
