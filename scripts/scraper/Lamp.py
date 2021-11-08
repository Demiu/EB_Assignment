class Lamp:
    def __init__(self, id, name, category, price, delivery, producer, amount, technicalData, description, url, image_lamp, logo):
        self.id = id
        self.name = name
        self.category = category
        self.price = price
        self.delivery = delivery
        self.producer = producer
        self.amount = amount
        self.technicalData = technicalData
        self.description = description
        self.url = url
        self.image_lamp = image_lamp
        self.logo = logo

# BYC MOZE PO SELF PRODUCER TRZEBA DODAC 1 ; DLA MPN, RACZEJ NIE ALE NA RAZIE JEST DODANE
    def convert_to_CSV(self):
        inf = str(self.id) + ";1;" + self.name + ";" + self.category + ";" + self.price + ";1;;0;;;;;;;;"
        inf += self.producer + ";;;;;;;;;" + str(self.delivery) + ";;" + str(self.amount) + ";1;1;1;both;;;;" + str(self.technicalData) + ";"
        inf += str(self.description) + ";" + self.producer + ";Meta title-" + str(self.id) + ";Meta keywords-" + str(self.id) + ";Meta description-" + str(self.id) + ";"
        inf += self.url + ";Dostępny;Niedostępny;1;;;1;" + self.image_lamp + ", " + self.logo + ";;0;;0;new;0;0;0;0;0;;;;;0;0;0;0;"

        return inf