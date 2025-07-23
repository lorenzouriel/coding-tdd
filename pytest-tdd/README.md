# TDD with Pytest
This project implements the `Funcionario` class using **Test-Driven Development (TDD)** with the **Pytest** framework. It focuses on best practices for automated testing in Python, including:
- Code coverage with `pytest-cov`
- The **Given / When / Then** methodology
- Custom **pytest markers**
- HTML, terminal, and XML test reports

## Project Structure
```bash
pytest-tdd/
├── code/                       # Source code
│   └── bytebank.py             # Funcionario class
├── tests/                      # Unit tests
│   ├── __init__.py
│   └── test\_bytebank.py
├── coverage\_relatorio\_html/    # HTML coverage report (generated)
├── .coveragerc                 # Coverage configuration
├── pytest.ini                  # Pytest configuration
├── report.xml                  # XML test report (generated)
└── requirements.txt            # Dependencies
```

## Requirements
- Python 3.12
- Virtual environment with dependencies installed:
```bash
uv venv
uv pip install -r requirements.txt
```

## Running Tests

```bash
pytest
```

This command will:
* Run all tests
* Show a coverage report in the terminal
* Respect all configuration in `pytest.ini`

## Running Specific Tests

### By name using `-k`
```bash
pytest -k idade
```

### By marker (`@mark.calcular_bonus`)
```bash
pytest -m calcular_bonus
```

## Code Coverage
### Terminal Report (default)
```bash
pytest
```

### HTML Report
```bash
pytest --cov=code tests/ --cov-report html
```

Open the generated file:
```bash
coverage_relatorio_html/index.html
```

## Generating XML Reports (for CI/CD or tools integration)
```bash
# Test report
pytest --junitxml=report.xml

# Coverage report
pytest --cov-report=xml
```

## Best Practices Applied
* Descriptive test names like `test_when_age_receives_13_03_2000_should_return_25`
* Use of **Given / When / Then** structure
* `pytest.ini` for automatic test and coverage configuration
* `.coveragerc` to exclude unnecessary methods (e.g., `__str__`) from coverage