import json
import requests
from bs4 import BeautifulSoup

class Lamp:
    def __init__(self, *, identifier, name, category, price, delivery, producer, amount,
    technicalData, description, url, image_lamp, producer_logo):
        self.identifier = identifier
        self.name = name
        self.category = category
        self.price = price
        self.delivery = delivery
        self.producer = producer
        self.amount = amount
        self.technical_data = technicalData
        self.description = description
        self.url = url
        self.image_lamp = image_lamp
        self.producer_logo = producer_logo

    # JEDEN ; BYC MOZE DO WYRZUCENIA PO SELF PRODUCER BO MOZE MPN JEST NIEPOTRZEBNE
    def convert_to_csv(self):
        answer = (str(self.identifier) + ";1;" + self.name + ";" + self.category + ";"
            + str(self.price) + ";1;;0;;;;;;;;")
        answer += (self.producer + ";;;;;;;;;" + str(self.delivery) + ";;" + str(self.amount)
            + ";1;1;1;both;;;;" + str(self.technical_data) + ";")
        answer += (f'"{self.description}"' + ";" + self.producer + ";Meta title-"
            + str(self.identifier) + ";Meta keywords-" + str(self.identifier)
            + ";Meta description-" + str(self.identifier) + ";")
        answer += (self.url + ";Dostępny;Niedostępny;1;;;1;" + self.image_lamp + ", " 
            + self.producer_logo + ";;0;;0;new;0;0;0;0;0;;;;;0;0;0;0;")

        return answer


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


def get_product(url, category):
    page = requests.get(url)
    soup = BeautifulSoup(page.text, 'html.parser')

    product_data = soup.select_one('#product-details')['data-product']
    data_json = json.loads(product_data)

    producer = data_json['id_manufacturer'] # TODO turn into the manufacturer name
    reference = data_json['reference']
    price = data_json['price_amount']
    images = [img['large']['url'] for img in data_json['images']]
    delivery_time = data_json['available_now']
    quantity = data_json['quantity']
    description = data_json['description'].replace('\n', '\\n').replace('\r', '').replace('"', '""')
    name = data_json['name']

    #producer = prod_info.select_one('.product-manufacturer img')['alt']

    return Lamp(
        identifier=identifier_gen(),
        name=name,
        category=category.name,
        price=price,
        delivery=delivery_time,
        producer=producer,
        amount=quantity,
        technicalData='', # TODO
        description=description,
        url=url,
        image_lamp=images[0], # TODO
        producer_logo=images[0]) # TODO


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