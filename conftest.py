import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default='chrome',
                     help="Choose browser: chrome (default) or firefox")
    parser.addoption('--language', action='store', default='en',
                     help="Choose language, default <en>")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption('browser_name')
    driver = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        driver = webdriver.Firefox()
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield driver
    print("\nquit browser..")
    driver.quit()
