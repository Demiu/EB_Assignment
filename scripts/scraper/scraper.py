#!/usr/bin/env python3

import os
import requests
from bs4 import BeautifulSoup

from lamp import Lamp
from category import get_categories
from combination import Combination


combinations_header = "ID;Indeks produktu;Atrybut (Nazwa:Typ:Pozycja)*;Wartość (Wartość:Pozycja)*;\
Identyfikator dostawcy;Indeks;EAN13;UPC;MPN;Koszt własny;Wpływ na cenę;Podatek ekologiczny;Ilość;\
Minimalna ilość;Niski poziom produktów w magazynie;Wyślij do mnie e-mail, gdy ilość jest poniżej \
tego poziomu;Wpływ na wagę;Domyślny (0 = Nie, 1 = Tak);Data dostępnościkombinacji;Wybierz z \
pośród zdjęć produktów wg pozycji (1,2,3...);Adresy URL zdjęcia (x,y,z...);Tekst alternatywny dla \
zdjęć (x,y,z...);ID / Nazwa sklepu;Zaawansowane zarządzanie magazynem;Zależny od stanu magazynowego;\
Magazyn"

products_header = "ID;Aktywny (0 lub 1);Nazwa;Kategorie (x,y,z…);Cena zawiera podatek. (brutto);\
ID reguły podatku;Koszt własny;W sprzedaży (0 lub 1);Wartość rabatu;Procent rabatu;Rabat od dnia \
(rrrr-mm-dd);Rabat do dnia (rrrr-mm-dd);Indeks #;Kod dostawcy #;Dostawca;Marka;EAN13;UPC;MPN;\
Ecotax;Szerokość;Wysokość;Głębokość;Waga;Czas dostawy produktów dostępnych w magazynie:;\
Czas dostawy wyprzedanych produktów z możliwością rezerwacji:;Ilość;Minimalna ilość;Niski poziom \
produktów w magazynie;Wyślij do mnie e-mail, gdy ilość jest poniżej tego poziomu;Widoczność;\
Dodatkowe koszty przesyłki;Jednostka dla ceny za jednostkę;Cena za jednostkę;Podsumowanie;Opis;\
Tagi (x,y,z…);Meta-tytuł;Słowa kluczowe meta;Opis meta;Przepisany URL;Etykieta, gdy w magazynie;\
Etykieta kiedy dozwolone ponowne zamówienie;Dostępne do zamówienia (0 = Nie, 1 = Tak);Data \
dostępności produktu;Data wytworzenia produktu;Pokaż cenę (0 = Nie, 1 = Tak);Adresy URL zdjęcia \
(x,y,z…);Tekst alternatywny dla zdjęć (x,y,z…);Usuń istniejące zdjęcia (0 = Nie, 1 = Tak);Cecha\
(Nazwa:Wartość:Pozycja:Indywidualne);Dostępne tylko online (0 = Nie, 1 = Tak);Stan:;\
Konfigurowalny (0 = Nie, 1 = Tak);Można wgrywać pliki (0 = Nie, 1 = Tak);Pola tekstowe (0 = Nie, \
1 = Tak);Akcja kiedy brak na stanie;Wirtualny produkt (0 = No, 1 = Yes);Adres URL pliku;Ilość \
dozwolonych pobrań;Data wygaśnięcia (rrrr-mm-dd);Liczba dni;ID / Nazwa sklepu;Zaawansowane \
zarządzanie magazynem;Zależny od stanu magazynowego;Magazyn;Akcesoria (x,y,z…)"


def save_to_file(file, header, objects):
    if not os.path.exists(os.path.dirname(file)):
        os.makedirs(os.path.dirname(file))

    with open(file, 'w', encoding='utf-8') as file:
        if header:
            file.write(header + '\n')
        for obj in objects:
            file.write(obj.convert_to_csv() + '\n')

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
    categories = get_categories(site_url, 'Home')
    products_id_url = "js-product-list"
    product_substring = "js-product-miniature-wrapper"
    identifier = 0

    for category in categories:
        url = category.url
        category_name = category.name
        products = get_content(url, products_id_url)

        page_results = products.find_all("div",
            lambda value: value and value.startswith(product_substring))

        lamps = []
        for result in page_results:
            a_href = result.find("a").attrs['href']

            a_link = requests.get(a_href)
            content = a_link.text
            soup = BeautifulSoup(content, "html.parser")

            main_section = soup.find("main")
            section_product = main_section.find("section")

            lamp_name, image_lamp, producer_logo, producer, price, delivery, amount = (
                get_lamp_informations(main_section, section_product))

            cards = section_product.find_all("div", class_="card")
            description = get_description(cards[0])
            technical_data = get_technical_data(cards[1])

            identifier += 1
            lamps.append(Lamp(identifier, lamp_name, category_name, price, delivery, producer, amount,
                    technical_data, description, url, image_lamp, producer_logo))

        lamps = [lamp for lamp in lamps if lamp.amount != "0"]
        save_to_file('data/products.csv', products_header, lamps)

if __name__ == "__main__":
    main()
