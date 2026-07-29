# Contributing to Selenium Test Automation Framework

## Code of Conduct

Be respectful, inclusive, and professional in all interactions.

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/YOUR_USERNAME/selenium-tests.git`
3. Create a feature branch: `git checkout -b feature/your-feature`
4. Install dependencies: `pip install -r requirements.txt`

## Development Setup

```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env
```

## Running Tests Locally

```bash
# Run all tests
pytest tests/ -v

# Run specific test file
pytest tests/test_login.py -v

# Run with markers
pytest -m "smoke" -v

# Run with coverage
pytest --cov=. tests/ --cov-report=html
```

## Code Style

- Follow PEP 8 guidelines
- Use type hints where applicable
- Maximum line length: 100 characters
- Use meaningful variable and function names

### Formatting

```bash
# Format code with black
black . --line-length=100

# Sort imports with isort
isort .

# Lint with pylint
pylint pages/ utils/ tests/
```

## Test Structure

### Page Object Model

```python
from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)

class MyPage:
    """Page Object for My Page."""
    
    # Define locators
    element_name = (By.ID, "element_id")
    
    def __init__(self, driver):
        self.driver = driver
    
    def perform_action(self):
        """Perform action on the page."""
        logger.info("Performing action")
        self.driver.find_element(*self.element_name).click()
```

### Test File Structure

```python
import pytest
from pages.my_page import MyPage
from utils.test_data import TestData

class TestMyFeature:
    """Test suite for My Feature."""
    
    @pytest.mark.smoke
    def test_happy_path(self, driver):
        """Test happy path scenario."""
        page = MyPage(driver)
        page.perform_action()
        assert page.verify_action()
```

## Commit Message Guidelines

Use conventional commits:

```
feat: Add new feature
fix: Fix bug in existing feature
docs: Update documentation
test: Add or update tests
style: Code formatting changes
refactor: Code refactoring without changing functionality
chore: Dependencies update, build changes
```

Example:
```
feat: Add login page object and tests

- Implement LoginPage class with locators and methods
- Add test_login.py with login validation tests
- Update README with setup instructions
```

## Pull Request Process

1. Update README.md with any new features
2. Add or update tests for new functionality
3. Ensure all tests pass locally: `pytest tests/ -v`
4. Run linting: `black .` and `flake8`
5. Update CHANGELOG.md
6. Create PR with clear description of changes
7. Request review from maintainers
8. Address review comments

## Test Coverage

Aim for at least 80% code coverage:

```bash
pytest --cov=. --cov-report=html tests/
open htmlcov/index.html
```

## Reporting Issues

Include:
- Clear description of the issue
- Steps to reproduce
- Expected vs actual behavior
- Python version and OS
- Relevant logs or screenshots

## Questions?

- Open an issue with the `question` label
- Check existing issues/discussions
- Review documentation in README.md

## License

By contributing, you agree your code will be licensed under the MIT License.

Thank you for contributing! 🎉
