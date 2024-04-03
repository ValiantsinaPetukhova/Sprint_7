import pytest
import requests
import json

from helpers import GenerateTestData
from data import Urls


@pytest.fixture(scope='function')
def generate_courier_data():
    test_data = GenerateTestData()
    courier_data = test_data.create_register_information()
    return courier_data


@pytest.fixture(scope='function')
def generate_courier_data_and_delete_after_test(generate_courier_data):
    yield generate_courier_data
    # Логин курьера для получения его id
    login_data = {
        "login": generate_courier_data["login"],
        "password": generate_courier_data["password"]
    }
    login_response = requests.post(f"{Urls.COURIER_LOGIN_ENDPOINT}", json=login_data)
    courier_id = login_response.json()

    # Удаление курьера после завершения теста
    requests.delete(f"{Urls.COURIER_ENDPOINT}/{courier_id["id"]}")


@pytest.fixture(scope='function')
def create_courier_and_delete_after_test(generate_courier_data):
    requests.post(f'{Urls.COURIER_ENDPOINT}', data=generate_courier_data)
    login_data = {
        "login": generate_courier_data["login"],
        "password": generate_courier_data["password"]
    }
    yield login_data
    login_response = requests.post(f"{Urls.COURIER_LOGIN_ENDPOINT}", json=login_data)
    courier_id = login_response.json()

    # Удаление курьера после завершения теста
    requests.delete(f"{Urls.COURIER_ENDPOINT}/{courier_id["id"]}")


@pytest.fixture(scope='function')
def create_courier(generate_courier_data):
    requests.post(f'{Urls.COURIER_ENDPOINT}', data=generate_courier_data)
    login_data = {
        "login": generate_courier_data["login"],
        "password": generate_courier_data["password"]
    }
    return login_data


@pytest.fixture(scope='function')
def create_order():
    test_data = GenerateTestData()
    order_data = test_data.create_order_data()
    create_order_response = requests.post(url=Urls.ORDERS_ENDPOINT,
                             data=json.dumps(order_data), timeout=8)
    track = create_order_response.json()['track']
    response_get_id = requests.get(f'{Urls.ORDER_GET_ENDPOINT}?t={track}')
    order_id = response_get_id.json()['order']['id']
    return order_id


@pytest.fixture(scope='function')
def create_order_track():
    test_data = GenerateTestData()
    order_data = test_data.create_order_data()
    create_order_response = requests.post(url=Urls.ORDERS_ENDPOINT,
                             data=json.dumps(order_data), timeout=8)
    track = create_order_response.json()['track']
    return track




