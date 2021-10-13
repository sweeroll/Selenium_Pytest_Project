from faker import Faker

fake = Faker("Ru-ru")


class SignUpData:
    def __init__(self, login=None, password=None, email=None, first_name=None, last_name=None):
        self.login = login
        self.password = password
        self.email = email
        self.password = password
        self.first_name = first_name
        self.last_name = last_name

    @staticmethod
    def random():
        login = fake.user_name()
        password = fake.password(length=8)
        email = fake.email()
        first_name = fake.first_name()
        last_name = fake.last_name()
        return SignUpData(login, password, email, first_name, last_name)
