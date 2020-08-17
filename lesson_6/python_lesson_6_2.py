class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def weight(self, kg, h):
        return round((kg * h * self._length * self._width) / 1000, 3)

road = Road(10, 200)
print("Асфальт весит {} т.".format(road.weight(int(input("вес асфальта: ")), int(input("толщина асфальта: ")))))
        
