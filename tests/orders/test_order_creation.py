import json

import allure
import pytest
import requests

from data import Urls, Data, ErrorMessages
from helpers import GenerateTestData


class TestOrderCreation:
    @allure.title('Создание заказа с разными вариантами цвета самоката')
    @pytest.mark.parametrize('color', Data.color_data)
    def test_order_creation(self, color):
        test_data = GenerateTestData()
        order_data = test_data.create_order_data()
        order_data['color'] = color
        response = requests.post(url=Urls.ORDERS_ENDPOINT,
                                 data=json.dumps(order_data), timeout=8)
        assert ErrorMessages.ORDER_CREATION_TRACK in response.text and response.status_code == 201


