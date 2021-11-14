from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup

class Product:
    def __init__(self, *, identifier, name, category, price, reference, delivery, producer, quantity,
    minimal_quantity, technical_data, description, url, available_date, images, features):
        self.identifier = identifier
        self.name = name
        self.category = category
        self.price = price
        self.reference = reference
        self.delivery = delivery
        self.producer = producer
        self.quantity = quantity
        self.minimal_quantity = minimal_quantity
        self.technical_data = technical_data
        self.description = description
        self.url = url
        self.available_date = available_date
        self.images = images
        self.features = features

    # JEDEN ; BYC MOZE DO WYRZUCENIA PO SELF PRODUCER BO MOZE MPN JEST NIEPOTRZEBNE
    def write_to_csv(self, csvwriter):
        csvwriter.writerow([
            self.identifier,
            1, # Active (0/1)
            self.name, # Name*
            self.category, # Categories (x,y,z...)
            self.price, # Price tax excluded
            #self.price, # Price tax included # excluded, see: PRODUCT_HEADER
            '', # Tax rule ID
            '', # Cost price
            0, # On sale (0/1)
            '', # Discount amount
            '', # Discount percent
            '', # Discount from (yyyy-mm-dd)
            '', # Discount to (yyyy-mm-dd)
            self.reference, # Reference #
            self.reference, # Supplier reference #
            '', # Supplier
            self.producer, # Brand
            '', # EAN13
            '', # UPC
            '', # MPN
            '', # Ecotax
            '', # Width
            '', # Height
            '', # Depth
            '', # Weight
            self.delivery, # Delivery time of in-stock products:
            '', # Delivery time of out-of-stock products with allowed orders:
            self.quantity, # Quantity
            self.minimal_quantity, # Minimal quantity
            '', # Low stock level
            '', # Send me an email when the quantity is under this level
            '', # Visibility
            '', # Additional shipping cost
            '', # Unit for base price
            '', # Base price
            '', # Summary
            self.description, # Description
            '', # Tags (x,y,z...)
            '', # Meta title
            '', # Meta keywords
            '', # Meta description
            self.url, # Rewritten URL
            '', # Label when in stock
            '', # Label when backorder allowed
            1, # Available for order (0 = No, 1 = Yes)
            self.available_date, # Product availability date
            '', # Product creation date
            1, # Show price (0 = No, 1 = Yes)
            ','.join(self.images), # Image URLs (x,y,z...)
            '', # Image alt texts (x,y,z...)
            1, # Delete existing images (0 = No, 1 = Yes)
            ','.join(self.features), # Feature (Name:Value:Position:Customized)
            0, # Available online only (0 = No, 1 = Yes)
            '', # Condition
            0, # Customizable (0 = No, 1 = Yes)
            0, # Uploadable files (0 = No, 1 = Yes)
            0, # Text fields (0 = No, 1 = Yes)
            '', # Action when out of stock
            0, # Virtual product (0 = No, 1 = Yes)
            '', # File URL
            '', # Number of allowed downloads
            '', # Expiration date (yyyy-mm-dd)
            '', # Number of days
            '', # ID / Name of shop
            '', # Advanced Stock Management
            '', # Depends on stock
            '', # Warehouse
            '', # Accessories (x,y,z...)
        ])


class _IdentiferGen:
    i = 0


def identifier_gen_reset(new_i):
    _IdentiferGen.i = new_i


def identifier_gen():
    ret = _IdentiferGen.i
    _IdentiferGen.i += 1
    return ret


def get_num_pages_in_category(page_soup):
    paginator = page_soup.select_one('#main #products nav')
    a_links = paginator.find_all('a')
    page_numbers = [int(s.text.strip()) for s in a_links if (s.text and s.text.strip() != '')]

    return max(page_numbers) if page_numbers else 1


def get_product_urls_on_page(url, page):
    page = requests.get(url, params={'page': page})
    soup = BeautifulSoup(page.text, 'html.parser')

    articles = soup.select('#main #products #js-product-list article')
    return [a.find('a')['href'] for a in articles]


def get_product_features(details_json):
    features = []
    for feature in details_json['features']:
        feature_str = f"{feature['name']}:{feature['value']}:{feature['position']}"
        features.append(feature_str)

    return features


def get_product(url, category):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_data = soup.select_one('#product-details')['data-product']
    data_json = json.loads(product_data)

    name = data_json['name']
    price = data_json['price_amount']
    reference = data_json['reference']
    delivery_time = data_json['available_now']
    producer = data_json['id_manufacturer'] # TODO turn into the manufacturer name
    quantity = data_json['quantity']
    minimal_quantity = data_json['minimal_quantity']
    description = data_json['description']
    images = [img['bySize']['large_default']['url'] for img in data_json['images']]
    features = get_product_features(data_json)

    #producer = prod_info.select_one('.product-manufacturer img')['alt']

    return Product(
        identifier=identifier_gen(),
        name=name,
        category=category.name,
        price=price,
        reference=reference,
        delivery=delivery_time,
        producer=producer,
        quantity=quantity,
        minimal_quantity=minimal_quantity,
        technical_data='', # TODO
        description=description,
        url=url,
        available_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        images=images,
        features=features
    )

def get_products_for_category(category):
    url = category.url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    pages_count = get_num_pages_in_category(soup)
    print(f'\tFound {pages_count} pages...')

    products = []
    for page_num in range(pages_count):
        print(f'\tProcessing page {page_num}', end='\r')

        product_urls = get_product_urls_on_page(url, page_num)
        for product_url in product_urls:
            product = get_product(product_url, category)
            products.append(product)
        for p in products:
            print(p)
        return products # TODO REMOVE

    return products

def get_products_for_categories(categories):
    identifier_gen_reset(100)

    products = []
    for category in categories:
        print(f'Getting products for {category.name}...')
        products.extend(get_products_for_category(category))
        return products # TODO REMOVE

    exit()
    
    return products