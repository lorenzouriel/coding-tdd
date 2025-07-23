from user_service import UserService, User

def test_register_with_fake_repository():
    class FakeRepository:
        def __init__(self):
            self.storage = []

        def save(self, user):
            self.storage.append(user)
    
    class DummyEmailService:
        def send_welcome_email(self, user):
            pass
    
    fake_repo = FakeRepository()
    service = UserService(fake_repo, DummyEmailService())

    service.register("lorenzouriel@gmail.com")

    assert len(fake_repo.storage) == 1
    assert fake_repo.storage[0]['email'] == "lorenzouriel@gmail.com"