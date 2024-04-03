import allure
import requests

from data import Urls


class TestOrderList:
    @allure.title('Проверка получения списка заказа')
    def test_order_list(self):
        response = requests.get(url=Urls.ORDERS_ENDPOINT)
        assert 'orders' in response.text and response.status_code == 200

