import pytest
from pages.faq_page import FAQPage
from utils.test_data import TestData

def test_create_faq(driver):
    faq = FAQPage(driver)

    faq.open_url()
    faq.create_faq(TestData.question, TestData.answer)

    assert faq.is_faq_present(TestData.question)
