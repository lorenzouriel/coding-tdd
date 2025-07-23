from unittest.mock import Mock
from user_service import UserService, User

def test_email_service_called_with_mock():
    mock_email = Mock()
    mock_email.send_welcome_email = Mock()

    class DummyRepository:
        def save(self, user):
            pass
    
    service = UserService(DummyRepository(), mock_email)

    service.register("lorenzouriel@gmail.com")

    mock_email.send_welcome_email.assert_called_once_with("lorenzouriel@gmail.com")