import pytest
import icontract
from user_with_contracts import Repository, EmailService, UserService, User


@pytest.fixture
def service():
    repo = Repository()
    email = EmailService()
    return UserService(repo, email)


# Positive Test: Valid email
def test_register_valid_user(service):
    user = service.register("john@example.com")
    assert user.email == "john@example.com"
    assert user.active is True


# Negative Test: Invalid email (no @) → triggers precondition
def test_register_invalid_email(service):
    with pytest.raises(icontract.ViolationError, match="Email must contain '@'"):
        service.register("invalid-email.com")


# Negative Test: Save user with empty email → triggers precondition on save()
def test_save_user_with_empty_email():
    repo = Repository()
    user = User(email="")

    with pytest.raises(icontract.ViolationError, match="Email must not be empty"):
        repo.save(user)


# Postcondition Check: User must be saved
def test_user_saved_to_repository():
    repo = Repository()
    user = User(email="bob@example.com")
    repo.save(user)
    assert repo.find_by_email("bob@example.com") == user


# Postcondition Check: Register should return user with non-empty email
def test_postcondition_failure_hack(monkeypatch):
    repo = Repository()
    email = EmailService()

    # monkeypatch User to simulate a bug
    class BrokenUser:
        def __init__(self, email):
            self.email = ""

    monkeypatch.setattr("user_with_contracts.User", BrokenUser)

    service = UserService(repo, email)
    with pytest.raises(icontract.ViolationError, match="Email must not be empty"):
        service.register("bob@example.com")
