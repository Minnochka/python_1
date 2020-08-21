class Clothes:
    
    def __add__(self, other):
        return self.expenditure + other.expenditure

    @property
    def expenditure(self):
        pass

class Coat(Clothes):
    def __init__(self, v):
        if v < 36:
            print("Минимально допустимый размер 36")
            self.v = 36
        elif v > 52:
            print("Максимально допустимый размер 52")
            self.v = 52
        else:
            self.v = v

    
    @property
    def expenditure(self):
        return round(self.v/6.5 + 0.5, 2)

class Suit(Clothes):
    def __init__(self, h):
        if h < 150:
            print("Минимально допустимый рост 150")
            self.h = 150
        elif h > 200:
            print("Максимально допустимый рост 200")
            sef.h = 200
        else:
            self.h = h


    @property
    def expenditure(self):
        return round(2*self.h + 0.3, 2)






c = Coat(48)
s = Suit(160)
print("Expenditure of coat = {}".format(c.expenditure))
print("Expenditure of suit = {}".format(s.expenditure))
print("Summa = {}".format(c + s))
