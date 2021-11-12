import os
import random
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


os.environ['PATH'] += r'/home/grudos/Pulpit/Biz/scripts/seleniumDriver/linux/chromedriver'
driver = webdriver.Chrome()
driver.maximize_window()

admin_panel = "https://localhost/admin123456"
login_admin = "prestashop@prestashop.pl"
password_admin = "prestashop"

categories_import_settings = ["truncate_1", "regenerate_0", "forceIDs_0", "sendemail_0"]
products_import_settings = ["truncate_1", "match_ref_0", "regenerate_0", "forceIDs_0", "sendemail_0"]


def loggingIn():
    login_field = driver.find_element(By.CSS_SELECTOR, 'input[name="email"]')
    login_field.clear()
    login_field.send_keys(login_admin)

    password_field = driver.find_element(By.CSS_SELECTOR, 'input[name="passwd"]')
    password_field.clear()
    password_field.send_keys(password_admin)

    driver.find_element(By.CSS_SELECTOR, 'button[id="submit_login"]').click()


def goToTheCategoryPage():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "subtab-AdminCategories")))

    categories_page = driver.find_element(By.CSS_SELECTOR, 'li[id="subtab-AdminCategories"] a').get_attribute("href")
    driver.get(categories_page)


def importCategories():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'a[id="category-grid-action-import"]')))

    import_categories_page = driver.find_element(By.CSS_SELECTOR, 'a[id="category-grid-action-import"]').get_attribute("href")
    driver.get(import_categories_page)

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'span[class="ps-switch"]')))

    import_categories = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="entity"]'))
    import_categories.select_by_visible_text("Kategorie")

    file_upload = driver.find_element(By.CSS_SELECTOR, 'input[id="file"]')
    # Z WYKORZYSTANIEM os.getcwd() DO OBECNEJ SCIEZKI MOZNA COS TUTAJ WYKOMBINOWAC
    file_upload.send_keys("/home/grudos/Pulpit/Biz/scripts/scraper/data/categories.csv")
    time.sleep(1)

    adjustSettings(categories_import_settings)
    confirmImport()


def importProducts():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'select[name="entity"]')))

    import_products = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="entity"]'))
    import_products.select_by_visible_text("Produkty")

    file_upload = driver.find_element(By.CSS_SELECTOR, 'input[id="file"]')
    # Z WYKORZYSTANIEM os.getcwd() DO OBECNEJ SCIEZKI MOZNA COS TUTAJ WYKOMBINOWAC
    # PLIK NIZEJ JEST PRAWIDLOWY ALE DUZY TO NIE CHCE NA NIM TESTOWAC BO DLUGO BY TRWALO NA RAZIE
    # file_upload.send_keys("/home/grudos/Pulpit/Biz/scripts/scraper/data/products.csv")
    file_upload.send_keys("/home/grudos/Pulpit/Biz/scripts/scraper/data/product.csv")
    time.sleep(1)

    adjustSettings(products_import_settings)
    confirmImport()


def confirmImport():
    driver.find_element(By.CSS_SELECTOR, 'button[name="submitImportFile"]').click()
    driver.switch_to.alert.accept()

    driver.find_element(By.CSS_SELECTOR, 'button[name="import"]').click()

    # LINIA NIZEJ DO WYRZUCENIA JAK SIE SCRAPERA POPRAWI I NIE BEDZIE SIE CZEPIAL O PODATKI
    try:
        driver.find_element(By.CSS_SELECTOR, 'button[id="import_continue_button"]').click()
    except:
        pass

    WebDriverWait(driver, 10000).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[id="import_close_button"]')))
    driver.find_element(By.CSS_SELECTOR, 'button[id="import_close_button"]').click()


def adjustSettings(import_settings):
    for i in range(len(import_settings)):
        try:
            driver.find_element(By.CSS_SELECTOR, 'input[id=' + import_settings[i] + ']').click()
        except:
            pass


def settingIndexingProducts():
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'li[id="subtab-AdminParentSearchConf"]')))

    search_preferences = driver.find_element(By.CSS_SELECTOR, 'li[id="subtab-AdminParentSearchConf"] a').get_attribute("href")
    driver.get(search_preferences)

    rebuild_index = driver.find_element(By.LINK_TEXT, "Przebuduj cały indeks")
    rebuild_index.click()

    announcement = driver.find_element(By.CSS_SELECTOR, 'div[class="alert alert-success"] button')
    announcement.click()
    time.sleep(1)




driver.get(admin_panel)
loggingIn()
goToTheCategoryPage()
importCategories()
importProducts()
settingIndexingProducts()
driver.close()