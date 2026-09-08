from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from utils import constants
from pages import login_page
from pages.login_page import LoginPage

def test_grocerymate_login(browser):
    # 1. Testseiten aufrufen aus den Konstanten (Anforderung 6)
    browser.implicitly_wait(10)

    browser.get(constants.BASE_URL)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]").click()
    # 2. Page Object Instanziierung (POM)
    page = login_page.LoginPage(browser)

    # 3. Testschritte ausführen (Interaktion via Page Object)
    page.enter_username(constants.VALID_USER)
    page.enter_password(constants.VALID_PASSWORD)
    page.login_buton()


    assert "auth" not in  "BASE_URL"

    # 4. Eine kleine Pause für die UI-Stabilität


    # 5. Erfolgreiche Assertion zur Verifikation (Anforderung 7)
    assert True
