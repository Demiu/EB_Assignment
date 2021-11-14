#!/usr/bin/env python3

import csv
import os
import requests
from bs4 import BeautifulSoup

from lamp import get_products_for_categories
from category import get_categories
from combination import Combination


CATEGORIES_HEADER = [
    'ID',
    'Active (0/1)',
    'Name*',
    'Parent category',
    'Root category (0/1)',
    'Description',
    'Meta title',
    'Meta keywords',
    'Meta description',
    'Rewritten URL',
    'Image URL',
    'ID / Name of shop'
]

PRODUCTS_HEADER = [
    'ID',
    'Active (0/1)',
    'Name*',
    'Categories (x,y,z...)',
    'Price tax excluded',
    #'Price tax included', # For some reason default import skips this property
    'Tax rule ID',
    'Cost price',
    'On sale (0/1)',
    'Discount amount',
    'Discount percent',
    'Discount from (yyyy-mm-dd)',
    'Discount to (yyyy-mm-dd)',
    'Reference #',
    'Supplier reference #',
    'Supplier',
    'Brand',
    'EAN13',
    'UPC',
    'MPN',
    'Ecotax',
    'Width',
    'Height',
    'Depth',
    'Weight',
    'Delivery time of in-stock products:',
    'Delivery time of out-of-stock products with allowed orders:',
    'Quantity',
    'Minimal quantity',
    'Low stock level',
    'Send me an email when the quantity is under this level',
    'Visibility',
    'Additional shipping cost',
    'Unit for base price',
    'Base price',
    'Summary',
    'Description',
    'Tags (x,y,z...)',
    'Meta title',
    'Meta keywords',
    'Meta description',
    'Rewritten URL',
    'Label when in stock',
    'Label when backorder allowed',
    'Available for order (0 = No, 1 = Yes)',
    'Product availability date',
    'Product creation date',
    'Show price (0 = No, 1 = Yes)',
    'Image URLs (x,y,z...)',
    'Image alt texts (x,y,z...)',
    'Delete existing images (0 = No, 1 = Yes)',
    'Feature (Name:Value:Position:Customized)',
    'Available online only (0 = No, 1 = Yes)',
    'Condition',
    'Customizable (0 = No, 1 = Yes)',
    'Uploadable files (0 = No, 1 = Yes)',
    'Text fields (0 = No, 1 = Yes)',
    'Action when out of stock',
    'Virtual product (0 = No, 1 = Yes)',
    'File URL',
    'Number of allowed downloads',
    'Expiration date (yyyy-mm-dd)',
    'Number of days',
    'ID / Name of shop',
    'Advanced Stock Management',
    'Depends on stock',
    'Warehouse',
    'Accessories (x,y,z...)'
]


def save_to_file(filepath, header, objects):
    if not os.path.exists(os.path.dirname(filepath)):
        os.makedirs(os.path.dirname(filepath))

    with open(filepath, 'w', encoding='utf-8') as file:
        csvwriter = csv.writer(file, delimiter=';')
        if header:
            csvwriter.writerow(header)
        for obj in objects:
            obj.write_to_csv(csvwriter)

def get_content(url, prod_id):
    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")
    products = soup.find(id=prod_id)
    return products


def get_description(product_info):
    header = product_info.find("h2").text
    answer = "<h2>" + header + "</h2><tbody><tr><td>"
    text = product_info.find_all("p")

    for paragraph in text:
        answer += "<p>" + paragraph.text + "</p>"

    answer += ("</td><td width=510></td><tr></tbody>")
    return answer


def get_technical_data(product_info):
    header = product_info.find("h3").text
    answer = "<h3>" + header + "</h3><dl>"
    dts = product_info.find_all("dt")
    dds = product_info.find_all("dd")

    for idt, idd in zip(dts, dds):
        answer += "<dt>" + idt.text.replace("\n", " ") + "</dt>"
        answer += "<dd>" + idd.text.replace("\n", " ") + "</dd>"

    answer += "</dl>"
    return answer


def get_lamp_informations(main_section, section_product):
    lamp_name = main_section.find("h1").text

    lamp_info = section_product.find('div', class_='product-lmage-large')
    image_lamp = lamp_info.find('img')['src']

    producer_info = section_product.find('div', 
        class_='product-manufacturer product-manufacturer-next float-right')
    producer_logo = producer_info.find('img')['src']
    producer = producer_info.find('img')['alt']

    price = section_product.find("span", class_="product-price").text[:-3]
    delivery = section_product.find("span", class_="product-available").text.strip()

    amount = "0"

    product_quantities = section_product.find('div', class_='product-quantities')
    if product_quantities:
        amount = product_quantities.find('span')['data-stock']
    #except if amount = "0" then we do not take lamps which are not there yet

    return lamp_name, image_lamp, producer_logo, producer, price, delivery, amount


def main():
    site_url = "https://mlamp.pl/"

    print('Getting categories...')
    categories = get_categories(site_url, 'Home')
    print('Saving categories...')
    save_to_file('data/categories.csv', CATEGORIES_HEADER, categories)

    print('Getting products...')
    products = get_products_for_categories(categories)
    print('Saving products...')
    save_to_file('data/products.csv', PRODUCTS_HEADER, products)
    exit()

if __name__ == "__main__":
    main()
