# Selenium Test Automation Framework

## Application Information

- **Application Name**: Selenium Test Automation Framework
- **Description**: Automated end-to-end testing framework for web applications using Selenium WebDriver and pytest
- **Programming Language**: Python 3.8+
- **Framework**: Selenium WebDriver
- **Runtime**: Python 3.8, 3.9, 3.10, 3.11
- **Build Tool**: pytest
- **Package Manager**: pip
- **Entry Point**: pytest (test runner)

## Project Overview

This is a robust test automation framework using:
- **Page Object Model (POM)** for maintainability
- **pytest** for test execution and fixtures
- **Selenium WebDriver** for browser automation
- **Logging** for debugging and monitoring
- **Environment variables** for configuration management
- **Docker** for containerization
- **GitHub Actions** for CI/CD

## Repository Structure

```
AI-testing/
├── pages/                    # Page Object Model classes
│   ├── login_page.py        # Login page object
│   └── faq_page.py          # FAQ page object
├── tests/                    # Test files
│   ├── test_login.py
│   ├── test_faq.py
│   └── test_checkout_with_errors.py
├── utils/                    # Utility modules
│   ├── test_data.py         # Test data constants
│   ├── logger.py            # Logging configuration
│   └── file_reader.py       # File utilities
├── config/                   # Configuration files
│   ├── config.yaml          # Main configuration
│   └── locators.yaml        # UI element locators
├── conftest.py              # pytest configuration and fixtures
├── pytest.ini               # pytest settings
├── requirements.txt         # Python dependencies
├── .env.example             # Environment variables template
├── .gitignore               # Git ignore rules
├── Dockerfile               # Docker configuration
├── docker-compose.yml       # Docker compose setup
├── .github/workflows/       # CI/CD pipelines
│   └── tests.yml           # GitHub Actions workflow
├── README.md                # Project documentation
├── CONTRIBUTING.md          # Contribution guidelines
└── setup.py                 # Python package setup
```

## Configuration Files

### Key Files:
- **pytest.ini**: pytest configuration
- **requirements.txt**: Python package dependencies
- **.env**: Environment-specific variables
- **config/config.yaml**: Application configuration
- **conftest.py**: pytest fixtures and hooks

## Testing Framework

- **Framework**: pytest
- **Browser Automation**: Selenium WebDriver
- **Pattern**: Page Object Model (POM)

## External Services

- **Application Under Test**: https://www.saucedemo.com/ (Demo site)
- **Browser**: Chrome (via ChromeDriver)

## CI/CD Pipeline

- **Tool**: GitHub Actions
- **Triggers**: Push to main/develop branches, Pull Requests
- **Actions**: Run tests, Generate reports

## Environment Management

Configure via `.env` file:
```
BASE_URL=https://www.saucedemo.com/
BROWSER=chrome
HEADLESS=false
WAIT_TIME=10
LOG_LEVEL=INFO
```

## Installation

```bash
# Install dependencies
pip install -r requirements.txt

# Download ChromeDriver
# Place in PATH or update config

# Run tests
pytest tests/ -v
```

## Running Tests

```bash
# Run all tests
pytest

# Run specific test file
pytest tests/test_login.py -v

# Run with markers
pytest -m "login" -v

# Run with coverage
pytest --cov=. tests/

# Run in parallel
pytest -n auto tests/
```

## Docker

```bash
# Build image
docker build -t selenium-tests .

# Run tests in container
docker run --rm selenium-tests pytest tests/
```

## Logging

Logs are written to `logs/` directory with timestamps and levels (DEBUG, INFO, WARNING, ERROR).

## Security Tools

- Environment variable validation
- Credentials stored in `.env` (not in code)
- No hardcoded URLs or sensitive data

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT
