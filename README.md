Automation test suite (Page Object Model) for OFD test cases.

Run:
1. pip install -r requirements.txt
2. Set environment variables (QA_URL, TEST_USER, TEST_PASSWORD, etc.) or create a .env file
3. pytest -k "end_to_end or payment or tracking" -v

Notes:
- Tests assume a QA web application; locators are placeholders and must be updated to match the AUT.
- Payment and tracking tests include stubs for sandbox/mock services and may require additional configuration.
