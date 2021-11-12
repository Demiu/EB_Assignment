class Lamp:
    def __init__(self, identifier, name, category, price, delivery, producer, amount,
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
            + self.price + ";1;;0;;;;;;;;")
        answer += (self.producer + ";;;;;;;;;" + str(self.delivery) + ";;" + str(self.amount)
            + ";1;1;1;both;;;;" + str(self.technical_data) + ";")
        answer += (str(self.description) + ";" + self.producer + ";Meta title-"
            + str(self.identifier) + ";Meta keywords-" + str(self.identifier)
            + ";Meta description-" + str(self.identifier) + ";")
        answer += (self.url + ";Dostępny;Niedostępny;1;;;1;" + self.image_lamp + ", " 
            + self.producer_logo + ";;0;;0;new;0;0;0;0;0;;;;;0;0;0;0;")

        return answer
