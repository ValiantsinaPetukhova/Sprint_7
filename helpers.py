from faker import Faker
from datetime import datetime, timedelta


class GenerateTestData:
    faker = Faker('ru_RU')

    def create_register_information(self):
        # генерируем логин, пароль и имя курьера
        login = self.faker.user_name()
        password = self.faker.password()
        first_name = self.faker.first_name()

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password,
            "firstName": first_name
        }
        return payload

    def create_login_information(self):
        # генерируем логин, пароль и имя курьера
        login = self.faker.user_name()
        password = self.faker.password()

        # собираем тело запроса
        payload = {
            "login": login,
            "password": password
        }
        return payload

    def create_order_data(self):
        delivery_date = datetime.now().date() + timedelta(days=self.faker.random_int(min=1, max=10))
        order_data = {
            "firstName": self.faker.first_name(),
            "lastName": self.faker.last_name(),
            "address": self.faker.address()[:20],
            "metroStation": self.faker.random_int(min=1, max=225),
            "phone": self.faker.phone_number().replace("-", " ").replace("(", "").replace(")", ""),
            "rentTime": self.faker.random_int(min=1, max=7),
            "deliveryDate": delivery_date.strftime('%Y-%m-%d'),
            "comment": self.faker.text(max_nb_chars=20)
        }
        return order_data





