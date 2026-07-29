"""FAQ Page Object Model."""

from selenium.webdriver.common.by import By
from utils.logger import get_logger

logger = get_logger(__name__)


class FAQPage:
    """FAQ Page Object."""

    # Locators
    question_input = (By.ID, "faq_question")
    answer_textarea = (By.ID, "faq_answer")
    submit_button = (By.ID, "submit_faq")
    faq_list = (By.ID, "faq_list")

    def __init__(self, driver):
        """Initialize FAQ Page.
        
        Args:
            driver: Selenium WebDriver instance
        """
        self.driver = driver
        logger.info("FAQ Page initialized")

    def open_url(self, url: str = "https://example.com/faq"):
        """Open FAQ page.
        
        Args:
            url: URL to open
        """
        logger.info(f"Opening FAQ page: {url}")
        self.driver.get(url)

    def create_faq(self, question: str, answer: str):
        """Create a new FAQ entry.
        
        Args:
            question: FAQ question
            answer: FAQ answer
        """
        logger.info(f"Creating FAQ: {question}")
        self.driver.find_element(*self.question_input).send_keys(question)
        self.driver.find_element(*self.answer_textarea).send_keys(answer)
        self.driver.find_element(*self.submit_button).click()
        logger.info("FAQ submitted successfully")

    def is_faq_present(self, question: str) -> bool:
        """Check if FAQ question is present.
        
        Args:
            question: FAQ question to search
            
        Returns:
            True if FAQ is present, False otherwise
        """
        logger.info(f"Checking if FAQ present: {question}")
        try:
            faq_element = self.driver.find_element(
                By.XPATH, f"//*[contains(text(), '{question}')]"
            )
            logger.info("FAQ found")
            return True
        except Exception as e:
            logger.warning(f"FAQ not found: {e}")
            return False

    def delete_faq(self, question: str):
        """Delete a FAQ entry.
        
        Args:
            question: FAQ question to delete
        """
        logger.info(f"Deleting FAQ: {question}")
        delete_button = self.driver.find_element(
            By.XPATH,
            f"//*[contains(text(), '{question}')]/ancestor::*//button[contains(@class, 'delete')]",
        )
        delete_button.click()
        logger.info("FAQ deleted successfully")
