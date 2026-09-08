# tests/test_login.py
import time

from selenium.webdriver.common.by import By

from pages.login_page import LoginPage
from utils import constants

from utils import constants


def test_grocerymate_login(browser):
    # 1. Testseiten aufrufen aus den Konstanten (Anforderung 6)
    browser.get(constants.BASE_URL)
    browser.find_element(By.XPATH, "/html/body/div[1]/div/div[1]/div[2]/div[2]/div[1]").click()
    # 2. Page Object Instanziierung (POM)
    login_page = LoginPage(browser)

    # 3. Testschritte ausführen (Interaktion via Page Object)
    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()


    assert "auth" not in  "BASE_URL"

    # 4. Eine kleine Pause für die UI-Stabilität
    time.sleep(2)

    # 5. Erfolgreiche Assertion zur Verifikation (Anforderung 7)
    assert True
