import random


class Urls:
    # Базовый URL эндпоинтов API
    BASE_URL = "https://qa-scooter.praktikum-services.ru/api"

    COURIER_ENDPOINT = f"{BASE_URL}/v1/courier"
    COURIER_LOGIN_ENDPOINT = f"{BASE_URL}/v1/courier/login"
    ORDERS_ENDPOINT = f"{BASE_URL}/v1/orders"
    ORDER_DELETE_ENDPOINT = f"{BASE_URL}/v1/orders/cancel"
    ORDER_GET_ENDPOINT = f"{BASE_URL}/v1/orders/track/"
    ORDER_ACCEPT_ENDPOINT = f"{BASE_URL}/v1/orders/accept/"


class ErrorMessages:
    LOGIN_COURIER_ERROR_400 = "Недостаточно данных для входа"
    LOGIN_COURIER_ERROR_404 = "Учетная запись не найдена"
    COURIER_CREATION_ERROR_400 = "Недостаточно данных для создания учетной записи"
    COURIER_CREATION_ERROR_409 = "Этот логин уже используется. Попробуйте другой."
    COURIER_DELETION_ERROR_400 = "Недостаточно данных для удаления курьера"
    COURIER_DELETION_ERROR_404 = "Курьера с таким id нет"
    COURIER_CREATION_201 = '{"ok":true}'
    COURIER_DELETION_200 = '{"ok":true}'
    COURIER_DELETION_404 = "Курьера с таким id нет."
    COURIER_DELETION_WITHOUT_ID = '{"code":404,"message":"Not Found."}'
    ORDER_ACCEPTION_200 = '{"ok":true}'
    ORDER_ACCEPTION_400 = "Недостаточно данных для поиска"
    ORDER_ACCEPTION_404 = "Not Found."
    ORDER_ACCEPTION_409 = "Этот заказ уже в работе"
    ORDER_ACCEPTION_404_COURIER = "Курьера с таким id не существует"
    ORDER_ACCEPTION_404_ORDER = "Заказа с таким id не существует"
    ORDER_CREATION_TRACK = "track"
    ORDER_GET = "order"
    ORDER_GET_400 = "Недостаточно данных для поиска"
    ORDER_GET_404 = "Заказ не найден"
    COURIER_ID = 'id'


class Data:
    color_data = (
        ['BLACK'], ['GREY'], ['BLACK', 'GREY'], []
    )
    courier_id = random.randint(1000000, 9999999)
    order_id = random.randint(1000000, 9999999)
    track_number = random.randint(1000000, 9999999)


