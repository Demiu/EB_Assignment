class Combination:
    def __init__(self, product, reference_suffix, attributes, values, impact_on_price, is_default):
        self.product = product
        self.reference_suffix = reference_suffix
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
            self.product.reference + self.reference_suffix, #Reference
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
        warranty6_value = '6 miesięcy:0'
        warranty12_value = '12 miesięcy:0'
        no_warranty_comb = Combination(product, '', attribute, no_warranty_value, 0, 0)
        warranty6_comb = Combination(product, '-warranty6', attribute, warranty6_value, 30, 0)
        warranty12_comb = Combination(product, '-warranty12', attribute, warranty12_value, 50, 1)

        combinations.append(warranty12_comb)
        combinations.append(warranty6_comb)
        combinations.append(no_warranty_comb)

    return combinations
