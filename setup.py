"""Setup configuration for Selenium Test Automation Framework."""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="selenium-test-automation",
    version="1.0.0",
    author="Your Name",
    author_email="your.email@example.com",
    description="Selenium WebDriver based test automation framework with POM pattern",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/selenium-tests",
    packages=find_packages(exclude=["tests", "*.tests"]),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
    ],
    python_requires=">=3.8",
    install_requires=[
        "selenium>=4.0.0",
        "pytest>=7.0.0",
        "python-dotenv>=0.20.0",
        "pyyaml>=6.0",
        "loguru>=0.6.0",
        "webdriver-manager>=3.8.0",
    ],
    extras_require={
        "dev": [
            "pytest-cov>=3.0.0",
            "pytest-xdist>=2.5.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "pylint>=2.0.0",
            "isort>=5.10.0",
        ],
        "reporting": [
            "allure-pytest>=2.10.0",
            "pytest-html>=3.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "run-tests=pytest:main",
        ],
    },
    include_package_data=True,
    project_urls={
        "Bug Reports": "https://github.com/yourusername/selenium-tests/issues",
        "Source": "https://github.com/yourusername/selenium-tests",
        "Documentation": "https://github.com/yourusername/selenium-tests/wiki",
    },
)
