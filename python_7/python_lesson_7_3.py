class Cell:
    def __init__(self, cnt):
        self.cnt = cnt

    #@property
    #def cnt(self):
    #    return cnt

    #@cnt.setter
    #def cnt(self, cnt):
    #        cnt = abs(round(cnt))


    def __add__(self, other):
        return self.cnt + other.cnt
            
    def __sub__(self, other):
        if self.cnt < other.cnt:
            return - 1
        else:
            return self.cnt - other.cnt

    def __mul__(self, other):
        return self.cnt * other.cnt

    def __truediv__(self, other):
        return self.cnt // other.cnt

    def make_order(self, line):
        res = ''
        for i in range(self.cnt // line):
            l = ''.join('*' for i in range(line))
            res += l
            if (self.cnt - line * (i + 1)) > 0:
                res += '\n'
        if (self.cnt % line) != 0:
            l = ''.join('*' for i in range(self.cnt % line))
            res += l
        return res


c1 = Cell(25)
c2 = Cell(3)
print("Кол-во ячеек: {} {}".format(c1.cnt, c2.cnt))
print("add: {}".format(c1 + c2))
print("sub: {}".format(c1 - c2))
print("mul: {}".format(c1 * c2))
print("truediv: {}".format(c1 / c2))
print(c1.make_order(int(input("Введите кол-во элементов в ряду: "))))
