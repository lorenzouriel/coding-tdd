from user_service import UserService, User

def test_register_with_dummy():
    class DummyRepository:
        def save(self, user):  # Not actually used
            pass

    class DummyEmailService:
        def send_welcome_email(self, email):  # Not actually used
            pass

    service = UserService(DummyRepository(), DummyEmailService())
    user = service.register("lorenzouriel@gmail.com")

    assert user.email == "lorenzouriel@gmail.com"