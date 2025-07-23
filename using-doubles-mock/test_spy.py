from user_service import UserService, User

def test_send_email_called_with_spy():
    class DummyRepository:
        def save(self, user):
            pass
    
    class SpyEmailService:
        def __init__(self):
            self.sent_emails = []

        def send_welcome_email(self, email):
            self.sent_emails.append(email)

    spy_email = SpyEmailService()
    service = UserService(DummyRepository(), spy_email)

    service.register("lorenzouriel@gmail.com")

    assert "lorenzouriel@gmail.com" in spy_email.sent_emails, "Email should have been sent to the spy email service"