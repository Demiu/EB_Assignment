class Combination:
    def __init__(self, identifier, is_LED):
        self.identifier = identifier
        self.attribute = 'Rodzaj żarówek dla lampy:select:1'
        self.value = ("Świetlówki:1", "Żarówki LED:1")[is_LED]
        self.impact_on_price = (0, 10)[is_LED]
        self.default = (0, 1)[is_LED]

# JEDEN ; BYC MOZE DO WYRZUCENIA PO VALUE BO MOZE MPN JEST NIEPOTRZEBNE
    def convert_to_csv(self):
        answer = (str(self.identifier) + ";" + self.attribute + ";" + self.value + ";;;;;;0;"
            + str(self.impact_on_price))
        answer += ";0;10;1;0;0;" + str(self.default) + ";;;;;0;0;0;"
        return answer
