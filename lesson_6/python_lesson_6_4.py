class Car:
    direction = ["север", "восток", "запад", "юг"]
    
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print("Car {} go with speed {}.".format(self.name, self.speed))

    def stop(self):
        print("Car {} stop.".format(self.name))

    def turn( self, direction):
        t = 0
        for d in self.direction:
            if d == direction:
                print("turn - " + d)
                t = 1
        if t == 0:
            print("Wrong direction!")
        
    def show_speed(self):
        print("Car's speed is {}".format(str(self.speed)))


class TownCar(Car):
    limit = 60

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > TownCar.limit:
            print ("Car's speed is so high!")
        else:
            print("Car's speed is {}".format(str(self.speed)))


class SportCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    limit = 40

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > WorkCar.limit:
            print ("Car's speed is so high!")
        else:
            print("Car's speed is {}".format(str(self.speed)))


class PoliceCar(Car):

    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)



t1 = TownCar(30, "red", "t1", False)
t1.go()
t1.turn("север")
t1.turn("Канада")
t1.show_speed()
t1.stop()
print("--------------------")

t2 = TownCar(130, "green", "t2", False)
t2.go()
t2.turn("север")
t2.turn("Канада")
t2.show_speed()
t2.stop()
print("--------------------")

s1 = SportCar(200, "white", "s1", False)
s1.go()
s1.turn("север")
s1.turn("Канада")
s1.show_speed()
s1.stop()
print("--------------------")

w1 = WorkCar(10, "black", "w1", False)
w1.go()
w1.turn("север")
w1.turn("Канада")
w1.show_speed()
w1.stop()
print("--------------------")

w2 = WorkCar(50, "blue", "w2", False)
w2.go()
w2.turn("север")
w2.turn("Канада")
w2.show_speed()
w2.stop()
print("--------------------")

p1 = PoliceCar(300, "brown", "p1", True)
p1.go()
p1.turn("север")
p1.turn("Канада")
p1.show_speed()
p1.stop()

