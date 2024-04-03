import allure
import requests

from data import Urls, ErrorMessages, Data


class TestGetOrderByTrack:
    @allure.title('Успешное получение заказа по его трек-номеру')
    def test_get_order_success(self, create_order_track):
        response = requests.get(f'{Urls.ORDER_GET_ENDPOINT}?t={create_order_track}', timeout=5)
        assert response.status_code == 200 and ErrorMessages.ORDER_GET in response.text, \
            f"Ожидаемый код ошибки 200, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Проверка запроса заказа без его трек-номера')
    def test_get_order_without_track_number(self):
        response = requests.get(f'{Urls.ORDER_GET_ENDPOINT}?t=', timeout=5)
        assert response.status_code == 400 and response.json()["message"] == ErrorMessages.ORDER_GET_400, \
            f"Ожидаемый код ошибки 400, актуальный - {response.status_code}, текст ответа: {response.text}"

    @allure.title('Проверка запроса заказа с неверным трек-номером')
    def test_get_order_wrong_track_number(self):
        track_number = Data.track_number
        response = requests.get(f'{Urls.ORDER_GET_ENDPOINT}?t={track_number}', timeout=5)
        assert response.status_code == 404 and response.json()["message"] == ErrorMessages.ORDER_GET_404, \
            f"Ожидаемый код ошибки 404, актуальный - {response.status_code}, текст ответа: {response.text}"

