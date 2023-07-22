import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from utilities.readConfigFile import Read_values
from pageObject.nopCommercePOM   import RegistrationPage
from pageObject.nopCommercePOM import LoginPage
import pytest
from utilities.logger import LogGenerate

class Test_LoginPage():

    get_Login_Email = Read_values.getEmail()
    get_Login_Password = Read_values.getPassword()
    logs = LogGenerate.loggen()

    def test_correct_URL_001(self, setup):
        self.driver = setup
        self.logs.info("checking if URL is correct.")
        if self.driver.title == 'nopCommerce demo store':
            self.logs.info("URL is correct, Test Passed.")
            assert True
        else:
            self.logs.info("URL is incorrect, Test Failed.")
            assert False
        self.driver.close()
        self.logs.info("Test 'test_correct_URL_001' completed")

    def test_Correct_login_002(self, setup):
        self.driver = setup

        self.login_attribute = LoginPage(self.driver)
        self.logs.info("click Login option")
        self.login_attribute.Click_Login_option()
        time.sleep(3)
        self.logs.info("Enter Email id.")
        self.login_attribute.Enter_email_ID(self.get_Login_Email)
        self.logs.info("Enter password.")
        self.login_attribute.Enter_password(self.get_Login_Password)
        print(self.get_Login_Password)
        self.logs.info("Click 'Remember me' box.")
        self.login_attribute.Remember_me()
        self.logs.info("Click Login Button.")
        self.login_attribute.Hit_login_button()
        self.logs.info("Test 'test_Correct_login_002' completed")

    def test_Incorrect_login_003(self, setup):
        self.driver = setup

        self.login_attribute = LoginPage(self.driver)
        self.login_attribute.Click_Login_option()
        time.sleep(3)
        self.login_attribute.Enter_email_ID("akshay@gmail.com")
        time.sleep(3)
        self.login_attribute.Enter_password("@123")
        time.sleep(3)
        self.login_attribute.Hit_login_button()
        self.login_attribute.Error_message()

        if self.login_attribute.Error_message() == "No customer account found":
            print("No customer account found.")
            assert True
        else:
            assert False


    # @pytest.mark.parametrize("email, password, status", [("akshay@gmail.com", "Babayaga@123", "Fail"),
    #                                                      ("akshay16sakhare@gmail.com", "Babayaga", "Fail"),
    #                                                      ("akshay@gmail.com", "Babayaga", "Fail"),
    #                                                      ("akshay16sakhare@gmail.com", "Babayaga@123", "Pass")])
    # def test_params004(self, setup, email, password, status):
    #     self.driver = setup
    #
    #     self.login_attribute = LoginPage(self.driver)
    #     self.login_attribute.Click_Login_option()
    #     time.sleep(3)
    #     self.login_attribute.Enter_email_ID(email)
    #     self.login_attribute.Enter_password(password)
    #     self.login_attribute.Hit_login_button()
    #
    #     if status == "Pass":
    #         # for login test cases where test cases are expected to be successful.
    #         assert self.login_attribute.is_login_successful(), "Login Successful, Test Passed"
    #     elif status == "Fail":
    #         # For negative test cases where login is expected to fail
    #         assert self.login_attribute.is_login_failed(), "Login Failed, Test Passed"
    #

            # if status == "Pass":
        #     #for login test cases where test cases are expected to be successful.
        #     self.logs.info("Checking if login is successfull.")
        #     if self.login_attribute.is_login_successful():
        #         self.logs.info("Login Successful, Test Passed")
        #         assert True
        #     else:
        #         self.logs.info("Login Failed, Test Failed")
        #         assert False
        #
        # elif status == "Fail":
        #     # For negative test cases where login is expected to fail
        #     self.logs.info("Checking if login is unsuccessful.")
        #     if self.login_attribute.is_login_failed():
        #         self.logs.info("Login failed, Test Passed.")
        #         assert True
        #     else:
        #         assert False

            self.driver.close()
            self.logs.info("Test 'test_params004' completed")







