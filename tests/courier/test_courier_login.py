import allure
import requests

from data import Urls, ErrorMessages
from helpers import GenerateTestData


class TestCourierLogin:
    @allure.title('Проверка успешной авторизации')
    def test_login_success(self, create_courier_and_delete_after_test):
        response = requests.post(f'{Urls.COURIER_LOGIN_ENDPOINT}',
                      data=create_courier_and_delete_after_test)
        assert response.status_code == 200 and ErrorMessages.COURIER_ID in response.json(), \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, "\
            f"Отсутствует ключ 'id' в ответе на запрос авторизации курьера"

    @allure.title('Проверка авторизации с неверным паролем')
    def test_login_wrong_password(self, create_courier_and_delete_after_test):
        test_data = GenerateTestData()
        courier_data = test_data.create_login_information()
        courier_data["login"] = create_courier_and_delete_after_test["login"]
        # Пробуем залогиниться с неверным паролем
        response = requests.post(f'{Urls.COURIER_LOGIN_ENDPOINT}',
                                 data=courier_data)
        assert response.status_code == 404 and response.json()["message"] == ErrorMessages.LOGIN_COURIER_ERROR_404, \
            f"Ожидаемый код ошибки 404, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Проверка авторизации с неверным логином')
    def test_login_wrong_login(self, create_courier_and_delete_after_test):
        test_data = GenerateTestData()
        courier_data = test_data.create_login_information()
        courier_data["password"] = create_courier_and_delete_after_test["password"]
        # Пробуем залогиниться с неверным логином
        response = requests.post(f'{Urls.COURIER_LOGIN_ENDPOINT}',
                                 data=courier_data)
        assert response.status_code == 404 and response.json()["message"] == ErrorMessages.LOGIN_COURIER_ERROR_404, \
            f"Ожидаемый код ошибки 404, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Проверка авторизации без логина')
    def test_login_without_login(self, create_courier_and_delete_after_test):
        # Пробуем залогиниться без логина
        test_data = GenerateTestData()
        courier_data = test_data.create_login_information()
        courier_data["password"] = create_courier_and_delete_after_test["password"]
        del courier_data["login"]
        response = requests.post(f'{Urls.COURIER_LOGIN_ENDPOINT}',
                                 data=courier_data)
        assert response.status_code == 400 and response.json()["message"] == ErrorMessages.LOGIN_COURIER_ERROR_400, \
            f"Ожидаемый код ошибки 400, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Проверка авторизации незарегистрированного пользователя')
    def test_login_with_unregistered_user(self, generate_courier_data):
        del generate_courier_data["firstName"]
        # Пробуем залогиниться c несуществующим логином
        response = requests.post(f'{Urls.COURIER_LOGIN_ENDPOINT}',
                                 data=generate_courier_data)
        assert response.status_code == 404 and response.json()["message"] == ErrorMessages.LOGIN_COURIER_ERROR_404, \
            f"Ожидаемый код ошибки 404, актуальный - {response.status_code}, текст ответа: {response.text}"
