"""Login Page Object Model."""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.logger import get_logger
from utils.test_data import TestData, BrowserConfig

logger = get_logger(__name__)


class LoginPage:
    """Login Page Object."""

    # Locators
    username_field = (By.ID, "username")
    password_field = (By.ID, "password")
    login_button = (By.ID, "loginBtn")
    error_message = (By.CLASS_NAME, "error-message")

    def __init__(self, driver):
        """Initialize Login Page.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, BrowserConfig.wait_time)
        logger.info("Login Page initialized")

    def open_url(self, url: str = None):
        """Open login page.
        
        Args:
            url: URL to open. Defaults to configured login URL.
        """
        url = url or TestData.login_url
        logger.info(f"Opening login page: {url}")
        self.driver.get(url)

    def enter_username(self, username: str):
        """Enter username in the login form.
        
        Args:
            username: Username to enter
        """
        logger.info(f"Entering username: {username}")
        self.wait.until(EC.visibility_of_element_located(self.username_field)).send_keys(username)

    def enter_password(self, password: str):
        """Enter password in the login form.
        
        Args:
            password: Password to enter
        """
        logger.info("Entering password")
        self.wait.until(EC.visibility_of_element_located(self.password_field)).send_keys(password)

    def click_login_button(self):
        """Click the login button."""
        logger.info("Clicking login button")
        self.wait.until(EC.element_to_be_clickable(self.login_button)).click()

    def login(self, username: str, password: str):
        """Perform login action.
        
        Args:
            username: Username for login
            password: Password for login
        """
        logger.info(f"Logging in as: {username}")
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
        logger.info("Login action completed")

    def is_login_successful(self) -> bool:
        """Check if login was successful.
        
        Returns:
            True if login successful, False otherwise
        """
        logger.info("Checking login success")
        try:
            # Wait for page to load after login
            self.wait.until(EC.url_contains("dashboard"))
            logger.info("Login successful")
            return True
        except Exception as e:
            logger.warning(f"Login check failed: {e}")
            return False

    def get_error_message(self) -> str:
        """Get login error message if any.
        
        Returns:
            Error message text
        """
        logger.info("Getting error message")
        try:
            error_element = self.wait.until(EC.visibility_of_element_located(self.error_message))
            error_text = error_element.text
            logger.warning(f"Login error: {error_text}")
            return error_text
        except Exception as e:
            logger.info("No error message found")
            return None
