#!/usr/bin/env python3

from bs4 import BeautifulSoup
import requests

from Lamp import Lamp
from Page import Page
from Combination import Combination

pages_urls = ["11-lampy-sufitowe-plafony", "10-lampy-wiszace-zyrandole", "13-lampy-scienne-kinkiety",
              "14-lampki-stolowe-biurkowe", "15-lampy-podlogowe", "21-lampy-zewnetrzne-sufitowe",
              "22-lampy-zewnetrzne-wiszace", "23-lampy-scienne-elewacyjne", "153-lampy-stojace-slupki",
              "24-lampy-masztowe-latarnie", "4-zarowki-zrodla-swiatla"]
pages_categories = ["Lampy sufitowe | plafony", "Lampy wiszące | żyrandole", "Lampy ścienne | kinkiety",
                   "Lampki stołowe | biurkowe", "Lampy stojące podłogowe", "Lampy zewnętrzne sufitowe",
                   "Lampy zewnętrzne wiszące", "Kinkiety ścienne i oświetlenie elewacyjne",
                   "Lampy stojące ogrodowe i słupki ogrodowe", "Latarnie ogrodowe i dekoracyjne lampy masztowe",
                   "Żarówki"]


def selectPages():
    pages = []
    for i in range(len(pages_urls)):
        pages.append(Page(pages_urls[i], pages_categories[i]))
    return pages


def getContent(url, prod_id):
    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")
    products = soup.find(id=prod_id)
    return products


def getDescription(productInfo):
    header = productInfo.find("h2").text
    answer = "<h2>" + header + "</h2><tbody><tr><td>"
    text = productInfo.find_all("p")

    for p in text:
        answer += "<p>" + p.text + "</p>"

    answer += ("</td><td width=510></td><tr></tbody>")
    return answer


def getTechnicalData(productInfo):
    header = productInfo.find("h3").text
    answer = "<h3>" + header + "</h3><dl>"
    dts = productInfo.find_all("dt")
    dds = productInfo.find_all("dd")

    for i in range(len(dts)):
        answer += "<dt>" + dts[i].text.replace("\n", " ") + "</dt>"
        answer += "<dd>" + dds[i].text.replace("\n", " ") + "</dd>"

    answer += "</dl>"
    return answer


def getLampInformations(main, section_product):
    lamp_name = main.find("h1").text

    lamp_info = section_product.find('div', class_='product-lmage-large')
    image_lamp = lamp_info.find('img')['src']

    producer_info = section_product.find('div', class_='product-manufacturer product-manufacturer-next float-right')
    producer_logo = producer_info.find('img')['src']
    producer = producer_info.find('img')['alt']

    price = section_product.find("span", class_="product-price").text[:-3]
    delivery = section_product.find("span", class_="product-available").text.strip()

    amount = "0"

    try:
        product_quantities = section_product.find('div', class_='product-quantities')
        amount = product_quantities.find('span')['data-stock']
    except:
        # if amount = "0" then we do not take lamps which are not there yet
        pass

    return lamp_name, image_lamp, producer_logo, producer, price, delivery, amount


def createProductsCombinations(id_start_combinations, id_end_combinations):
    file = open('data/combinations.csv', 'w', encoding='utf-8')
    file.write("ID;Indeks produktu;Atrybut (Nazwa:Typ:Pozycja)*;Wartość (Wartość:Pozycja)*;Identyfikator dostawcy;Indeks;\
EAN13;UPC;MPN;Koszt własny;Wpływ na cenę;Podatek ekologiczny;Ilość;Minimalna ilość;Niski poziom produktów w magazynie;\
Wyślij do mnie e-mail, gdy ilość jest poniżej tego poziomu;Wpływ na wagę;Domyślny (0 = Nie, 1 = Tak);Data dostępności\
kombinacji;Wybierz z pośród zdjęć produktów wg pozycji (1,2,3...);Adresy URL zdjęcia (x,y,z...);Tekst alternatywny dla\
zdjęć (x,y,z...);ID / Nazwa sklepu;Zaawansowane zarządzanie magazynem;Zależny od stanu magazynowego;Magazyn")
    file.close()

    for i in range(len(id_start_combinations)):
        for j in range(id_start_combinations[i], id_end_combinations[i] + 1):
            combination = Combination(j, True)
            combination = "\n" + combination.convertToCSV()
            with open('data/combinations.csv', 'a', encoding='utf-8') as file:
                file.write(combination)
            combination = Combination(j, False)
            combination = "\n" + combination.convertToCSV()
            with open('data/combinations.csv', 'a', encoding='utf-8') as file:
                file.write(combination)

    file.close()


