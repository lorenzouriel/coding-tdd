# Test Doubles in Python
This project demonstrates **Test Doubles** using a simple `UserService` class in Python. You'll learn how to apply:

## Project Structure
```bash
.
├── user_service.py
├── test_dummy.py
├── test_stub.py
├── test_fake.py
├── test_spy.py
├── test_mock.py
└── README.md
```

## ⚙️ Requirements
- Python 3.8+

Install dependencies:
```bash
pip install pytest
```

## Base Class: UserService
```python
# user_service.py

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
```

## Dummy
Dummies are objects passed to satisfy parameter requirements but not used.
**File:** `test_dummy.py`
```bash
pytest test_dummy.py
```

## Stub
Stubs return hardcoded data used by the system under test.
**File:** `test_stub.py`
```bash
pytest test_stub.py
```

## Fake
Fakes are working implementations but are simplified (like in-memory DBs).
**File:** `test_fake.py`
```bash
pytest test_fake.py
```

## Spy
Spies record information about how they were used for manual assertions.
**File:** `test_spy.py`
```bash
pytest test_spy.py
```

## Mock
Mocks simulate objects and use a framework to verify interaction behavior.
**File:** `test_mock.py`
```bash
pytest test_mock.py
```

## Summary

| Type  | Description                              | Use Case                          |
| ----- | ---------------------------------------- | --------------------------------- |
| Dummy | Passed around but not used               | Argument filler                   |
| Stub  | Returns predefined data                  | Control the test environment      |
| Fake  | Realistic but lightweight implementation | In-memory DB, simplified logic    |
| Spy   | Records interactions                     | Manual verification of behavior   |
| Mock  | Automated behavior verification          | With `unittest.mock` or libraries |