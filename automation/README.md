Automation suite (POM, Selenium, Python)

Structure:
- pom/pages: Page object models
- tests: pytest testcases mapped to TC-OBJ-xxx
- performance: locust and synthetic scripts

Run tests:
1. pip install -r requirements.txt
2. copy .env.example to .env and configure BASE_URL and credentials
3. pytest -q

Performance:
- Locust: locust -f performance/locustfile.py --host=https://staging-your-app
- Synthetic: python performance/synthetic_performance.py

Notes:
- Locators in page objects are placeholders. Update selectors to match the application under test.
- Some tests require sandbox endpoints to be configured via environment variables.
