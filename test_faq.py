"""FAQ functionality tests."""

import pytest
from pages.faq_page import FAQPage
from utils.test_data import TestData
from utils.logger import get_logger

logger = get_logger(__name__)


class TestFAQ:
    """Test suite for FAQ functionality."""

    @pytest.mark.smoke
    def test_create_faq(self, driver):
        """Test creating a new FAQ entry.
        
        Steps:
            1. Open FAQ page
            2. Enter question and answer
            3. Submit FAQ
            4. Verify FAQ appears in list
        """
        logger.info("Starting test_create_faq")
        faq = FAQPage(driver)

        faq.open_url()
        faq.create_faq(TestData.question, TestData.answer)

        assert faq.is_faq_present(TestData.question), "FAQ not found after creation"
        logger.info("Test passed: FAQ created successfully")

    @pytest.mark.regression
    def test_delete_faq(self, driver):
        """Test deleting an FAQ entry."""
        logger.info("Starting test_delete_faq")
        faq = FAQPage(driver)

        faq.open_url()
        faq.create_faq(TestData.question, TestData.answer)
        faq.delete_faq(TestData.question)

        assert not faq.is_faq_present(TestData.question), "FAQ still present after deletion"
        logger.info("Test passed: FAQ deleted successfully")
