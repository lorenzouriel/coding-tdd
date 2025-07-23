from user_service import UserService, User

def test_user_has_id_from_stub():
    class StubRepository:
        def save(self, user):
            user.id = 147  # Pretend it's persisted in a database
            return user

    class DummyEmailService:
        def send_welcome_email(self, email):
            pass
    
    service = UserService(StubRepository(), DummyEmailService())
    user = service.register("lorenzouriel@gmail.com")

    assert hasattr(user, 'id') and user.id == 147