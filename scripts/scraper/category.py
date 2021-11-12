import itertools
import re
import requests
from bs4 import BeautifulSoup

class Category:
    def __init__(self, url, name, parent_category):
        self.url = url
        self.name = name
        self.parent_category = parent_category

    def __str__(self):
        return f'Category "{self.name}" at {self.url}, under {self.parent_category}'


def isCategoryLink(site_url, href):
    b1 = href.startswith(site_url)
    b2 = re.match(r'^.*\.pl/[0-9]+.*', href) is not None
    return b1 and b2


def getCategories(site_url, default_parent_category):
    is_cat_link_pred = lambda href: isCategoryLink(site_url, href)

    page = requests.get(site_url)
    content = page.text
    soup = BeautifulSoup(content, "html.parser")
    banner_elems = (soup
        .find('header')
        .find(id='desktop-header')
        .find('ul')
        .find_all(class_='cbp-hrmenu-tab'))

    categories = []
    for e in banner_elems:
        main_category = e.find('a', recursive=False, href=is_cat_link_pred)
        if not main_category:
            continue

        mcat_url = main_category['href']
        mcat_name = main_category.select_one('span').get_text().strip()
        categories.append(Category(mcat_url, mcat_name, default_parent_category))

        # skip the first element, since it was already added
        for cat in e.find_all('a', href=is_cat_link_pred)[1:]:
            cat_url = cat['href']
            cat_name = cat.get_text()
            categories.append(Category(cat_url, cat_name, mcat_name))

    # remove duplicates, overwrite sub categories with top level ones
    unique_categories = {cat.name: cat for cat in categories}
    for cat in categories:
        if (cat.name == default_parent_category
        and unique_categories[cat.name] != default_parent_category):
            unique_categories[cat.name] = cat

    return list(unique_categories.values())