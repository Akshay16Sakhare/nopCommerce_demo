from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select

class RegistrationPage():

    reg_button = (By.XPATH, "//a[@class='ico-register']")
    my_gender = (By.XPATH, "//input[@id='gender-male']")
    first_name = (By.NAME, "FirstName")
    last_name = (By.NAME, "LastName")
    date = (By.NAME, "DateOfBirthDay")
    month = (By.NAME, "DateOfBirthMonth")
    year = (By.NAME, "DateOfBirthYear")
    inp_email = (By.NAME, "Email")
    company_name = (By.NAME, "Company")
    password = (By.NAME, "Password")
    confirm_password = (By.NAME, "ConfirmPassword")
    reg_button_clk = (By.ID, "register-button")


    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver,3)
        self.drop = Select

    def Reg_Button(self):
        self.driver.find_element(*self.reg_button).click()

    def My_Gender(self):
        ele_1 = self.wait.until(EC.visibility_of_element_located(self.my_gender))
        ele_1.click()

    def First_Name(self, fname):
        self.driver.find_element(*self.first_name).send_keys(fname)

    def Last_Name(self, lname):
        self.driver.find_element(*self.last_name).send_keys(lname)

    def Date(self, dvalue):
        ele_2 = self.driver.find_element(*self.date)
        Select(ele_2).select_by_value(dvalue)

    def Month(self, mvalue):
        ele_3 = self.driver.find_element(*self.month)
        Select(ele_3).select_by_value(mvalue)

    def Year(self, yvalue):
        ele_4 = self.driver.find_element(*self.year)
        Select(ele_4).select_by_value(yvalue)

    def Email(self, Evalue):
        self.driver.find_element(*self.inp_email).send_keys(Evalue)

    def Company_Name(self, company):
        self.driver.find_element(*self.company_name).send_keys(company)

    def Password(self, password_val):
        self.driver.find_element(*self.password).send_keys(password_val)

    def Confirm_Password(self, password_val):
        self.driver.find_element(*self.confirm_password).send_keys(password_val)

    def Click_Resgister(self):
        self.driver.find_element(*self.reg_button_clk).click()

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    login_button = (By.XPATH, "//a[@class='ico-login']")
    email_ID = (By.ID, "Email")
    login_password = (By.ID, "Password")
    remember_me = (By.ID, "RememberMe")
    hit_login = (By.XPATH, "//button[@class='button-1 login-button']")
    error_message = (By.XPATH, "//li[normalize-space()='No customer account found']")

    def Click_Login_option(self):
        self.driver.find_element(*self.login_button).click()

    def Enter_email_ID(self, email):
        self.driver.find_element(*self.email_ID).send_keys(email)

    def Enter_password(self, password):
        self.driver.find_element(*self.login_password).send_keys(password)

    def Remember_me(self):
        self.driver.find_element(*self.remember_me).click()

    def Hit_login_button(self):
        self.driver.find_element(*self.hit_login).click()

    def Error_message(self):
        message = self.driver.find_element(*self.error_message)
        return message.text




