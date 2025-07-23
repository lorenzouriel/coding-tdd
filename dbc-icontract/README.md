# Design by Contract (DbC) in Python with `icontract`
This project demonstrates the use of **Design by Contract (DbC)** in Python using the [`icontract`](https://github.com/Parquery/icontract) library. It shows how to apply **preconditions**, **postconditions**, and **invariants** to ensure code correctness and clearly express assumptions and guarantees.

## Project Structure
```
.
├── user\_with\_contracts.py        # Implementation of User, Repository, EmailService, UserService with contracts
├── test\_user\_service.py          # Pytest tests validating contract enforcement
├── requirements.txt              # Python dependencies
└── README.md                    # This documentation

```

## Setup
1. **Create a virtual environment**:
```bash
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.\.venv\Scripts\activate   # Windows PowerShell
```

2. **Install dependencies:**
```bash
pip install icontract pytest
```

## Implementation Highlights (`user_with_contracts.py`)
* **Preconditions (`@icontract.require`)**: Validate inputs before method runs.
* **Postconditions (`@icontract.ensure`)**: Validate outputs/results after method completes.
* **Invariants (`@icontract.invariant`)**: (Not used here, but supported) Ensure class state consistency.

### Key Contracts Used
| Method                        | Contract Purpose                      | Example Condition                            |
| ----------------------------- | ------------------------------------- | -------------------------------------------- |
| `UserService.register(email)` | Email must contain '@' (precondition) | `@require(lambda email: "@" in email)`       |
| `Repository.save(user)`       | User email must not be empty          | `@require(lambda user: user.email != "")`    |
| `UserService.register(email)` | Return user must have non-empty email | `@ensure(lambda result: result.email != "")` |

## Testing with `pytest`
Tests are in `test_user_service.py` and cover:
| Test Name                         | What It Tests                                                                 | Expected Result                   |
| --------------------------------- | ----------------------------------------------------------------------------- | --------------------------------- |
| `test_register_valid_user`        | Successful registration with valid email                                      | Pass                              |
| `test_register_invalid_email`     | Registration with invalid email (missing '@') triggers precondition violation | Raises `icontract.ViolationError` |
| `test_save_user_with_empty_email` | Saving user with empty email triggers precondition violation                  | Raises `icontract.ViolationError` |
| `test_user_saved_to_repository`   | User saved correctly and can be retrieved                                     | Pass                              |
| `test_postcondition_failure_hack` | Monkeypatching to break postcondition (empty email returned)                  | Raises `icontract.ViolationError` |

### Run all tests:
```bash
pytest -v
```

## What is Design by Contract?
Design by Contract is a programming methodology where functions and methods define formal, precise and verifiable interface specifications, including:
* **Preconditions**: What must be true before execution.
* **Postconditions**: What must be true after execution.
* **Invariants**: What must always be true for a class/object.

This helps catch bugs early, improve code quality, and provide clearer documentation.

## Benefits of using `icontract`
* Declarative and readable contracts with decorators.
* Automatic runtime checks with informative error messages.
* Can integrate easily with any Python codebase.
* Helps to explicitly document assumptions and guarantees.