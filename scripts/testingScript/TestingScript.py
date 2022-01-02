#!/usr/bin/env python3

import os
import random
import time
import string

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

os.chdir("../seleniumDriver/linux")
path = os.getcwd() + "/chromedriver"
s = Service(r"{}".format(path))
driver = webdriver.Chrome(service=s)
driver.maximize_window()

added_lamps_count = 10
categories_urls = ["https://localhost/120-lampy-zewnetrzne-sufitowe", "https://localhost/150-oswietlenie-garderoby"]
lamp_count_on_site = 12

first_category_lamps_count = 5
second_category_lamps_count = added_lamps_count - first_category_lamps_count

ascii_letters = string.ascii_letters
ascii_numbers = string.digits


def generateRandomStrings(min_characters, max_characters):
    string = ''
    for _ in range(min_characters, max_characters):
        string += random.choice(ascii_letters)
    return string


def generatePostcode():
    postcode = ''
    for _ in range(0, 2):
        postcode += random.choice(ascii_numbers)
    postcode += "-"
    for _ in range(3, 6):
        postcode += random.choice(ascii_numbers)
    return postcode


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

        lamp = driver.find_elements(By.CSS_SELECTOR, 'a[class="thumbnail product-thumbnail"]')[site_lamp_num].get_attribute("href")
        driver.get(lamp)

        # if there are 0 products in stock, it is not added
        try:
            quantity = driver.find_element(By.CSS_SELECTOR, 'div[class="product-quantities"] span').get_attribute(
                "data-stock")
            amount = random.randint(1, int(quantity) - 1)
            input_amount = driver.find_element(By.CSS_SELECTOR, 'div[class="qty"] input')
            input_amount.send_keys(Keys.DELETE)
            input_amount.send_keys(amount)

            driver.find_element(By.CSS_SELECTOR, 'button[class$="add-to-cart"]').click()
            added_lamp_num += 1
        except:
            pass

        site_lamp_num += 1


def deleteOneProductFromCart():
    driver.get("https://localhost/koszyk")

    # removing the first product on the list from the cart
    time.sleep(1)
    driver.find_element(By.CSS_SELECTOR, 'i[class="material-icons float-xs-left"]').click()


def createAccount():
    make_order = driver.find_element(By.CSS_SELECTOR, 'div[class="text-sm-center"] a').get_attribute("href")
    driver.get(make_order)

    gender = random.randint(0, 1)
    driver.find_elements(By.CSS_SELECTOR, 'span[class="custom-radio"] input')[gender].click()

    name = driver.find_element(By.CSS_SELECTOR, 'input[id="field-firstname"]')
    created_name = generateRandomStrings(3, 15)
    name.clear()
    name.send_keys(created_name)

    surname = driver.find_element(By.CSS_SELECTOR, 'input[id="field-lastname"]')
    created_surname = generateRandomStrings(3, 15)
    surname.clear()
    surname.send_keys(created_surname)

    email = driver.find_element(By.CSS_SELECTOR, 'input[id="field-email"]')
    created_email = generateRandomStrings(3, 15) + "@gmail.com"
    email.clear()
    email.send_keys(created_email)

    password = driver.find_element(By.CSS_SELECTOR, 'input[id="field-password"]')
    created_password = generateRandomStrings(8, 15)
    password.clear()
    password.send_keys(created_password)

    # processing of personal data
    driver.find_element(By.CSS_SELECTOR, 'input[name="customer_privacy"]').click()
    # agree to the terms and conditions
    #driver.find_element(By.CSS_SELECTOR, 'input[name="psgdpr"]').click()
    driver.find_element(By.CSS_SELECTOR, 'span[class="VIiyi"]').click()

    driver.find_element(By.CSS_SELECTOR, 'button[name = "continue"]').click()

    return created_email, created_password


def completeAddresses():
    address = driver.find_element(By.CSS_SELECTOR, 'input[id="field-address1"]')
    created_address = generateRandomStrings(3, 15)
    address.clear()
    address.send_keys(created_address)

    city = driver.find_element(By.CSS_SELECTOR, 'input[id="field-city"]')
    created_city = generateRandomStrings(3, 15)
    city.clear()
    city.send_keys(created_city)

    postcode = driver.find_element(By.CSS_SELECTOR, 'input[id="field-postcode"]')
    created_postcode = generatePostcode()
    postcode.clear()
    postcode.send_keys(created_postcode)

    country = Select(driver.find_element(By.CSS_SELECTOR, 'select[name="id_country"]'))
    country.select_by_visible_text("Polska")

    driver.find_element(By.CSS_SELECTOR, 'button[name="confirm-addresses"]').click()


def chooseDelivery():
    carrier = random.randint(0, 1)
    try:
        driver.find_elements(By.CSS_SELECTOR, 'div[class="col-sm-1"] input')[carrier].click()
    except:
        pass
    driver.find_element(By.CSS_SELECTOR, 'button[name="confirmDeliveryOption"]').click()


def choosePayment():
    # payment on delivery
    try:
        driver.find_elements(By.CSS_SELECTOR, 'div[class="payment-option clearfix"] input')[1].click()
    except:
        pass

    # agree to the terms of service
    driver.find_element(By.CSS_SELECTOR, 'input[id="conditions_to_approve[terms-and-conditions]"]').click()
    # submit button
    driver.find_element(By.CSS_SELECTOR, 'button[class="btn btn-primary center-block"]').click()


def checkOrderStatus(email, password):
    my_account = driver.find_element(By.CSS_SELECTOR, 'a[class="account"]').get_attribute("href")
    driver.get(my_account)

    # history and details of the order
    order_histories = driver.find_element(By.CSS_SELECTOR, 'a[id="history-link"]').get_attribute("href")
    driver.get(order_histories)

    order_status = driver.find_element(By.CSS_SELECTOR, 'a[data-link-action="view-order-details"]').get_attribute("href")
    driver.get(order_status)




addLampsToCart(categories_urls[0], first_category_lamps_count)
addLampsToCart(categories_urls[1], second_category_lamps_count)

deleteOneProductFromCart()
email_account, password_account = createAccount()
completeAddresses()
chooseDelivery()
choosePayment()
checkOrderStatus(email_account, password_account)
