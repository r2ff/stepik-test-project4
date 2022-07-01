import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default="en",
                     help="Choose language browser")


@pytest.fixture(scope="function")
def browser(request):
    browser_language = request.config.getoption("language")
    if browser_language is not None:
        print("\nstart chrome browser for test..")
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': browser_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should not be None")
    yield browser
    print("\nquit browser..")
    browser.quit()
