from datetime import datetime
import json
import requests
from bs4 import BeautifulSoup

class Product:
    def __init__(self, *, identifier, name, categories, price, reference, delivery, producer, 
    quantity, minimal_quantity, description, url, available_date, images, features):
        self.identifier = identifier
        self.name = name
        self.categories = categories
        self.price = price
        self.reference = reference
        self.delivery = delivery
        self.producer = producer
        self.quantity = quantity
        self.minimal_quantity = minimal_quantity
        self.description = description
        self.url = url
        self.available_date = available_date
        self.images = images
        self.features = features


    def get_feature_str(self):
        feature_str = ''
        for feature in self.features:
            feature_str += f"{feature}:{feature['value']}:{feature['position']}"

        return feature_str


    def write_to_csv(self, csvwriter):
        csvwriter.writerow([
            self.identifier,
            1, # Active (0/1)
            self.name, # Name*
            self.categories, # Categories (x,y,z...)
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
    features = {}
    for feature in details_json['features']:
        if 'name' in features:
            features['name'].append((feature['value'], feature['position']))
        else:
            features['name'] = [(feature['value'], feature['position'])]

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
        categories=category.name,
        price=price,
        reference=reference,
        delivery=delivery_time,
        producer=producer,
        quantity=quantity,
        minimal_quantity=minimal_quantity,
        description=description,
        url=url,
        available_date=datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
        images=images,
        features=features
    )

def get_products_for_category(category, already_fetched_dict, limit=None):
    url = category.url
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    pages_count = get_num_pages_in_category(soup)
    print(f'\tFound {pages_count} pages...')

    products = []
    for page_num in range(pages_count):
        print(f'\tProcessing page {page_num}...', end='\r')

        product_urls = get_product_urls_on_page(url, page_num)
        for product_url in product_urls:
            if product_url not in already_fetched_dict:
                product = get_product(product_url, category)
                products.append(product)
                if len(products) >= limit:
                    print('\tReached product limit')
                    return products
            else:
                already_fetched_dict[product_url].categories += f',{category.name}'

    print('\tProcessed all pages')

    return products

def get_products_for_categories(categories, limit=None):
    identifier_gen_reset(100)

    url_to_products = {}
    for category in categories:
        print(f'Getting products for {category.name}...')

        cat_limit = (limit - len(url_to_products)) if limit else None
        products = get_products_for_category(category, url_to_products, cat_limit)
        url_to_products_new = {p.url: p for p in products}
        url_to_products.update(url_to_products_new)

        if len(url_to_products) == limit:
            return list(url_to_products.values())

    return list(url_to_products.values())
