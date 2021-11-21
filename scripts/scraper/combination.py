class Combination:
    def __init__(self, product, attributes, values, impact_on_price, is_default):
        self.product = product
        self.attributes = attributes
        self.values = values
        self.impact_on_price = impact_on_price
        self.is_default = is_default


    def write_to_csv(self, csvwriter):
        csvwriter.writerow([
            self.product.identifier,
            self.product.reference, #Product reference
            self.attributes,
            self.values,
            self.product.reference, #Supplier reference
            self.product.reference, #Reference
            '', #EAN13
            '', #UPC
            '', #MPN
            '', #Cost price
            self.impact_on_price, #Impact on price
            '', #Ecotax
            self.product.quantity, #Quantity
            self.product.minimal_quantity, #Minimal quantity
            '', #Low stock level
            '', #Send me an email when the quantity is under this level
            '', #Impact on weight
            self.is_default, #Default (0 = No, 1 = Yes)
            self.product.available_date, #Combination availability date
            '', #Choose among product images by position (1,2,3...)
            '', #Image URLs (x,y,z...)
            '', #Image alt texts (x,y,z...)
            '', #ID / Name of shop
            '', #Advanced Stock Management
            '', #Depends on stock
            '', #Warehouse
        ])


def get_warranty_combinations_for_products_in_category(products, category):
    combinations = []
    for product in products:
        if category not in product.categories:
            continue

        attribute = 'Gwarancja:select:0'
        no_warranty_value = 'Brak:0'
        warranty_value = '12 miesięcy:0'
        no_warranty_comb = Combination(product, attribute, no_warranty_value, 0, 0)
        warranty_comb = Combination(product, attribute, warranty_value, 50, 1)

        combinations.append(no_warranty_comb)
        combinations.append(warranty_comb)

    return combinations
