class Woker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Woker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, {"wage": wage, "bonus": bonus})
        
    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return round(self._income.get("wage") + self._income.get("bonus"), 2)

       
p = Position("Stive", "Black","artist", 30000, 5000)
print ("Полное имя: " + p.get_full_name())
print("Доход: " + str(p.get_total_income()))
