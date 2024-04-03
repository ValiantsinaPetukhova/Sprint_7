import allure
import requests

from data import Urls, ErrorMessages, Data


class TestCourierDeletion:
    @allure.title('Проверка успешного удаления курьера')
    def test_delete_courier_sucess(self, create_courier):
        # Логин курьера для получения его id
        login_response = requests.post(f'{Urls.COURIER_LOGIN_ENDPOINT}',
                                 data=create_courier)
        courier_id = login_response.json()['id']
        # Удаляем курьера
        response = requests.delete(f"{Urls.COURIER_ENDPOINT}/{courier_id}")
        assert (response.status_code == 200 and response.text == ErrorMessages.COURIER_DELETION_200), \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Проверка удаления курьера c неверным ID')
    def test_delete_wrong_id(self):
        courier_id = Data.courier_id
        # Удаляем курьера
        response = requests.delete(f"{Urls.COURIER_ENDPOINT}/{courier_id}")
        assert (response.status_code == 404 and response.json()['message'] == ErrorMessages.COURIER_DELETION_404), \
            f"Ожидаемый код ошибки 404, актуальный - {response.status_code}, текст ответа: {response.json()['message']}"

    @allure.title('Проверка удаления курьера без его ID')
    def test_delete_without_id(self):
        response = requests.delete(f"{Urls.COURIER_ENDPOINT}/")
        assert (response.status_code == 404 and response.text == ErrorMessages.COURIER_DELETION_WITHOUT_ID), \
            f"Ожидаемый код ошибки 404, актуальный - {response.status_code}, текст ответа: {response.text}"
        #Ошибка в документации (там запрос без id - код 400)
