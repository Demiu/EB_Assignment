import re
import unicodedata
import requests
from bs4 import BeautifulSoup

class Category:
    def __init__(self, identifier, url, name, parent_category):
        self.identifier = identifier
        self.url = url
        self.name = name
        self.parent_category = parent_category

    def __str__(self):
        return f'Category "{self.name}" at {self.url}, under {self.parent_category}'

    def write_to_csv(self, csvwriter):
        csvwriter.writerow([
            str(self.identifier),
            '1', # Active
            self.name,
            self.parent_category,
            '0', # Root Category
            '', # Description
            '', # Meta title
            '', # Meta keywords
            '', # Meta description
            '-'.join( # Rewritten URL
                re.findall(
                    r'[a-zA-Z]+',
                    unicodedata.normalize('NFD', self.name.lower())
                        .encode('ascii', 'ignore')
                        .decode('utf-8'))),
            '', # Image URL
            '', # ID / Name of shop
        ])


def is_category_link(site_url, href):
    cond1 = href.startswith(site_url)
    cond2 = re.match(r'^.*\.pl/[0-9]+.*', href) is not None
    return cond1 and cond2


def get_categories(site_url, default_parent_category):
    is_cat_link_pred = lambda href: is_category_link(site_url, href)
    identifier = 100

    page = requests.get(site_url)
    soup = BeautifulSoup(page.text, 'html.parser')
    banner_elems = (soup
        .find('header')
        .find(id='desktop-header')
        .find('ul')
        .find_all(class_='cbp-hrmenu-tab'))

    categories = []
    for elem in banner_elems:
        main_category = elem.find('a', recursive=False, href=is_cat_link_pred)
        if not main_category:
            continue

        mcat_url = main_category['href']
        mcat_name = main_category.select_one('span').get_text().strip()
        categories.append(Category(identifier, mcat_url, mcat_name, default_parent_category))
        identifier += 1

        # skip the first element, since it was already added
        for cat in elem.find_all('a', href=is_cat_link_pred)[1:]:
            cat_url = cat['href']
            cat_name = cat.get_text()
            categories.append(Category(identifier, cat_url, cat_name, mcat_name))
            identifier += 1

    # remove duplicates, overwrite sub categories with top level ones
    unique_categories = {cat.url: cat for cat in categories}
    for cat in categories:
        if (cat.parent_category == default_parent_category
        and unique_categories[cat.url].parent_category != default_parent_category):
            unique_categories[cat.url] = cat

    return list(unique_categories.values())
