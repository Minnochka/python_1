import time

class TrafficLights:
    __color = "RED"
    #__color_dict = {"RED" : 7, "YELLOW" : 2, "GREEN" : 15}

    def running(self):
        if (self.__color == "RED"):
            self.__color = "YELLOW"
            time.sleep(7)
        elif (self.__color == "YELLOW"):
            self.__color = "GREEN"
            time.sleep(2)
        elif (self.__color == "GREEN"):
            self.__color = "RED"
            time.sleep(15)


tr_light = TrafficLights()
while True:
    if input("test: ")  == 'end':
        break
    else:
        tr_light.running()
            
