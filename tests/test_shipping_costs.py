from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.age_page import AgePage
from pages.shipping_page import ShippingPage
from utils import constants


def test_shipping_free_at_20_euro(browser):
    # Schritt 1: Cookies loeschen für eine saubere Testumgebung
    browser.delete_all_cookies()

    # Schritt 2: Homepage oeffnen
    browser.get(constants.BASE_URL)


    # Schritt 3: Einloggen (Account Icon und Daten eingeben)
    login_page = LoginPage(browser)
    login_page.click_profile()

    login_page.enter_username(constants.VALID_USER)
    login_page.enter_password(constants.VALID_PASSWORD)
    login_page.login_buton()


    # Schritt 4: Auf die Shop-Schaltflaeche klicken
    login_page.enter_shop()


    # Schritt 5: Altersverifikation ausfuellen
    age_page = AgePage(browser)
    age_page.enter_birthdate(constants.TEST_AGE_1987)
    age_page.click_confirm()


    # Schritt 6: Gala Apples auf 10 setzen (20€) und zum Checkout gehen
    shipping_page = ShippingPage(browser)
    shipping_page.enter_apples_quantity("0")


    shipping_page.click_add_to_cart()

    browser.refresh()
    shipping_page.click_add_to_cart()

    # تحديث الصفحة
    browser.refresh()

    # 🚀 الانتظار المشروط الذكي (Explicit Wait) اللي يبيك باتريك تديره توا:
    # بنقولوا للروبوت: معاك ليميت 10 ثواني، استنى مشروط لين زر الـ Checkout يبدأ قابل للضغط
    # (تأكد من الـ locator بتاع الزر جوة كلاس الـ shipping_page)
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//button[contains(., 'Buy now')]"))
    )



    # أول ما يظهر ويجهز الزر، اضغط عليه بنظافة وطير
    shipping_page.go_to_checkout()

    # Schritt 7: Verifikation - überprüfen, ob der Logik-Bug existiert
    # الميزان الذكي اللي يصيد البق تاعت الـ 20 يورو
    assert "Free shipment if your purchase is 20€ or more." in browser.page_source
