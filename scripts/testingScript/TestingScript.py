import os
import random
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


os.environ['PATH'] += r'/home/grudos/Pulpit/Biz/scripts/seleniumDriver/linux/chromedriver'
driver = webdriver.Chrome()
driver.maximize_window()

added_lamps_count = 10
categories_urls = ["https://localhost/pl/25-lampy-sufitowe-plafony", "https://localhost/pl/31-lampy-zewnetrzne-wiszace"]
lamp_count_on_site = 12

def addLampsToCart(category_url, category_lamps_count):
    driver.get(category_url)

    page = 1
    added_lamp_num = 0
    site_lamp_num = 0

    while added_lamp_num < category_lamps_count:

        if site_lamp_num == lamp_count_on_site:
            page += 1
            site_lamp_num = 0

        if page == 1:
            driver.get(category_url)
        else:
            driver.get(category_url+"?page="+str(page))

        lamp = driver.find_elements(By.CSS_SELECTOR, 'a[class="thumbnail product-thumbnail"]')[site_lamp_num]
        driver.get(lamp.get_attribute("href"))

        quantity = driver.find_element(By.CSS_SELECTOR, 'div[class="product-quantities"] span').get_attribute("data-stock")
        #print(quantity)

        # if there are 0 products in stock, it is not added
        try:
            amount = random.randint(1, int(quantity) - 1)

            input_amount = driver.find_element(By.CSS_SELECTOR, 'div[class="qty"] input')
            # MOZE LEPIEJ UZYC .clear() O ILE TUTAJ ZADZIALA BO NIE SPRAWDZALEM
            #input_amount.clear()
            input_amount.send_keys(Keys.DELETE)
            input_amount.send_keys(amount)

            driver.find_element(By.CSS_SELECTOR, 'button[class$="add-to-cart"]').click()

            added_lamp_num += 1
        except:
            pass

        site_lamp_num += 1

def deleteOneProductFromCart():
    driver.get("https://localhost/pl/koszyk")

    # MOZNA EWENTUALNIE ZROBIC ZEBY WYRZUCALO PRODUKT O LOSOWYM INDEKSIE A NIE ZAWSZE PIERWSZY
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'i[class="material-icons float-xs-left"]').click()


first_category_lamps_count = 5
second_category_lamps_count = added_lamps_count - first_category_lamps_count

addLampsToCart(categories_urls[0], first_category_lamps_count)
addLampsToCart(categories_urls[1], second_category_lamps_count)

deleteOneProductFromCart()

