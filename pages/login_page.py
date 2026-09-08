# pages/login_page.py
from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver


        # --- Element-Lokatoren ---
        self.Profile_icon = (By.XPATH,"//div[@class='headerIcon']")
        self.username_input = (By.XPATH, "//input[@type='email' or placehoder = 'Email Address']")
        self.password_input = (By.XPATH, "//input[@type='password']")
        self.login_button = (By.XPATH, "//button[@type='submit' and text()='Sign In']")
        self.shop_button = (By.XPATH, "//a[text()='Shop']")
        self.birth_input = (By.XPATH,"//input[@type='text']")

    # --- Seiten-Aktionen ---

    def click_profile(self):
        self.driver.find_element(*self.Profile_icon).click()

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)

    def login_buton(self):
        self.driver.find_element(*self.login_button).click()

    def enter_shop(self):
        self.driver.find_element(*self.shop_button).click()

    def enter_birth(self):
        self.driver.find_element(*self.birth_input).click()



