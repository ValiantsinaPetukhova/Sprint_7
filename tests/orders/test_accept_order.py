import requests
import allure

from data import Urls, ErrorMessages, Data


class TestAcceptOrder:
    @allure.title('Успешное принятие заказа')
    def test_accept_order_success(self, create_courier_and_delete_after_test, create_order):
        login_response = requests.post(f"{Urls.COURIER_LOGIN_ENDPOINT}", json=create_courier_and_delete_after_test)
        courier_id = login_response.json()['id']
        response = requests.put(f'{Urls.ORDER_ACCEPT_ENDPOINT}{create_order}?courierId={courier_id}')
        assert response.status_code == 200 and response.text == ErrorMessages.ORDER_ACCEPTION_200, \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Принятие заказа без ID курьера')
    def test_accept_order_without_courier_id(self, create_order):
        response = requests.put(f'{Urls.ORDER_ACCEPT_ENDPOINT}{create_order}?courierId=')
        assert response.status_code == 400 and response.json()["message"] == ErrorMessages.ORDER_ACCEPTION_400, \
            f"Ожидаемый код ошибки 400, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Принятие заказа без ID заказа')
    def test_accept_order_without_order_id(self, create_courier_and_delete_after_test):
        login_response = requests.post(f"{Urls.COURIER_LOGIN_ENDPOINT}", json=create_courier_and_delete_after_test)
        courier_id = login_response.json()['id']
        response = requests.put(f'{Urls.ORDER_ACCEPT_ENDPOINT}?courierId={courier_id}', timeout=5)
        assert response.status_code == 404 and response.json()["message"] == ErrorMessages.ORDER_ACCEPTION_404, \
            f"Ожидаемый код ошибки 404, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Принятие заказа дважды')
    def test_accept_order_twice(self, create_courier_and_delete_after_test, create_order):
        login_response = requests.post(f"{Urls.COURIER_LOGIN_ENDPOINT}", json=create_courier_and_delete_after_test)
        courier_id = login_response.json()['id']
        requests.put(f'{Urls.ORDER_ACCEPT_ENDPOINT}{create_order}?courierId={courier_id}')
        response = requests.put(f'{Urls.ORDER_ACCEPT_ENDPOINT}{create_order}?courierId={courier_id}')
        assert response.status_code == 409 and response.json()["message"] == ErrorMessages.ORDER_ACCEPTION_409, \
            f"Ожидаемый код ошибки 409, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Принятие заказа c неверным ID курьера')
    def test_accept_order_wrong_courier_id(self, create_order):
        courier_id = Data.courier_id
        response = requests.put(f'{Urls.ORDER_ACCEPT_ENDPOINT}{create_order}?courierId={courier_id}')
        assert response.status_code == 404 and response.json()["message"] == ErrorMessages.ORDER_ACCEPTION_404_COURIER, \
            f"Ожидаемый код ошибки 404, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Принятие заказа c неверным ID заказа')
    def test_accept_order_wrong_order_id(self, create_courier_and_delete_after_test):
        login_response = requests.post(f"{Urls.COURIER_LOGIN_ENDPOINT}", json=create_courier_and_delete_after_test)
        courier_id = login_response.json()['id']
        order_id = Data.order_id
        response = requests.put(f'{Urls.ORDER_ACCEPT_ENDPOINT}{order_id}?courierId={courier_id}', timeout=8)
        assert response.status_code == 404 and response.json()["message"] == ErrorMessages.ORDER_ACCEPTION_404_ORDER, \
            f"Ожидаемый код ошибки 404, актуальный - {response.status_code}, текст ответа: {response.text}"



