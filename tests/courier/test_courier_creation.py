import allure
import requests

from data import Urls, ErrorMessages
from helpers import GenerateTestData


class TestCourierCreation:
    @allure.title('Проверка успешного создания курьера')
    def test_create_courier_success(self, generate_courier_data_and_delete_after_test):
        # Проверяем успешное создание курьера
        response = requests.post(f'{Urls.COURIER_ENDPOINT}',
                                 data=generate_courier_data_and_delete_after_test)
        assert (response.status_code == 201 and response.text == ErrorMessages.COURIER_CREATION_201), \
            f"Ожидаемый код ошибки 201, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Проверка создания двух курьеров с одинаковыми данными')
    def test_creating_two_identical_couriers(self, generate_courier_data_and_delete_after_test):
        # Создаем первого курьера
        requests.post(f'{Urls.COURIER_ENDPOINT}',
                                 data=generate_courier_data_and_delete_after_test)
        # Отправляем такой же запрос
        response = requests.post(f'{Urls.COURIER_ENDPOINT}',
                                 data=generate_courier_data_and_delete_after_test)
        assert response.status_code == 409 and response.json()["message"] == ErrorMessages.COURIER_CREATION_ERROR_409, \
            f"Ожидаемый код ошибки 409, актуальный - {response.status_code}, текст ответа: {response.text}"
        # Сообщение об ошибке не соответствует документации

    @allure.title('Проверка создания курьера без логина и пароля')
    def test_create_courier_without_login_and_password(self, generate_courier_data):
        # Удаляем логин и пароль из сгенерированных данных
        del generate_courier_data["login"]
        del generate_courier_data["password"]
        # Пробуем создать курьера
        response = requests.post(f'{Urls.COURIER_ENDPOINT}',
                                 data=generate_courier_data)
        # Проверяем код ошибки и сообщение об ошибке
        assert response.status_code == 400 and response.json()["message"] == ErrorMessages.COURIER_CREATION_ERROR_400, \
            f"Ожидаемый код ошибки 400, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Проверка создания двух курьеров с одинаковым логином')
    def test_create_courier_with_same_login(self, generate_courier_data_and_delete_after_test):
        # Создаем первого курьера
        requests.post(f'{Urls.COURIER_ENDPOINT}',
                      data=generate_courier_data_and_delete_after_test)
        test_data = GenerateTestData()
        courier_data = test_data.create_register_information()
        courier_data["login"] = generate_courier_data_and_delete_after_test["login"]
        # Пробуем создать второго курьера с тем же логином
        response = requests.post(f'{Urls.COURIER_ENDPOINT}',
                      data=courier_data)
        assert response.status_code == 409 and response.json()["message"] == ErrorMessages.COURIER_CREATION_ERROR_409, \
            f"Ожидаемый код ошибки 409, актуальный - {response.status_code}, текст ответа: {response.text}"
        # Сообщение об ошибке не соответствует документации

    @allure.title('Проверка создания курьера без имени')
    def test_create_courier_without_first_name(self, generate_courier_data_and_delete_after_test):
        # Удаляем имя сгенерированных данных
        del generate_courier_data_and_delete_after_test["firstName"]
        # Пробуем создать курьера с двумя полями
        response = requests.post(f'{Urls.COURIER_ENDPOINT}',
                                 data=generate_courier_data_and_delete_after_test)
        # Проверяем код ошибки и сообщение
        assert (response.status_code == 201 and response.text == ErrorMessages.COURIER_CREATION_201), \
            f"Ожидаемый код ошибки 201, актуальный - {response.status_code}, текст ответа: {response.text}"

