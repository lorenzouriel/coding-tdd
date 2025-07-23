class User:
    def __init__(self, email):
        self.email = email

class UserService:
    def __init__(self, repository, email_service):
        self.repository = repository
        self.email_service = email_service

    def register(self, email):
        user = User(email)
        self.repository.save(user)
        self.email_service.send_welcome_email(email)
        return user