from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from utilities.readConfigFile import Read_values
from pageObject.nopCommercePOM import RegistrationPage
from utilities.logger import LogGenerate
from pageObject.nopCommercePOM import LoginPage
import time

class Test_regi():

    get_fName = Read_values.getFirstName()
    get_lName = Read_values.getLastName()
    get_passwrd = Read_values.getPassword()
    get_confirm_passwrd = Read_values.getConfirmPassword()
    get_email = Read_values.getEmail()
    logs = LogGenerate.loggen()

    get_Login_Email = Read_values.getEmail()
    get_Login_Password = Read_values.getPassword()

    def test_register(self, setup):
        self.driver = setup
        self.regi_attribute = RegistrationPage(self.driver)
        self.logs.info("click REGISTER Option.")
        self.regi_attribute.Reg_Button()
        self.logs.info("click GENGER Option.")
        self.regi_attribute.My_Gender()
        self.logs.info("Enter First_Name Option.")
        self.regi_attribute.First_Name(self.get_fName)
        self.logs.info("Enter Last_Name Option.")
        self.regi_attribute.Last_Name(self.get_lName)
        self.logs.info("Select Date Option.")
        self.regi_attribute.Date('16')
        self.logs.info("Select Month Option.")
        self.regi_attribute.Month('6')
        self.logs.info("Select Year Option.")
        self.regi_attribute.Year('1993')
        self.logs.info("Enter Email Option.")
        self.regi_attribute.Email(self.get_email)
        print(self.get_email)
        self.logs.info("Select Company_Name Option.")
        self.regi_attribute.Company_Name('IBM')
        self.logs.info("Enter Password Option.")
        self.regi_attribute.Password(self.get_passwrd)
        print(self.get_passwrd)
        self.logs.info("Confirm_Password Option.")
        self.regi_attribute.Confirm_Password(self.get_confirm_passwrd)
        print(self.get_confirm_passwrd)
        self.logs.info("Click Register Button.")
        self.regi_attribute.Click_Resgister()
        self.logs.info("Successfull Registration complete, test_register Passed.")
        time.sleep(10)

    # def test_Correct_login_002(self, setup):
    #     self.driver = setup
    #
    #     self.login_attribute = LoginPage(self.driver)
    #     self.logs.info("click Login option")
    #     self.login_attribute.Click_Login_option()
    #     time.sleep(3)
    #     self.logs.info("Enter Email id.")
    #     self.login_attribute.Enter_email_ID(self.get_Login_Email)
    #     print(self.get_Login_Email)
    #     self.logs.info("Enter password.")
    #     self.login_attribute.Enter_password(self.get_Login_Password)
    #     print(self.get_Login_Password)
    #     self.logs.info("Click 'Remember me' box.")
    #     self.login_attribute.Remember_me()
    #     self.logs.info("Click Login Button.")
    #     self.login_attribute.Hit_login_button()
    #     self.logs.info("Test 'test_Correct_login_002' completed")
    #     print(self.driver.title)
    #     time.sleep(10)
