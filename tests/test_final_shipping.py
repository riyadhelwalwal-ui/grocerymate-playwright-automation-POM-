
from pages.login_page import LoginPage
from pages.shipping_page import ShippingPage
from pages.age_page import AgePage
from utils import constants


def test_shipping_costs_validation(browser):
    # Schritt 1: Cookies loeschen und Homepage oeffnen
    browser.delete_all_cookies()
    browser.get(constants.BASE_URL)


    # Schritt 2: Erfolgreich einloggen
    login_page = LoginPage(browser)
    login_page.click_profile()

    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()


    # Schritt 3: Shop oeffnen
    login_page.enter_shop()



    age_page = AgePage(browser)
    age_page.enter_birthdate(constants.TEST_AGE_1987)
    age_page.click_confirm()


    # Schritt 4: Zahl 5 eingeben, um 15 Gala Apples zu erhalten (30 Euro)
    shipping_page = ShippingPage(browser)
    shipping_page.enter_apples_quantity("5")

    shipping_page.click_add_to_cart()

    browser.refresh()


    # Schritt 5: Zum Checkout wechseln
    shipping_page.go_to_checkout()


    # Schritt 6: Verifikation - Sicherstellen, dass bei 30 Euro Versandkosten kostet 4.95
    assert "4.95" in browser.page_source
