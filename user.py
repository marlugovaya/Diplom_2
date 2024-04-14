import allure
import pytest
import requests
from faker import Faker


class User:
    url = 'https://stellarburgers.nomoreparties.site/'
    response = None

    @allure.step("Создаем нового пользователя")
    def create_user_return_user_data(self):
        fake = Faker()
        user_data = []
        email = fake.email(),
        password = fake.password()
        name = fake.user_name()
        payload = {
            'email': email,
            'password': password,
            'name': name
        }
        self.response = requests.post(self.url + 'api/auth/register', data=payload)
        if self.response.status_code == 200:
            user_data.append(email)
            user_data.append(password)
            user_data.append(name)
            user_data.append(self.response.json()['accessToken'])
        return user_data

    def delete_user(self, access_token):
        payload = {
            'authorization': access_token
        }
        self.response = requests.delete(self.url + 'api/auth/user', data=payload)
        return self.response

    @allure.step("Создаем нового пользователя и авторизуемся")
    def login_user_return_user_data(self):
        user = User()
        user_data = user.create_user_return_user_data()
        payload = {
            'email': user_data[0],
            'password': user_data[1],
        }
        requests.post(user.url + 'api/auth/login', data=payload)
        return user_data