site_url = "https://mlamp.pl/"
pages = selectPages()
products_id_url = "js-product-list"
product_substring = "js-product-miniature-wrapper"
id = 0

with open('data/products.csv', 'w', encoding='utf-8') as file:
    file.write("ID;Aktywny (0 lub 1);Nazwa;Kategorie (x,y,z…);Cena zawiera podatek. (brutto);ID reguły podatku;\
Koszt własny;W sprzedaży (0 lub 1);Wartość rabatu;Procent rabatu;Rabat od dnia (rrrr-mm-dd);Rabat do dnia \
(rrrr-mm-dd);Indeks #;Kod dostawcy #;Dostawca;Marka;EAN13;UPC;MPN;Ecotax;Szerokość;Wysokość;Głębokość;Waga;\
Czas dostawy produktów dostępnych w magazynie:;Czas dostawy wyprzedanych produktów z możliwością rezerwacji:;\
Ilość;Minimalna ilość;Niski poziom produktów w magazynie;Wyślij do mnie e-mail, gdy ilość jest poniżej tego \
poziomu;Widoczność;Dodatkowe koszty przesyłki;Jednostka dla ceny za jednostkę;Cena za jednostkę;Podsumowanie;Opis;\
Tagi (x,y,z…);Meta-tytuł;Słowa kluczowe meta;Opis meta;Przepisany URL;Etykieta, gdy w magazynie;Etykieta kiedy \
dozwolone ponowne zamówienie;Dostępne do zamówienia (0 = Nie, 1 = Tak);Data dostępności produktu;Data wytworzenia \
produktu;Pokaż cenę (0 = Nie, 1 = Tak);Adresy URL zdjęcia (x,y,z…);Tekst alternatywny dla zdjęć (x,y,z…);Usuń \
istniejące zdjęcia (0 = Nie, 1 = Tak);Cecha(Nazwa:Wartość:Pozycja:Indywidualne);Dostępne tylko online (0 = Nie, \
1 = Tak);Stan:;Konfigurowalny (0 = Nie, 1 = Tak);Można wgrywać pliki (0 = Nie, 1 = Tak);Pola tekstowe (0 = Nie, \
1 = Tak);Akcja kiedy brak na stanie;Wirtualny produkt (0 = No, 1 = Yes);Adres URL pliku;Ilość dozwolonych pobrań;\
Data wygaśnięcia (rrrr-mm-dd);Liczba dni;ID / Nazwa sklepu;Zaawansowane zarządzanie magazynem;Zależny od stanu \
magazynowego;Magazyn;Akcesoria (x,y,z…)")
file.close()

id_start_combinations = []
id_end_combinations = []

for page in pages:
    url = page.url
    category = page.category
    products = getContent(site_url + url, products_id_url)

    if page.category == "Lampy sufitowe | plafony":
        id_start_combinations.append(id + 1)
        id_end_combinations.append(id + 1)

    if page.category == "Lampy zewnętrzne sufitowe":
        id_start_combinations.append(id + 1)
        id_end_combinations.append(id + 1)

    page_results = products.find_all("div", lambda value: value and value.startswith(product_substring))

    for result in page_results:
        a_href = result.find("a").attrs['href']

        a_link = requests.get(a_href)
        content = a_link.text
        soup = BeautifulSoup(content, "html.parser")

        main = soup.find("main")
        section_product = main.find("section")

        lamp_name, image_lamp, producer_logo, producer, price, delivery, amount = getLampInformations(main, section_product)

        cards = section_product.find_all("div", class_="card")
        description = getDescription(cards[0])
        technicalData = getTechnicalData(cards[1])

        if amount != "0":
            id += 1
            lamp = Lamp(id, lamp_name, category, price, delivery, producer, amount, technicalData, description, url, image_lamp, producer_logo)
            product = "\n" + lamp.convertToCSV()
            with open('data/products.csv', 'a', encoding='utf-8') as file:
                file.write(product)

            if page.category == "Lampy sufitowe | plafony":
                id_end_combinations[0] = id

            if page.category == "Lampy zewnętrzne sufitowe":
                id_end_combinations[1] = id

    file.close()

createProductsCombinations(id_start_combinations, id_end_combinations)
