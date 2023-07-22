import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium import webdriver

@pytest.fixture()
def setup():
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_argument("headless")
    driver = webdriver.Chrome() #options=chrome_options
    driver.get("https://demo.nopcommerce.com/")
    driver.maximize_window()
    return driver

#===================================              FOR CROSS-BROWSING TESING                  ===========================
# def pytest_addoption(parser):
#     parser.addoption("--browser")
#
# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")
#
# @pytest.fixture()
# def setup(browser):
#
#     if browser == "chrome":
#         driver = webdriver.Chrome()
#         driver.get("https://demo.nopcommerce.com/")
#
#
#     elif browser == "edge":
#         driver = webdriver.Edge()
#         driver.get("https://demo.nopcommerce.com/")
#
#     elif browser == "firefox":
#         driver = webdriver.Firefox()
#         driver.get("https://demo.nopcommerce.com/")
#
#
#     else:
#         chrome_options = webdriver.ChromeOptions()
#         chrome_options.add_argument("headless")
#         driver = webdriver.Chrome(options=chrome_options)
#         driver.get("https://demo.nopcommerce.com/")
#         driver.maximize_window()
#         print("opening in non-GUI mode.")
#
#     driver.maximize_window()
#     return driver



