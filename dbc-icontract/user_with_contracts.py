import icontract

class User:
    def __init__(self, email: str, active: bool = True):
        self.email = email
        self.active = active

    def deactivate(self):
        self.active = False

    def activate(self):
        self.active = True

class Repository:
    def __init__(self):
        self.users = {}

    @icontract.require(lambda user: user.email != "", "Email must not be empty")
    @icontract.ensure(lambda self, user: user.email in self.users, "User must be stored")
    def save(self, user: User):
        self.users[user.email] = user

    def find_by_email(self, email: str) -> User | None:
        return self.users.get(email)

class EmailService:
    def send_welcome_email(self, email: str):
        print(f"Welcome email sent to {email}")

class UserService:
    def __init__(self, repository: Repository, email_service: EmailService):
        self.repository = repository
        self.email_service = email_service

    @icontract.require(lambda email: "@" in email, "Email must contain '@'")
    @icontract.ensure(lambda result: result is not None and result.email != "", "User must be returned with non-empty email")
    def register(self, email: str) -> User:
        user = User(email=email)
        self.repository.save(user)
        self.email_service.send_welcome_email(email)
        return user