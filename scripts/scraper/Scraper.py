from bs4 import BeautifulSoup
import requests

from Lamp import Lamp
from Page import Page


def select_pages():
    pages = []
    pages.append(Page("11-lampy-sufitowe-plafony", "Lampy sufitowe | plafony"))
    pages.append(Page("10-lampy-wiszace-zyrandole", "Lampy wiszące | żyrandole"))
    pages.append(Page("13-lampy-scienne-kinkiety", "Lampy ścienne | kinkiety"))
    pages.append(Page("14-lampki-stolowe-biurkowe", "Lampki stołowe | biurkowe"))
    pages.append(Page("15-lampy-podlogowe", "Lampy stojące podłogowe"))
    pages.append(Page("21-lampy-zewnetrzne-sufitowe", "Lampy zewnętrzne sufitowe"))
    pages.append(Page("22-lampy-zewnetrzne-wiszace", "Lampy zewnętrzne wiszące"))
    pages.append(Page("23-lampy-scienne-elewacyjne", "Kinkiety ścienne i oświetlenie elewacyjne"))
    pages.append(Page("23-lampy-scienne-elewacyjne", "Kinkiety ścienne i oświetlenie elewacyjne"))
    pages.append(Page("153-lampy-stojace-slupki", "Lampy stojące ogrodowe i słupki ogrodowe"))
    pages.append(Page("24-lampy-masztowe-latarnie", "Latarnie ogrodowe i dekoracyjne lampy masztowe"))
    pages.append(Page("4-zarowki-zrodla-swiatla", "Żarówki"))
    return pages

def get_content(url, prodID):
    page = requests.get(url)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")
    products = soup.find(id = prodID)
    return products

def get_description(productInfo):
    header = productInfo.find("h2").text
    #answer = "<h2>" + header + "</h2>\n<tbody>\n<tr>\n<td>\n"
    answer = "<h2>" + header + "</h2><tbody><tr><td>"
    text = productInfo.find_all("p")
    for p in text:
        #answer += "<p>" + p.text + "</p>\n"
        answer += "<p>" + p.text + "</p>"

    #answer += ("</td>\n<td width=510></td>\n<tr>\n</tbody>\n")
    answer += ("</td><td width=510></td><tr></tbody>")
    #print(answer)
    return answer

def get_technicalData(productInfo):
    header = productInfo.find("h3").text
    #answer = "<h3>" + header + "</h3>\n<dl>\n"
    answer = "<h3>" + header + "</h3><dl>"
    dts = productInfo.find_all("dt")
    dds = productInfo.find_all("dd")
    for i in range(len(dts)):
        #print(dts[i].text)
        #print(dds[i].text)
        #answer += "<dt>" + dts[i].text.replace("\n", " ") + "</dt>\n"
        answer += "<dt>" + dts[i].text.replace("\n", " ") + "</dt>"
        #answer += "<dd>" + dds[i].text.replace("\n", " ") + "</dd>\n"
        answer += "<dd>" + dds[i].text.replace("\n", " ") + "</dd>"

    answer += "</dl>"
    #print(answer)
    return answer


mainUrl = "https://mlamp.pl/"
pages = select_pages()
productsIdInUrl = "js-product-list"
productSubstring = "js-product-miniature-wrapper"
id = 0

with open('data/productsInCSV.csv', 'w', encoding='utf-8') as file:
    file.write("ID;Aktywny (0 lub 1);Nazwa;Kategorie (x,y,z…);Cena zawiera podatek. (brutto);ID reguły podatku;Koszt własny;W sprzedaży (0 lub 1);Wartość rabatu;Procent rabatu;Rabat od dnia (rrrr-mm-dd);Rabat do dnia (rrrr-mm-dd);Indeks #;Kod dostawcy #;Dostawca;Marka;EAN13;UPC;Ecotax;Szerokość;Wysokość;Głębokość;Waga;Czas dostawy produktów dostępnych w magazynie:;Czas dostawy wyprzedanych produktów z możliwością rezerwacji:;Ilość;Minimalna ilość;Niski poziom produktów w magazynie;Wyślij do mnie e-mail, gdy ilość jest poniżej tego poziomu;Widoczność;Dodatkowe koszty przesyłki;Jednostka dla ceny za jednostkę;Cena za jednostkę;Podsumowanie;Opis;Tagi (x,y,z…);Meta-tytuł;Słowa kluczowe meta;Opis meta;Przepisany URL;Etykieta, gdy w magazynie;Etykieta kiedy dozwolone ponowne zamówienie;Dostępne do zamówienia (0 = Nie, 1 = Tak);Data dostępności produktu;Data wytworzenia produktu;Pokaż cenę (0 = Nie, 1 = Tak);Adresy URL zdjęcia (x,y,z…);Tekst alternatywny dla zdjęć (x,y,z…);Usuń istniejące zdjęcia (0 = Nie, 1 = Tak);Cecha(Nazwa:Wartość:Pozycja:Indywidualne);Dostępne tylko online (0 = Nie, 1 = Tak);Stan:;Konfigurowalny (0 = Nie, 1 = Tak);Można wgrywać pliki (0 = Nie, 1 = Tak);Pola tekstowe (0 = Nie, 1 = Tak);Akcja kiedy brak na stanie;Wirtualny produkt (0 = No, 1 = Yes);Adres URL pliku;Ilość dozwolonych pobrań;Data wygaśnięcia (rrrr-mm-dd);Liczba dni;ID / Nazwa sklepu;Zaawansowane zarządzanie magazynem;Zależny od stanu magazynowego;Magazyn;Akcesoria (x,y,z…)")
file.close()

for page in pages:
    url = page.url
    category = page.category
    products = get_content(mainUrl + url, productsIdInUrl)

    results = products.find_all("div", lambda value: value and value.startswith(productSubstring))
    for result in results:
        save = True

        a_href = result.find("a").attrs['href']
        #print(a_href)

        a_link = requests.get(a_href)
        content = a_link.text
        soup = BeautifulSoup(content, "html.parser")
        main = soup.find("main")

        lamp_name = main.find("h1").text
        #print(lamp_name)

        section_product = main.find("section")

        lamp_info = section_product.find('div', class_='product-lmage-large')
        image_lamp = lamp_info.find('img')['src']

        #print("image_lamp = " + str(image_lamp))

        producer_info = section_product.find('div', class_='product-manufacturer product-manufacturer-next float-right')
        producer_logo = producer_info.find('img')['src']
        producer = producer_info.find('img')['alt']

        #print("producer_logo = " + str(producer_logo))
        #print("producer = " + str(producer))

        price = section_product.find("span", class_="product-price").text[:-3]
        #print(price)

        delivery = section_product.find("span", class_="product-available").text.strip()
        #print(delivery)

        cards = section_product.find_all("div", class_="card")
        #cards[0] for description, cards[1] for technicalData
        description = get_description(cards[0])
        technicalData = get_technicalData(cards[1])

        amount = "0"

        try:
            product_quantities = section_product.find('div', class_='product-quantities')
            amount = product_quantities.find('span')['data-stock']
        except:
            # if amount = "0" then we do not take lamps which are not there yet
            pass

        if amount != "0":
            id += 1
            #print("id = " + str(id))
            lamp = Lamp(id, lamp_name, category, price, delivery, producer, amount, technicalData, description, url, image_lamp, producer_logo)
            product = "\n" + lamp.convert_to_CSV()
            with open('data/productsInCSV.csv', 'a', encoding='utf-8') as file:
                file.write(product)
    file.close()
